"""
verify_csv.py
Cross-check the new flat CSV ("RT and UFS Bouillon 4.13.csv") against the
derived CSVs (sku_master.csv, monthly_volume.csv) built from the xlsx.

Run from the project root:
    python3 data/verify_csv.py
"""

import csv, sys
from pathlib import Path

ROOT       = Path(__file__).parent.parent
NEW_CSV    = ROOT / "RT and UFS Bouillon 4.13.csv"
SKU_MASTER = ROOT / "data" / "sku_master.csv"
MONTHLY    = ROOT / "data" / "monthly_volume.csv"

MONTH_LABELS = [
    "Jan-25","Feb-25","Mar-25","Apr-25","May-25","Jun-25",
    "Jul-25","Aug-25","Sep-25","Oct-25","Nov-25","Dec-25",
]
MONTH_KEYS = [
    "2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
    "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12",
]

def to_float(s):
    """Parse CSV cell: strip whitespace/quotes, handle (123) negatives and '-' zeros."""
    s = s.strip().strip('"').replace(",", "").replace(" ", "")
    if s in ("", "-"):
        return 0.0
    if s.startswith("(") and s.endswith(")"):
        return -float(s[1:-1])
    return float(s)

errors   = []
warnings = []

# ── 1. Parse the new CSV with csv.reader ─────────────────────────────────────
with open(NEW_CSV, newline="", encoding="utf-8") as f:
    all_rows = list(csv.reader(f))

# Row 0 = "Cases" label, Row 1 = monthly totals, Row 2 = header, Row 3+ = data
hdr      = [h.strip() for h in all_rows[2]]
data_raw = all_rows[3:]

def col(name): return hdr.index(name)

C_UNIT  = col("Sourcing Unit")
C_DU    = col("DU")
C_PROD  = col("Product DU")
C_CTRY  = col("Sales Org OpCo")
C_TPCS  = col("Tonnes/CS")
C_TOTAL = col("Total 25")
m_cols  = {MONTH_KEYS[i]: col(MONTH_LABELS[i]) for i in range(12)}

new_rows = []
for parts in data_raw:
    if not any(p.strip() for p in parts):
        continue
    monthly = {mk: to_float(parts[ci]) for mk, ci in m_cols.items()}
    new_rows.append({
        "du":      parts[C_DU].strip(),
        "unit":    parts[C_UNIT].strip(),
        "prod":    parts[C_PROD].strip(),
        "country": parts[C_CTRY].strip(),
        "tpcs":    to_float(parts[C_TPCS]),
        "total":   to_float(parts[C_TOTAL]),
        "monthly": monthly,
    })

print(f"New CSV : {len(new_rows)} data rows parsed")

# ── 2. Load derived CSVs ──────────────────────────────────────────────────────
sku_rows = {}
with open(SKU_MASTER, newline="") as f:
    for r in csv.DictReader(f):
        key = (r["du"], r["sourcing_unit"], r["product_du"], r["sales_org_opco"].strip())
        sku_rows[key] = r

monthly_rows = {}
with open(MONTHLY, newline="") as f:
    for r in csv.DictReader(f):
        key = (r["du"], r["sourcing_unit"], r["product_du"], r["country"].strip())
        monthly_rows.setdefault(key, {})[r["month"]] = float(r["cases"])

print(f"sku_master     : {len(sku_rows)} rows")
print(f"monthly_volume : {len(monthly_rows)} unique SKU×channel keys")

# ── 3. Grand-total check ──────────────────────────────────────────────────────
new_grand     = sum(r["total"] for r in new_rows)
sku_grand     = sum(float(r["total_cases_2025"]) for r in sku_rows.values())
monthly_grand = sum(v for d in monthly_rows.values() for v in d.values())

print(f"\nGrand-total cases:")
print(f"  New CSV      : {new_grand:>12,.1f}")
print(f"  sku_master   : {sku_grand:>12,.1f}")
print(f"  monthly_vol  : {monthly_grand:>12,.1f}")

TOL = 2.0
if abs(new_grand - sku_grand) > TOL:
    errors.append(f"Grand total mismatch: new CSV {new_grand:.1f} vs sku_master {sku_grand:.1f}")
else:
    print("  ✓ Grand totals match within tolerance")

# ── 4. Row-level total check ──────────────────────────────────────────────────
unmatched = 0
for row in new_rows:
    key = (row["du"], row["unit"], row["prod"], row["country"])
    if key not in sku_rows:
        unmatched += 1
        warnings.append(f"No sku_master match DU={row['du']} prod='{row['prod'][:40]}'")
        continue
    sm_total = float(sku_rows[key]["total_cases_2025"])
    if abs(row["total"] - sm_total) > TOL:
        errors.append(
            f"Total mismatch DU={row['du']} prod='{row['prod'][:35]}': "
            f"new={row['total']:.1f} sku_master={sm_total:.1f}"
        )

print(f"\nRow-level check: {unmatched} unmatched, "
      f"{len(errors)} total errors so far")

# ── 5. Monthly spot-check (flagship Chicken 15.9oz at Indy) ──────────────────
TARGET_DU   = "64784933"
TARGET_PROD = "KNR MEX BOUIL CHK 12/15.9 OZ"
flagship = next((r for r in new_rows
                 if r["du"] == TARGET_DU and r["unit"] == "Indy"), None)
if flagship:
    flag_key    = (TARGET_DU, "Indy", TARGET_PROD, "US Retail")
    flag_monthly = monthly_rows.get(flag_key, {})
    print(f"\nFlagship monthly spot-check (DU {TARGET_DU} Indy):")
    all_ok = True
    for mk in MONTH_KEYS:
        nv = flagship["monthly"].get(mk, 0.0)
        mv = flag_monthly.get(mk, 0.0)
        ok = abs(nv - mv) <= TOL
        status = "✓" if ok else "✗"
        print(f"  {mk}: new={nv:>8.0f}  monthly_vol={mv:>8.0f}  {status}")
        if not ok:
            all_ok = False
            errors.append(f"Flagship {mk}: new={nv} vs monthly_vol={mv}")
    if all_ok:
        print("  ✓ All 12 monthly cells match")

# ── 6. Monthly sum cross-check ────────────────────────────────────────────────
new_monthly_total = sum(
    v for r in new_rows for v in r["monthly"].values()
)
print(f"\nNew CSV sum of all monthly cells: {new_monthly_total:,.1f}")
print(f"New CSV Total 25 column sum     : {new_grand:,.1f}")
if abs(new_monthly_total - new_grand) > 5:
    warnings.append(
        f"Monthly cell sum {new_monthly_total:.1f} ≠ Total 25 sum {new_grand:.1f}"
    )
else:
    print("  ✓ Monthly cells sum to Total 25")

# ── 7. Summary ────────────────────────────────────────────────────────────────
print("\n" + "="*65)
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors[:20]: print(f"  ✗ {e}")
    if len(errors) > 20: print(f"  ... and {len(errors)-20} more")
else:
    print("✓ NO ERRORS — new CSV is fully consistent with derived data")

if warnings:
    print(f"\nWARNINGS ({len(warnings)}):")
    for w in warnings[:5]: print(f"  ⚠ {w}")

sys.exit(1 if errors else 0)
