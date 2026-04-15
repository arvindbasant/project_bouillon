# Current-State Network Map — NA Bouillon

**Week:** 1 · **Day:** 2 (Tue 2026-04-14) · **Scope:** A — Current-State Network Mapping
**Source:** `data/sku_master.csv`, `data/monthly_volume.csv` · All numbers traceable to `Copy of RT and UFS Bouillon 4.13.26.xlsx`.

---

## 1. One-line view

> **The NA bouillon network is a three-site system carrying 5.25M cases in 2025. Lerma (MX) makes 73% of everything, Indy is a Retail-only single-line factory running 16%, and Batavia is the specialty UFS site running 11%. Roughly 44% of all volume sits in SKUs that are already mid-transfer from Lerma to Indy — the Lerma → Indy shift is not theoretical, it's in progress.**

---

## 2. The three nodes

### 2.1 Lerma (Mexico) — the scale site
- **3,842,764 cases (73.3%)** · ~28,800 tonnes directional
- **3 lines:** Mateer 1, Mateer 2, Mateer 3
- **6 formats:** 7.9 oz (1.79M), 2 lb (1.20M), 7.9 lb UFS (372K), 15.9 oz (284K), 3.5 oz (184K), 40.5 oz (18K)
- **Channel:** 90% US Retail, 10% UFS, trace UI
- **Both sub-categories:** Sabor + Granulated Bases/Bouillon
- **Role in network:** mother plant. Makes everything, including formats neither of the other two sites run (7.9 oz, 3.5 oz).

### 2.2 Indy (Independence, MO) — the strategic site
- **818,537 cases (15.6%)** · ~4,400 tonnes directional
- **1 line:** "15"
- **2 formats:** 2 lb Large Granulated (510K, 62%), 15.9 oz Small Granulated (309K, 38%)
- **Channel:** ~100% US Retail. **Zero UFS volume in 2025.**
- **Role in network:** absorption node for the Lerma → Indy transfer that started during 2025.
- **Notable:** everything Indy runs today, it overlaps with Lerma — Indy is not running any format Lerma isn't already making. This is what makes the transfer physically possible without new capability.

### 2.3 Batavia — the specialty UFS site
- **584,756 cases (11.1%)** · ~10,000 tonnes directional (punches above its case weight because of large UFS formats)
- **2 lines:** "13" (539K), "0" (45K)
- **7 formats**, dominated by **4.4 lb UFS (457K)** and **"0" size Caldo (83K — UFS + CDA)**
- **Channel:** ~91% UFS, ~7% US Retail, ~2% CDA Retail. **The only site that carries CDA Retail.**
- **Technologies:** Knorr Caldo 4.4, Knorr Caldo 25 lb, Large Granulated MixMod, Small Granulated Natural — **none of which run at Indy today.**
- **Role in network:** UFS specialist + CDA Retail fulfillment. Technology-differentiated, not a direct Lerma overlap.

---

## 3. Network flows (what moves where)

From the 2025 data alone:

| Flow | Cases 2025 | Evidence |
|---|---:|---|
| **Lerma → US Retail** | 3,469,125 | Largest single flow in the network |
| **Lerma → UFS** (7.9 lb) | 371,525 | Mateer 2 dedicated |
| **Indy → US Retail** | 818,078 | Full Indy output |
| **Batavia → UFS** (4.4 lb, 25 lb, Caldo) | 530,312 | Batavia primary role |
| **Batavia → US Retail** | 42,899 | Small residual Retail footprint |
| **Batavia → CDA Retail** | 11,545 | Only CDA source in the network |
| **Lerma → UI** | 2,113 | Trace |
| **Indy → UI** | 459 | Trace |

**Cross-border intra-network flows (inferred, to validate with sponsor):** Lerma's US Retail + UFS + UI volumes physically have to cross the US/MX border to reach US customers. This is an **implicit logistics dependency** the Week-1 map should flag — duty, customs, cross-border truck capacity, and FX all sit on top of 3.8M cases of annual flow. **Not quantified in this workbook; flagged as an open item.**

**Co-manufacturers / overflow partners:** not present in the dataset. The brief says to map them. **This is an open data request for Wednesday's call** — we need named co-mans and what they run, or a confirmation that there are none in scope.

---

## 4. Portfolio split (brief asks for Total → Retail → UFS)

