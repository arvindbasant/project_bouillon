# NA Bouillon Network & Indy Consolidation — Project Plan

> **Situation:** This project was scoped as an external engagement. I have been given **Week 1** as an audition. If the Week-1 current-state deliverable is strong enough, the **full 3-week project will be assigned to me**. Weeks 2–3 are therefore *conditional* on Week-1 quality.
>
> **Mandate for Week 1:** Produce a current-state network + business baseline that is **leadership-ready, fact-based, and clearly points toward the right strategic question** — using only the brief (`NA_Bouillon_Indy_Consolidation 4.12.2026.docx`) and the data in `Copy of RT and UFS Bouillon 4.13.26.xlsx`. No other inputs are guaranteed.
>
> **Today:** 2026-04-13 · **Week-1 window:** Mon 2026-04-13 → Fri 2026-04-17

---

## 1. Project Metadata

| Field | Value |
|---|---|
| Project name | North America Bouillon Network & Indy Consolidation |
| Sponsor | Wez Beauplan — Associate Director, Foods Transformation (NA) |
| Primary site | Independence, MO ("Indy") |
| Originally scoped duration | 3 weeks |
| Original audience | External contractor / engineer |
| Current audience | Same — but the Week-1 output is also an **internal audition deliverable** |
| Source brief | `NA_Bouillon_Indy_Consolidation 4.12.2026.docx` |
| Source data (Week 1) | `Copy of RT and UFS Bouillon 4.13.26.xlsx` |

---

## 2. Context & Background (from the brief)

- Bouillon is a **strategic growth + margin driver** for NA Foods.
- Indy is positioned as the **long-term Bouillon Center of Excellence**.
- Parallel initiatives are already running (performance ramp-up, resiliency, recipe / raw-material harmonization) but **no integrated, fact-based view** of the NA bouillon manufacturing network exists today.
- The brief is explicit: **reuse existing Unilever materials and the R&D harmonization track — do not rebuild analysis from scratch.**
- Project is intended to be **rapid** — 3 weeks from current state to leadership recommendation.

---

## 3. Objectives (from the brief)

1. Map the current NA bouillon manufacturing & logistics network.
2. Establish a clear current-state business baseline by site / country.
3. Develop **two** future-state consolidation scenarios centered on Indy.
4. Provide a **realistic three-year glidepath** for each scenario.

**Week-1 is objectives 1 + 2.** Objectives 3 + 4 are Weeks 2 + 3 and are the prize for winning Week 1.

---

## 4. Scope of Work (from the brief)

### A. Current-State Network Mapping *(Week 1)*
- Manufacturing locations (Indy, Lerma, Batavia, co-mans, overflow/resiliency partners).
- Portfolio split: **Total Portfolio → Retail → UFS**.
- Product formats (cubes, granulated, pastes; sizes).
- Logistics flows + interfaces between Indy, co-mans, overflow partners.
- Constraints, complexity drivers, **known network fragilities**.

### B. Current-State Business Assessment *(Week 1)*
Fact-based baseline **by manufacturing site / country**:
- Volume (tonnes, cases).
- Cost structure (directional where data is available).
- Procurement considerations.
- Gross margin (directional).
- Key operational / commercial challenges.
- **Where Indy is advantaged vs constrained** relative to the network.

### C. Future-State Scenarios *(Weeks 2–3, contingent)*
- **Scenario 1 — Maximize Bouillon Tonnes at Indy.**
- **Scenario 2 — Full Bouillon Consolidation at Indy.**
- Each with a 3-year glidepath, enablers, risks, trade-offs.

---

## 5. Source Data Structures

### 5.1 `NA_Bouillon_Indy_Consolidation 4.12.2026.docx`
Plain narrative brief. Sections: Context, Objectives, Scope (A/B/C), Timeline & Phases. No embedded tables or figures. Used as the **requirements anchor**.

### 5.2 `Copy of RT and UFS Bouillon 4.13.26.xlsx`
Single sheet. Header row **3**. Data rows **4–60 (57 SKUs)**.

