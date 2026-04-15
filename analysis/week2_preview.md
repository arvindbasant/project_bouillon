# Week 2 Preview — Scenario Framing, Hypotheses, Data Needs

**Week:** 1 · **Day:** 4 (Thu 2026-04-16) · **Purpose:** End the Week-1 pack with a one-page signal that Week 2 can be executed cleanly. Not a plan for Week 2 — a *preview* of how Week 2 will be framed the day it starts.

---

## 1. Headline

> **Week 2 does not answer "should we consolidate at Indy". The current-state baseline already shows consolidation is partially in motion. Week 2 answers two much sharper questions:**
>
> **Q1.** *How much more of the 1.48M Lerma-addressable pool can Indy absorb without new line investment, and what does the second-line decision look like if the answer is "not much more"?*
>
> **Q2.** *For the 2.94M cases of network volume Indy cannot run today, which subset is worth building capability for at Indy — and on what 3-year glidepath, with what harmonization dependency?*
>
> **Scenario 1 answers Q1. Scenario 2 answers Q2. They are different kinds of projects and should not share a single set of assumptions.**

---

## 2. The two scenarios, reframed

| | **Scenario 1 — Maximize Indy** | **Scenario 2 — Full Consolidation at Indy** |
|---|---|---|
| **What it is** | Capacity / throughput question on formats Indy already runs | Capability-build + harmonization program |
| **Scope** | ~1.48M Lerma cases in 2 lb + 15.9 oz | ~2.94M cases across 6 new formats + 4 new technology types + UFS footprint from scratch |
| **Primary gating question** | Line-15 headroom (+ second-line decision) | Which Batavia / Lerma-unique SKUs survive harmonization and end up at Indy |
| **Capex profile** | Low–medium (line, shift, minor packaging) | High (new lines, new tech, new UFS footprint, possible building scope) |
| **R&D dependency** | Low (same recipes already running at Indy) | **High** (Caldo / MixMod / Natural harmonization is the critical path) |
| **Time horizon** | Near-term, possibly within 12 months for the shift itself | 3-year glidepath; the first year is harmonization + engineering, not tonnage |
| **Risk concentration** | Execution risk on line 15 throughput | Capability and harmonization risk, plus Canadian regulatory scope from Batavia CDA |
| **Who the quantification depends on** | NA Ops (Indy capacity, shift model) + Finance (unit cost) | NA Ops + Finance **+ R&D** (harmonization roadmap status per SKU family) |
| **What kills it** | Line-15 is already maxed and no second-line path exists | Harmonization roadmap is immature or Batavia technology cannot be replicated at Indy at comparable cost |

Framing Scenarios 1 and 2 as two different programs (rather than "low case / high case" of the same program) is the single most important analytical move Week 2 has to make.

---

## 3. Scenario 1 — Maximize Indy

### Working hypotheses *(to confirm / falsify in Week 2)*

- **H1.1** — Indy line "15" has headroom above 2025 run rate on at least one of its two formats, in the range needed to absorb a meaningful fraction of the ~1.48M Lerma-addressable pool. *(Falsifiable with D3: line 15 theoretical capacity + 2025 utilization.)*
- **H1.2** — Approximately 350K cases of the Lerma-addressable pool have already moved to Indy during H2 2025. The **net new** Scenario 1 opportunity is therefore smaller than the gross 1.48M figure suggests. *(Quantifiable from `monthly_volume.csv` + sponsor confirmation on D8.)*
- **H1.3** — The flagship SKU `KNR MEX BOUIL CHK 6 2 LB` (1.18M cases total, 85% still at Lerma) is the biggest single lever in Scenario 1. Its migration path alone could account for most of the achievable Scenario 1 volume.
- **H1.4** — A second line at Indy (new or reactivated) is the binary decision that separates "Scenario 1 capped at line-15 headroom" from "Scenario 1 capable of fully absorbing Lerma 2 lb + 15.9 oz." *(Confirmable against any existing Indy capex / shift-expansion study — D11.)*
- **H1.5** — 7.9 lb UFS (Lerma Mateer 2, 371K cases) is **not** a Scenario 1 item because Indy has no UFS line. It must be carried into Scenario 2 despite being "Lerma-unique Retail formats" being the Scenario 2 headline.

### Questions Week 2 must answer

