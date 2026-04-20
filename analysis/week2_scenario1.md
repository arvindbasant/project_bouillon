# Week 2 — Scenario 1: Maximize Indy

**Week:** 2 · **Day:** 1 (Wed 2026-04-15)
**Scope:** Quantify the S1 addressable pool · separate already-booked from net-new · build glidepath skeleton
**Source:** `data/monthly_volume.csv` · `data/sku_master.csv`

---

## 1. Headline

> **The Scenario 1 transfer is already ~55% complete by tonnes.** Of the 12,488 t total S1 pool (Lerma 2 lb + 15.9 oz production), 4,445 t was at Indy in 2025 and growing fast. At H2 2025 run rates, Indy is already running 7,475 t/yr of S1 volume. The remaining Lerma S1 volume to capture is **~3,684 t/yr** — overwhelmingly concentrated in one SKU.
>
> **The critical question is no longer "can we transfer" — it's "how much faster than the current trajectory, and does line 15 have the headroom to absorb 3,684 additional tonnes per year?"**

---

## 2. The S1 pool — full picture

The S1 addressable pool is all Lerma volume in formats Indy already runs: 2 lb Large Granulated + 15.9 oz Small Granulated.

| | Cases | Tonnes | % of Network Tonnes |
|---|---:|---:|---:|
| **S1 total pool** (Lerma + Indy in S1 formats) | 1,476,494 | 12,488 t | 28.9% |
| Already at Indy (2025 FY) | 657,942 | 4,445 t | 10.3% |
| Still at Lerma (2025 FY) | 818,552 | 8,044 t | 18.6% |

**All 9 SKUs in the S1 pool are already in-flight transfer.** There are no Lerma-only S1 SKUs that haven't started moving. The question is velocity, not direction.

---

## 3. SKU-level transfer status

| SKU | Lerma t | Indy t | Total t | % Indy | Status |
|---|---:|---:|---:|---:|---|
| KNR MEX BOUIL CHK 6 2 LB | 5,449 | 952 | 6,401 | **14.9%** | **EARLY — biggest lever** |
| KNR MEX BOUIL CHK 12/15.9 OZ | 1,182 | 1,213 | 2,395 | 50.6% | Partial |
| KNR MEX BOUIL Beef 6 2 LB | 1,003 | 587 | 1,590 | 36.9% | Partial |
| KNR MEX BOL TOM/CHK 6 2 LB | 52 | 1,237 | 1,290 | **95.9%** | Nearly done |
| KNORR BOUIL TOM/CHK 12/15.9 OZ | 263 | 295 | 558 | 52.8% | Partial |
| KNR MEX BOUIL BEEF 12 15.9z | 92 | 159 | 251 | 63.4% | Partial |
| 3 small UI/trace SKUs | 2 | 2 | 5 | ~60% | Trace |

**Key read:** the top 3 SKUs account for 83% of the S1 pool by tonnes. The flagship CHK 6 2 LB alone is 51% of the total S1 pool and is the least migrated (15% at Indy).

---

## 4. The H2 2025 velocity picture — transfer is accelerating

| SKU | H1 Lerma (cases) | H2 Lerma (cases) | H1 Indy (cases) | H2 Indy (cases) | Direction |
|---|---:|---:|---:|---:|---|
| KNR MEX BOUIL CHK 6 2 LB | 740,800 | 260,352 | 33,203 | 141,710 | →INDY ↑ |
| KNR MEX BOUIL CHK 12/15.9 OZ | 189,435 | 29,054 | 59,899 | 164,310 | →INDY ↑ |
| KNR MEX BOUIL Beef 6 2 LB | 137,300 | 47,005 | 13,313 | 94,449 | →INDY ↑ |
| KNR MEX BOL TOM/CHK 6 2 LB | 9,600 | 0 | 7,957 | 219,348 | →INDY ✓ done |
| KNORR BOUIL TOM/CHK 12/15.9 OZ | 46,418 | 2,207 | 9,408 | 45,034 | →INDY ✓ |
| KNR MEX BOUIL BEEF 12 15.9z | 16,963 | 0 | 6,589 | 22,858 | →INDY ✓ done |

**All 9 SKUs show Lerma declining H1→H2 and Indy increasing H1→H2.** The transfer is directionally unambiguous and accelerating.

### H2 2025 annualized run rate (proxy for early-2026 state)

| | Annualized from H2 2025 | Notes |
|---|---|---|
| **Indy S1 run rate** | **7,475 t/yr** | Up from ~4,445 t FY 2025 |
| **Lerma S1 remaining** | **3,684 t/yr** | Down from ~8,044 t FY 2025 |
| Flagship CHK 6 2 LB at Lerma | 2,834 t/yr | Dominates the remaining pool |
| All other S1 SKUs at Lerma | ~850 t/yr | Nearly fully transferred |

**The remaining S1 opportunity is almost entirely one SKU.** If the CHK 6 2 LB transfer completes at H2 velocity, it contributes ~2,834 t/yr net-new to Indy and ~1,543 t/yr is already flowing.

---

## 5. What this means for the S1 glidepath

### 5a. What's effectively already done (no Week-2 decision needed)

By the H2 2025 data, 7 of 9 S1 SKUs are ≥66% at Indy. At current velocity, these complete by mid-2026 without any new decision:
- TOM/CHK 6 2 LB → 100% at Indy in H2 2025 (done)
- BOUIL BEEF 12 15.9z → 100% at Indy in H2 2025 (done)
- CHK 12/15.9 OZ → 85% at H2 run rate; completion expected Q1-Q2 2026
- BOUIL TOM/CHK 12/15.9 OZ → 95% at H2 run rate; completion expected Q1 2026
- BOUIL Beef 6 2 LB → 67% at H2 run rate; completion expected Q2-Q3 2026

