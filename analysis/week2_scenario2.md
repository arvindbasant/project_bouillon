# Week 2 — Scenario 2: Full Consolidation at Indy

**Week:** 2 · **Day:** 1 (Wed 2026-04-15)
**Scope:** Frame the S2 capability build · size the gap · structure the glidepath skeleton · identify critical-path decisions
**Source:** `data/sku_master.csv` · `analysis/format_line_complexity.md`

---

## 1. Headline

> **Scenario 2 requires Indy to stand up ~30,746 t of production capability it has never run.** This is not a volume-transfer — it is a capability-build program gated on R&D harmonization, multi-line investment, and a new UFS channel footprint at Indy.
>
> The 30,746 t breaks into three distinct risk tiers, each with a different program structure:
> 1. **Lerma small formats (~5,300 t)** — same technology as Indy, different pack sizes. Medium complexity.
> 2. **Lerma UFS (~5,325 t)** — different channel, different format, different logistics. High complexity.
> 3. **Batavia specialty (~10,007 t)** — different technology (Caldo, MixMod, Natural), Canadian scope, unique RM. Highest complexity.
>
> The R&D harmonization roadmap (D7) is the critical-path input. Until that's in hand, the glidepath is structural, not quantified.

---

## 2. The S2 capability-build map

### 2a. What Indy would need to build (tonnes basis)

| Format / Technology | Currently at | 2025 Tonnes | Capability lift | Complexity |
|---|---|---:|---|---|
| **7.9 oz Small Granulated** | Lerma Mateer 1 | **4,806 t** | New pack size (Indy runs 15.9 oz, not 7.9 oz). Mateer 1-type technology. Different packaging line / fill weight. | Medium |
| **3.5 oz Small Granulated** | Lerma Mateer 1 | **439 t** | New pack size. Same technology class. | Medium-low |
| **40.5 oz Large Granulated** | Lerma Mateer 3 | **10,167 t** | Wait — this is 40.5 oz, which is also Large Granulated. But at 0.55 kg/case Lerma can make it on Mateer 3. Indy would need a large-format pack line. | Medium |
| **7.9 lb UFS (Large Gran)** | Lerma Mateer 2 | **5,325 t** | New channel (UFS). New pack format. New UFS distribution + labeling at Indy. No UFS precedent at Indy. | **High** |
| **4.4 lb Caldo (UFS)** | Batavia line 13 | **3,644 t** | Entirely new technology (Knorr Caldo). New UFS line. New RM sourcing. Caldo recipe ≠ Granulated recipe. | **Very High** |
| **25 lb bulk Caldo (UFS)** | Batavia | **838 t** | New technology + new foodservice drum format. | **Very High** |
| **2 lb palletized (480/pallet)** | Batavia line 0 | **2,695 t** | Same Large Granulated technology as Indy's 2 lb, but packed as 480-unit wholesale pallets (SKU: KNR LAT Chicken GRAN 480 2.0LB PAL). Requires a palletizing / bulk-pack line that Indy doesn't run. Small in cases (6,188 pallets) but significant in tonnes because each pallet = 435 kg. Rationalization candidate (merge with retail 2 lb at a pallet-pack partner). | Low-medium |
| **2.5 lb Large Gran** | Batavia line 0 | **2,242 t** | New pack size. Large Granulated technology (same as Indy). R&D harmonization could merge into 2 lb. | Low-medium |
| **2.6 oz Zero Salt** | Batavia line 0 | **19 t** | New pack size + Zero Salt variant. Niche volume. | Low |
| **160 g Zero Salt (CDA Retail)** | Batavia line 13 | **22 t** | New pack + **Canadian regulatory scope** (bilingual labeling, CFIA compliance). Only 22 t. | Medium (regulatory) |
| **Large Gran MixMod** | Batavia | **545 t** | Proprietary MixMod technology (mixed commodity format). New at Indy. May be harmonizable to standard Large Gran. | High (R&D gate) |
| **Small Gran Natural** | Batavia | **37 t** | Zero-Salt / Natural variant. Small volume. Harmonization candidate. | Low-medium |

**Total S2 capability build: ~30,746 t (30,084 cases)**

### 2b. Risk-tier segmentation

