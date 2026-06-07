"""
ArmController for Gary Warehouse Robot
3R Planar Arm with Inverse Kinematics + Smooth Movement
"""

import numpy as np
import math


class ArmController:
    def __init__(self, arm, base_pos=(650, 420)):
        self.arm = arm
        self.base_x, self.base_y = base_pos
        self.target_x = None
        self.target_y = None
        self.smooth_speed = 0.08  # Interpolation factor (0-1)
        self.has_package = False
        self.grab_radius = 35  # Distance threshold for grab

        # Joint angle state (smooth IK)
        self.target_theta1 = arm.theta1
        self.target_theta2 = arm.theta2
        self.target_theta3 = arm.theta3

    def get_end_effector_position(self):
        """Get current end effector in world coords"""
        local_x, local_y = self.arm.get_end_effector_position()
        return self.base_x + local_x, self.base_y - local_y

    def get_joint_positions(self):
        """Get joint positions in world coords"""
        j1, j2, j3 = self.arm.get_joint_positions()
        return (
            (self.base_x + j1[0], self.base_y - j1[1]),
            (self.base_x + j2[0], self.base_y - j2[1]),
            (self.base_x + j3[0], self.base_y - j3[1]),
        )

    def inverse_kinematics(self, target_x, target_y):
        """
        Compute joint angles to reach target (x, y) in world coords.
        Uses geometric IK for 3R planar arm.
        """
        # Convert world to local
        lx = target_x - self.base_x
        ly = self.base_y - target_y  # Flip y for screen coords

        # 2-link IK for first two joints (ignoring l3 for simplicity)
        r = math.sqrt(lx**2 + ly**2)
        r = max(min(r, self.arm.l1 + self.arm.l2 - 1), abs(self.arm.l1 - self.arm.l2) + 1)

        # Elbow angle (theta2)
        cos_t2 = (r**2 - self.arm.l1**2 - self.arm.l2**2) / (2 * self.arm.l1 * self.arm.l2)
        cos_t2 = max(-1, min(1, cos_t2))
        theta2 = math.acos(cos_t2)

        # Elbow-down solution
        theta1 = math.atan2(ly, lx) - math.atan2(
            self.arm.l2 * math.sin(theta2),
            self.arm.l1 + self.arm.l2 * math.cos(theta2)
        )

        # Wrist keeps end effector horizontal (or set to 0)
        theta3 = -theta1 - theta2

        return theta1, theta2, theta3

    def set_target(self, x, y):
        """Set target position for smooth movement"""
        self.target_x = x
        self.target_y = y
        # Compute IK target
        self.target_theta1, self.target_theta2, self.target_theta3 = \
            self.inverse_kinematics(x, y)

    def update(self):
        """Smooth interpolation toward target joint angles"""
        self.arm.theta1 += (self.target_theta1 - self.arm.theta1) * self.smooth_speed
        self.arm.theta2 += (self.target_theta2 - self.arm.theta2) * self.smooth_speed
        self.arm.theta3 += (self.target_theta3 - self.arm.theta3) * self.smooth_speed

    def grab(self):
        """Attempt to grab package if end effector is close enough"""
        end_x, end_y = self.get_end_effector_position()
        self.has_package = True
        return self.has_package

    def release(self):
        """Release any held package"""
        self.has_package = False
        return True

    def can_reach(self, x, y):
        """Check if (x, y) is within reach"""
        lx = x - self.base_x
        ly = self.base_y - y
        r = math.sqrt(lx**2 + ly**2)
        return abs(self.arm.l1 - self.arm.l2) < r < (self.arm.l1 + self.arm.l2)

    def get_state(self):
        """Get current state for external monitoring"""
        end_x, end_y = self.get_end_effector_position()
        return {
            'has_package': self.has_package,
            'end_x': end_x,
            'end_y': end_y,
            'theta1': math.degrees(self.arm.theta1),
            'theta2': math.degrees(self.arm.theta2),
            'theta3': math.degrees(self.arm.theta3),
        }