```
Total NA Bouillon 2025: 5,246,057 cases

├── US Retail          4,330,103   82.5%
│   ├── Lerma          3,469,125   (80.1% of Retail)
│   ├── Indy             818,078   (18.9% of Retail)
│   └── Batavia           42,899   ( 1.0% of Retail)
│
├── UFS                  901,837   17.2%
│   ├── Batavia          530,312   (58.8% of UFS)
│   └── Lerma            371,526   (41.2% of UFS)
│
├── CDA Retail            11,545    0.2%
│   └── Batavia           11,545   (100%)
│
└── UI                     2,572    0.0%
    ├── Lerma              2,113
    └── Indy                 459
```

**What this tells us:**
- **US Retail is a two-site problem** (Lerma + Indy); Batavia is a rounding error in Retail.
- **UFS is a two-site problem** (Batavia + Lerma); Indy does not participate at all.
- These are **two almost-disjoint networks** stacked on top of each other. The "consolidate at Indy" question is really two questions: (1) absorb Lerma's Retail into Indy; (2) stand up a UFS capability at Indy that doesn't exist today.

---

## 5. Known network fragilities (from the data)

| # | Fragility | Evidence | Why it matters |
|---:|---|---|---|
| F1 | **Single-line Indy** | Indy runs line "15" only — one line carries 100% of its 818K cases | No internal redundancy. Any unplanned downtime routes back to Lerma. Scenario 1/2 *must* address shift/line expansion. |
| F2 | **Cross-border dependency** on 3.8M cases | All Lerma volume for US customers crosses the US/MX border | Duty, FX, customs time — single point of disruption for 73% of volume. Confirm with sponsor if historical disruption data exists. |
| F3 | **Batavia technology monopoly** | Knorr Caldo 4.4/25lb, MixMod, Natural run only at Batavia | Any Batavia disruption affects product categories with no secondary source. |
| F4 | **In-flight Lerma → Indy transfers with no stable handoff date visible** | 9 SKUs split across Lerma + Indy during 2025 with overlapping, non-clean monthly profiles | Network inventory, service levels, and cost reporting all sit in a transitional state — "current state" is moving underneath the analysis. |
| F5 | **Indy format narrowness (2 sizes only)** | 2 lb + 15.9 oz only | Any Indy absorption of new Lerma/Batavia formats requires new sizing/packaging — not a line-transfer. |
| F6 | **Negative monthly cells at Indy** | 3 cells: -480, -192, -98 | Harmless individually but suggests manual corrections are happening in the Indy ramp-up → inventory/ERP reconciliation may be loose during transfer. |

---

## 6. What this map does NOT yet show *(gap list for Wednesday's call)*

- Named co-manufacturers and overflow partners.
- Cost per case / per tonne by site.
- Gross margin by site / channel (directional or actual).
- Indy line "15" capacity ceiling and current utilization %.
- Lerma Mateer 1 / 2 / 3 capacity ceilings.
- Batavia line 13 + line 0 capacity ceilings.
- R&D recipe / RM harmonization roadmap status per SKU.
- Formal status of the in-flight Lerma → Indy transfers (tracked program vs tactical).
- US/MX cross-border logistics cost and recent disruption history.
- Raw-material supply points (bouillon cube / granulated base sourcing).

These are the open items raised into `logs/open_data_requests.md` for the Wednesday call.

---

## 7. Visual (to be drawn for the pack)

```
                       NA BOUILLON NETWORK — 2025

     ┌──────────────────────────────────────────────────────────┐
     │                        US RETAIL                         │
     │                      4.33M cases                         │
     └───────▲─────────────────▲──────────────────▲─────────────┘
             │ 3.47M            │ 818K             │ 43K
             │                  │                  │
     ┌───────┴──────┐    ┌──────┴──────┐    ┌──────┴──────┐
     │   LERMA  MX  │    │    INDY     │    │   BATAVIA   │
     │  3 lines     │    │  1 line     │    │  2 lines    │
     │ 3.84M cases  │    │ 819K cases  │    │ 585K cases  │
     │  73% of net  │◀──▶│  16% (↑)    │    │  11%        │
     │ Retail+UFS   │    │ Retail only │    │ UFS spec.   │
     └───────┬──────┘    └─────────────┘    └──────┬──────┘
             │ 372K                                │ 530K
             ▼                                     ▼
     ┌──────────────────────────────────────────────────────────┐
     │                           UFS                            │
     │                      902K cases                          │
     └──────────────────────────────────────────────────────────┘
                                              │
                                              │ 12K
                                              ▼
                                     ┌────────────────┐
                                     │   CDA Retail   │
                                     │   12K cases    │
                                     └────────────────┘

     ◀──▶ = in-flight transfer: 44% of all cases are in SKUs
           already running at two sites, predominantly Lerma → Indy.
```