**Columns (A → Z):**

| Col | Field | Notes |
|---|---|---|
| A | `Sourcing Unit` | Mfg site: `Indy`, `Lerma`, `Batavia` |
| B | `DU` | Distribution-unit / material ID |
| C | `Brand` | Blank in sample — likely all Knorr; confirm |
| D | `Sub-Category` | `Sabor` or `Granulated Bases/Bouillon` |
| E | `Technology Detailed` | `Small Granulated`, `Large Granulated`, … |
| F | `Line` | `Mateer 1`, `Mateer 3`, `15`, `0` |
| G | `Size` | `7.9oz`, `2lb`, `2.5lb`, `40.5oz`, … |
| H | `Country` | `US Retail`, `UFS`, `CDA Retail`, `UI` |
| I | `Sales Org OpCo` | e.g. `US Retail` |
| J | `Product DU` | SKU description |
| K | `Pouches/CS` | Mostly blank |
| L | `Tonnes/CS` | Case → tonnage conversion factor |
| M | `2025 Growth` | Growth factor |
| N–Y | Monthly cases 2025 | 12 buckets; headers are Excel date serials (45658 = Jan-25 … 46010 = Dec-25) |
| Z | `Total 25` | Full-year cases |

**Volume snapshot (2025):** 5,246,057 cases across 57 SKUs.

| Sourcing Unit | Cases 2025 | Share | Approx tonnes\* |
|---|---:|---:|---:|
| Lerma (MX) | 3,842,764 | **73.3%** | ~28,800 |
| Indy (MO) | 818,537 | 15.6% | ~4,400 |
| Batavia | 584,756 | 11.1% | ~10,000 |

\* `Σ(cases × Tonnes/CS)` — directional only.

| Channel | Cases | Share | | Sub-Category | Cases | Share |
|---|---:|---:|---|---|---:|---:|
| US Retail | 4,330,103 | 82.5% | | Sabor | 4,307,514 | 82.1% |
| UFS | 901,837 | 17.2% | | Granulated Bases/Bouillon | 938,544 | 17.9% |
| CDA Retail | 11,545 | 0.2% | | | | |
| UI | 2,572 | 0.0% | | | | |

**Site × channel (cases):**
- **Lerma** → US Retail 3.47M · UFS 372K · UI 2K
- **Indy** → US Retail 818K · UI 0.5K *(Retail-only today)*
- **Batavia** → UFS 530K · US Retail 43K · CDA Retail 12K *(UFS-dominant)*

### 5.3 Data quality notes & gaps
- **Brand** column blank — confirm intent.
- **Pouches/CS** mostly blank — derive from size if needed.
- Several SKUs show **mid-year site transfers** (zeros in H1 then volume, e.g. `KNR MEX BOUIL CHK 6 2 LB` shifting Lerma → Indy). These are in-flight moves the baseline must explicitly reconcile.
- Negative monthly values (`-480`, `-192`) — likely returns/corrections; flag in cleanse.
- Monthly headers are **Excel date serials**, not strings — decode before presenting.
- **No cost, GM, procurement, or capacity data in this workbook.** Week-1 business assessment must be framed as *volume-complete, cost/GM directional-only* and cost-data gaps must be **called out, not hidden**.

---

## 6. Target Analysis Data Model (Week 1)

1. **SKU master** — one row per `DU`: site, sub-category, tech, line, size, channel, `Tonnes/CS`, `Pouches/CS`.
2. **Monthly volume fact** — `(DU, month) → cases, tonnes`.
3. **Site roll-up** — `site → cases, tonnes, channel mix, format mix, top SKUs, in-flight transfers`.
4. **Format / line map** — `(site, line, format) → current load`.

Items 1–4 are fully buildable from the Excel **today**. Anything that needs cost / GM / capacity data is flagged as an **open data request**, not silently omitted.

---

## 7. How I Win Week 1 *(the audition rubric)*

This section is the whole point of this plan. Week 1 has to demonstrate five things — if any one is weak, the project walks.