| Tier | Segment | Tonnes | Cases | Key gate |
|---|---|---:|---:|---|
| **T1 — Pack-only** | Lerma 7.9 oz + 3.5 oz (same tech, new sizes); Batavia 2.5 lb; Zero Salt 2.6 oz | **5,262 t** | ~2,225K | Line-15 / new-line pack capability; R&D recipe confirmation |
| **T2 — UFS channel build** | Lerma 7.9 lb UFS + Batavia 4.4 lb Caldo + 25 lb bulk Caldo | **9,807 t** | ~901K | UFS footprint at Indy: new line(s) + new channel logistics + new RM sources |
| **T3 — Technology + R&D** | MixMod, Natural, Caldo variants, CDA scope | **604 t** | ~128K | R&D harmonization roadmap — can these be collapsed into T1/T2 products or must they be built separately? |
| **Lerma 40.5 oz** | Large Gran, large format | **10,167 t** | ~18K | Pack line capacity — technically same technology as Indy's 2 lb, just different fill |
| **CDA Retail** | 160 g Zero Salt | **22 t** | ~12K | Canadian regulatory scope — build at Indy vs retain at Batavia vs exit |

**Note:** The 40.5 oz row is unusual — it's 10,167 t from only 18,457 cases (~17.3 kg/case). This is a very large-format pack running at tiny volume. At this volume level it is likely a rationalization candidate, not a transfer candidate.

---

## 3. The three critical-path decisions

### CPD-1: R&D harmonization roadmap (D7 — P0 gate)

The R&D harmonization roadmap determines whether Batavia's specialty technologies (Caldo, MixMod, Natural) need to be replicated at Indy or can be simplified out. Two outcomes:

| Harmonization outcome | S2 scope impact | Indy build required |
|---|---|---|
| **Optimistic:** Caldo variants → harmonized into 1 Granulated recipe; MixMod → retired; Natural → merged into standard | T3 (604 t) disappears; Caldo UFS shrinks | ~2 new lines at Indy (retail small format + UFS large format) |
| **Pessimistic:** all Batavia technologies survive harmonization | Full T3 required; each technology needs its own Indy capability | 4+ new lines at Indy; significant RM supply complexity |

**This is the single most important S2 unknown.** The difference between optimistic and pessimistic is multiple lines and potentially a program-vs-project distinction.

### CPD-2: UFS footprint at Indy (D3 + capex gate)

Indy has **zero UFS production today.** The 9,807 t UFS build (T2) requires:
- At minimum 1 new line for 7.9 lb Large Granulated UFS
- At minimum 1 new line for Caldo 4.4 lb (different technology than granulated)
- New UFS-spec packaging and distribution capability
- New RM contracts for Caldo-specific ingredients

This is not a shift-model or headroom question — it is a multi-line greenfield build at Indy. Order-of-magnitude capex: likely $10–50M range (rough benchmark only, D11 for Indy specifics).

**Gate:** Capex approval is the CPD-2 gate. Without an approved capex envelope, the UFS build cannot start. This makes it Year 2-3 at the earliest.

### CPD-3: Batavia exit state

Scenario 2 implicitly assumes Batavia is closed or repurposed. But Batavia has:
- 7 formats, 6 technology types, 2 lines
- The only CDA Retail source in the network
- Unique UFS technology (Caldo) with its own RM supply chain

**Three options for Batavia's endgame:**
| Option | Description | S2 complexity |
|---|---|---|
| **Close** | Full transfer of all Batavia volume to Indy | Maximum build at Indy; requires all T1+T2+T3 |
| **Retain UFS specialist** | Indy takes Retail; Batavia retains UFS (4.4 lb, 25 lb, 7.9 lb) | ~10K t stays at Batavia; Indy builds ~20K t only |
| **Partial close** | Indy takes Retail + select UFS; Batavia retained for residual specialty | Depends on harmonization outcome |

**This is a Week-3 recommendation input, not a Week-2 decision.** But Week 2 must frame the options and their volume/cost implications.

---

## 4. What S2 actually requires at Indy — a line-build map

If Batavia is fully closed (maximum S2), Indy would need:

| New capability | Volume supported | Line type | Technology |
|---|---:|---|---|
| Small format pack line (7.9 oz + 3.5 oz) | ~5,300 t | Retail small gran line | Same base tech as line 15 — different fill / pack |
| 40.5 oz large-format line | ~10,200 t | Large format Retail | Same tech as line 15 — very large fill weight |
| UFS 7.9 lb line | ~5,325 t | UFS large granulated | Similar to Mateer 2 at Lerma |
| Caldo 4.4 lb line | ~3,644 t | UFS specialty | New technology — Knorr Caldo process |
| Caldo 25 lb bulk line | ~838 t | UFS foodservice drum | New technology + new format |

