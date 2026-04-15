# Data Quality Memo — `Copy of RT and UFS Bouillon 4.13.26.xlsx`

**Author:** project owner · **Date:** 2026-04-13 · **Week:** 1, Day 1
**Source:** `Copy of RT and UFS Bouillon 4.13.26.xlsx` (single sheet, 57 SKU rows, header on row 3)
**Purpose:** Establish trust in the dataset before any analysis is built on top of it.

---

## 1. Headline

- **Grand total reconciles: 5,246,057 cases (2025).** Sum of `Total 25` column equals sum of monthly columns, no hidden rows.
- **Shape:** 57 product rows × 12 monthly buckets × 3 sourcing units (Indy, Lerma, Batavia).
- **Most important finding for Week 1:** **44.2% of all 2025 cases (2,316,546) live in SKUs already running at more than one site.** 9 of the 10 multi-site SKUs are split between **Lerma and Indy**, and the monthly pattern makes the direction explicit: **Lerma is handing volume off to Indy mid-year 2025.** The strategic premise of this project — Maximize / Consolidate at Indy — is already partially in motion and the data shows it.

---

## 2. Structure & decoding

| Area | Finding | Action taken |
|---|---|---|
| Header row | Row 3 (not row 1) | Parser anchored to row 3 |
| Data rows | Rows 4–60 (57 SKUs) | Captured, no orphans |
| Monthly column headers | Stored as **Excel date serials** (45658 … 46010), not strings | Decoded to `2025-01` … `2025-12` |
| Sourcing units present | `Indy`, `Lerma`, `Batavia` only | Treated as canonical |
| Channels present | `US Retail`, `UFS`, `CDA Retail`, `UI` | Trailing space on `US Retail` normalized |
| Sub-categories present | `Sabor`, `Granulated Bases/Bouillon` | No others |

Cleaned outputs:
- `data/sku_master.csv` — one row per SKU (57 rows), with `total_tonnes_2025` derived as `total_cases_2025 × Tonnes/CS`.
- `data/monthly_volume.csv` — long-format `(du, site, month, cases, tonnes)`.
- `logs/dq_findings.json` — full machine-readable findings.

---

## 3. Missing / blank fields

| Field | Blank rows | Interpretation |
|---|---:|---|
| `Brand` | **57 / 57** | Systematic — the column is empty for every row. Likely intentional (all rows are Knorr). **Confirm with sponsor.** Does not block analysis. |
| `Pouches/CS` | **57 / 57** | Systematic blank. Not blocking — tonnage comes from `Tonnes/CS`, which is populated. If pouch-level math is ever needed, derive from `Size`. |
| `Tonnes/CS` | 0 / 57 | Fully populated — tonnage analysis is safe. |
| Cost, GM, procurement, capacity, shift, line-availability | n/a | **Not in this workbook at all.** Scope B business assessment will be **volume-complete but cost/GM directional-only** until external data is sourced. Logged as an open data request. |

---

## 4. Negative & zero values

### Negative monthly cells (3)
All three are at **Indy**, all are **small in magnitude**, all are **single-month corrections** in the middle of a product's run. Almost certainly returns / accounting corrections. Treated as **valid signed values** (not errors) but flagged:

| Row | Product | Site | Month | Cases |
|---:|---|---|---|---:|
| 7 | `KNR MEX BOUIL CHK 6 2 LB` | Indy | 2025-07 | -480 |
| 11 | `KNR MEX BOUIL Beef 6 2 LB` | Indy | 2025-06 | -192 |
| 32 | `KNORR BOUIL TOM/CHK 12/15.9 OZ` | Indy | 2025-08 | -98 |

**Rule applied:** kept as-is for volume reconciliation; will not materially affect any aggregation.

### All-zero rows (1)
| Row | Product | Site | Note |
|---:|---|---|---|
| 14 | `KNR MEX BOUIL CHK 480 2.53lb 40.5z` | Batavia | Listed but produced **zero cases** in 2025. Keep in master as an active DU with zero run; flag to sponsor — is this an inactive item or a new item not yet launched? |

---

## 5. Multi-site SKUs & the Lerma → Indy transfer pattern *(the important finding)*

**10 product DUs are made at more than one site.** Combined they represent **2,316,546 cases (44.2%) of the 2025 total.** 9 of the 10 are Lerma ↔ Indy; 1 is Lerma ↔ Batavia.

A heuristic "in-flight transfer" scan (first half of 2025 volume at one site, second half at another) flags 10 row-level patterns. The monthly profile for the largest multi-site SKU tells the story in a single line:

```
KNR MEX BOUIL CHK 6 2 LB   (1.18M cases / year across both sites)
  Lerma    115k  85k  135k  113k  124k  166k   63k   45k    .   95k  55k    .      Jan→Dec
  Indy       .    .    .    .     5k   27k   -0k    .    .   89k  28k  24k      Jan→Dec
```

Lerma is running it heavy Jan–Oct; Indy starts picking it up from May and ramps sharply in October. Same pattern, at different scales, visible across the other Lerma↔Indy SKUs. The data is consistent with an **active, partially-executed Lerma → Indy shift in 2025**.

**Implications for Week-1 baseline:**
1. The 5.25M-case network total is **not a stable snapshot** — roughly 2.3M of it is mid-transfer. Any "current state" needs to distinguish **settled production** from **in-flight volume** or the scenarios downstream will double-count.
2. Scenario 1 (Maximize Indy) partially describes **work already in flight**, not greenfield planning. Week 2 will need to separate "already booked" from "net new" Indy upside.
3. Scenario 2 (Full consolidation) still has to answer the **UFS capability gap** — Batavia's 530K UFS cases don't appear in the Lerma↔Indy in-flight set at all.

