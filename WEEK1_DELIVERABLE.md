# NA Bouillon — Current-State Pack
## Week 1 Deliverable · 2026-04-17

**Prepared for:** Wez Beauplan, Associate Director, Foods Transformation (NA)
**Scope:** Current-state network + business baseline (Scope A + Scope B). Scenario development (Scope C) begins Week 2.
**Source of truth:** `Copy of RT and UFS Bouillon 4.13.26.xlsx` — 57 SKUs, 5,246,057 cases, 2025 full-year. All numbers traceable to source; reconciliation in the appendix.

---

## Page 1 — Executive Summary

> **The NA bouillon network is 5.25M cases across three sites running three different kinds of factory. Lerma (73%) is the scale plant. Indy (16%) is a single-line, two-format, Retail-only Lerma-mirror already absorbing transfer volume in 2025. Batavia (11%) is a technology-specialist UFS plant with zero overlap with either other site.**
>
> **The real project question is not "should we consolidate at Indy." The Lerma → Indy shift is already in motion for the formats Indy can run today. The question is where the line sits between formats Indy can absorb with headroom (~1.48M Lerma cases, Scenario 1) and formats Indy would have to build new capability for (~2.94M cases, including all UFS, Scenario 2). Those two scenarios have fundamentally different cost, capex, and risk profiles — and framing them that way is how leadership gets a decision it can act on.**

### The five facts that carry the pack

1. **5,246,057 cases across three sites.** Lerma 3,842,764 (73.3%) · Indy 818,537 (15.6%) · Batavia 584,756 (11.1%). By tonnage the split is 67 / 10 / 23 — Batavia punches twice its case weight because its UFS packs are heavy.

2. **44% of all network cases are in multi-site SKUs.** 2,298,089 cases sit in SKUs running at more than one site. **100% of Indy's output is in Lerma-shared SKUs** — Indy has no unique product footprint. **Batavia has zero overlap with anyone** — every Batavia SKU is unique in the network. Lerma is 38.5% shared with Indy and 61.5% Lerma-unique.

3. **The Lerma → Indy shift is already executing.** Six 2 lb / 15.9 oz SKUs are mid-handoff in 2025, one of them (KNR MEX BOL TOM/CHK 6 2 LB) is 96% complete at Indy. The flagship SKU (KNR MEX BOUIL CHK 6 2 LB, 1.18M cases) is 15% at Indy and 85% still at Lerma — the biggest single lever in Scenario 1 has barely moved.

4. **Indy today is a single-line, two-format, Retail-only factory.** One physical line ("15"), two pack sizes (2 lb Large Granulated + 15.9 oz Small Granulated), 100% US Retail, 0 UFS cases. Every other format in the NA network runs somewhere else.

5. **Scenario 2 is a capability build, not a volume transfer.** 2.94M cases of network volume (56%) sit in formats or technologies Indy has never run. The biggest single piece is Lerma's 7.9 oz Small Granulated (1.79M cases); the hardest is the UFS footprint at Batavia + Lerma (900K cases across Caldo 4.4, Caldo 25 lb, MixMod, Natural, 7.9 lb FS Large Granulated) because Indy has zero UFS capability today. R&D harmonization maturity is the critical path.

### What this pack is missing — and the plan to close it

The source workbook contains **no unit cost, gross margin, procurement, line capacity, utilization, or shift-model data.** The Week-1 baseline is therefore volume-complete and cost/GM directionally framed only. Twelve data requests (D1–D12) are logged; the four P0 items — cost (D1), GM (D2), Indy line 15 capacity (D3), and in-flight transfer program status (D8) — are Scope B's critical path. Week 2 cannot start scenario quantification without them.

### What Week 2 will do

Answer two questions, cleanly separated:
- **Q1 (Scenario 1).** How much of the 1.48M Lerma-addressable pool can Indy absorb without new line investment, and what does the second-line decision look like if the answer is "not much more"?
- **Q2 (Scenario 2).** For the 2.94M cases of network volume Indy cannot run today, which subset is worth building capability for at Indy, on what 3-year glidepath, with what harmonization dependency?

