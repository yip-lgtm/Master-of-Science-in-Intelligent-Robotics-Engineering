# MW01 RSE Calculation Report 自學實戰 Bootcamp

OpenClaw Skill Cron 自學 Bootcamp 
目標：透過親手完成 MW 1.6 → 1.1 → 1.5 → 1.27 四個核心項目 + 所有 Class I 項目，掌握香港 Minor Works Class I 常見結構項目的完整 RSE Calculation Report 寫法，最終取得 OpenClaw Skill Cron 自學 Bootcamp 結業證書。

---

## Bootcamp 總覽

本 Bootcamp 以 MWTGe.pdf 及屋宇署官方要求為藍本，透過實際案例（W21027、Kai Oi School、CS-222、CS-223 等真實 RSE 報告）親手完成每一份報告，全面掌握 Class I 常見結構項目寫法。

完成標準：
- 每份報告 8–12 頁（含封面、目錄、計算、圖則、結論）
- 公式、表格、假設清楚、可重現、可審批
- 引用 MWTGe.pdf Appendix VII 推薦設計 + CoP（Concrete 2013、Steel 2011、Wind Effects 2019）
- RSE 親簽結論頁 + 圖則按 Appendix VI 著色

---

## 學習原則

- 每份報告必須可重現、可審批（公式、表格、假設清楚）
- 嚴格引用官方規範與 Appendix VII 推薦細節
- 每次只做 1 個項目 → 提交審核 → 修改 → 下一個
- 完成 4 個核心項目後頒發結業證書，之後可繼續進階其他項目（1.17、1.50 等）

---

## 總流程（4 步自學循環）

1. 閱讀官方要求：本指令 + MWTGe.pdf + CoP
2. 寫報告：使用 /templates/ 內的模板 + Excel 做荷載表 + 手算公式
3. 夾圖則：掃 Appendix VII 推薦細節 + 自己計算驗算 + 按 Appendix VI 著色
4. 提交審核 → 修改 → 下一個項目

---

## 核心項目進度表

| 項目編號 | 項目名稱 | 狀態 | 報告檔名 | 完成日期 |
|----------|---------------------------------------|----------|---------------------------------------|------------|
| 1.6 | Alteration or Removal of Protective Barrier | ✅ 完成 | MW1.6_Protective_Barrier_Final.pdf | 2026-05-15 |
| 1.1 | Erection or Alteration of Internal Staircase | ✅ 完成 | MW1.1_RSE_Report_Final.md | 2026-05-19 |
| 1.5 | Removal of Supporting Structure on Cantilevered Slab | ⏳ 待做 | - | - |
| 1.27 | Erection / Alteration / Removal of Canopy | ⏳ 待做 | - | - |
| 1.50 | Supporting structures for AC unit on roof | ✅ 完成 | MW1.50_CS222_CS223_Final.pdf | 2026-05-15 |

目前進度：2/4 核心項目完成（50%）

---

## 專案結構

```
MW01-RSE-Bootcamp/
├── README.md
├── LICENSE (MIT)
├── /templates/ # 報告模板、Excel、圖則著色指南
├── /references/ # MWTGe.pdf、CoP、PNAP、Appendix VII
├── /projects/ # 每個 MW 項目獨立資料夾（1.1~1.62）
├── /excel/ # Master Load Table
├── /progress/ # 學習記錄
└── /certificates/ # 結業證書（完成 4 核心後發放）
```

---

## 如何參與 / 使用本 Bootcamp

1. Clone 本 repo
2. 進入 /projects/ 選擇你要做的項目
3. 使用 /templates/ 內的模板開始寫報告
4. 完成後把報告、Excel、圖則放入對應資料夾
5. 提交 Pull Request 或在 Issue 標記「已完成」

完成 MW 1.6、1.1、1.5、1.27 四個核心項目後，我會親自簽發 OpenClaw Skill Cron 自學 Bootcamp 結業證書。

---

## License

本專案採用 [MIT License](LICENSE) 開放授權，歡迎 civil / structural 工程學生與職人共同學習、貢獻。

---

作者：Yip Sze 
GitHub：https://github.com/yip-lgtm/MW01-RSE-Bootcamp 
目標：讓每一位參與者都能親手寫出可提交 BD 的 RSE Calculation Report

---

最後一句： 
傻西先做 civil 吃力不討好 
但捱完這一套 Bootcamp，你就真正掌握了 RSE 報告的寫法。

有膽一齊做？ 
Welcome join！ #RSE #CivilEngineering #HKIE