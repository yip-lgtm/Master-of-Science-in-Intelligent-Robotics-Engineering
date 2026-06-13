# Week 3/13 — Soft Robotics 詳細 Notes 🦑

> **Topic**: Soft Robotics — Materials, Actuators, Modeling, Control
> **Course Reference**: MAEG3060 Intro to Robotics (Phase 3) + MAEG5080 Smart Materials (Phase 3)
> **Week**: 3 (intro level) OR 13 (deeper dive)
> **Word Count**: ~1,500 字
> **Date**: 13 June 2026

---

## 1. What is Soft Robotics? 🦑

**Definition**: Soft robots are made from **compliant materials** (silicone, rubber, fabric) with **continuously deformable bodies**, contrasting with rigid robots made of metal and plastic.

**Key characteristics**:
- **Compliance**: Body can bend, stretch, twist
- **Adaptability**: Conforms to environment
- **Safety**: Inherently safe for human interaction
- **Versatility**: One morph for many tasks

**Why soft robotics matters**:
- Medical: Minimally invasive surgery, rehabilitation
- Search & rescue: Squeeze through rubble
- Food/agriculture: Handle delicate produce
- Wearable: Soft exoskeletons, prosthetics
- Research: New paradigm in embodied intelligence

**Inspiration from nature**:
- Octopus (no rigid skeleton) 🐙
- Elephant trunk (10,000+ muscles, no bones)
- Worm/inchworm locomotion
- Plant tendrils (coiling)

---

## 2. Materials (Soft Robot Body)

| Material | Type | Stiffness (MPa) | Use Case |
|----------|------|-----------------|----------|
| Ecoflex 00-30 | Silicone rubber | 0.1 | Skin, fingers |
| Ecoflex 00-50 | Silicone rubber | 0.2 | Stronger skin |
| PDMS (Sylgard 184) | Silicone elastomer | 1-3 | Lab fabrication |
| Dragon Skin 10 | Silicone | 0.15 | High elongation (>800%) |
| Polyurethane (PU) | Thermoplastic | 5-50 | 3D printing soft parts |
| TPU (NinjaFlex) | Filament | 50-100 | 3D printing flexible |
| Latex | Natural rubber | 1-5 | Cheap, available |
| Fabric/textile | Composite | Variable | Pneumatic nets |

**Material selection criteria**:
- Young's modulus (stiffness)
- Elongation at break (must be >100% for actuators)
- Tear strength (for durability)
- Biocompatibility (for medical)
- 3D printability or moldability
- Cost

**Yip's practical experience**: 3R robot arm uses rigid aluminium + servo motors. Soft robotics is a **paradigm shift** — instead of controlling joints, you control **shape**.

---

## 3. Actuators (How Soft Robots Move)

### 3.1 Pneumatic Artificial Muscles (PAM)
- **Principle**: Compressed air inflates a bladder inside a braided mesh
- **Contraction**: 25-35% when inflated
- **Force**: Up to 100N for 10mm diameter
- **Examples**: McKibben muscle (1950s, still used)
- **Pros**: High power-to-weight, simple
- **Cons**: Needs compressor, slow response

### 3.2 Pneumatic Networks (PneuNets)
- **Principle**: Embedded channels in elastomer, pressurise to bend
- **Channel design**: Embedded chambers that inflate
- **Bending**: Up to 180° with 50 kPa
- **Examples**: Harvard soft robotics (Whitesides group)
- **Pros**: Simple fabrication (mold + pour)
- **Cons**: Needs air supply, leakage

### 3.3 Dielectric Elastomer Actuators (DEA)
- **Principle**: Electrodes on either side of elastomer film; voltage → compression
- **Voltage**: 1-5 kV (high!)
- **Strain**: Up to 300% area strain
- **Pros**: No compressor, fast
- **Cons**: High voltage = safety concern

### 3.4 Shape Memory Alloys (SMA) / Polymers (SMP)
- **Principle**: Heat → phase change → shape change
- **Nitinol (Ni-Ti)**: Most common SMA, 4-8% strain
- **Activation temp**: 70-100°C (Nitinol)
- **Pros**: Silent, high force, no compressor
- **Cons**: Slow, hysteresis, energy-inefficient

### 3.5 Fluidic Elastomer Actuators (FEA)
- **Principle**: Hydraulic fluid in embedded channels
- **Advantage over pneumatic**: Incompressible, better control
- **Disadvantage**: Heavier system (need pump + reservoir)

### 3.6 Comparison Table

