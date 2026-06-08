"""
Bootcamp Weekly Skill — 24-Week Weekend Bootcamp
Generates weekly focus + tasks for Saturday morning reminder.

Used by OpenClaw cron job: 0 9 * * 6 (Asia/Hong_Kong)
"""
import datetime
import json
import os


# Bootcamp configuration
BOOTCAMP_START = datetime.date(2026, 6, 13)  # First Saturday
TOTAL_WEEKS = 24

# Phase definitions
PHASES = {
    1: {
        "name": "Phase 1: Foundations",
        "weeks": "1-6",
        "focus": "Math, Physics, Mechanics, Materials, Circuits, Thermo",
        "core_courses": [
            "ENGG1110 - Problem Solving By Programming",
            "ENGG1120 - Linear Algebra for Engineers",
            "ENGG1130 - Multivariable Calculus for Engineers",
            "MATH1510 - Calculus for Engineers",
            "PHYS1110 - Engineering Physics",
            "MAEG1020 - Computational Design and Fabrication",
            "MAEG2020 - Engineering Mechanics ⭐⭐⭐⭐⭐",
            "MAEG3010 - Mechanics of Materials",
            "MAEG2030 - Thermodynamics",
            "EEEN3030 - Engineering Materials",
            "ELEG2202 - Fundamentals of Electric Circuits",
            "ENGG2720 - Complex Variables for Engineers",
            "ENGG2740 - Differential Equations for Engineers",
        ],
        "simulator_tasks": [
            "Strengthen 3R arm kinematics (DH parameters)",
            "Add basic dynamics (inertia, friction, gravity)",
            "Implement basic trajectory planning",
            "Document kinematics with workspace visualization",
        ],
    },
    2: {
        "name": "Phase 2: Mechatronics & Control",
        "weeks": "7-12",
        "focus": "Control Systems, Mechanical Design, Manufacturing, Fluid, Heat Transfer, Mechatronics",
        "core_courses": [
            "MAEG3050 - Introduction to Control Systems ⭐⭐⭐⭐⭐",
            "MAEG3020 - Manufacturing Technology",
            "MAEG3030 - Fluid Mechanics",
            "MAEG3040 - Mechanical Design",
            "MAEG4030 - Heat Transfer",
            "MAEG4040 - Mechatronic Systems ⭐⭐⭐⭐⭐",
            "MAEG2601 - Technology, Society and Engineering Practice",
            "MAEG2602 - Engineering Practicum",
        ],
        "simulator_tasks": [
            "Optimize PID control (already implemented!)",
            "Add smooth movement with acceleration limits",
            "Improve force feedback with sensor fusion",
            "Refine state machine (5 states) with FSM best practices",
        ],
    },
    3: {
        "name": "Phase 3: Robotics & Advanced",
        "weeks": "13-18",
        "focus": "Robotics, Advanced Control, Smart Materials, AI, Vision, Soft Robotics",
        "core_courses": [
            "MAEG3060 - Introduction to Robotics ⭐⭐⭐⭐⭐",
            "MAEG2050 - Robot Development in Practice",
            "MAEG4050 - Modern Control Systems ⭐⭐⭐⭐⭐",
            "MAEG3080 - Fundamentals of Machine Intelligence",
            "MAEG5080 - Smart Materials and Structures ⭐⭐⭐⭐",
            "ENGG2020 - Digital Logic and Systems (FSM)",
            "ENGG5404 - Micromachining and MEMS",
            "ENGG5402 - Advanced Robotics",
            "ENGG5403 - Linear System Theory and Design",
            "BMEG3420 - Medical Robotics",
        ],
        "simulator_tasks": [
            "Full warehouse robot + state machine (already done!)",
            "Add trajectory planning (spline interpolation)",
            "Improve IK (analytical + numerical fallback)",
            "Add vision sensor (cameras, blob detection)",
            "Replace rule-based Agent with ML-based (MAEG3080)",
        ],
    },
    4: {
        "name": "Phase 4: Integration & FYP Prep",
        "weeks": "19-24",
        "focus": "Integration, remaining electives, FYP ideas, portfolio",
        "core_courses": [
            "MAEG4998 - Final Year Project I ⭐⭐⭐⭐⭐",
            "MAEG4999 - Final Year Project II ⭐⭐⭐⭐⭐",
            "MAEG4010 - Computer-Integrated Manufacturing",
            "MAEG4020 - Finite Element Modelling and Analysis",
            "MAEG5060 - Computational Intelligence",
            "MAEG5070 - Nonlinear Control Systems",
            "MAEG5090 - Topics in Robotics",
            "MAEG5110 - Quantum Control",
            "ENGG5405 - Theory of Engineering Design",
        ],
        "simulator_tasks": [
            "Final integration demo (everything together)",
            "Multi-robot coordination (extension)",
            "LLM-based Agent thinking (replace rule-based)",
            "Full documentation + portfolio write-up",
            "FYP project proposal + initial implementation",
        ],
    },
}