**Open question for Wednesday's call:** are these in-flight Lerma → Indy transfers (a) part of an existing formally-tracked program, (b) tactical overflow moves, or (c) opportunistic? This changes how Scope B reports "current state" vs. how Scope C models "future state".

### Multi-site SKU list

| Product DU | Sites | Note |
|---|---|---|
| `KNR MEX BOUIL CHK 6 2 LB` | Indy, Lerma | Largest — 1.18M cases combined; clear Lerma→Indy handoff |
| `KNR MEX BOL TOM/CHK 6 2 LB` | Indy, Lerma | Lerma wound down in Jan; Indy picked up from May |
| `KNR MEX BOUIL Beef 6 2 LB` | Indy, Lerma | Lerma Jan–Sep; Indy May onward |
| `KNR MEX BOUIL CHK 12/15.9 OZ` | Indy, Lerma | Both sites active across the year |
| `KNR MEX BOUIL BEEF 12 15.9z` | Indy, Lerma | Small; Lerma→Indy pattern |
| `KNORR BOUIL TOM/CHK 12/15.9 OZ` | Indy, Lerma | Small; Lerma→Indy pattern |
| `KNORR MEX BOUILLON CHK 12 15.9Z` | Indy, Lerma | Small; Lerma→Indy pattern |
| `KNR MEX BOUILLON BEEF 12 15.9Z` | Indy, Lerma | Tiny; effectively rounding |
| `KNORR BOUIL TOMATO/CHICKEN 12P 15.9Z` | Indy, Lerma | Small; Lerma→Indy pattern |
| `KNR MEX BOUIL CHK 480 2.53lb 40.5z` | Batavia, Lerma | Only multi-site SKU **not** involving Indy — UFS 40.5 oz format, Lerma runs it, Batavia listed but zero volume 2025 |

---

## 6. Reconciled totals *(for use in the Week-1 pack)*

**By sourcing unit**

| Site | Cases 2025 | Share | Approx tonnes |
|---|---:|---:|---:|
| Lerma | 3,842,764 | 73.3% | ~28,800 |
| Indy | 818,537 | 15.6% | ~4,400 |
| Batavia | 584,756 | 11.1% | ~10,000 |
| **Total** | **5,246,057** | **100.0%** | **~43,200** |

**By channel** — US Retail 82.5% · UFS 17.2% · CDA Retail 0.2% · UI 0.0%
**By sub-category** — Sabor 82.1% · Granulated Bases/Bouillon 17.9%

**Site × channel (cases)**

| Site | US Retail | UFS | CDA Retail | UI |
|---|---:|---:|---:|---:|
| Lerma | 3,469,125 | 371,526 | — | 2,113 |
| Indy | 818,078 | — | — | 459 |
| Batavia | 42,899 | 530,312 | 11,545 | — |

**Read:** Indy today is **~100% Retail**. Batavia today is **~91% UFS**. Lerma runs both but is **~90% Retail**. These are the starting positions for every scenario discussion downstream.

---

## 7. Assumptions applied in this pass

1. `Brand` blank = all Knorr, not data loss. *(Confirm with sponsor.)*
2. `Pouches/CS` blank = not needed for tonnage math; `Tonnes/CS` is authoritative. *(Confirm.)*
3. Negative monthly values = legitimate returns/corrections, not data errors. Kept signed.
4. Row 14 (`KNR MEX BOUIL CHK 480 2.53lb 40.5z` at Batavia, zero volume) = active DU with no 2025 run, retained in master. *(Confirm status with sponsor.)*
5. The "in-flight transfer" heuristic (H1 concentrated at one site → H2 concentrated at another) is a **flag**, not a rule. Sponsor confirmation upgrades it to a fact.
6. Tonnes values derived as `cases × Tonnes/CS` are directional; actual reported tonnes may differ based on pack-level mass balances.

---

## 8. Open data needed to complete Scope B *(for Wednesday's call)*

| # | Ask | Why |
|---:|---|---|
| 1 | Site-level conversion cost by sub-category (Indy, Lerma, Batavia) | Week-1 business baseline is otherwise volume-only |
| 2 | Directional gross margin by site/channel | §B explicitly asks for it |
| 3 | Indy capacity + shift model (theoretical and current utilization, by line) | Required before Scenario 1 (Max Indy) can be quantified |
| 4 | Named co-manufacturers / overflow partners in the NA bouillon network | Not in the workbook; needed for Scope A network map |
| 5 | Status of R&D recipe / raw-material harmonization roadmap | Brief says "leverage, don't recreate" — need the owner |
| 6 | Are the 2025 Lerma → Indy moves part of a tracked program or tactical? | Determines how we frame "current state" vs. "future state" |
| 7 | Confirm Brand column is intentionally blank (= Knorr) | Closes a data question |
| 8 | Confirm Row-14 Batavia 40.5oz item status (active / discontinued / pre-launch) | Closes a data question |

---

## 9. Status

- Data ingest: **done**.
- Cleansing rules: **documented and applied**.
- Reconciliation: **passes to source grand total**.
- Ready for Day-2 work: **network map + format/line complexity + capability-gap narrative** *(Tuesday)*.