1. What is Indy line "15" theoretical capacity (cases/shift, shifts/day)?
2. What is 2025 utilization %?
3. At what utilization does line 15 stop being able to absorb transfer volume?
4. What is the net-new (post-H2-2025) addressable Lerma volume for Scenario 1 once already-in-flight transfer is separated out?
5. Is there an existing Indy second-line / shift-expansion study, and what does it say?
6. What is the Scenario 1 3-year glidepath by SKU: which SKUs shift first, in what quarters, hitting what case run rate at Indy by end of Year 3?

### Data needed
- **D3** Indy line 15 capacity + utilization (**P0**, blocks all S1 quantification)
- **D4** Lerma Mateer 1 / 2 / 3 capacity + utilization (P1 — needed to confirm Lerma has the excess to hand off)
- **D8** Formal status of the Lerma → Indy transfers (tracked program vs tactical) (**P0** — reframes the "net new" calculation)
- **D11** Existing Indy capex / shift-expansion study (P2 — informs the second-line decision)
- Monthly 2026 actuals or 2026 S&OP view for Indy line 15, if available

---

## 4. Scenario 2 — Full Consolidation at Indy

### Working hypotheses *(to confirm / falsify in Week 2)*

- **H2.1** — Scenario 2 is not a tonnage problem, it is a **capability problem**. The 2.94M cases of non-Indy-today volume consists of 6 pack formats and at least 4 technology types Indy has never run; "consolidating" them is a build program that consumes harmonization + engineering + capex, not a production reassignment.
- **H2.2** — The UFS half of Scenario 2 (~900K cases: Batavia 530K + Lerma 372K) is the highest-cost, longest-lead portion because it requires standing up not just new lines but a new channel capability at Indy (packaging, labeling, distribution, possibly RM supply).
- **H2.3** — The Lerma 7.9 oz / 3.5 oz Small Granulated pool (~1.97M cases, ~38% of NA network) is the largest single non-Indy Retail block but is tied to specific Mateer 1 technology. Whether it moves to Indy depends on whether Indy's line 15 (or a new Indy line) can run Small Granulated at 7.9 oz and 3.5 oz pack sizes — **not a given, to confirm**.
- **H2.4** — **R&D harmonization is the critical path.** Batavia runs Caldo 4.4 / Caldo 25 lb / MixMod / Small Granulated Natural — technology variants that need to either be harmonized out or replicated at Indy. The R&D roadmap status (D7) determines whether Scenario 2 even has an executable path.
- **H2.5** — Batavia's 11,545 CDA Retail cases are a **regulatory scope** item, not a tonnage item. Scenario 2 has to explicitly decide whether to carry CDA Retail to Indy (new Canadian labeling scope), leave it at Batavia, or exit.
- **H2.6** — The "2 lb 480 at Batavia" residuals (7.4K cases of palletized 2 lb across three DUs) and the 2.5 lb Retail (10K cases) are Week-2 rationalization candidates, not transfer candidates. Simplifying them is cheaper than moving them.

### Questions Week 2 must answer

1. What is the current state of the NA bouillon R&D harmonization roadmap, per SKU family? Which Batavia technologies are targeted for harmonization, which are to be retained as-is, which are in flight?
2. What subset of the 2.94M non-Indy-today cases survives harmonization as "still needed"? (Harmonization could legitimately reduce the addressable pool.)
3. For each surviving format, is Indy technically capable of running it with a line addition, or does it require a new line + new tech + new RM arrangement?
4. What is the indicative capex envelope for a UFS footprint at Indy (4.4 lb line, 7.9 lb line, new channel capability)? Order-of-magnitude only — the question is "is this $10M or $100M".
5. What is a credible 3-year glidepath for Scenario 2? Most likely pattern: Year 1 = harmonization + engineering + capex approval, Year 2 = first new line commissioning + transfer of formats where harmonization is complete, Year 3 = UFS footprint ramp.
6. What happens to Batavia at the end of Scenario 2 — closed, repurposed, retained as backup? The Week-1 baseline cannot answer this; Week 2 must.