| Actuator | Strain (%) | Response (Hz) | Force | Power Density |
|----------|-----------|---------------|-------|---------------|
| Pneumatic | 25-35 | 1-5 | High | High |
| DEA | 100-300 | 100+ | Medium | Medium |
| SMA | 4-8 | 0.1-1 | Very High | High |
| FEA | 20-40 | 1-10 | High | High |
| Biological muscle | 20-40 | 5-10 | High | High |

---

## 4. Sensors in Soft Robots

Soft robots need **soft sensors** to match their compliance:

| Sensor | Principle | Use Case |
|--------|-----------|----------|
| **Liquid metal channels (EGaIn)** | Resistive | Strain, curvature |
| **Conductive silicone** | Piezoresistive | Pressure, touch |
| **Optical fibers** | Light loss | Distributed strain |
| **Capacitive sensor** | Capacitance change | Proximity, force |
| **Soft pneumatic sensor** | Air pressure change | Contact detection |
| **Conductive fabric** | Resistance change | E-Textile, wearable |

**Soft sensing challenge**: Traditional rigid sensors break when robot deforms. New approaches:
- **Stretchable electronics** (e.g., metal nanoparticles in elastomer)
- **Self-sensing actuators** (e.g., DEA capacitance = strain)
- **Vision-based sensing** (external cameras track deformation)

---

## 5. Modeling (The Hard Part)

### 5.1 Why Modeling is Hard
- **Infinite degrees of freedom** (vs 6 for rigid robot)
- **Nonlinear materials** (hyperelastic, large strain)
- **Coupled physics** (fluid + structure + thermal for some)
- **Time-varying geometry** (changing under load)

### 5.2 Common Modeling Approaches

#### (a) FEM (Finite Element Method)
- **Software**: ABAQUS, ANSYS, COMSOL
- **Accuracy**: High
- **Speed**: Slow (minutes to hours per simulation)
- **Use**: Design optimization, validation
- **Example**: Static deflection of a soft finger

#### (b) Cosserat Rod Theory
- **Principle**: Model as a 1D curve with bending, twist, shear
- **Speed**: Real-time capable
- **Software**: Elastica, SOFA framework
- **Use**: Real-time control of continuum robots

#### (c) Reduced-Order Models (PCC — Piecewise Constant Curvature)
- **Principle**: Approximate as series of constant-curvature segments
- **Speed**: Very fast (real-time)
- **Accuracy**: Moderate
- **Use**: Real-time control, trajectory planning

#### (d) Machine Learning
- **Approach**: Learn forward/inverse model from data
- **Speed**: Real-time (after training)
- **Accuracy**: Depends on training data
- **Use**: When classical modeling is too complex

### 5.3 Typical Workflow
```
1. Design geometry (CAD, e.g., Fusion 360)
2. Material selection (Ecoflex, PDMS)
3. FEM simulation (ABAQUS) — calibrate
4. Reduced-order model (Cosserat or PCC)
5. Real-time control implementation
6. Validation with physical prototype
```

---

## 6. Control Strategies

### 6.1 Open-Loop Control
- **Method**: Pre-computed pressure sequences
- **Use**: Repetitive tasks (gripper)
- **Limitation**: No adaptation

### 6.2 Closed-Loop with Visual Feedback
- **Method**: Camera tracks deformation, controller adjusts pressure
- **Use**: Grasping unknown objects
- **Tools**: OpenCV, DeepLabCut for tracking

### 6.3 Model-Based Control
- **Method**: Use Cosserat / PCC model, feedforward + feedback
- **Use**: Precise trajectory tracking
- **Examples**: Model Predictive Control (MPC)

### 6.4 Learning-Based Control
- **Method**: Reinforcement learning (RL) or Imitation Learning
- **Use**: Complex tasks, no model
- **Examples**: PPO, SAC algorithms
- **Tools**: Stable Baselines, PyTorch

---

## 7. Key Research Groups and Resources

### Academic Labs
- **Harvard (Whitesides Group)**: Pioneers of PneuNets
- **MIT CSAIL (Rus Group)**: Soft robotics + AI
- **Stanford (Cutkosky Group)**: Haptic + soft
- **Festo**: Industrial soft robotics
- **Imperial College (Rossiter Group)**: Soft actuators

### Open-Source Software
- **SOFA Framework**: Real-time soft body simulation
- **Elastica**: Cosserat rod simulation (Python)
- **PyElastica**: Python version
- **MuJoCo**: Physics simulation for robotics
- **Bullet**: Physics engine

