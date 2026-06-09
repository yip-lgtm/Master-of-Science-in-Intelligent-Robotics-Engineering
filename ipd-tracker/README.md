# ICE IPD / CPD / DAP Progress Tracker

> **Auto-tracks ICE IPD 7 Attributes evidence from real project work**
> **Project**: 悅麗苑 Yuet Lai Court 11NW-A/C16 斜坡維修工程
> **Stage**: Remedial works (Pit-by-pit no-fines concrete + soil nailing + I&M)

## 🎯 What This Does

A weekly cron-driven tool that:
1. **Reads** your existing DAP.xlsx (32 tasks 100% achieved in 2025)
2. **Auto-generates** 5 new DAP tasks from current project work
3. **Maps** each task to ICE 7 Attributes (2022 onwards)
4. **Generates** bilingual (中/英) weekly report
5. **Appends** new tasks to DAP.xlsx (yellow highlight for review)
6. **Suggests** CPD activities to fill Attribute gaps

## 📁 Structure

```
ipd-tracker/
├── DAP.xlsx                      # 32 (2025) + 5 (2026) = 37 tasks
├── reports/
│   └── IPD_Weekly_YYYY-MM-DD.md  # Weekly reports
├── evidence/                     # Upload evidence here
├── templates/
│   └── IPD_Online_Template.md    # IPD Online format
└── README.md
```

## 🏃 Quick Start

```bash
# Run weekly (default: this Monday's report)
python3 /app/skills/cpd_ipd_dap_progress_cron.py

# Use custom DAP path
python3 /app/skills/cpd_ipd_dap_progress_cron.py --dap /path/to/DAP.xlsx

# Custom output directory
python3 /app/skills/cpd_ipd_dap_progress_cron.py --output-dir /custom/reports
```

## 📋 ICE IPD 7 Attributes (2022)

| # | Attribute | Chinese |
|---|-----------|---------|
| 1 | Understanding and Practical Application of Engineering | 工程學理解與應用 |
| 2 | Management and Control | 管理與執行 |
| 3 | Health, Safety and Welfare | 健康、安全與福利 |
| 4 | Sustainable Development | 可持續發展 |
| 5 | Communication | 溝通 |
| 6 | Professional Commitment and Ethical Conduct | 專業承諾與道德 |
| 7 | Technical Leadership | 技術領導力 |

## 🎓 Current DAP Tasks (37 total)

### 2025 Tasks (32, all Achieved ✅)
- **GI (5)**: Survey, mapping, trial pits, sampling, GW monitoring
- **Design (8)**: SLOPE/W, PLAXIS 3D, soil nail, drainage, manual, BD submission
- **Tender (3)**: Tender docs, assessment, contract award
- **Construction (16)**: H&S plan, MS, RA, PTW, supervision, monitoring, pit work, soil nails

### 2026 Tasks (5, new this week — yellow highlight)
1. **YLC-Remedial-01** — Pit-by-pit no-fines concrete replacement 施工監督 (Attr 1, 2, 3, 7)
2. **YLC-Remedial-02** — Soil nail installation + pull-out test (Attr 1, 3, 5, 6)
3. **YLC-Monitoring-01** — Bi-weekly monitoring report (Attr 1, 3, 5, 7)
4. **YLC-CPD-Leadership** — Internal lunch-and-learn (Attr 7 ⭐)
5. **YLC-Sustainability-01** — Drainage re-check + Maintenance Manual (Attr 2, 4, 5)

## 🔄 Cron Setup

```bash
# Every Monday 8:00 AM HKT
openclaw cron add \
  --name "ICE_IPD_Weekly" \
  --cron "0 8 * * 1" \
  --tz "Asia/Hong_Kong" \
  --system-event "cpd_ipd_dap_progress_cron" \
  --wake now
```

## 💡 3 Things To Do Now

1. **Execute** — Pick 1-2 new tasks, start + photo/sign record (strongest evidence)
2. **Mentor discussion** — Schedule with Dr. Alberto Ortigão, share this report
3. **Tech talk** — Prepare internal lunch-and-learn (YLC case study) for Attr 7 + CPD hours

## 🔗 Related Skills

- `bootcamp_weekly.py` — 24-Week Bootcamp weekly reminder
- `bootcamp_sunday_summary.py` — Sunday reflection
- `bootcamp_log.py` — Quick progress logger
- `cpd_ipd_dap_progress_cron.py` — IPD/DAP tracker (this file)

## 📊 Why This Works

- **Auto-mapping** — Task → Attributes 自動, 你唔使諗
- **Bilingual** — 中英並列, IPD Online 同 internal 用都得
- **CPD filling** — 自動 identify Attributes 缺口 + suggest 活動
- **Yellow highlight** — 你 review 過先 confirm, 唔會盲 add
- **DAP.xlsx 直接** — 唔使人手輸入 Excel

**Last Updated:** 2026-06-09