1. **Fact discipline.** Every number traceable to the Excel. A one-page data-quality memo proves rigor before the first chart.
2. **Analytical insight, not description.** The deliverable must explicitly state the strategic insight the numbers reveal — *this is fundamentally a Lerma → Indy question, not a Batavia question* (73% of NA cases live in Lerma today). Most contractor decks describe; I need to *point*.
3. **Capability-gap framing.** Call out that **Indy today is ~100% Retail** and **Batavia today is UFS-dominant**. Any "consolidate at Indy" path requires Indy to stand up a UFS footprint it doesn't run — large formats (2.5 lb / 40.5 oz), different lines. This single observation reframes Scenario 2 and is the kind of senior thinking that wins the project.
4. **Preview Week 2 without overreaching.** End the Week-1 pack with a **one-page "what Week 2 will answer"** — questions, hypotheses, data I'd need. Signals I already see the path forward and can execute it.
5. **Leadership-ready craft.** Exec summary on page 1. Clean visuals. Tight writing. No jargon dumps. Assumption + open-question log in the appendix. Reads like something Wez could forward to his boss unchanged.

**Differentiators to build in explicitly:**
- A **single "one-chart" view** of the network (site × channel × volume) that lands the story in five seconds.
- A **format / line complexity map** showing which formats run where — sets up Scenario 2 capability gap.
- An **in-flight transfer callout** — SKUs already moving Lerma→Indy in 2025 — proves I read the data, not just summed it.
- A short, direct **"advantaged / constrained" read on Indy** — not hedged.

**Anti-patterns to avoid:**
- Reciting the brief back at the sponsor.
- Stacking charts without an insight line above each one.
- Hiding data gaps — better to name them and show the plan to close them.
- Premature Scenario 1 / 2 answers — stay in Week 1 lane, but *signal* I can do Weeks 2–3.

---

## 8. Week 1 — Daily Plan *(Mon 04-13 → Fri 04-17)*

**Goal:** Produce a pitch-quality current-state pack + baseline tables that make Weeks 2–3 mine.

### Mon 04-13 — Ingest, clean, reconcile
- Normalize the Excel into `sku_master.csv` and `monthly_volume.csv`.
- Decode monthly date-serial headers.
- Compute totals by site, channel, sub-category, format, line.
- Reconcile to grand total 5,246,057 cases.
- Flag negatives, blanks, in-flight transfers in a data-quality memo.
- **EOD artifact:** cleaned data tables + `data_quality_memo.md`.

### Tue 04-14 — Network map + format/line complexity
- Draft the network map: Indy, Lerma, Batavia, implied co-man / overflow nodes, Retail vs UFS flows.
- Build the **format × line × site** complexity view.
- Identify the **capability gap** (Indy = Retail; Batavia = UFS) and write the narrative for it.
- **EOD artifact:** `network_map.md` + complexity table.

### Wed 04-15 — Business baseline by site
- For each site (Indy / Lerma / Batavia): volume (cases + tonnes), channel mix, format mix, top SKUs, in-flight transfers, known constraints.
- Explicit **"Indy: advantaged / constrained"** section.
- Cost / GM / procurement: short, honest directional read **plus** an open-data-request list for Finance / Procurement.
- **EOD artifact:** `baseline_by_site.md`.

### Thu 04-16 — Insight synthesis + Week-2 preview
- Write the **exec summary** (one page, insight-led, not description-led).
- Write the **Week-2 preview page** (hypotheses, questions, data needed).
- Pull the **"one-chart" network view** and the **strategic insight line** to the very front.
- Build the assumption log + open-questions log.
- **EOD artifact:** `week1_pack_draft.md` + `logs/*`.

### Fri 04-17 — Polish, pressure-test, deliver
- Self-review against the §7 rubric — kill anything that doesn't earn its place.
- Dry-run the 5-minute verbal pitch: *situation → insight → baseline → gap → what I'll do in Week 2*.
- Final edit pass. Lock the pack.
- **EOD artifact:** `WEEK1_DELIVERABLE.md` (or `.pdf` / `.pptx` if slide format is preferred).

---

