# Current-State Business Baseline — By Site

**Week:** 1 · **Day:** 3 (Wed 2026-04-15) · **Scope:** B — Current-State Business Assessment
**Source:** `data/sku_master.csv`, `data/monthly_volume.csv` · All numbers traceable to `Copy of RT and UFS Bouillon 4.13.26.xlsx`.

---

## 1. One-line view

> **The NA bouillon network is not three factories doing the same job at different scales — it's three disjoint production systems stacked on top of each other.** Indy is a Lerma-mirror: 100% of Indy's 2025 volume is in SKUs also running at Lerma, zero unique products. Batavia is the opposite — 0% overlap with either site; everything Batavia makes is unique to Batavia. Lerma holds both: 38.5% of its volume is in the Indy-shared set (the Scenario-1 addressable pool), the other 61.5% is Lerma-unique (the Scenario-2 capability-build pool). The "consolidate at Indy" question is therefore *two* questions — absorb the overlap, and build from scratch everything else.

---

## 2. One-chart view

```
           2025 NA BOUILLON — SITE × CHANNEL × VOLUME (cases · tonnes)

                              US Retail         UFS       CDA Retail     UI         TOTAL
                              4,330,103      901,837        11,545     2,572      5,246,057

    LERMA  MX  3 lines          3,469,125     371,526           —      2,113      3,842,764   73.3%
                                 ~26.0kt       ~2.7kt                                 ~28.8kt
       Mateer 1/2/3 · 6 formats · Retail + UFS · Sabor + Granulated Bases
       38.5% of Lerma volume is in Indy-shared SKUs (the S1 transfer pool)

    INDY       1 line              818,078           0           —        459       818,537   15.6%
                                  ~4.4kt                                              ~4.4kt
       Line 15 · 2 formats (2 lb + 15.9 oz) · 100% US Retail · 0 UFS
       100% of Indy volume is in multi-site (= Lerma-shared) SKUs

    BATAVIA    2 lines              42,899     530,312       11,545         —       584,756   11.1%
                                   ~0.4kt      ~9.2kt       ~0.4kt                   ~10.0kt
       Line 13 + line 0 · 7 formats · UFS specialist · Caldo / MixMod / Natural
       0% of Batavia volume is shared — every Batavia SKU is unique in the network

    TOTAL                      4,330,103     901,837        11,545     2,572      5,246,057
                                ~31.4kt      ~11.2kt      ~0.4kt                    ~43.2kt
```

**Read:** case share (73 / 16 / 11) is not tonnage share (67 / 10 / 23). Batavia punches twice its case weight in tonnage because its UFS packs are heavy (2.5 lb, 4.4 lb, 7.9 lb, 25 lb). Any "which site makes the most bouillon" conversation needs to specify the unit.

---

## 3. Indy — Independence, MO

### Volume
- **818,537 cases** · **~4,445 tonnes** · 15.6% of NA cases, 10.3% of NA tonnes.
- **Lightest average pack in the network** (5.4 kg/case vs 7.5 at Lerma, 17.1 at Batavia) — consistent with Retail-only small-pack mix.
- **1 physical line** (line "15").

### Channel mix
- **US Retail 99.94%** · **UI 0.06%** · **UFS 0%** · **CDA Retail 0%**.
- Indy is effectively a single-channel site.

### Format mix
- **2 lb Large Granulated**: 509,980 cases (62%)
- **15.9 oz Small Granulated**: 308,557 cases (38%)
- Two formats. Nothing else.