Scenarios 1 and 2 are different kinds of projects and should not share a single set of assumptions. Full framing in `analysis/week2_preview.md`.

---

## Page 2 — The One Chart

```
           2025 NA BOUILLON — SITE × CHANNEL × VOLUME (cases)

                              US Retail         UFS       CDA Retail     UI         TOTAL     SHARE
                              4,330,103      901,837        11,545     2,572      5,246,057

    LERMA  MX  3 lines         3,469,125     371,526           —      2,113      3,842,764   73.3%
       Mateer 1/2/3 · 6 formats · Retail + UFS · Sabor + Granulated Bases
       38.5% of Lerma is in Indy-shared SKUs — the S1 transfer pool

    INDY       1 line            818,078          0           —         459       818,537   15.6%
       Line 15 · 2 formats (2 lb + 15.9 oz) · 100% US Retail · 0 UFS
       100% of Indy is in multi-site SKUs → zero unique product footprint

    BATAVIA    2 lines            42,899    530,312       11,545          —       584,756   11.1%
       Line 13 + line 0 · 7 formats · UFS specialist · Caldo / MixMod / Natural
       0% of Batavia is shared — every Batavia SKU is unique in the network

    TOTAL                      4,330,103    901,837        11,545     2,572      5,246,057   100%

    ◀──▶ 43.8% of all cases are in SKUs running at 2 sites — the Lerma → Indy shift is in progress.
```

**Read in five seconds:** three sites, three disjoint manufacturing systems. Lerma is scale. Indy is a Lerma-mirror in execution. Batavia is a technology monopoly. The consolidation conversation is really two conversations — one about the overlap, one about the rest.

---

## Page 3 — Network Map

### Three nodes

**Lerma (Mexico) — the scale site.** 3.84M cases. 3 lines. 6 formats. 90% Retail / 10% UFS. Runs everything, including the two formats (7.9 oz, 3.5 oz) that no one else makes. Mother plant of the network.

**Indy (Independence, MO) — the absorption site.** 819K cases. 1 line. 2 formats. 100% Retail. Zero UFS. Everything Indy runs, Lerma also runs — Indy is the execution vehicle for the Lerma → Indy shift that started in 2025.

**Batavia — the specialty site.** 585K cases. 2 lines. 7 formats. 91% UFS, 7% Retail, 2% CDA. Knorr Caldo 4.4, Caldo 25 lb, MixMod, Small Granulated Natural — technology monopolies with no second source in the network.

### Flows (2025)

| Flow | Cases | |
|---|---:|---|
| Lerma → US Retail | 3,469,125 | Largest single flow — **crosses the US-MX border** |
| Indy → US Retail | 818,078 | Full Indy output |
| Batavia → UFS | 530,312 | Batavia primary role |
| Lerma → UFS (7.9 lb, Mateer 2) | 371,526 | Supplements Batavia |
| Batavia → US Retail | 42,899 | Small residual Retail footprint |
| Batavia → CDA Retail | 11,545 | Only CDA source in network |
| Lerma / Indy → UI (trace) | 2,572 | De minimis |

