# MW 1.50 鋼支承架報告 Workflow 完整教學
## 自學筆記（Based on CS-223）

---

## Workflow 總覽（10 大步驟）

1. **Design Brief** → 設計簡介
2. **Structural analysis** → 結構分析方法  
3. **Design Information** → 設計資料
4. **Design parameters** → 設計參數
5. **Design load** → 荷載計算
6. **Design check** → 主樑檢查
7. **Checking of main beam** → 主樑檢查
8. **Checking of short column** → 短柱檢查
9. **Checking of CH + Welding + Plate + Shear + Overturn + Block Shear** → 細部檢查
10. **Conclusion + RSE 親簽** → 結論

---

## Step 1: Design Brief（設計簡介）

**模板**：
> Design check of the steel frame support for the Air-cooled magnetic levitation unit. The reaction force from the machine units transfers to the steel beams of CH 100×50×10 kg/m then transfers to the 200 mm steel short post support CH 100×50×10 kg/m which sits on the waffle slab.

**目的**：讓審批人 10 秒內知道這係 MW 1.50 鋼架項目。

---

## Step 2: Structural analysis（結構分析方法）

**模板**：
> The steel frame is modelled as simply supported beams with short posts. Total 6 nos. of supporting posts. Wind load is converted to additional point load at each reaction point.

---

## Step 3: Design Information（設計資料）

**表格**：

| Item | Value |
|------|-------|
| Location | 2/F which the new plant is sitting |
| No. of posts | Total 6 nos. |
| Drawing | Structural frame layout and detail |

---

## Step 4: Design parameters（設計參數）

**表格**：

| Item | Value |
|------|-------|
| Main Beam (MB) | CH 100×50×10 |
| Secondary Beam (SB) | CH 100×50×10 |
| Post Beam (PB) | CH 100×50×10 |
| Steel grade | S275 |
| Bolts | Hilti HST3-R-M10 |
| Plate | 150×150×6 mm thk |
| Weld | 4 mm F.W. min 50 mm |

---

## Step 5: Design load（荷載計算 – 最重要步驟）

### Step 5.1：機器反力（supplier data）
列出 8 個點荷載（kg）

### Step 5.2：ULS 轉換
```
P1 = 306 × 9.81 / 1000 × 1.4 = 4.28 kN
```
（依此類推）

### Step 5.3：風荷載
```
W = 0.85 × 1.59 × 1.4 = 1.89 kPa
W1 = 1.89 × 5.2 × 2.4 × 1.4 = 4.13 kN / 每點
```

### Step 5.4：設計包絡荷載
```
Max Reaction R* = 26.4 kN（呢個係後面所有檢查既控制值）
```

---

## Step 6: Design check（主樑檢查）

**模板**（直接抄 CS-223）：
> 
> **Vertical load model**:
> Shear force distribution: Max V* = 14.2 kN
> Bending moment distribution: Max Sag M* = 3.1 kNm, Max Hog M* = 6.9 kNm
> Deflection: Max δ = 4.2 mm
> 
> **Envelope summary**:
> Mx* = 6.9 kNm
> My* = 2.4 kNm  
> V* = 14.2 kN
> δ* = 4.2 mm < L/200 = 11.98 mm → O.K.

---

## Step 7: Checking of short column（短柱檢查）

**模板**：
> Height of post = 200 mm
> Max reaction = 26.4 kN
> Max bending = 1.76 kNm
> Compression capacity = 253 kN > 26.4 kN (util 0.10) → O.K.
> Bending capacity = 12.2 kNm > 1.76 kNm (util 0.14) → O.K.
> Axial + Bending util = 0.65 < 1.0 → O.K.

---

## Step 8: Checking of CH + Welding + Plate + Shear + Overturn + Block Shear

### Welding check：
```
Design Shear = 14 kN
Weld strength = 0.7 × 220 × 4 = 616 N/mm > 284 N/mm (util 0.46) → O.K.
```

### Plate check：
```
Provide 150×150×6 mm plate
A_req = 1760 mm² < 22500 mm² → O.K.
```

### Shear Check：
```
Vc = 21.4 kN > 14 kN → O.K.
```

### Overturn Check（最常被問）：
```
Ow = 28.34 kNm
OD = 39.45 kNm
F.O.S = 1.671 > 1.5 → O.K.
（結論：pure compression）
```

### Base bolts check：
```
4 nos. Hilti HST3-R-M10
Per bolt = 6.6 kN
Shear util 0.46 / Tension util 0.63 → O.K.
（必須夾 Hilti PROFIS 報告）
```

---

## 最終報告結構建議（直接套用）

1. 封面（含 RSE 簽名欄）
2. Design Brief
3. Structural analysis
4. Design Information + 圖則
5. Design parameters（表格）
6. Design load（step-by-step + 表格）
7. Design check（主樑 + 短柱 + CH）
8. Welding + Plate + Shear + Overturn + Block Shear + Thickness check
9. Base bolts check（夾 PROFIS）
10. 結論 + RSE 親簽

---

## Key Formulas Summary

| 項目 | Formula | Limit |
|------|--------|-------|
| ULS Load | P* = P × 1.4 | - |
| Wind | W = 0.85 × Vz² × Cp | - |
| Moment | M* = F × L | < M_cap |
| Shear | V* | < V_cap |
| Deflection | δ | < L/200 |
| Weld | f_w = V / (0.7 × a × L) | < 220 N/mm |
| Overturn | FOS = OD / Ow | > 1.5 |
| Anchor | Util | < 100% |