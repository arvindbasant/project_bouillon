# Assumption Log

Assumptions made during Week 1 analysis. Each one must be either confirmed or replaced by fact before the Friday Week-1 deliverable.

| # | Assumption | Basis | Impact if wrong | Status |
|---:|---|---|---|---|
| A1 | `Brand` blank for all 57 rows = all Knorr (intentional blank, not missing data) | Systematic blank pattern, not random | Low — does not affect aggregation | Raised on call (Q8) |
| A2 | `Pouches/CS` blank is not needed; `Tonnes/CS` is authoritative for tonnage math | Systematic blank pattern | Low — tonnage still directional | Raised on call (Q9) |
| A3 | 3 negative monthly cells at Indy are legitimate returns / corrections, not data errors | Small magnitude, single-month, all at Indy during ramp-up | Low — immaterial to aggregates | Raised on call (Q11) |
| A4 | Row 14 zero-volume Batavia 40.5oz SKU is an active DU with no 2025 production | Listed in master, zero monthly | Low — <1% impact | Raised on call (Q10) |
| A5 | Multi-site SKUs showing H1-Lerma / H2-Indy pattern represent in-flight transfers | Heuristic from monthly profile | **High** — if these are normal dual-sourcing, not transfers, Scope B framing changes | Raised on call (Q12) |
| A6 | `Tonnes/CS × cases` = site tonnage, directional only | Spreadsheet-level conversion; not mass-balance reconciled | Low — used only for directional site-level tonnage | Will note in Week-1 pack |
| A7 | "Format" is approximated by `Size` column; size × tech combinations are treated as single format for line-capacity purposes | Simplification for Week 1 | Medium — Week 2 should revalidate Size × Tech | Will note in Week-1 pack |
| A8 | `Sourcing Unit` = site of physical production (not sales org / planning DU) | Column name + cross-reference to `Sales Org OpCo` | Medium — if this is planning DU not physical site, all network analysis needs redoing | To confirm with sponsor if any doubt |
| A9 | NA scope excludes CDA Retail and UI for scenario purposes (they are 0.2% combined) | De minimis; brief focuses on US Retail + UFS | Low | Raised on call (Q16) |
| A10 | Cross-border logistics cost and customs exposure is real but not quantifiable in Week 1 | Not in workbook | Medium — affects Lerma cost framing | Flag in business baseline |
| A11 | Indy line "15" has capacity headroom to absorb some additional volume | Evidence: Lerma → Indy transfers are already happening in 2025 | **High** — if line 15 is already maxed, Scenario 1 needs a second-line decision | Raised on call (Q3) |
| A12 | Indy's 0 UFS cases in 2025 means Indy has no UFS manufacturing capability today, not just no UFS bookings | Strongest reading of the data | **High** — if Indy has latent UFS capability, Scenario 2 is easier | Raised on call (Q3–Q5) |
