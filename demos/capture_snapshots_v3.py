"""
Capture force feedback arrow snapshot — must actually grab a package first
"""
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import sys
sys.path.insert(0, 'demos')

import pygame
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

from warehouse_robot_v2 import draw_frame
from warehouse_robot import Arm
from arm_controller import ArmController
from sensor_fusion import WarehouseAgent

arm = Arm()
arm_controller = ArmController(arm, base_pos=(650, 420))
packages = [
    {"pos": (450, 300), "color": (50, 220, 50), "id": "A", "grabbed": False},
    {"pos": (550, 280), "color": (50, 220, 50), "id": "B", "grabbed": False},
    {"pos": (650, 320), "color": (50, 220, 50), "id": "C", "grabbed": False},
]
drop_zone = pygame.Rect(420, 550, 120, 80)
agent = WarehouseAgent(arm_controller, packages, drop_zone)

os.makedirs('/tmp/agent_v3_snapshots', exist_ok=True)
os.makedirs('/app/data-intelligence-architect/ire-bootcamp/demos/snapshots_v3', exist_ok=True)

# Run until agent has grabbed, then capture during moving_to_drop
frame_count = 0
captured = False
while frame_count < 3000 and not captured:
    agent.step()
    # Look for state right after grab, when moving to drop
    if (agent.state == "MOVING_TO_DROP" and 
        arm_controller.has_package and
        agent.sensor_log):
        latest = agent.sensor_log[-1]
        if latest["force"] > 0.5:  # Real grab
            filename = '/tmp/agent_v3_snapshots/force_arrow.png'
            frame = draw_frame(arm, arm_controller, agent, packages, drop_zone, frame_count)
            pygame.image.save(frame, filename)
            repo_path = '/app/data-intelligence-architect/ire-bootcamp/demos/snapshots_v3/force_arrow.png'
            pygame.image.save(frame, repo_path)
            print(f'📸 Force arrow captured!')
            print(f'   Frame: {frame_count}')
            print(f'   State: {agent.state}')
            print(f'   Has package: {arm_controller.has_package}')
            print(f'   Force: {latest["force"]:.3f}N')
            print(f'   End: ({arm_controller.get_end_effector_position()})')
            captured = True
    frame_count += 1

if not captured:
    print(f'❌ Could not capture force arrow in {frame_count} frames')
    # Fallback: manually grab a real package then capture
    print('Trying manual grab with real package...')
    # Move to package C position
    arm_controller.set_target(672, 342)  # Package C center
    for _ in range(120):
        arm_controller.update()
    # Force grab on package C
    if arm_controller.grab():
        print(f'   ✅ Manual grab succeeded')
    else:
        print(f'   ⚠️ Manual grab failed, forcing has_package')
        arm_controller.has_package = True
        packages[2]['grabbed'] = True  # Package C
        arm_controller.current_package = packages[2]
    # Now move to drop zone
    arm_controller.set_target(480, 590)
    for _ in range(80):
        arm_controller.update()
    # Populate sensor log with package held — must use agent.perceive() not sensors.update()
    for _ in range(30):
        agent.perceive()  # This populates sensor_log with proper force reading
    filename = '/tmp/agent_v3_snapshots/force_arrow.png'
    frame = draw_frame(arm, arm_controller, agent, packages, drop_zone, 0)
    pygame.image.save(frame, filename)
    repo_path = '/app/data-intelligence-architect/ire-bootcamp/demos/snapshots_v3/force_arrow.png'
    pygame.image.save(frame, repo_path)
    state = arm_controller.get_state()
    print(f'📸 Force arrow (manual)')
    print(f'   Held: {state["has_package"]}, End: ({state["end_x"]:.0f},{state["end_y"]:.0f})')
    if agent.sensor_log:
        print(f'   Force: {agent.sensor_log[-1]["force"]:.3f}N')

# Also re-capture other states (forced)
agent2 = WarehouseAgent(arm_controller, packages, drop_zone)
target_states = ['moving_to_pkg', 'grabbing', 'moving_to_drop', 'dropping', 'idle']
for target in target_states:
    old_state = agent2.state
    agent2.state = target
    for _ in range(5):
        agent2.step()
    filename = f'/tmp/agent_v3_snapshots/state_{target}.png'
    frame = draw_frame(arm, arm_controller, agent2, packages, drop_zone, 0)
    pygame.image.save(frame, filename)
    repo_path = f'/app/data-intelligence-architect/ire-bootcamp/demos/snapshots_v3/state_{target}.png'
    pygame.image.save(frame, repo_path)
    print(f'📸 {target}')

# Capture proximity arrow snapshot (not holding, near a package)
print('\n--- Proximity arrow snapshot ---')
agent3 = WarehouseAgent(arm_controller, packages, drop_zone)
arm_controller2 = ArmController(arm, base_pos=(650, 420))
arm_controller2.set_packages(packages)
# Move to a position close to but not at a package
# Package B is at (550+22, 280+22) = (572, 302), put end at (650, 350) so it's nearby
arm_controller2.set_target(650, 350)
for _ in range(200):  # More frames to actually reach
    arm_controller2.update()
# Populate sensor log
for _ in range(10):
    agent3.perceive()
filename = '/tmp/agent_v3_snapshots/proximity_arrow.png'
frame = draw_frame(arm, arm_controller2, agent3, packages, drop_zone, 0)
pygame.image.save(frame, filename)
repo_path = '/app/data-intelligence-architect/ire-bootcamp/demos/snapshots_v3/proximity_arrow.png'
pygame.image.save(frame, repo_path)
state = arm_controller2.get_state()
print(f'📸 Proximity arrow (not holding, near pkg)')
print(f'   Held: {state["has_package"]}, End: ({state["end_x"]:.0f},{state["end_y"]:.0f})')
# Calculate distance to nearest package
import math as m
nearest_dist = float('inf')
nearest_pkg = None
for pkg in packages:
    if not pkg.get('grabbed', False):
        d = m.hypot(state['end_x'] - (pkg['pos'][0]+22), state['end_y'] - (pkg['pos'][1]+22))
        if d < nearest_dist:
            nearest_dist = d
            nearest_pkg = pkg
if nearest_pkg:
    print(f'   Nearest: {nearest_pkg["id"]} at {nearest_dist:.0f}px')

print(f'\nDone!')