**Cross-border exposure:** ~3.47M cases of Lerma Retail (90% of Lerma's output) physically cross the US-MX border each year. Duty, FX, customs lead time, and cross-border truck capacity are material costs on this flow — none quantified in the source workbook (logged as D10).

**Co-manufacturers / overflow / resiliency partners:** not present in the dataset. The brief asks for them mapped. Logged as open data request **D6** — named co-mans and what they run, or sponsor confirmation that there are none in NA bouillon scope.

### Known network fragilities

| # | Fragility | Why it matters |
|---:|---|---|
| F1 | **Indy is single-line** | No internal redundancy. Any line-15 disruption routes back to Lerma — the exact dependency this project exists to reduce. |
| F2 | **Cross-border on 3.47M cases** | ~66% of all NA bouillon cases cross one border annually. Single point of disruption for most of the network. |
| F3 | **Batavia technology monopoly** | Caldo 4.4 / Caldo 25 lb / MixMod / Natural run only at Batavia. Any Batavia disruption affects product categories with no secondary source. |
| F4 | **In-flight transfer with no stable handoff date** | 6 Retail SKUs are partially-migrated across Lerma ↔ Indy in 2025 with overlapping monthly profiles. "Current state" is moving underneath the analysis. |
| F5 | **Indy format narrowness** | Only 2 sizes. Any absorption of new formats requires new line / packaging, not line reassignment. |
| F6 | **Indy zero-UFS** | Not a ramp issue — Indy has never run UFS. The NA UFS network (901K cases) cannot move to Indy without a capability build. |

*(Full network map — including site-level line detail, flow table, portfolio hierarchy, and visual — in `analysis/network_map.md`.)*

---

## Page 4 — Business Baseline by Site

### Indy · 818,537 cases · ~4,445 tonnes · 15.6%
- **1 line · 2 formats · 100% US Retail · 0 UFS**
- Top SKUs: KNR MEX BOL TOM/CHK 6 2 LB (228K, **96% moved**) · KNR MEX BOUIL CHK 12/15.9 OZ (224K, 51% moved) · KNR MEX BOUIL CHK 6 2 LB (175K, 15% moved)
- **100% of Indy's 2025 volume is in SKUs also produced at Lerma.** Indy has zero unique product footprint — every case it makes, Lerma also makes.
- **Cost/GM:** unverified; structural advantage on US Retail logistics vs Lerma (no border). Quantification gated on D1/D2/D3.
- **Key challenges:** single line; two formats only; no UFS capability; absorption mid-execution makes baseline a moving target.

### Lerma (Mexico) · 3,842,764 cases · ~28,783 tonnes · 73.3%
- **3 lines (Mateer 1/2/3) · 6 formats · 90% Retail / 10% UFS**
- Mateer 1: Small Granulated 7.9/3.5/15.9 oz — **1.79M cases of 7.9 oz alone** (biggest line load in network)
- Mateer 3: Large Granulated 2 lb + 40.5 oz — the multi-site transfer lane to Indy
- Mateer 2: FS Large Granulated 7.9 lb UFS
- **38.5% of Lerma volume (1.48M cases)** sits in the Indy-shared 2 lb + 15.9 oz pool — the Scenario-1 addressable set.
- **61.5% (2.36M cases)** is Lerma-unique and has no current home at Indy or Batavia.
- **Cost/GM:** scale-driven advantage vs the other sites, offset by unquantified cross-border logistics burden on 3.47M cases/year.
- **Key challenges:** cross-border exposure; Scenario-2 capability load concentrated here (7.9 oz + 3.5 oz + 7.9 lb UFS); flagship SKU still 85% at Lerma despite in-flight transfer.

### Batavia · 584,756 cases · ~10,007 tonnes · 11.1% cases / **23% tonnes**
- **2 lines (13, 0) · 7 formats · 91% UFS / 7% Retail / 2% CDA**
- Top SKUs: KNORR CALDO DE POLLO 4 4.4LB (218K) · KNORR CALDO DE TOMATE 4 4.4LB (146K combined) · Knorr Caldo De Pollo 1p 25 lb (71K) · Knorr Caldo de Res 4 4.4lb (68K) — top 4 = 86% of Batavia
- **Zero overlap with any other site.** Batavia is a technology monopoly — Caldo 4.4, Caldo 25 lb, MixMod, Small Granulated Natural all run only here.
- Only CDA Retail source in the network (11,545 cases).
- **Cost/GM:** technology-specific cost base not comparable to Retail-format lines at Indy or Lerma; site-to-site unit cost comparisons would be misleading without recipe-normalized data.
- **Key challenges:** technology monopoly (no second source); scale disadvantage in the fragmented Retail tail (8 low-volume SKUs); only Canadian regulatory scope in the network.

*(Full baseline including site-level tonnage, top-SKU tables, format mix, challenge detail, and the complete cost/GM gap statement in `analysis/baseline_by_site.md`.)*

---

## Page 5 — Format / Line Complexity & the Indy Capability Gap

### The line that wins the scenario framing

> **Indy runs 2 formats. Lerma runs 6. Batavia runs 7. The union across the network is 11. Indy participates in 18% of the format taxonomy and 16% of the cases.**

### The Scenario 1 vs Scenario 2 divide, in three numbers

| | Cases 2025 | % of NA | What it requires |
|---|---:|---:|---|
| **Already at Indy** | 818,537 | 15.6% | — |
| **S1 addressable — formats Indy already runs** | **1,479,552** | **28.2%** | Line 15 capacity headroom + possible second-line decision |
| **S2 capability build — formats Indy does NOT run** | **2,940,525** | **56.1%** | 6 new formats, 4+ new technology types, new UFS footprint, capex, harmonization |
| Residual (CDA, UI, 0-volume rows) | ~7,443 | 0.1% | Scope decision |
| **Total** | **5,246,057** | **100%** | |

That's the whole project in four rows.

### The Indy capability gap, concretely

**What Indy can absorb without new capability** *(Lerma volume in formats Indy already runs)*

| Format | Lerma 2025 | Note |
|---|---:|---|
| 2 lb Large Granulated | 1,195,057 | Mateer 3 ↔ line 15 — proven, already mid-transfer |
| 15.9 oz Small Granulated | 284,495 | Line 15 already runs the pack — proven, already mid-transfer |
| **Addressable without new capability** | **1,479,552** | Gross; net-new is smaller after in-flight deduction |

**What Indy would have to build** *(formats Indy does not run)*

| Format | Where today | Cases | Capability lift |
|---|---|---:|---|
| 7.9 oz Small Granulated | Lerma Mateer 1 | 1,789,350 | New pack size — biggest single volume in network |
| 4.4 lb Caldo (UFS) | Batavia line 13 | 456,612 | New technology + new UFS channel |
| 7.9 lb FS Large Granulated (UFS) | Lerma Mateer 2 | 371,525 | New UFS line + new UFS logistics |
| 3.5 oz Small Granulated | Lerma Mateer 1 | 183,878 | New pack size |
| "0"-size Caldo (UFS/CDA) | Batavia | 82,929 | New technology + only CDA source |
| 2.6 oz Zero Salt | Batavia | 25,161 | New pack size + new variant |
| 40.5 oz (Retail) | Lerma | 18,457 | New pack size |
| 2.5 lb | Batavia | 10,298 | New pack size |
| 25 lb UFS Caldo | Batavia | 2,315 | New pack size + new technology |
| **Total requiring new capability at Indy** | | **2,940,525** | |

### What this means for the two scenarios
- **Scenario 1 is a capacity question.** Line 15 headroom + second-line decision + net-new volume after in-flight deduction. Low capability risk, near-term, cheap relative to S2.
- **Scenario 2 is a capability + harmonization program.** Six new formats, four new technology types, UFS footprint from scratch. High capex, R&D-gated, 3-year horizon at best. Different risk profile from Scenario 1 — not "more of the same."

*(Full format × line × technology tables, site-line breakdown, and the Scenario-2 harmonization dependency discussion in `analysis/format_line_complexity.md`.)*

---

## Page 6 — In-Flight Transfers Callout

### The finding

**43.8% of 2025 NA bouillon volume (2,298,089 cases) is in SKUs running at more than one site.** Every multi-site SKU with nonzero volume at both sites is Lerma ↔ Indy in the 2 lb + 15.9 oz transfer lane. Batavia has zero overlap. The monthly profile shows the handoff physically happening during 2025.

### The six in-flight Lerma ↔ Indy SKUs *(excluding UI trace)*

| SKU | Lerma 2025 | Indy 2025 | Total | Indy % | Read |
|---|---:|---:|---:|---:|---|
| KNR MEX BOL TOM/CHK 6 2 LB | 9,600 | 227,305 | 236,905 | **96%** | Essentially complete |
| KNR MEX BOUIL BEEF 12 15.9z | 16,963 | 29,447 | 46,410 | 63% | Mostly moved |
| KNORR BOUIL TOM/CHK 12/15.9 OZ | 48,625 | 54,442 | 103,067 | 53% | Halfway |
| KNR MEX BOUIL CHK 12/15.9 OZ | 218,489 | 224,209 | 442,698 | 51% | Halfway |
| KNR MEX BOUIL Beef 6 2 LB | 184,305 | 107,762 | 292,067 | 37% | One-third moved |
| **KNR MEX BOUIL CHK 6 2 LB** | **1,001,152** | **174,913** | **1,176,065** | **15%** | **Flagship — barely started** |

**Key pattern:** the flagship SKU — the biggest single product in the entire NA network at 1.18M cases — is the *least* migrated. The easy wins are nearly done; the bulk of Scenario 1's addressable volume is in one SKU that has barely moved.

### The monthly profile tells the story *(flagship SKU, 2025)*

```
KNR MEX BOUIL CHK 6 2 LB  (1.18M cases / year across both sites)
  Lerma    115k  85k  135k  113k  124k  166k   63k   45k    .   95k  55k    .      Jan→Dec
  Indy       .    .    .    .     5k   27k   -0k    .    .   89k  28k  24k       Jan→Dec
```

Lerma runs it heavy Jan–Oct, tapering in Q4; Indy starts picking it up from May and ramps sharply in October. Same shape, different magnitudes, visible across all six in-flight SKUs.

### Why this matters for Week 1 — and Week 2

1. **The 5.25M-case network total is not a stable snapshot.** ~2.3M of it is mid-transfer. Any "current state" that ignores this risks double-counting in Scope C.
2. **Scenario 1's gross addressable pool is 1.48M** but some fraction — directionally ~350K — is already booked into H2 2025. **Net new** Scenario 1 upside is smaller than the gross figure; Week 2 separates the two precisely.
3. **Open question D8 on the call:** is this a formally-tracked program, or tactical / opportunistic? The answer changes how Scope B reports "current state" and how Scope C frames "future state". This is the single highest-leverage question on the Wednesday list.

*(Full DQ evidence, multi-site SKU list, and monthly profile in `logs/data_quality_memo.md` §5.)*

---

## Page 7 — Week 2 Preview

### The two questions Week 2 answers

**Q1 — Scenario 1 (Maximize Indy).** How much of the 1.48M Lerma-addressable pool can Indy absorb without new line investment, and what does the second-line decision look like if the answer is "not much more"?

**Q2 — Scenario 2 (Full Consolidation).** For the 2.94M cases of network volume Indy cannot run today, which subset is worth building capability for at Indy — on what 3-year glidepath, with what harmonization dependency?

### Scenarios 1 and 2 are different kinds of projects

| | **Scenario 1 — Maximize Indy** | **Scenario 2 — Full Consolidation** |
|---|---|---|
| Shape | Capacity / throughput question | Capability-build + harmonization program |
| Scope | ~1.48M cases in 2 lb + 15.9 oz | ~2.94M cases, 6 new formats, 4+ new technologies, UFS from scratch |
| Gate | Line-15 headroom + second-line decision | Harmonization roadmap + capex envelope |
| Capex | Low–medium | High |
| R&D dependency | Low | **High — critical path** |
| Horizon | Near-term | 3-year glidepath |

### Week 2 deliverables

1. Scenario 1 3-year glidepath (SKU-level, year-by-year, with decision gates)
2. Scenario 2 3-year glidepath (harmonization-first, then first new line, then UFS ramp)
3. Comparative matrix across volume, cost signal, capex signal, risk, harmonization load, timing
4. Draft recommendation framing (the recommendation itself lands in Week 3)

### What Week 2 needs from the sponsor *(arriving this week)*

- **D1** Site-level conversion cost by sub-category *(P0)*
- **D2** Directional GM by site × channel *(P0)*
- **D3** Indy line 15 theoretical capacity + 2025 utilization *(P0)*
- **D7** R&D harmonization roadmap status per SKU family *(P0 — Scenario 2 critical path)*
- **D8** Formal status of Lerma → Indy in-flight transfers *(P0 — reframes Scenario 1 net-new)*

Plus P1 items: Lerma/Batavia line capacity (D4/D5), named co-mans (D6), RM sourcing (D9), cross-border logistics benchmark (D10), existing Indy capex / shift studies (D11).

*(Full Scenario 1 / 2 hypothesis tables, Week-2 day plan, risk register, and decision gates in `analysis/week2_preview.md`.)*

---

## Page 8 — Appendix

### Data quality & reconciliation
- Source: `Copy of RT and UFS Bouillon 4.13.26.xlsx`, single sheet, header row 3, data rows 4–60 (57 SKUs).
- Grand total reconciles to **5,246,057 cases** (2025 `Total 25` column = sum of monthly columns, no hidden rows).
- Three negative monthly cells at Indy (returns/corrections, immaterial). One all-zero row (Batavia 40.5 oz). `Brand` and `Pouches/CS` columns systematically blank (confirmed handled).
- Full DQ memo: `logs/data_quality_memo.md`.

### Site × channel reconciliation *(used throughout the pack)*

| Site | US Retail | UFS | CDA Retail | UI | Total |
|---|---:|---:|---:|---:|---:|
| Lerma | 3,469,125 | 371,526 | — | 2,113 | 3,842,764 |
| Indy | 818,078 | — | — | 459 | 818,537 |
| Batavia | 42,899 | 530,312 | 11,545 | — | 584,756 |
| **Total** | **4,330,103** | **901,837** | **11,545** | **2,572** | **5,246,057** |

### Assumption log
All assumptions applied during Week 1 are tracked in `logs/assumptions.md`, with impact ratings and status against sponsor confirmation. Highest-impact items: A5 (in-flight transfer interpretation), A11 (Indy line 15 headroom), A12 (Indy zero-UFS = no latent capability).

### Open questions
18 questions raised on the Wednesday call, tracked in `logs/open_questions.md` across four categories: Data / Scope / Data definition / Framing. Highest-leverage question: **Q12 — are the in-flight Lerma → Indy transfers a tracked program or tactical?** Changes the framing of both Scope B and Scope C.

### Open data requests
12 P0–P3 data requests, tracked in `logs/open_data_requests.md`. P0 items (D1, D2, D3, D8) are Scope B's critical path to completion. P1 items (D4, D5, D6, D7) are Week-2 gates.

### Supporting artifacts *(produced this week)*
- `data/sku_master.csv` — cleaned SKU master, 57 rows, derived tonnage
- `data/monthly_volume.csv` — long-format monthly fact table, dates decoded
- `logs/dq_findings.json` — machine-readable DQ findings
- `analysis/network_map.md` — full network map (Scope A)
- `analysis/format_line_complexity.md` — capability-gap detail
- `analysis/baseline_by_site.md` — site-level business baseline (Scope B)
- `analysis/week2_preview.md` — Week 2 hypotheses, questions, data needs
- `logs/data_quality_memo.md` · `logs/assumptions.md` · `logs/open_questions.md` · `logs/open_data_requests.md`

### What Week 1 does not contain *(named, not hidden)*
1. Unit conversion cost by site — not in source workbook; requested as D1
2. Gross margin by site × channel — not in source workbook; requested as D2
3. Line capacity / utilization at any site — not in source workbook; requested as D3/D4/D5
4. Named co-manufacturers / overflow partners — not in source workbook; requested as D6
5. R&D harmonization roadmap status — not in source workbook; requested as D7
6. Cross-border logistics cost / disruption history — not in source workbook; requested as D10

Week 1 ships with these gaps named, not hidden, and with the plan to close them in Week 2.

---

**End of pack.**
