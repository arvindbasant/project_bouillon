# Format / Line Complexity & the Indy Capability Gap

**Week:** 1 · **Day:** 2 (Tue 2026-04-14)
**Purpose:** Answer the single question that governs every Indy scenario downstream —
**"What can Indy make today, and what can't it?"**

This is the page that wins Wednesday's call.

---

## 1. Headline

> **Indy today is a single-line, two-format factory.** 100% of its 819K cases run on line "15" in just **two sizes (2 lb Large Granulated + 15.9 oz Small Granulated)**. Every other format in the NA network — and there are **10 of them** — runs somewhere else.
>
> As a result:
> - **Scenario 1 (Maximize Indy)** can only absorb volume where Lerma runs **formats Indy already makes.** That headroom is **~1.5M additional cases**, almost entirely from Lerma's 2 lb and 15.9 oz production — provided line "15" has capacity (to be confirmed) or a second line is added.
> - **Scenario 2 (Full consolidation)** requires Indy to stand up **6 new formats and at least 4 new technology types** it has never run before. This is a **capability build, not a line transfer.** The UFS footprint (Batavia's 530K UFS cases + Lerma's 372K UFS cases) is the hardest part of the build.

Everything else in this file is the evidence for those two statements.

---

## 2. Site × format (cases, 2025)

| Format | Indy | Lerma | Batavia | Total | Notes |
|---|---:|---:|---:|---:|---|
| **2 lb** | **509,980** | **1,195,057** | 7,440 | 1,712,477 | Only format Indy and Lerma run at scale together. **Prime transfer format.** |
| **15.9 oz** | **308,557** | **284,495** | — | 593,052 | Second Indy-Lerma overlap. Roughly balanced. |
| 7.9 oz | — | 1,789,350 | — | 1,789,350 | **Biggest single format in the network. Only Lerma runs it.** Indy would need to build this capability. |
| 7.9 lb (UFS) | — | 371,525 | — | 371,525 | Lerma's sole UFS format, Mateer 2 dedicated. |
| 3.5 oz | — | 183,878 | — | 183,878 | Lerma-only. |
| 40.5 oz | — | 18,457 | — | 18,457 | Lerma runs it; Batavia listed with zero volume (data-quality flag). |
| **4.4 lb (UFS)** | — | — | **456,612** | 456,612 | **Largest Batavia format.** Caldo / UFS. Indy can't touch it today. |
| "0" size Caldo (UFS/CDA) | — | — | 82,929 | 82,929 | Batavia-only technology. |
| 2.6 oz | — | — | 25,161 | 25,161 | Batavia-only. Zero Salt variants. |
| 2.5 lb | — | — | 10,298 | 10,298 | Batavia-only. |
| 25 lb (UFS) | — | — | 2,315 | 2,315 | Batavia-only. |

**Read:** Indy runs 2 formats. Lerma runs 6. Batavia runs 7. The **union** across the network is 11 distinct pack formats. Indy participates in **18%** of the format taxonomy and **31%** of the case volume.

---

## 3. Site × technology (cases, 2025)

| Technology | Indy | Lerma | Batavia | Note |
|---|---:|---:|---:|---|
| **Large Granulated** | 509,980 | 1,213,514 | 16,486 | Indy + Lerma overlap, Mateer 3 on the Lerma side |
| **Small Granulated** | 308,557 | 2,257,724 | — | Indy + Lerma overlap, Mateer 1 on the Lerma side — but **different pack sizes** (Indy = 15.9 oz, Lerma = 7.9 oz / 3.5 oz) |
| FS Large Granulated (7.9 lb UFS) | — | 371,525 | — | Lerma Mateer 2 specialty — UFS |
| Knorr Caldo 4.4 | — | — | 456,600 | **Batavia-only technology.** |
| Knorr Caldo (other) | — | — | 71,384 | Batavia-only. |
| Knorr Caldo 25 lb | — | — | 2,327 | Batavia-only. |
| Large Granulated — MixMod | — | — | 1,251 | Batavia-only variant. |
| Small Granulated — Natural | — | — | 36,706 | Batavia-only variant. |

**Read:** Indy runs **2 technology categories**. Lerma runs **3**. Batavia runs **6** (most of them unique). Moving Batavia's 585K cases to Indy means **standing up at least 4 new technology types at Indy**, not just running existing processes harder.

---

## 4. Site × line

| Site | Lines | Cases |
|---|---|---:|
| **Indy** | `15` *(one line, carries everything)* | 818,537 |
| **Lerma** | `Mateer 1` | 2,257,724 |
| **Lerma** | `Mateer 3` | 1,213,514 |
| **Lerma** | `Mateer 2` | 371,525 |
| **Batavia** | `13` | 539,529 |
| **Batavia** | `0` | 45,226 |

- Indy = **1 physical line**.
- Lerma = **3 physical lines**, clearly specialized: Mateer 1 → Small Granulated 7.9 oz/3.5 oz, Mateer 2 → UFS 7.9 lb, Mateer 3 → Large Granulated 2 lb/15.9 oz.
- Batavia = **2 physical lines**, line 13 carrying nearly all the volume.

