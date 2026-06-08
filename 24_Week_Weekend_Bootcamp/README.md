# 24-Week Weekend Bootcamp

> **Mission:** Complete CUHK BEng (Mechanical and Automation Engineering)
> + PolyU MSc (Intelligent Robotics Engineering) — **all ~74 courses**
> in 24 weekends (~6 months).
>
> **Started:** 2026-06-13 (Saturday)
> **Target Completion:** 2026-11-28

## 🎯 Strategy

| Component | Approach |
|-----------|----------|
| **Theory** | Read course `.md` files (we already have 75+ in `mae-cuhk/courses/`) |
| **Practice** | Update `3R Pygame arm` + `warehouse robot` simulator each weekend |
| **Recording** | Update `progress.md` + course `.md` notes |
| **Review** | Light weekday reviews (15-30 min) — no pressure |

## ⏰ Weekend Schedule (8-12 hours)

| Time | Activity | Duration |
|------|----------|----------|
| **Sat AM** | Theory — read course `.md` + textbook | 3-4 hrs |
| **Sat PM** | Practice — update simulator | 3-4 hrs |
| **Sun AM** | Reflection + Documentation | 2-3 hrs |
| **Sun PM** | Light review or rest | Optional |

## 📅 4 Phases Overview

### Phase 1: Foundations (Week 1-6) — `phase1_foundations/`

**Focus:** Math, Physics, Mechanics, Materials, Circuits, Thermo

**Core Courses:**
- ENGG1110/1120/1130 (Programming, Linear Algebra, Multivariable Calc)
- MATH1510 + PHYS1110 (Calculus, Engineering Physics)
- MAEG2020 (Engineering Mechanics) ⭐⭐⭐⭐⭐
- MAEG3010 (Mechanics of Materials)
- MAEG2030 (Thermodynamics)
- EEEN3030 (Engineering Materials)
- ELEG2202 (Electric Circuits)
- ENGG2720/2740 (Complex Variables, Diff Eq)

**Simulator Updates:**
- Strengthen 3R arm kinematics
- Add basic dynamics (inertia, friction)
- Implement basic trajectory planning

### Phase 2: Mechatronics & Control (Week 7-12) — `phase2_mechatronics_control/`

**Focus:** Control Systems, Mechanical Design, Manufacturing, Fluid, Heat Transfer, Mechatronics

**Core Courses:**
- MAEG3050 (Intro to Control Systems) ⭐⭐⭐⭐⭐
- MAEG3020 (Manufacturing Technology)
- MAEG3030 (Fluid Mechanics)
- MAEG3040 (Mechanical Design)
- MAEG4030 (Heat Transfer)
- MAEG4040 (Mechatronic Systems) ⭐⭐⭐⭐⭐
- MAEG1020 (Computational Design)
- MAEG2601/2602 (Tech/Society, Practicum)

**Simulator Updates:**
- Optimize PID control (we already have it!)
- Smooth movement with acceleration limits
- Force feedback improvements
- State machine core functionality

### Phase 3: Robotics & Advanced (Week 13-18) — `phase3_robotics_advanced/`

**Focus:** Robotics fundamentals, Advanced Control, Smart Materials, AI, Vision, Soft Robotics

**Core Courses:**
- MAEG3060 (Intro to Robotics) ⭐⭐⭐⭐⭐
- MAEG2050 (Robot Development in Practice) ⭐⭐⭐⭐
- MAEG4050 (Modern Control Systems) ⭐⭐⭐⭐⭐
- MAEG3080 (Machine Intelligence)
- MAEG4040 (Mechatronic Systems, full)
- MAEG5080 (Smart Materials) ⭐⭐⭐⭐
- ENGG2020 (Digital Logic — FSM)
- ENGG5404 (MEMS)
- ENGG5402/5403 (Advanced Robotics, Linear System Theory)
- BMEG3420 (Medical Robotics)

**Simulator Updates:**
- Full warehouse robot + state machine
- Basic Agent Loop (already done!)
- Add trajectory planning
- Improve IK
- Add vision sensor (cameras)

### Phase 4: Integration & FYP Prep (Week 19-24) — `phase4_integration_fyp/`

**Focus:** Final integration, remaining electives, FYP ideas, portfolio

**Core Courses:**
- MAEG4998/4999 (FYP I & II) ⭐⭐⭐⭐⭐
- MAEG4010/4020 (Computer-Integrated Mfg, FEA)
- MAEG5060/5070/5110 (Computational Intelligence, Nonlinear, Quantum)
- ENGG5405 (Theory of Engineering Design)
- MAEG5090 (Topics in Robotics)
- Energy electives (EEEN2020, etc.)
- Business electives (SEEM2440, etc.)

**Simulator Updates:**
- Final integration demo
- Multi-robot coordination
- LLM-based Agent thinking (instead of rule-based)
- Full documentation + portfolio

## 📊 Progress Tracker

See [`progress.md`](./progress.md) for the full week-by-week table.

## 🎮 Auto-Reminders

This bootcamp is supported by:
- **Weekly cron:** Saturday 9:00 AM HKT — sends focus + tasks
- **Daily reminder:** Weekday 8:00 PM HKT — light review prompt
- **Skill:** `skills/bootcamp_weekly.py` — generates the weekly message

## 🔗 Related Folders

- [`../mae-cuhk/`](../mae-cuhk/) — All 75+ CUHK BEng course .md files
- [`../subjects/`](../subjects/) — PolyU MSc IRE 13-week notes
- [`../demos/`](../demos/) — 3R Pygame arm + warehouse robot (the simulator)

## 🚀 Why This Works

1. **Sustained pace** — 8-12 hrs/weekend, 24 weekends = 192-288 hours total
2. **Theory + practice** — every concept gets applied to existing simulator
3. **Portfolio growth** — by Week 24, you have a complete robotics+mechatronics
   project that covers both degrees
4. **Low pressure** — no weekday requirement, weekend focus only
5. **Already started** — warehouse_robot, PID, force feedback, Agent Loop
   all exist and just need extension

**Last Updated:** 2026-06-08