**Total "already in motion" volume at Indy by end 2026: ~4,641 t/yr** (excluding CHK 6 2 LB)

### 5b. The active decision: CHK 6 2 LB

The flagship (KNR MEX BOUIL CHK 6 2 LB) is 6,401 t total, with **2,834 t still at Lerma** at H2 2025 run rate. This single SKU is the dominant S1 decision:

| | Indy today (H2 rate) | After full transfer | Incremental |
|---|---:|---:|---:|
| CHK 6 2 LB at Indy | 1,543 t/yr | 4,377 t/yr | **+2,834 t/yr** |
| All Indy S1 | 7,475 t/yr | 10,309 t/yr | **+2,834 t/yr** |

**This is the single number that matters for Scenario 1:** can Indy line 15 absorb **+2,834 t/yr (280K additional cases/yr)** on top of the H2 2025 rate?

If yes → S1 is fully executable, no new line required, probably complete by end 2026.
If no → the decision is: (a) cap S1 at line-15 ceiling, (b) invest in a second line or additional shifts at Indy.

### 5c. What D3 (Indy capacity) unlocks

| With D3 available | Without D3 (current state) |
|---|---|
| Know exact line-15 headroom in tonnes/yr | Can only say "gap is ~2,834 t" |
| Know if CHK 6 2 LB can complete without investment | Framed as binary question only |
| Can size a second-line/shift investment if needed | Can signal it's needed but not scope it |
| Can date-stamp S1 completion | Can say "completion likely 2026" directionally |

---

## 6. Scenario 1 glidepath skeleton (data-dependent, current structure)

### Year 1 (2026) — Complete the in-flight transfer

| Action | Volume | Tonnes | Gate |
|---|---|---|---|
| Complete CHK 12/15.9 OZ transfer | ~29K cases remaining at Lerma | ~157 t | No gate — already in motion |
| Complete Beef 6 2 LB transfer | ~47K cases/6 months at Lerma | ~512 t remaining | No gate — already in motion |
| Begin CHK 6 2 LB acceleration | 260K at Lerma H2 → target 0 | ~2,834 t/yr | **Gate: line-15 headroom (D3)** |
| **Indy S1 run rate target EoY 2026** | **~830-860K cases** | **~4,600-4,700 t** | Contingent on D3 |

### Year 2 (2027) — Full S1 at Indy

| Action | Volume | Tonnes | Gate |
|---|---|---|---|
| CHK 6 2 LB fully at Indy | 400K→520K cases/yr at Indy | 2,175-2,834 t/yr | D3: confirmed headroom |
| All S1 formats stable at Indy | ~1.48M cases total | ~8,044 t/yr | — |
| Lerma S1 production → 0 | 0 cases | 0 t | Lerma reallocates Mateer 3 to other formats |

### Year 3 (2028) — Steady state

| | Cases | Tonnes | Indy line-15 load |
|---|---:|---:|---|
| All S1 at Indy (steady state) | ~1.48M | ~8,044 t | ~1.8× today's run rate — second line likely required |
| Lerma freed (Mateer 3) | 3,471K → will run 7.9 oz + 3.5 oz at Mateer 1 only | — | Lerma simplified to Mateer 1 + 2 |

---

## 7. The second-line question

Indy's current H2 2025 annualized run rate is ~7,475 t/yr. The full S1 steady-state is ~8,044 t/yr. The incremental is **~570 t/yr** above the current run rate on line 15.

However, line 15 was already running at some utilization level in H2 2025. We don't know if 7,475 t/yr is 70% utilization or 95% utilization. **This is the exact gap D3 fills.**

Rough bounds (pending D3):
- If line 15 theoretical max ≈ 9,000-10,000 t/yr (typical for single food-grade granulation line), steady-state S1 is comfortably within one line.
- If line 15 theoretical max ≈ 7,500-8,000 t/yr, Indy is already near ceiling and CHK 6 2 LB completion requires a second line or additional shifts.

**Decision structure:**
```
D3 line-15 capacity → compare to 8,044 t/yr S1 steady-state
         │
         ├── Headroom exists → S1 complete on line 15 alone  (LOW CAPEX path)
         │
         └── No headroom → second-line / shift investment required  (MEDIUM CAPEX path)
                    │
                    └── If capex approved → S1 on 2 lines by 2027; Lerma Mateer 3 freed
```

---

## 8. Assumptions & open items

1. **All H2 annualized figures** assume H2 2025 is representative of the transfer trajectory. A deliberate Q3 pause (consistent with the Sep-25 zero finding in the monthly data) followed by Oct-25 ramp suggests H2 is a better proxy for 2026 than FY 2025 averages.
2. **"Net new" is dominated by one SKU.** The analytical leverage is almost entirely on CHK 6 2 LB. All other S1 SKUs appear to be completing transfer without a Week-2 decision.
3. **Tonnes/case for 2 lb ≈ 5.4 kg.** Used for all case-to-tonne conversions on this SKU.
4. **Line-15 headroom is the only hard unknown.** The direction, velocity, and SKU-level specifics are clear from the data. The constraint is physical capacity, not will.
5. **D8 (formal transfer program status)** — if the in-flight transfers are tracked against formal milestones, the glidepath above may already have committed dates. Week 2 should confirm whether the "net new" framing above agrees with the sponsor's program records.