### Top SKUs (2025)
| Rank | SKU | Cases | Share of Indy | Also at |
|---:|---|---:|---:|---|
| 1 | KNR MEX BOL TOM/CHK 6 2 LB | 227,305 | 27.8% | Lerma (9,600) — **96% already at Indy** |
| 2 | KNR MEX BOUIL CHK 12/15.9 OZ | 224,209 | 27.4% | Lerma (218,489) — 51% at Indy |
| 3 | KNR MEX BOUIL CHK 6 2 LB | 174,913 | 21.4% | Lerma (1,001,152) — **15% at Indy** (flagship, least-migrated) |
| 4 | KNR MEX BOUIL Beef 6 2 LB | 107,762 | 13.2% | Lerma (184,305) — 37% at Indy |
| 5 | KNORR BOUIL TOM/CHK 12/15.9 OZ | 54,442 | 6.7% | Lerma (48,625) — 53% at Indy |
| 6 | KNR MEX BOUIL BEEF 12 15.9z | 29,447 | 3.6% | Lerma (16,963) — 63% at Indy |
| — | UI trace | 459 | 0.1% | — |
| | **Total** | **818,537** | **100%** | |

**Every case Indy makes in 2025 is in an SKU also made at Lerma.** Indy has no unique product footprint. This is not a criticism of Indy — it's the evidence that the Lerma → Indy shift is real and already running.

### In-flight transfer status
Indy's Retail volume (818K) sits entirely inside the 6-SKU Lerma ↔ Indy transfer set. The migration ranges from 15% done (the flagship KNR MEX BOUIL CHK 6 2 LB, 1.18M cases in total across both sites) to 96% done (KNR MEX BOL TOM/CHK 6 2 LB). Weighted by volume, the **gross remaining addressable Lerma volume in formats Indy already runs is ~1.48M cases** — of which ~350K appears to be moving in H2 2025 per monthly profile (open data request D8 to confirm).

### Cost / GM / procurement *(directional — gap)*
- **Conversion cost, gross margin, utilization % and shift model are not in the source workbook.** Not estimated here.
- **Directional read:** Indy has the **structural advantage of domestic US Retail logistics** (no cross-border duty, FX, or customs latency) against Lerma on any Retail volume — but without unit cost and line-15 utilization data this cannot be quantified for the Week-1 pack. Logged as P0 data requests D1, D2, D3.

### Key challenges
- **Single line, no internal redundancy.** Any line-15 disruption reroutes to Lerma, which is exactly the dependency the project is trying to reduce.
- **No UFS capability** — blocks Scenario 2 at the structural level.
- **Two formats only** — blocks any "absorb Batavia" path without a new line for 4.4 lb, 7.9 lb, 2.6 oz, etc.
- **Absorption mid-execution** — the 2025 transfer is a moving target; baselining Indy right now is a snapshot of a ramp, not a steady state.

---

## 4. Lerma — Mexico

### Volume
- **3,842,764 cases** · **~28,783 tonnes** · 73.3% of NA cases, 66.6% of NA tonnes.
- **3 physical lines**: Mateer 1 (Small Granulated — 2.26M), Mateer 3 (Large Granulated — 1.21M), Mateer 2 (FS Large Granulated / UFS — 372K).

### Channel mix
- **US Retail 90.3%** · **UFS 9.7%** · **UI 0.1%** · **CDA Retail 0%**.
- The dominant Retail node in the network; secondary UFS source.

### Format mix
| Format | Cases | Share | Line |
|---|---:|---:|---|
| 7.9 oz Small Granulated | 1,789,350 | 46.6% | Mateer 1 |
| 2 lb Large Granulated | 1,195,057 | 31.1% | Mateer 3 |
| 7.9 lb FS Large Granulated (UFS) | 371,525 | 9.7% | Mateer 2 |
| 15.9 oz Small Granulated | 284,495 | 7.4% | Mateer 1 |
| 3.5 oz Small Granulated | 183,878 | 4.8% | Mateer 1 |
| 40.5 oz Large Granulated | 18,457 | 0.5% | Mateer 3 |

**Lerma is the only site running 7.9 oz and 3.5 oz — nearly half its total volume (1.97M cases) is in pack sizes no other site in the network makes.**