### Open-Source Hardware
- **Soft Robotics Toolkit** (softroboticstoolkit.com)
- **Open-Source Soft Pneumatic Actuator** (GitHub)
- **PneuNet designs** (Harvard)

### Datasets
- **Yale-CMU-Berkeley (YCB) Object Set**: For grasping
- **Contact DB**: Soft robot grasping

---

## 8. Week 3/13 Deliverable: Build a Soft Gripper

**Goal**: Build a 2-finger soft pneumatic gripper that can pick up a delicate object (e.g., a soft fruit or an egg).

### Required Materials
- Ecoflex 00-30 (silicone)
- 3D printed mold (or laser-cut acrylic)
- Pneumatic tubing
- 2 solenoid valves (e.g., 12V)
- Arduino Uno
- Air compressor or syringe pump
- Paper clips, rubber bands

### Steps
1. **Mold design** (Fusion 360, 1 hour)
   - 2 fingers, each with 3 chambers
   - 20mm long, 10mm wide, 5mm thick
2. **3D print mold** (or laser cut)
3. **Pour Ecoflex** (30 min cure time)
4. **Demold** + **attach tubing**
5. **Wire up valves + Arduino**
6. **Write Arduino code** (open/close on button press)
7. **Test grip on egg** (gently!)

### Stretch Goals
- Add pressure sensor for closed-loop
- Add 3rd finger for stable grasp
- Add camera for object detection + auto-grasp

### Time Estimate
- **Basic version**: 4-6 hours
- **With stretch goals**: 8-12 hours

---

## 9. Code Snippet (Arduino Soft Gripper Control)

```cpp
// Arduino code for 2-finger soft pneumatic gripper
const int VALVE_1 = 9;  // Open finger 1
const int VALVE_2 = 10; // Open finger 2
const int BUTTON = 2;   // Push to grip

void setup() {
  pinMode(VALVE_1, OUTPUT);
  pinMode(VALVE_2, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(BUTTON) == LOW) {
    // Grip
    digitalWrite(VALVE_1, HIGH);
    digitalWrite(VALVE_2, HIGH);
    delay(2000);  // Hold for 2s
  } else {
    // Release
    digitalWrite(VALVE_1, LOW);
    digitalWrite(VALVE_2, LOW);
  }
}
```

---

## 10. Week 3 Reflection Questions

1. **Why use soft materials instead of rigid?** (compliance, safety, adaptability)
2. **What's the trade-off between pneumatic and DEA?** (power vs voltage safety)
3. **Why is modeling soft robots harder than rigid?** (infinite DOF, nonlinear)
4. **What's the role of soft sensors?** (matching compliance, distributed sensing)
5. **How would you control a soft arm to write your name?** (model-based? learning?)

---

## 11. Resources to Read This Week

- **Paper**: "Soft Robotics: A Journey from Materials to Systems" (Rus & Tolley, Nature 2015)
- **Paper**: "PneuNets" (Ilievski et al., Angew. Chem. 2011)
- **Book**: "Soft Robotics: Transferring Theory to Application" (Springer 2015)
- **YouTube**: "Harvard soft robotics" channel
- **GitHub**: SOFA Framework tutorials
- **Course**: MIT 6.881 (Computational Fabrication, free on OCW)

---

## 12. Connection to Yip's IRE Journey

| Yip Background | Soft Robotics Link |
|----------------|---------------------|
| 3R rigid robot arm | Learn deformable counterpart |
| PID control (rigid) | Learn model-free / learning control |
| Sensor fusion (rigid) | Learn soft distributed sensing |
| Mechanics of Materials | Learn hyperelastic material behavior |
| Geotechnical engineering (soil) | Soil IS a soft material! Cosserat theory applies to both |

**Surprising connection**: Geotechnical engineering already uses **constitutive models** for soil (Mohr-Coulomb, Hardening Soil) that are similar to soft robot material models (Neo-Hookean, Ogden hyperelastic). Yip's geotech background is a **unique advantage** in soft robotics modeling.

---

**Week 3/13 完成指標**:
- ✅ Read this notes file
- ✅ Watch 2-3 soft robotics YouTube videos
- ✅ Build a 2-finger gripper (or simulate in SOFA)
- ✅ Write 300-word reflection in progress_log.txt
- ✅ Plan next week (e.g., continuum robot arm, or fluidic control)

**加油! Soft robotics 係 IRE 最有 paradigm-shifting 嘅 topic** 🦑💪

— KANG YIP SZE, 13 June 2026