### Data needed
- **D1** Site-level conversion cost by sub-category (**P0** — required for any Scenario 2 cost framing)
- **D2** Directional GM by site × channel (**P0**)
- **D5** Batavia line 13 + line 0 capacity + utilization (P1)
- **D6** Named co-manufacturers / overflow partners (P1 — could materially change Scenario 2 scope)
- **D7** R&D harmonization roadmap status per SKU family (**P0** — critical path)
- **D9** RM sourcing points (P2 — cost framing for Batavia's Caldo recipes)
- Indicative capex benchmarks for new US food-manufacturing lines (external, not in sponsor's hands)

---

## 5. The glidepath approach *(how Week 2 builds them)*

For **each** scenario, Week 2 produces a 3-year year-by-year view:

```
                    Y1 (2026)       Y2 (2027)       Y3 (2028)
Scenario 1:         ← which SKUs move, at what run rate, ending at what Indy total →
Scenario 2:         Harmonization   First new line   UFS ramp + Batavia decision
                    + engineering   + transfer of
                    + approvals     harmonized
                                    formats
```

Each year carries: **volume moved / volume still at origin / enablers done / enablers outstanding / risks / decision gates**. The gates are what make the glidepath executable rather than aspirational. Examples of Week 2 decision gates:

- End of Q2 2026 — line-15 utilization floor for Scenario 1 to be alive.
- End of Q4 2026 — harmonization roadmap maturity gate for Scenario 2 go / no-go on first build year.
- End of Q2 2027 — first new Indy line commissioning signoff for Scenario 2.

Without gates, a glidepath is a wish-list. With gates, it's a plan.

---

## 6. Week 2 — working day plan *(outline, not committed)*

*(Day-level commitment happens only after Week 1 is accepted and the gating data from D1/D2/D3/D7/D8 is in hand. Outline only.)*

- **Mon 04-20** — Quantify Indy line 15 headroom. Separate "already booked" from "net new" Scenario 1 volume using monthly profiles. Start Scenario 1 glidepath skeleton.
- **Tue 04-21** — Scenario 1 glidepath with sequencing by SKU, enablers, risks, gate points. Internal challenge against capacity numbers.
- **Wed 04-22** — Scenario 2 capability map: which of the 2.94M cases survives harmonization, which requires build at Indy, which is a candidate for rationalization. Batavia exit-state options.
- **Thu 04-23** — Scenario 2 glidepath. Capex signal (order of magnitude). Comparative matrix draft (S1 vs S2 on volume, cost, capex, harmonization load, risk, time).
- **Fri 04-24** — Synthesis + internal review + pack draft for Week 3 sponsor readout.

---

## 7. Risks to Week 2 execution *(surface now, manage early)*

| # | Risk | Mitigation |
|---|---|---|
| W2-R1 | D1 / D2 (cost, GM) arrive late or never — Scenario framing stays volume-only | Have a volume-only Scenario 1 glidepath ready that stands up without unit cost; treat cost as an overlay, not a gate |
| W2-R2 | R&D harmonization roadmap (D7) is immature or not shareable | Scenario 2 fallback — frame the capability build as gated on harmonization rather than quantified against it; make harmonization maturity the first Week-2 decision gate |
| W2-R3 | Indy capacity (D3) reveals line 15 is already maxed — Scenario 1 collapses unless the second-line path is real | Pre-commit to a "constrained Scenario 1" variant that shows what's achievable without a second line; force the second-line decision into the Week-3 recommendation |
| W2-R4 | Sponsor wants a single recommended scenario, not two | Hold the two-scenario frame through Week 2, bring the recommendation in Week 3 — don't pre-collapse Week 2 |
| W2-R5 | In-flight transfer (D8) turns out to be tactical, not a tracked program | Scenario 1 gets scoped against the full 1.48M gross pool rather than the smaller net-new pool. Easier case, not harder. |

---

## 8. What this preview commits to

By end of Week 2 the sponsor should have, in the pack:

1. A Scenario 1 3-year glidepath with year-by-year volume, enablers, and gates.
2. A Scenario 2 3-year glidepath framed as a capability-build program with harmonization as the critical path.
3. A comparative matrix covering volume, cost signal, capex signal, risk, harmonization dependency, and timing.
4. A draft recommendation framing (the full recommendation lands in Week 3).
5. An updated assumption log, open-data log, and risk log.

**What this preview does not commit to:** single-number unit cost deltas, a dollar-precise capex envelope, or a final Batavia exit-state decision. Those are Week-3 outputs contingent on Week-2 data arriving.