### Top SKUs (2025)
| Rank | SKU | Cases | Note |
|---:|---|---:|---|
| 1 | KNR MEX BOUIL CHK 6 2 LB | 1,001,152 | Multi-site w/ Indy (85% still at Lerma) — **biggest single SKU in network** |
| 2 | KNORR MEX BOUIL CHK 12/7.9 OZ | 919,031 | Lerma-unique (Mateer 1) |
| 3 | KN MEX BOUIL TOM/CHK 12/7.9 OZ | 446,705 | Lerma-unique (Mateer 1) |
| 4 | KNORR MEX BOUIL BEEF 12/7.9 OZ | 303,148 | Lerma-unique (Mateer 1) |
| 5 | Knorr Caldo de Pollo 4 7.9lb Display | 263,648 | Lerma-unique UFS (Mateer 2) |

Top 5 = 2.93M cases = **76% of Lerma's output.** The dominant line is Mateer 1 (7.9 oz Small Granulated), which carries 1.79M cases of Lerma-unique volume.

### In-flight transfer status
**38.5% of Lerma's volume (1,479,552 cases)** sits in SKUs also running at Indy. All six multi-site Lerma ↔ Indy SKUs are 2 lb or 15.9 oz — i.e. formats Indy already runs. This is the Scenario-1-addressable pool.

The remaining **61.5% of Lerma (2,363,212 cases)** is Lerma-unique: 7.9 oz (1.79M), 7.9 lb UFS (372K), 3.5 oz (184K), 40.5 oz (18K). These are not moveable without Indy building new pack sizes and, for 7.9 lb UFS, a new channel.

### Cost / GM / procurement *(directional — gap)*
- **Unit cost, GM, line capacity ceilings not in the source workbook.** Not estimated.
- **Directional read:** Lerma carries the network's scale advantage — 73% of cases on 3 lines is the lowest-fixed-cost position structurally available in NA bouillon — but that advantage lives on top of an implicit **cross-border logistics dependency of ~3.47M cases/year** (all Lerma US Retail moving across the US-MX border). Duty, FX exposure, customs lead time, and cross-border truck capacity are not quantified in the dataset and should not be read as zero. Logged as D10.

### Key challenges
- **Cross-border exposure on 90% of its output.** Single largest network dependency in the project.
- **Scenario-2 capability load is concentrated here.** 1.97M cases of 7.9 oz and 3.5 oz have nowhere else to go without Indy building new formats.
- **In-flight transfer on the flagship 2 lb line** — the largest SKU in the network (1.18M cases) is 85% still at Lerma with 15% already moved, creating an unstable 2025 cost and inventory picture at both ends.

---

## 5. Batavia

### Volume
- **584,756 cases** · **~10,007 tonnes** · 11.1% of NA cases, **23.1% of NA tonnes** (punches 2× its case share by mass).
- **2 physical lines**: line 13 (539K) and line 0 (45K).

### Channel mix
- **UFS 90.7%** · **US Retail 7.3%** · **CDA Retail 2.0%** · **UI 0%**.
- The only UFS-dominant site and the only CDA source in the network.

### Format mix
| Format | Cases | Share | Technology |
|---|---:|---:|---|
| 4.4 lb UFS | 456,612 | 78.1% | Knorr Caldo 4.4 (line 13) |
| "0"-size Caldo (UFS + CDA) | 82,929 | 14.2% | Knorr Caldo + Small Granulated Natural (line 13) |
| 2.6 oz Retail | 25,161 | 4.3% | Small Granulated Natural — Zero Salt (line 0) |
| 2.5 lb Retail | 10,298 | 1.8% | Large Granulated (line 0) |
| 2 lb Retail | 7,440 | 1.3% | Large Granulated + MixMod (line 0) |
| 25 lb UFS | 2,315 | 0.4% | Knorr Caldo 25 lb (line 0) |
| 40.5 oz Retail | 0 | 0.0% | (listed but no 2025 production — DQ flag) |
| 2 kg UFS | 12 | 0.0% | Knorr Caldo 25 lb (line 0) |