**That is 5 new production lines at Indy** (vs 1 today). Even with harmonization removing T3, the minimum is 3-4 new lines.

---

## 5. S2 three-year glidepath skeleton

*(Quantification pending D1, D7, capex benchmarks. Structure is fixed.)*

### Year 1 (2026) — R&D + Engineering + Approvals

| Stream | Activity | Output | Gate |
|---|---|---|---|
| R&D | Complete harmonization roadmap per SKU family | Which Batavia technologies survive, which are rationalized | **D7 required** |
| Engineering | Scope new lines at Indy (small format, UFS, Caldo) | Capex estimate ±30% | Site capacity study |
| Finance | Cost-delta model S2 vs status quo | NPV envelope for approval package | D1, D2 required |
| Regulatory | CDA Retail scope decision (Indy vs Batavia retain vs exit) | Definitive scope | Legal/regulatory review |

### Year 2 (2027) — First Line + T1 Transfers

| Stream | Activity | Volume added at Indy | Gate |
|---|---|---:|---|
| Line build | Commission small-format line (7.9 oz capability) | ~5,300 t | Capex approved Q4 2026 |
| Transfer | Begin 7.9 oz + 3.5 oz Lerma → Indy transfers | ~5,300 t/yr | New line commissioned |
| UFS — start | Begin UFS footprint engineering | — | Harmonization complete |
| Batavia | Reduce Batavia Retail footprint (2.5 lb + Zero Salt rationalization) | — | S2 scope confirmed |

### Year 3 (2028) — UFS Build + Batavia Wind-down

| Stream | Activity | Volume added at Indy | Gate |
|---|---|---:|---|
| UFS line 1 | Commission 7.9 lb UFS line | ~5,325 t | Year-2 engineering complete |
| UFS line 2 | Commission Caldo 4.4 lb line | ~3,644 t | Caldo harmonization + recipe transfer |
| Transfer | 7.9 lb UFS from Lerma; Caldo from Batavia | ~9,000 t | Lines commissioned |
| Batavia | Evaluate close vs partial retain | — | Volume milestones met |

### Steady state (2029+)

| Site | Volume | Lines | Formats |
|---|---:|---|---|
| **Indy (post-S2)** | **~35,000 t** | **5-6 lines** | All retail formats + UFS 7.9 lb + Caldo |
| **Lerma** | ~6,000 t residual or 0 | Mateer 1 (7.9 oz remains?) | To be confirmed |
| **Batavia** | 0 (or residual specialty) | — | Rationalized |

---

## 6. Open items — what blocks S2 quantification

| Item | Blocks | Expected source |
|---|---|---|
| **D7** R&D harmonization roadmap | The single most important S2 unknown — determines scope | R&D team |
| **D1** Site-level conversion cost | Cost-delta model, NPV for capex approval | Finance / Ops |
| **D2** Directional GM by site × channel | NPV, payback period | Finance |
| **D5** Batavia line 13 capacity and utilization | Transition timing | Ops |
| **D6** Named co-manufacturers | Could materially reduce S2 scope if overflow partners can absorb specialty formats | Sponsor |
| Capex benchmark for new US food lines | Order-of-magnitude sizing | Industry benchmarks / D11 |
| Batavia exit-state decision criteria | Scope of "full close" | Sponsor + Finance |

---

## 7. S2 risk log

| # | Risk | If realized | Mitigation |
|---|---|---|---|
| S2-R1 | Harmonization roadmap is immature (D7 not available or not actionable) | S2 cannot be scoped. Frame as gated on harmonization maturity. | Pre-build a "harmonization-first" variant where Year 1 is entirely R&D — no line build starts until roadmap is locked |
| S2-R2 | Caldo technology is not replicable at Indy at comparable cost | UFS Caldo (~3,644 t) stays at Batavia indefinitely | "Batavia UFS specialist retained" becomes the recommended endgame for Caldo; Batavia partial close |
| S2-R3 | CDA Retail (160 g) creates disproportionate regulatory complexity at Indy | 22 t of niche volume triggers Canadian regulatory scope for all of Indy | Exit CDA Retail SKUs or retain at Batavia permanently |
| S2-R4 | 40.5 oz format (10,167 t, 18K cases) is a single-buyer or private-label arrangement | Transfer to Indy is not viable; SKU is rationalized | Confirms the "rationalization candidate" read — remove from S2 scope |
| S2-R5 | Capex envelope for 3-5 new lines at Indy is not approvable | S2 is not executable as designed | Partial S2 (T1 only, ~5,300 t); Batavia retained for UFS |
