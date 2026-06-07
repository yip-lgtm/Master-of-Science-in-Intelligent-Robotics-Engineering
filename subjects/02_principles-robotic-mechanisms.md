# 02 Principles of Robotic Mechanisms

## 📅 Self-Study Roadmap
- Week 1-2: Kinematics basics + 3R Arm + Agent Loop ✅
- Week 3-4: DH parameters + Forward/Inverse kinematics
- Week 5-6: Webots simulation + Dynamics
- Week 7-12: Optimization + Real robot deployment

## 🔗 Resources
- "Introduction to Robotics" by Craig (PDF)
- Peter Corke Robotics Toolbox (Python)
- YouTube "Modern Robotics" series
- Stanford CS 223A (Embodied AI supplement)

## 📝 Weekly Progress
| Week | Date | Status | Notes |
|------|------|--------|-------|
| 1 | 2026-05-15 | ✅ | 3R Arm + Warehouse scene + Agent Loop demo |
| 2 | 2026-06-07 | ✅ | Kinematics + IK + Sensor Fusion + Actuator Selection |
| 3 | | ☐ | |
| 4 | | ☐ | |

---

## 2A. Kinematics (Week 2 核心)

### Forward Kinematics
- 已知 joint angles → 計 end effector position
- 2-link example:
  ```
  x_end = l1*cos(θ1) + l2*cos(θ1+θ2)
  y_end = l1*sin(θ1) + l2*sin(θ1+θ2)
  ```

### Inverse Kinematics (我們 demo 用)
- 已知 end effector target → 計 joint angles
- **Geometric approach** (2-link):
  ```
  r = sqrt(x² + y²)
  cos(θ2) = (r² - l1² - l2²) / (2*l1*l2)
  θ2 = -acos(cos(θ2))  # Elbow-down
  θ1 = atan2(y, x) - atan2(l2*sin(θ2), l1 + l2*cos(θ2))
  ```

### 3R Arm 嘅 wrist 處理
- 3R = R(l1) + R(l2) + R(l3) 喺 2D plane
- ⚠️ **Critical:** Wrist 補償唔可以簡單 `θ3 = -θ1-θ2`
- ✅ 改用 effective 2-link: `L1 = l1, L2 = l2 + l3`, `θ3 = 0` (wrist 直)
- 原因: Wrist 偏移 l3, IK 唔知會 miss target 100px

### Reach Check
```python
import math
r = math.sqrt(lx**2 + ly**2)
max_reach = l1 + l2 + l3
if r > max_reach:
    raise ValueError(f"Target outside reach ({r:.0f} > {max_reach})")
```

### DOF (Degrees of Freedom)
- Planar 3R arm: 3 DOF (3 rotations)
- Spatial 6R arm (e.g., PUMA): 6 DOF
- Gripper: +1 DOF (open/close)

---

## 2B. Advanced Product Mechatronics (Week 2 補完)

### 1. 感測器融合 (Sensor Fusion)

**核心目的:** 多感測器數據融合後, 比單一感測器更準確、更可靠.

**常見方法:**

| Method | 用途 | 優點 | 缺點 |
|--------|------|------|------|
| **Kalman Filter** | 位置、速度估計 | 最優線性估計 | 計算量大, 假設 Gaussian noise |
| **Complementary Filter** | IMU (gyro + accel) | 簡單、實時 | 唔係最優 |
| **Multi-Sensor Fusion** | Camera + Encoder + Force | 最高精度 | 標定複雜 |

**Complementary Filter 例子:**
```python
def fuse_sensors(gyro_angle, accel_angle, alpha=0.98):
    """High-pass gyro + low-pass accel"""
    return alpha * gyro_angle + (1 - alpha) * accel_angle
```

**Gary 倉庫機械人案例:**
- 📷 Vision (條碼定位) — 慢但絕對位置
- 🔄 Joint Encoders — 快但 drift
- 💪 Force Sensor — 抓取反饋

三個融合 → 抓取穩定性高

### 2. 致動器選擇 (Actuator Selection)

| 致動器類型 | 優點 | 缺點 | 適合應用 |
|------------------|--------------------------|--------------------|------------------------------|
| **DC Motor + Gear** | 扭力大、控制簡單 | 體積大 | 工業機械臂 |
| **Servo Motor** | 精準位置控制 | 扭力較小 | 小型機械臂、Gripper |
| **Stepper Motor** | 精準步進、無需反饋 | 效率低、發熱 | 3D Printer、精密定位 |
| **Pneumatic / Soft Actuator** | 柔軟、安全 | 控制複雜 | Soft Robotics |

**選擇原則:**
- 🎯 需要高精度位置 → **Servo**
- 💪 需要大扭力 + 速度 → **DC Motor + Encoder**
- 🤝 需要安全人機互動 → **Soft Actuator**
- 🖨️ 需要開環精準步進 → **Stepper**

### 3. 系統整合 (System Integration)

