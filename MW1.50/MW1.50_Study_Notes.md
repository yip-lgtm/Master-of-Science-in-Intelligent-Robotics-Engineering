# MW 1.50 – Supporting Structure for Building Services
## 自學筆記（Reference Report 分析）

---

## MW 1.50 官方描述

**MWTGe.pdf Item 1.50**：
> 豎設或改動支承只用於電訊服務既無綫電通訊站既構築物或金屬箱

**位置**：(a) 地面上 (b) 屋頂上（非懸臂式平板）(c) 簷篷上（非懸臂式平板）

**限制**：
- 機組櫃：長度 ≤ 1.5m，闊度 ≤ 1m，高度 ≤ 2.3m
- 天線/收發器：高度 ≤ 2.5m
- 其他設備：高度 ≤ 1.5m
- 不可增加懸臂板荷載

---

## Case Study 1: CS222 Waffle Slab (設備基礎)

### 5. Loading (Step-by-Step)
```
Plant total = 3845 kg → 3.29 kPa
Concrete plinth SDL = 4.6 kPa
Total Imposed = 7.89 kPa
ULS: 1.4 SDL + 1.6 LL = 14.72 kPa
```

### 6. Structural Analysis (Step-by-Step)
```
Waffle Slab: M* = 3.3 kNm/m, V* = 6.6 kN
Rib Beam: M* = 119.4 kNm, V* = 51.34 kN
```

### 7. Member Capacity (Step-by-Step)
```
Slab: k = 0.006 < 0.156 (balanced)
Ast req = 195 mm²/m
Provide T12@350 = 323 mm²/m O.K.
v = 0.06 < vc = 0.709 O.K.

Rib Beam: K = 0.047 < 0.156
Provide 2T20 tension + 2T16 compression
v = 0.491 < vc + vr
Deflection 17.55 < 27.1 O.K.
```

---

## Case Study 2: Cooling Tower Frame (钢结构)

### 5. Loading (Step-by-Step)
```
DL = 15 kN/tower
LL per leg = 3.75 kN
Wind = 5.52 kPa (Z-dir governing)
ULS: 1.4DL + 1.6LL + 1.2Wind_Z
```

### 6. Structural Analysis (STAAD.Pro)
```
Max: Fx = 39.1 kN, Mxx = 16.1 kNm, Vy = 38.4 kN
(ULS D+L+Wz)
```

### 7. Member Capacity
```
M_cap = 62.44 kNm > 16.1 kNm O.K.
V_cap = 380.2 kN > 38.4 kN O.K.
Interaction = 0.12 < 1.0 O.K.
```

### 8. Deflection Check
```
δ_max = 3.42 mm < L/200 = 4.25 mm O.K.
```

### 9. Anchor & Weld
```
Hilti HST3-R M12: 92% util O.K.
5mm fillet weld: 174.3 MPa < 220 MPa O.K.
```

---

## Case Study 3: Kai Oi School Steel Frame

### 5. Loading (Step-by-Step)
```
DL (wooden board) = 0.618 kPa
Notional horizontal = 0.5 kPa
ULS: 1.4DL + 1.6LL
```

### 6. Structural Analysis (SAP2000)
```
Max: P = 0.84 kN, V = 1.1 kN, M = 0.159 kNm
```

### 7. Member Capacity
```
V_c = 39.69 kN > 1.1 kN
M_b = 0.6 kNm > 0.159 kNm
Interaction = 0.49 < 1.0 O.K.
```

### 8. Connections
```
5mm fillet weld: 163.93 N/mm² < 770 N/mm² O.K.
Hilti HST3-M10 anchors (SF=3.0) O.K.
```

---

## Key Formulas

### Concrete Design (BS 8110)
```
k = M* / (fcu * b * d^2)
K_bal = 0.156 (balanced section)
Ast = M* / (0.87 * fy * z)
z = d[0.5 + sqrt(0.25 - k/0.9)]
v = V* / (b * d)
vc = 0.79 * (100As/bd) * (fcu/25)^(1/3) * (400/d)^(1/4)
```

### Steel Design (CoP Steel 2011)
```
M_cap = Sx * py
V_cap = 0.6 * py * Av
Deflection: δ < L/200
```

### Wind Load (CoP Wind 2019)
```
Pz = 0.5 * ρ * Vz^2 * Cz * Cs * Cd * Ca
```

### Anchor Bolt (PROFIS / ETAG 001)
```
N* < NRD
V* < VRD
(M*/N*) + (V*/V*) < 1.0
```

---

## Common Design Checks

| 項目 | Formula | Limit |
|------|--------|-------|
| Slab bending | k < 0.156 | Balanced |
| Steel moment | M* < M_cap | Capacity |
| Shear | v < vc | Capacity |
| Deflection | δ < L/200 | Serviceability |
| Weld | f < 220 MPa | Allowable |
| Anchor | Util < 100% | Capacity |