### Top SKUs (2025)
| Rank | SKU | Cases | Note |
|---:|---|---:|---|
| 1 | KNORR CALDO DE POLLO 4 4.4LB | 217,758 | Batavia-unique UFS |
| 2 | KNORR CALDO DE TOMATE 4 4.4LB (combined) | 146,119 | Batavia-unique UFS |
| 3 | Knorr Caldo De Pollo 1p 25 lb | 71,384 | Batavia-unique UFS |
| 4 | Knorr Caldo de Res 4 4.4lb | 67,718 | Batavia-unique UFS |
| 5 | KNR Bouillon CHKN Zero Salt 6p 2.6oz | 21,296 | Batavia-unique Retail |

Top 4 UFS SKUs = 502,979 cases = **86% of Batavia's total volume.**

### In-flight transfer status
**Zero.** Not a single Batavia SKU is produced anywhere else in the NA network. The one nominal exception — `KNR MEX BOUIL CHK 480 2.53lb 40.5z` — is listed at both Lerma and Batavia but Batavia had zero 2025 volume on it. Batavia carries no overlap with Indy or Lerma.

### Cost / GM / procurement *(directional — gap)*
- **Unit cost, GM, line 13 / line 0 capacity, and RM sourcing not in the source workbook.** Not estimated.
- **Directional read:** Batavia's cost position is **technology-specific, not scale-driven** — it runs Knorr Caldo 4.4, Caldo 25 lb, MixMod, and Small Granulated Natural on lines and with recipes that don't exist elsewhere in NA. This is the reason the site exists today, and it's the reason any "move Batavia to Indy" scenario is a capability build, not a line transfer. Logged as D1/D2/D5 and D7 (R&D harmonization).

### Key challenges
- **Technology monopoly.** Every Batavia volume driver (Caldo 4.4, Caldo 25 lb, MixMod, Small Granulated Natural) has no second source in the network. Batavia downtime = product-category downtime.
- **Scale disadvantage in Retail.** The small Retail footprint (43K cases, 7% of Batavia) is fragmented across 2 lb, 2.5 lb, 2.6 oz, 40.5 oz — 8 SKUs totalling less than one trailer per week. Whether to rationalize or shift this Retail tail is a clean Week-2 question.
- **Only source of CDA Retail** (11,545 cases). Any Batavia scenario touches a regulatory / labeling scope (Canadian Retail) that doesn't exist at Indy or Lerma.

---

## 6. Indy: advantaged / constrained *(the unhedged read)*

### Where Indy is advantaged

1. **Domestic US logistics.** Indy's entire 2025 output (818K cases) serves US Retail customers without crossing a border. Against Lerma's 3.47M cases of cross-border Retail flow, Indy has structurally lower customs latency, no duty, no FX on finished goods, and no border disruption risk. The *magnitude* of the advantage is unquantified (D10) but the *direction* is unambiguous.
2. **Already running the two biggest Retail formats.** 2 lb (32% of network) and 15.9 oz (11% of network) — together 1.77M cases of network-wide pack demand. Indy already runs these successfully and is absorbing Lerma volume in them during 2025.
3. **Proven transfer execution.** Six Lerma ↔ Indy multi-site SKUs are mid-handoff in 2025, one of them (KNR MEX BOL TOM/CHK 6 2 LB) is 96% complete. Indy has demonstrated it can receive volume, not just theoretically host it.
4. **Clean channel.** 100% US Retail = no split-channel complexity, no UFS packaging/logistics overhead, no CDA regulatory scope. The simplest channel profile in the network.

### Where Indy is constrained