**4 層架構:**
```
┌─────────────────────────┐
│  感知層 (Sensors)         │ ← Camera, Encoder, IMU, Force
├─────────────────────────┤
│  決策層 (Agent)           │ ← Rule-based / LLM / RL
├─────────────────────────┤
│  執行層 (Actuators)       │ ← Motor, Servo, Pneumatic
├─────────────────────────┤
│  反饋閉環 (Feedback)      │ ← Sensor → Agent → Actuator
└─────────────────────────┘
```

**Demo 對應:**
- 感知 → 末端位置 (FK) + 包裹狀態 (Game state)
- 決策 → `ArmController.move_to()` + `Agent` state machine
- 執行 → 關節角度 + 平滑移動 (interpolation)
- 反饋 → Re-perceive 每 frame

---

## 2C. Agent Loop 完整實現 (Perception → Think → Action)

### 5 個 States
```
IDLE → MOVING_TO_PKG → GRABBING → MOVING_TO_DROP → DROPPING → IDLE
```

### 完整 WarehouseAgent 實現
```python
class WarehouseAgent:
    def __init__(self, arm_controller, packages, drop_zone):
        self.arm = arm_controller
        self.packages = packages
        self.drop_zone = drop_zone
        self.state = "IDLE"
        self.target_package = None
        self.packages_delivered = 0

    def perceive(self):
        """PERCEPTION: Find nearest ungrabbed package"""
        import math
        end_x, end_y = self.arm.get_end_effector_position()
        candidates = [p for p in self.packages if not p['grabbed']]
        if not candidates:
            return None
        return min(candidates, key=lambda p: math.hypot(
            end_x - p['pos'][0] - 22,
            end_y - p['pos'][1] - 22
        ))

    def think(self):
        """THINKING: State machine 決定下一步"""
        end_x, end_y = self.arm.get_end_effector_position()
        import math

        if self.state == "IDLE":
            self.target_package = self.perceive()
            if self.target_package:
                self.state = "MOVING_TO_PKG"

        elif self.state == "MOVING_TO_PKG":
            pkg = self.target_package
            self.arm.set_target(pkg['pos'][0]+22, pkg['pos'][1]+22)
            if math.hypot(end_x - pkg['pos'][0]-22, end_y - pkg['pos'][1]-22) < 30:
                self.state = "GRABBING"

        elif self.state == "GRABBING":
            self.arm.grab()
            self.target_package['grabbed'] = True
            self.state = "MOVING_TO_DROP"

        elif self.state == "MOVING_TO_DROP":
            cx = self.drop_zone.x + self.drop_zone.width/2
            cy = self.drop_zone.y + self.drop_zone.height/2
            self.arm.set_target(cx, cy)
            if math.hypot(end_x - cx, end_y - cy) < 30:
                self.state = "DROPPING"

        elif self.state == "DROPPING":
            self.arm.release()
            self.target_package['grabbed'] = False
            self.packages_delivered += 1
            self.target_package = None
            self.state = "IDLE"

    def step(self):
        """Single Perception-Action cycle"""
        self.think()
        self.arm.update()
```

### Test 結果 (2026-06-07)

- **6 packages delivered 喺 3000 steps** (60 fps sim)
- 完整 cycle: IDLE → MOVING_TO_PKG → GRABBING → MOVING_TO_DROP → DROPPING → IDLE
- 全部用 sensor fusion 後嘅 single 末端位置做 perception

### 下一步升級方向

1. **LLM-based thinking** — 用 VLA 模型做 decision
2. **Force sensor** — 抓取前探測包裹重量
3. **Path planning** — 避開障礙物
4. **Multi-arm coordination** — 多個機械臂合作

---

## 💻 Code Files (Week 2 全部)

- `demos/warehouse_robot.py` — Main Pygame demo (140 lines)
- `demos/arm_controller.py` — IK + smooth movement (130 lines)
- `demos/capture_snapshots.py` — Headless capture (130 lines)
- `demos/snapshots/` — 5 state PNGs

**Run:**
```bash
cd /Master-of-Science-in-Intelligent-Robotics-Engineering
pip install -r demos/requirements.txt
python demos/warehouse_robot.py  # 按 SPACE 開 Agent Loop
```

---

## 🎓 學習成果 (Week 1-2)

✅ **Embodied AI 概念** (Week 1)
- Perception-Action Loop
- Embodiment Hypothesis
- VLA 模型 (RT-2, PaLM-E, LLaVA)

✅ **Robotic Mechanisms** (Week 2)
- Forward / Inverse Kinematics
- 3R Arm 設計
- Wrist 處理 + Reach check

✅ **Advanced Product Mechatronics** (Week 2 補完)
- Sensor Fusion (Kalman / Complementary)
- Actuator Selection
- System Integration

✅ **Agent Loop 完整實現**
- 5-state machine
- 6 packages delivered 驗證
- 對齊 Week 1 嘅 Perception-Action 概念

## 📊 整體進度: 2/12 weeks (16.7%) complete
