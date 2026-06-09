# ICE IPD / CPD / DAP Progress Tracker

> **KANG YIP SZE 施耿業 — Assistant Engineer (Geotechnical)**
> **ICE No.**: 093984510 (GMICE) | **HKIE No.**: GW0968329
> **Mentor**: Dr. Alberto Ortigão (CEng FICE) | **Company**: Kam Tat Surveyors LTD
> **Route**: Mentor-supported Training → CEng MICE / MHKIE (General Experience)
> **Period**: Aug 2025 – May 2026 (v2.0)

## 🎯 What This Does

A weekly cron-driven tool that:
1. **Reads** your existing DAP.xlsx (5 sheets: Cover/CPD/DAP/Work/Mentor)
2. **Auto-generates** 5 new DAP tasks from current project work
3. **Maps** each task to ICE 7 Attributes (2022 onwards)
4. **Generates** bilingual (中/英) weekly report
5. **Appends** new tasks to DAP.xlsx (yellow highlight for review)
6. **Suggests** CPD activities to fill Attribute gaps

## 📁 Structure

```
ipd-tracker/
├── DAP.xlsx                      # 5 sheets: Cover/CPD/DAP/Work/Mentor
├── reports/
│   └── IPD_Weekly_YYYY-MM-DD.md  # Weekly reports
├── evidence/                     # Original logbooks (input)
│   ├── CPD_Logbook_KANG_YIP_SZE_ICE_IPD_Complete.xlsx
│   └── KANG_YIP_SZE_CPD_IPD_Logbook_v2_June2026.xlsx
├── templates/
│   └── IPD_Online_Template.md    # IPD Online format
└── README.md
```

## 📊 Current Status (as of 2026-06-09)

| Metric | Value |
|--------|-------|
| **CPD Hours Total** | 94.5 h (ICE recommends ≥30/year) ✅ EXCEEDS |
| **CPD Entries** | 27 (mix of self-study + formal events) |
| **DAP Tasks Historical** | 21 (20 Achieved, 1 In Progress) |
| **DAP Tasks New (Jun 2026)** | 5 (yellow highlight) |
| **Work Experience** | 5 projects (YLC, MW01, I&M, etc.) |
| **Mentor Meetings** | 3 (Jan/Apr/May 2026) |

## 📈 Hours by ICE Attribute

| # | Attribute | Hours | Status |
|---|-----------|-------|--------|
| 1 | Understanding and Practical Application of Engineering | 28.5 | ✅ Strong |
| 2 | Management and Control | 18.0 | ✅ Strong |
| 3 | Commercial Ability / Health, Safety and Welfare | 3.0 | ⚠️ Medium |
| 4 | Sustainable Development | 4.5 | ⚠️ Medium |
| 5 | Communication | 12.0 | ✅ Strong |
| 6 | Professional Commitment and Ethical Conduct | 10.5 | ✅ Strong |
| 7 | Technical Leadership | 22.0 | ✅ Strong |

## 📋 Existing 5 Projects (Work Experience)

1. **Yuet Lai Court Dangerous Hillside Order (Kwai Chung)** — FOS 0.870 → 1.4 after remediation
2. **Kwai Chung Lai Cho Road — 4-year I&M contract**
3. **Minor Works Class 1 — Metal Protective Barriers (Yau Lai Estate)**
4. **MBIS/MWIS Tender Preparation & Submission**
5. **FSI Submissions & Minor Works Statutory Compliance**

## 📅 Recent Mentor Meetings

| Date | Type | Key Outcomes |
|------|------|--------------|
| 2026-01-14 | Initial Setup | Approved route, focus on slope/geotech |
| 2026-04-13 | Mid-IPD Review | YLC FOS 0.870, more commercial exposure needed |
| 2026-05-20 | Portfolio Prep (planned) | Final sign-off target end June 2026 |

## 🚀 Quick Start

```bash
# Run weekly
python3 /app/skills/cpd_ipd_dap_progress_cron.py

# Rebuild DAP.xlsx from real logbooks
python3 /app/skills/build_dap_from_logbooks.py
```

## 🔄 Cron Setup

```bash
openclaw cron add --name "ICE_IPD_Weekly" \
  --cron "0 8 * * 1" --tz "Asia/Hong_Kong" \
  --system-event "cpd_ipd_dap_progress_cron" --wake now
```

## 💡 Immediate Action Items (from mentor feedback)

1. **Continue** — keep logging CPD (already at 94.5h, exceeds 30h/year target)
2. **More commercial exposure** — mentor flagged this gap in Apr 2026 review
3. **Mock PR** — completed May 2026 workshop, target sign-off by end June 2026
4. **IStructE CM** — consider next year (post-CEng MICE)

## 🔗 Related Skills

- `cpd_ipd_dap_progress_cron.py` — Weekly tracker
- `build_dap_from_logbooks.py` — Build/merge DAP from raw .xlsx
- `bootcamp_weekly.py` — 24-Week Bootcamp
- `bootcamp_sunday_summary.py` — Sunday reflection
- `bootcamp_log.py` — Quick progress logger

**Last Updated:** 2026-06-09