def get_current_week(today=None):
    """Calculate current bootcamp week number (1-24)"""
    if today is None:
        today = datetime.date.today()
    days_elapsed = (today - BOOTCAMP_START).days
    week_num = (days_elapsed // 7) + 1
    if week_num < 1:
        return 0, "not_started"
    if week_num > TOTAL_WEEKS:
        return TOTAL_WEEKS + 1, "completed"
    return week_num, "active"


def get_phase(week_num):
    """Determine phase from week number"""
    if week_num <= 0:
        return 0
    if week_num <= 6:
        return 1
    if week_num <= 12:
        return 2
    if week_num <= 18:
        return 3
    return 4


def generate_weekly_message(week_num):
    """Generate the weekly focus message"""
    if week_num < 1:
        return f"""🚀 **24-Week Bootcamp** 仲未開始!

開始日期: {BOOTCAMP_START} (第一個星期六)
今日: {datetime.date.today()}

仲有 {(BOOTCAMP_START - datetime.date.today()).days} 日!

準備好嘅話, 之後可以隨時開始. 💪"""

    if week_num > TOTAL_WEEKS:
        return """🎉 **恭喜! 24-Week Bootcamp 完成!**

你已經完成晒 CUHK BEng + PolyU MSc IRE 全部課程!

下一步:
- 整理 portfolio
- 寫 FYP 完整 paper
- 或者開新嘅學習旅程! 🚀"""

    phase_num = get_phase(week_num)
    phase = PHASES[phase_num]

    # Find Saturday date
    today = datetime.date.today()
    days_to_saturday = (5 - today.weekday()) % 7
    if days_to_saturday == 0 and today.weekday() != 5:
        days_to_saturday = 7
    saturday = today + datetime.timedelta(days=days_to_saturday)
    week_end = saturday + datetime.timedelta(days=1)

    msg = f"""🚀 **【24-Week Bootcamp】Week {week_num} / 24**

📅 週末: {saturday} (Sat) - {week_end} (Sun)
🎯 Phase: {phase['name']} (Week {phase['weeks']})
📚 焦點: {phase['focus']}

---

**📖 理論 (Saturday AM, 3-4 小時):**
"""

    # Show 2-3 core courses to focus on this week
    courses_to_show = phase['core_courses'][:3]
    for c in courses_to_show:
        msg += f"- {c}\n"

    if len(phase['core_courses']) > 3:
        msg += f"- *仲有 {len(phase['core_courses']) - 3} 個 core courses*\n"

    msg += f"""
**💻 實踐 (Saturday PM, 3-4 小時):**
"""
    for task in phase['simulator_tasks'][:2]:
        msg += f"- {task}\n"

    msg += f"""
**📝 反思 (Sunday AM, 2-3 小時):**
- 更新 phase{phase_num}_* 嘅 notes
- 更新 [`progress.md`](./progress.md) 嘅 Week {week_num}
- 寫 short reflection 喺 commit message

---

**💡 提示:**
- Git commit 之後寫清楚做咗咩
- 如果有問題, 隨時 message 我
- 唔好 perfectionism, 8-12 小時做完就 OK!

💪 加油! Week {week_num} 衝刺!
"""
    return msg


def get_daily_reminder(week_num):
    """Generate weekday evening reminder (lighter)"""
    phase_num = get_phase(week_num)
    if phase_num == 0:
        return None  # No daily reminder before bootcamp starts
    if phase_num > 4:
        return None  # No daily reminder after bootcamp ends
    phase = PHASES[phase_num]
    return f"""📚 **24-Week Bootcamp Week {week_num}** - 平日 review 提示

🎯 Phase: {phase['name']}

今晚 15-30 分鐘可以 review 嘅:
- 返睇上週嘅 simulator commit
- 重温 {phase['core_courses'][0]} 嘅 notes
- 或者睇下 Week {week_num + 1} 嘅預習

💪 唔使強迫, 輕鬆就好!"""


def main():
    today = datetime.date.today()
    week_num, status = get_current_week(today)
    if status == "not_started":
        msg = generate_weekly_message(0)
    elif status == "completed":
        msg = generate_weekly_message(TOTAL_WEEKS + 1)
    else:
        msg = generate_weekly_message(week_num)
    print(msg)
    # Also output as JSON for structured consumption
    output = {
        "today": today.isoformat(),
        "week_num": week_num,
        "status": status,
        "phase": get_phase(week_num) if status == "active" else None,
        "message": msg,
    }
    print("\n--- JSON ---")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