1. **Single line.** One physical line (line 15) carries 100% of Indy's output. No internal redundancy, no second shift visible in the data, no second line. Any Scenario 1 conversation that adds volume has to first answer *"is there headroom on line 15, and if not, what's the second-line decision?"* (D3). Until that answer exists, Scenario 1 is capacity-blind.
2. **Two formats only — 2 lb and 15.9 oz.** Every other format in the NA network (7.9 oz, 3.5 oz, 7.9 lb, 4.4 lb, 25 lb, 2.5 lb, 2.6 oz, 40.5 oz) requires new pack capability. This rules out absorbing ~56% of network volume without new line investment.
3. **Zero UFS capability in 2025.** Not a ramp issue, not a scheduling issue — **0 UFS cases.** The entire 901K-case NA UFS network (Batavia + Lerma UFS) cannot move to Indy without standing up a UFS footprint that does not exist today: new line, new channel, new logistics, likely new RM supply arrangements.
4. **100% product dependence on Lerma.** Every SKU Indy runs, Lerma also runs. Indy has no unique recipe, no independent product authority, no R&D footprint in the dataset. This is fine while the Lerma → Indy transfer is in progress — it's what makes the transfer physically possible — but it means Indy is not yet operationally autonomous from Lerma even for the 818K cases it already owns.
5. **Scale is small in network terms.** 15.6% of NA cases, 10.3% of tonnes. "Indy-heavy" today means a factory running at one-sixth of total volume.

### The honest summary

> Indy today is a **single-line, two-format, Retail-only, Lerma-dependent site** that is already successfully absorbing transfer volume in the formats it was built to run. That is a strong foundation for Scenario 1 (Maximize Indy) provided line capacity and a second-line path exist. It is a **weak** foundation for Scenario 2 (Full consolidation) — that scenario requires standing up new formats, new technologies, and a UFS footprint that Indy has never run. Scenario 2 is not a harder version of Scenario 1; it is a different kind of project.

---

## 7. Cost / GM / procurement — honest directional paragraph

The source workbook contains no unit cost, gross margin, procurement, line capacity, utilization, or shift-model data for any of the three sites. The Week-1 baseline is therefore **volume-complete and cost/GM directionally-framed only**:

- **Lerma** carries the network's scale advantage (73% of cases on 3 dedicated lines) but the magnitude is offset by an unquantified cross-border logistics burden on ~3.47M cases/year of US-bound Retail flow.
- **Indy** carries a domestic-logistics advantage on Retail against Lerma but its cost base is unverified and any unit-cost conversation depends on line-15 utilization, which is unknown.
- **Batavia** carries a technology-specific cost position (Caldo / MixMod / Natural) that is not comparable to the Retail-format lines at Indy or Lerma, so site-to-site unit-cost comparisons would be misleading even if the data existed.

These gaps are raised as **P0 data requests D1, D2, D3** (cost, GM, Indy capacity) on the Wednesday call and are Scope B's critical path to completion. Week 1 ships with the gap named, not hidden; Week 2 cannot start the scenario quantification without D1/D2/D3 in hand.

---

## 8. Caveats

1. Tonnes are derived as `cases × Tonnes/CS` from the source workbook. Directional only; not mass-balance reconciled.
2. "Format" is approximated by `Size`. 2 lb Large Granulated at Indy and 2 lb Large Granulated MixMod at Batavia are treated as the same format for baseline purposes but run on different technologies — a Week-2 Size × Tech revalidation is on the list.
3. Top-SKU tables at Indy and Lerma reflect 2025 full-year `Total 25`. They are not weighted by month of transfer, so a SKU that is "47% at Indy for the full year" may be "0% at Indy in January and 90% at Indy in December" — the monthly profile has to be used for Scenario 1 headroom math in Week 2.
4. Multi-site counts exclude UI trace volume (small rounding). The strict "both sites > 0 in Retail + UFS" count is 6 Lerma ↔ Indy SKUs; the DQ memo's 10-SKU count includes UI trace and the zero-volume Batavia 40.5 oz row.
5. The 100% / 0% / 38.5% multi-site shares for Indy / Batavia / Lerma are case-weighted, not SKU-weighted.