**Implication:** The total installed line count in the NA bouillon network is **6** (1 + 3 + 2). Consolidation at Indy means either **adding physical lines at Indy** to cover what Mateer 1/2 + Batavia 13 do today, or **retiring technology/formats**. There is no third option.

---

## 5. The Indy Capability Gap *(the key slide)*

### 5a. What Indy can absorb **without new capability**

Formats Indy already runs and Lerma also runs:

| Format | At Lerma 2025 | Capability risk at Indy |
|---|---:|---|
| 2 lb Large Granulated | **1,195,057** | Same line type (Mateer 3 @ Lerma ↔ line 15 @ Indy). Proven — already mid-transfer in 2025. |
| 15.9 oz Small Granulated | **284,495** | Line 15 already runs this pack. Proven — already mid-transfer in 2025. |
| **Total addressable without new capability** | **~1,479,552 cases** | Subject to Indy line-15 capacity headroom (unknown — open data request) |

**But:** ~350K of that Lerma volume is already shifting toward Indy in H2 2025 per the in-flight transfer pattern. **Net new** Scenario-1 upside is smaller than the gross number. Week 2 will separate the two precisely.

### 5b. What Indy would have to **build** for full consolidation

Formats NOT at Indy today that would need to land there under Scenario 2:

| Format | Currently at | 2025 cases | Capability lift required |
|---|---|---:|---|
| 7.9 oz Small Granulated | Lerma Mateer 1 | **1,789,350** | New pack size (Indy runs 15.9 oz, not 7.9 oz) — sizing + packaging line build. Biggest single volume in the network. |
| 4.4 lb Caldo (UFS) | Batavia line 13 | **456,612** | Entirely new technology (Knorr Caldo), new line, new UFS channel at Indy. |
| 7.9 lb Large Granulated (UFS) | Lerma Mateer 2 | **371,525** | Indy has no UFS footprint. New line, new UFS logistics. |
| 3.5 oz Small Granulated | Lerma Mateer 1 | **183,878** | New pack size. |
| "0" size Caldo (UFS/CDA) | Batavia | **82,929** | New technology (Caldo). Only source of CDA Retail. |
| 2.6 oz Zero Salt | Batavia | **25,161** | New pack size + new variant line. |
| 40.5 oz (UFS) | Lerma | **18,457** | New UFS pack size. |
| 2.5 lb | Batavia | **10,298** | New pack size. |
| 25 lb UFS Caldo | Batavia | **2,315** | New pack size, new technology. |
| **Total requiring new capability at Indy** | | **~2,940,525** cases | |

**Read:** roughly **56% of all NA bouillon cases** sit in formats or technologies Indy does **not** currently run. Scenario 2 is therefore a capability-build story, not a volume-transfer story.

### 5c. The Scenario-1 vs Scenario-2 divide, in one number

| | Cases 2025 | % of NA total | What it requires |
|---|---:|---:|---|
| Format Indy already runs (S1 addressable) | **~1.48M** (Lerma) | 28% | Line 15 capacity headroom + maybe a second line |
| Format Indy does NOT run (S2 additional) | **~2.94M** | 56% | New formats, new technologies, new UFS footprint, capex |
| Already at Indy | 0.82M | 16% | — |

That's the whole story of this project in three rows.

---

## 6. What this tells us about the two future-state scenarios *(preview for Week 2)*

- **Scenario 1 (Maximize Indy)** is primarily a question of **line-15 capacity and a possible second line at Indy**, scoped against ~1.5M cases of Lerma 2 lb + 15.9 oz production — minus whatever has already moved in H2 2025. This scenario is real, near-term, low-capability-risk, and probably cheap relative to Scenario 2.
- **Scenario 2 (Full consolidation)** is fundamentally a **capability-build program**: 6 new formats, 4+ new technologies, new UFS capability at Indy, and probable capex. The UFS build (Batavia's 530K + Lerma's 372K = ~900K cases) is the hardest and most capital-intensive part. This scenario has a very different risk profile than Scenario 1 — it should not be framed as "more of the same."
- **Harmonization dependency is highest for Scenario 2.** The R&D harmonization roadmap directly determines whether some of Batavia's specialty tech (Caldo variants, MixMod, Natural) can be simplified before Indy has to build it. This is why the brief explicitly says "leverage the R&D harmonization track."

---

## 7. Assumptions & caveats

1. "Format" is approximated by the `Size` column. Two rows at the same pack size but different tech (e.g. a 2 lb Large Granulated at Indy vs 2 lb Large Granulated MixMod at Batavia) are treated as the **same format** for pack-line purposes. Week 2 should revalidate with a Size × Tech view.
2. Line capacity numbers are **not in the dataset**. "Headroom", "utilization", and "second line at Indy" are framed as open questions, not asserted.
3. The 2 lb Batavia row (7,440 cases) is treated as a residual, not Batavia running the format at scale.
4. The "0" size rows at Batavia are Knorr Caldo variants; "size 0" is a source-data encoding, not a zero-weight pack.
5. All multi-site SKU splits are from the in-flight transfer pattern noted in `logs/data_quality_memo.md`.