## 9. Weeks 2–3 *(conditional — outlined, not day-planned)*

Day-level planning for Weeks 2 + 3 happens **only after Week 1 is accepted**. Outline form only:

### Week 2 — Scenario Development · Apr 20 → Apr 24
- Quantify Indy headroom (capacity, shifts, theoretical max without capex).
- **Scenario 1** (Maximize Indy): which Lerma/Batavia SKUs move, in what order, enablers, risks.
- **Scenario 2** (Full consolidation): capability gaps, harmonization dependencies, capex signal.
- Build 3-year glidepaths for both.
- Internal challenge session; refine.

### Week 3 — Synthesis & Recommendation · Apr 27 → May 1
- Comparative matrix: Scenario 1 vs 2 across volume, cost signal, risk, harmonization load, timing.
- Draft recommendation + decision gates.
- Full pack assembly → sponsor review → final read-out.
- Close-out: data pack, assumption log, open risks.

---

## 10. Week-1 Deliverable Spec *(what actually lands on Wez's desk Friday)*

A single leadership-ready pack containing, in order:

1. **Exec summary** (1 page) — the strategic insight, stated plainly.
2. **One-chart network view** — site × channel × volume, 2025.
3. **Current-state network map** — sites, channels, formats, flows, fragilities.
4. **Business baseline by site** — Indy, Lerma, Batavia. Volume complete; cost/GM directional; advantaged/constrained read on Indy.
5. **Format / line complexity map** — the capability-gap page.
6. **In-flight transfers callout** — what's already moving in 2025.
7. **Week-2 preview** — hypotheses, questions, data needs.
8. **Appendix** — data-quality memo, assumption log, open questions, open data requests.

**Quality bar:** every page has an insight line at the top. Every number is traceable to the Excel. Nothing hedged that can be stated, nothing stated that can't be defended.

---

## 11. Risks to Winning Week 1

| # | Risk | Mitigation |
|---|---|---|
| R1 | Over-investing in decoration, under-investing in the insight | Write the exec summary **first**, Thursday morning, before polish |
| R2 | Cost / GM gap makes Scope B look thin | Frame directionally, name the gap proudly, show the plan to close it in Week 2 |
| R3 | Getting stuck in data cleansing on Monday and losing analysis time | Time-box Monday to EOD; accept imperfect cleansing if it blocks analysis |
| R4 | Describing instead of pointing | §7 rubric review on Friday — if a page has no insight line, it gets cut |
| R5 | Scope creep into Scenarios 1/2 | Hard rule: Week-1 pack previews Week 2 on **one** page only |
| R6 | Sponsor unreachable for questions in Week 1 | Log questions as I go; ship with clearly-stated assumptions rather than waiting |

---

## 12. Open Questions for Sponsor *(raise early, don't block on)*

1. Is the Week-1 deliverable expected as a **deck**, a **memo**, or both?
2. Confirm the scope of "NA" — does CDA Retail / UI channel matter, or is it de minimis?
3. Are co-manufacturers and overflow partners named somewhere I can reference?
4. Is there an existing Indy capacity / shift model?
5. Where does the R&D harmonization roadmap live, and who owns it?
6. Fastest route to site-level cost / GM data (SAP pull? Finance partner?)
7. Does the "3-week clock" start today or is it anchored to a later Scenario-phase start?

---

## 13. Working Artifacts *(to be produced this week, in this folder)*

- `PROJECT_PLAN.md` — *this file*
- `data/sku_master.csv` — normalized SKU master *(Mon)*
- `data/monthly_volume.csv` — monthly fact table *(Mon)*
- `logs/data_quality_memo.md` *(Mon)*
- `analysis/network_map.md` *(Tue)*
- `analysis/format_line_complexity.md` *(Tue)*
- `analysis/baseline_by_site.md` *(Wed)*
- `analysis/week2_preview.md` *(Thu)*
- `logs/assumptions.md`, `logs/open_questions.md`, `logs/open_data_requests.md`
- `WEEK1_DELIVERABLE.md` — the pack *(Fri)*
