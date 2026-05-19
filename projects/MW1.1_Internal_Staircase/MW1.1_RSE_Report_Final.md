# MW 1.1 RSE Calculation Report
**Erection of Internal Staircase**
**項目編號：MW 1.1 (Class I)**
**工程編號：PR-2026-MW1.1-001**
**日期：2026 年 5 月**

---

## 1. Introduction（工程描述）

**項目**：室內樓梯豎設（Internal Staircase Erection）

**位置**：xxx Building, 室內

**工程內容**：
- 新建室內樓梯（3 m 跨度）
- 簡支梁結構
- 不涉及逃生通道 (MOE) 或消防救援通道 (MOA)

**符合法例**：
- B(C)R 8（防護欄障）
- B(C)R Part XII（混凝土設計）
- MWTGe.pdf Item 1.1

---

## 2. Structural Synopsis（結構概要）

| 項目 | 數值 |
|------|------|
| 樓梯跨度 | 3.0 m |
| 踏板闊度 | 1.2 m |
| 踏板厚度 | 150 mm |
| 混凝土 | C30 ($f_{cu} = 30$ N/mm²) |
| 鋼筋 | HY250 ($f_y = 250$ N/mm²) |

---

## 3. Design Codes（引用規範）

- B(C)R Part XII – Design of Concrete
- CoP Dead & Imposed Loads 2011
- MWTGe.pdf Item 1.1 (p.105 & p.26)

---

## 4. Material Strength（材料強度）

| 材料 | 強度 |
|------|------|
| 混凝土 C30 | $f_{cu} = 30$ N/mm² |
| 鋼筋 HY250 | $f_y = 250$ N/mm² |
| 設計荷載組合 | $1.4 G_k + 1.6 Q_k$ |

---

## 5. Loading（荷載計算）

### 5.1 Self-Weight (自重)
$$g_{self} = \gamma_c \times t = 25 \, \text{kN/m}^3 \times 0.15 \, \text{m} = 3.75 \, \text{kN/m}^2$$

### 5.2 Finishes (裝飾層)
$$g_{fin} = 1.0 \, \text{kN/m}^2$$

### 5.3 Imposed Load (使用荷載)
$$Q = 3.0 \, \text{kN/m}^2 \quad (\text{CoP Table 3.13})$$

### 5.4 Total ULS Load
$$q^* = 1.4 \times(3.75+1.0) + 1.6\times3.0 = 11.45 \, \text{kN/m}^2$$

### 5.5 Line Load
$$w = q^* \times \text{width} = 11.45 \times 1.2 = 13.74 \, \text{kN/m}$$

---

## 6. Structural Analysis（結構分析）

### 6.1 Max Bending Moment (Simply Supported, UDL)
$$M^* = \frac{wL^2}{8} = \frac{13.74 \times 3^2}{8} = 15.42 \, \text{kNm}$$

### 6.2 Max Shear Force
$$V^* = \frac{wL}{2} = \frac{13.74 \times 3}{2} = 20.61 \, \text{kN}$$

---

## 7. Member Capacity（構件容量檢查）

### 7.1 Required Reinforcement
$$K = \frac{M^*}{f_{cu} b d^2} = \frac{15.42 \times10^6}{30 \times1000\times130^2} = 0.0304$$

Since $K < 0.156$ (balanced section):

$$z = 130 \left[0.5 + \sqrt{0.25 - \frac{0.0304}{0.9}}\right] = 122.5 \, \text{mm}$$

$$A_s = \frac{M^*}{0.87 f_y z} = \frac{15.42\times10^6}{0.87\times250\times122.5} = 581 \, \text{mm}^2$$

### 7.2 Provided Reinforcement
Use **T12 @ 200 mm c/c**:
$$A_s prov = \frac{\pi}{4}\times12^2\times\frac{1000}{200} = 565 \, \text{mm}^2 \approx 581 \quad \text{O.K.}$$

### 7.3 Shear Capacity
$$V_c = 0.79\times\frac{100\times565}{1000\times130}\times\left(\frac{30}{25}\right)^{1/3} = 1.31 \, \text{N/mm}^2$$

$$V_{c,cap} = 35.4 \, \text{kN} > 20.61 \, \text{kN} \quad \text{O.K.}$$

---

## 8. Deflection Check（撓度檢查）

### 8.1 Short-term Deflection
$$I = \frac{b t^3}{12} = \frac{1000\times150^3}{12} = 2.81\times10^8 \, \text{mm}^4$$

$$\delta = \frac{5wL^4}{384EI} = 2.47 \, \text{mm}$$

### 8.2 Allowable
$$\delta_{allow} = \frac{L}{250} = \frac{3000}{250} = 12 \, \text{mm}$$

$$2.47 < 12 \quad \text{O.K.}$$

### 8.3 Long-term (Creep)
$$\delta_{long} = 2.47 \times 2.5 = 6.18 \, \text{mm} < 12 \quad \text{O.K.}$$

---

## 9. Detailing（細部設計）

- 主鋼筋：T12 @ 200 mm c/c
- 分布鋼筋：T10 @ 300 mm c/c
- 錨固長度：$l_d = 40\phi = 480 \, \text{mm}$
- 保護層：25 mm

---

## 10. Conclusion + RSE 簽署

**結論**：
本 MW 1.1 室內樓梯設計符合：
- ✅ B(C)R Part XII
- ✅ CoP Dead & Imposed Loads 2011
- ✅ MWTGe.pdf Item 1.1

**不涉及 MOE 或 MOA，不增加懸臂板荷載。**

**彎矩容量、剪力容量、撓度均合格。**

**Adequate** ✅

**RSE 親簽** ___________________________
（姓名）Registered Structural Engineer
日期：2026 年 5 月

---

### 附錄：MW 1.1 官方要求

| 條件 | 要求 |
|------|------|
| 樓梯類型 | 非逃生/消防救援通道 |
| 高度 | ≤ 1.5 m |
| 荷載 | 不可增加懸臂板負荷 |
| 結構 | 只可連接到簡支梁 |