"""Generate charts for the Week-1 deck.

Run from repo root:  python3 deliverable/build_charts.py
Outputs PNGs into deliverable/charts/ at 1600x900 (16:9 slide).
"""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# --- Style ---------------------------------------------------------------
mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
    "axes.titlesize": 20,
    "axes.titleweight": "bold",
    "axes.labelsize": 14,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "axes.grid": True,
    "grid.color": "#EEEEEE",
    "grid.linewidth": 0.6,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.dpi": 160,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

# Consistent palette
C_LERMA   = "#2F5A8A"   # deep blue — scale site
C_INDY    = "#2E8B57"   # green — strategic site
C_BATAVIA = "#C97B1F"   # amber — specialty site
C_S1      = "#2E8B57"   # S1 addressable = Indy
C_S2      = "#B03030"   # S2 capability build = red-ish (build, not transfer)
C_AT_INDY = "#4A90D9"   # already at Indy
C_TEXT    = "#222222"
C_MUTED   = "#888888"

FIG_W, FIG_H = 16, 9    # inches; gives 2560x1440 at dpi=160

CHARTS = Path(__file__).parent / "charts"
CHARTS.mkdir(exist_ok=True)

DATA = Path(__file__).parent.parent / "data"


# --- Helpers -------------------------------------------------------------
def save(fig, name):
    path = CHARTS / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    print(f"  wrote {path.relative_to(Path.cwd())}")


def thousands(x, pos):
    if x >= 1_000_000:
        return f"{x/1_000_000:.1f}M"
    if x >= 1_000:
        return f"{x/1_000:.0f}K"
    return f"{int(x)}"


# --- Data load -----------------------------------------------------------
def load_sku_master():
    rows = []
    with open(DATA / "sku_master.csv") as f:
        for r in csv.DictReader(f):
            r["total_cases_2025"] = float(r["total_cases_2025"] or 0)
            r["total_tonnes_2025"] = float(r["total_tonnes_2025"] or 0)
            r["country"] = (r["country"] or "").strip()
            rows.append(r)
    return rows


def load_monthly():
    rows = []
    with open(DATA / "monthly_volume.csv") as f:
        for r in csv.DictReader(f):
            r["cases"] = float(r["cases"] or 0)
            rows.append(r)
    return rows


# --- Chart 1: site × channel × volume (the one chart) -------------------
def chart_one_network(sku):
    sites = ["Lerma", "Indy", "Batavia"]
    channels = ["US Retail", "UFS", "CDA Retail", "UI"]
    # Build matrix site -> channel -> cases
    mat = {s: {c: 0.0 for c in channels} for s in sites}
    for r in sku:
        mat[r["sourcing_unit"]][r["country"]] += r["total_cases_2025"]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    x = np.arange(len(sites))
    bottoms = np.zeros(len(sites))
    colors = {
        "US Retail": "#4A90D9",
        "UFS": "#C97B1F",
        "CDA Retail": "#8A8AA0",
        "UI": "#D0D0D0",
    }
    for c in channels:
        vals = np.array([mat[s][c] for s in sites])
        bars = ax.bar(
            x, vals, bottom=bottoms, color=colors[c], label=c,
            edgecolor="white", linewidth=1.2, width=0.55
        )
        for i, v in enumerate(vals):
            if v > 40_000:
                ax.text(
                    x[i], bottoms[i] + v / 2,
                    f"{v/1_000:,.0f}K",
                    ha="center", va="center",
                    color="white", fontsize=13, fontweight="bold",
                )
        bottoms += vals

    # Site totals on top
    site_totals = {s: sum(mat[s].values()) for s in sites}
    for i, s in enumerate(sites):
        ax.text(
            x[i], site_totals[s] + 90_000,
            f"{site_totals[s]/1_000_000:.2f}M\n{site_totals[s]/5_246_057:.0%}",
            ha="center", va="bottom",
            color=C_TEXT, fontsize=15, fontweight="bold",
        )

    ax.set_xticks(x)
    ax.set_xticklabels([
        "LERMA  (MX)\n3 lines · 6 formats",
        "INDY\n1 line · 2 formats",
        "BATAVIA\n2 lines · 7 formats",
    ], fontsize=14)
    ax.set_ylabel("2025 cases")
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands))
    ax.set_ylim(0, 4_500_000)
    ax.set_title("NA Bouillon network · 2025 · 5.25M cases across 3 sites", pad=20)
    ax.legend(loc="upper right", frameon=False, fontsize=13)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "01_one_network")


# --- Chart 2: 100% / 38.5% / 0% multi-site share ------------------------
def chart_three_systems(sku):
    from collections import defaultdict
    by_prod = defaultdict(lambda: defaultdict(float))
    for r in sku:
        if r["country"] == "UI":
            continue
        by_prod[r["product_du"]][r["sourcing_unit"]] += r["total_cases_2025"]
    multi = {p for p, s in by_prod.items() if sum(1 for v in s.values() if v > 0) > 1}

    sites = ["Indy", "Lerma", "Batavia"]
    totals = {s: 0.0 for s in sites}
    multi_tot = {s: 0.0 for s in sites}
    for p, s_map in by_prod.items():
        for s, v in s_map.items():
            totals[s] += v
            if p in multi:
                multi_tot[s] += v

    shares = [multi_tot[s] / totals[s] if totals[s] else 0 for s in sites]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    x = np.arange(len(sites))
    bar_colors = [C_INDY, C_LERMA, C_BATAVIA]
    bars = ax.bar(x, shares, color=bar_colors, width=0.5, edgecolor="white", linewidth=1.5)

    for i, (s, v) in enumerate(zip(sites, shares)):
        ax.text(
            x[i], v + 0.02,
            f"{v:.0%}",
            ha="center", va="bottom",
            color=C_TEXT, fontsize=28, fontweight="bold",
        )

    captions = [
        "100%\nEvery Indy case is\nalso made at Lerma.\nZero unique SKUs.",
        "38.5%\nLerma's shared pool\n(1.48M cases) is the\nScenario-1 addressable set.",
        "0%\nEvery Batavia SKU\nis unique in the network.\nNo second source.",
    ]
    for i, cap in enumerate(captions):
        ax.text(
            x[i], -0.13, cap,
            ha="center", va="top",
            color=C_TEXT, fontsize=13, linespacing=1.4,
        )

    ax.set_xticks(x)
    ax.set_xticklabels(sites, fontsize=18, fontweight="bold")
    ax.tick_params(axis="x", pad=12)
    ax.set_ylim(0, 1.15)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_ylabel("Share of site volume in multi-site SKUs")
    ax.set_title(
        "Three disjoint manufacturing systems  ·  not three factories doing the same job",
        pad=20,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.margins(x=0.15)
    plt.subplots_adjust(bottom=0.22)
    save(fig, "02_three_systems")


# --- Chart 3: format × site heatmap -------------------------------------
def chart_format_complexity(sku):
    # Aggregate cases by (size_family, site)
    formats = [
        ("7.9 oz", "7.9oz"),
        ("3.5 oz", "3.5oz"),
        ("15.9 oz", "15.9oz"),
        ("2 lb", "2lb"),
        ("2.5 lb", "2.5lb"),
        ("2.6 oz", "2.6oz"),
        ("40.5 oz", "40.5oz"),
        ("4.4 lb (UFS)", "4.4lb"),
        ("7.9 lb (UFS)", "7.9lb"),
        ("25 lb (UFS)", "25 lb"),
        ("0-size / CDA", "0"),
    ]
    sites = ["Indy", "Lerma", "Batavia"]
    mat = np.zeros((len(formats), len(sites)))
    for r in sku:
        size = r["size"]
        site = r["sourcing_unit"]
        if site not in sites:
            continue
        for i, (label, key) in enumerate(formats):
            if size == key:
                mat[i][sites.index(site)] += r["total_cases_2025"]
                break

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))

    # Use log-ish scale visually by taking sqrt for color mapping; show real numbers in labels
    color_vals = np.sqrt(mat)
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        "network",
        ["#F6F6F6", "#D6E8F5", "#4A90D9", "#1F4E79"],
    )
    im = ax.imshow(color_vals, cmap=cmap, aspect="auto")

    for i in range(len(formats)):
        for j in range(len(sites)):
            v = mat[i][j]
            if v == 0:
                txt = "—"
                color = "#BBBBBB"
            else:
                if v >= 1_000_000:
                    txt = f"{v/1_000_000:.2f}M"
                elif v >= 10_000:
                    txt = f"{v/1_000:.0f}K"
                else:
                    txt = f"{v/1_000:.1f}K"
                color = "white" if color_vals[i][j] > color_vals.max() * 0.45 else C_TEXT
            ax.text(j, i, txt, ha="center", va="center",
                    color=color, fontsize=13, fontweight="bold")

    ax.set_xticks(range(len(sites)))
    ax.set_xticklabels(sites, fontsize=16, fontweight="bold")
    ax.set_yticks(range(len(formats)))
    ax.set_yticklabels([f[0] for f in formats], fontsize=13)
    ax.set_title(
        "Indy runs 2 of 11 formats  ·  every other format is somewhere else",
        pad=20,
    )
    ax.tick_params(top=False, bottom=True, labelbottom=True, left=True)
    ax.set_xticks(np.arange(-.5, len(sites), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(formats), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "03_format_complexity")


# --- Chart 4: S1 vs S2 divide (horizontal stacked bar) -----------------
def chart_s1_s2_divide():
    segments = [
        ("Already at Indy", 818_537, C_AT_INDY,
         "Indy's existing 2025 output\n1 line · 2 formats · Retail only"),
        ("S1 addressable", 1_479_552, C_S1,
         "Lerma volume in formats\nIndy already runs  ·  2 lb + 15.9 oz\nCapacity question, not capability"),
        ("S2 capability build", 2_940_525, C_S2,
         "Formats Indy has never run\n6 new formats · 4+ new techs · UFS from scratch\nCapex + R&D harmonization"),
        ("Residual", 7_443, "#CCCCCC",
         "CDA / UI trace / zero-volume rows"),
    ]
    total = sum(s[1] for s in segments)

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    left = 0
    y = 0.5
    for label, val, color, caption in segments:
        ax.barh(y, val, left=left, color=color, height=0.45,
                edgecolor="white", linewidth=2)
        pct = val / total
        if pct > 0.04:
            ax.text(left + val / 2, y,
                    f"{label}\n{val/1_000_000:.2f}M  ·  {pct:.0%}",
                    ha="center", va="center",
                    color="white", fontsize=16, fontweight="bold",
                    linespacing=1.4)
        left += val

    # Captions under the bar
    left = 0
    for label, val, color, caption in segments:
        if val / total > 0.04:
            ax.text(left + val / 2, -0.15, caption,
                    ha="center", va="top",
                    color=C_TEXT, fontsize=12, linespacing=1.4)
        left += val

    ax.set_xlim(0, total * 1.02)
    ax.set_ylim(-0.6, 1.1)
    ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands))
    ax.set_yticks([])
    ax.set_xlabel("2025 NA bouillon cases")
    ax.set_title(
        "The whole project in one bar  ·  S1 = capacity question  ·  S2 = capability build",
        pad=20,
    )
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.grid(axis="x", color="#EEEEEE", linewidth=0.6)
    save(fig, "04_s1_s2_divide")


# --- Chart 5: flagship SKU monthly profile ------------------------------
def chart_flagship_monthly(monthly):
    target = "KNR MEX BOUIL CHK 6 2 LB"
    prof = defaultdict(lambda: defaultdict(float))
    for r in monthly:
        if r.get("product_du") == target:
            prof[r["sourcing_unit"]][r["month"]] += r["cases"]

    months = sorted({m for s in prof.values() for m in s})
    month_labels = [m[-2:] for m in months]
    lerma = [prof["Lerma"].get(m, 0) for m in months]
    indy = [prof["Indy"].get(m, 0) for m in months]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.plot(month_labels, lerma, marker="o", markersize=10, linewidth=3,
            color=C_LERMA, label="Lerma")
    ax.plot(month_labels, indy, marker="o", markersize=10, linewidth=3,
            color=C_INDY, label="Indy")
    ax.fill_between(month_labels, 0, lerma, color=C_LERMA, alpha=0.08)
    ax.fill_between(month_labels, 0, indy, color=C_INDY, alpha=0.08)

    ax.annotate(
        "Indy ramp starts\nmid-year",
        xy=(4, max(indy[4], 1_000)), xytext=(3.2, 95_000),
        fontsize=13, color=C_INDY,
        arrowprops=dict(arrowstyle="->", color=C_INDY, lw=1.5),
    )
    ax.annotate(
        "Lerma still carries\n85% of the SKU",
        xy=(5, lerma[5]), xytext=(6.5, 150_000),
        fontsize=13, color=C_LERMA,
        arrowprops=dict(arrowstyle="->", color=C_LERMA, lw=1.5),
    )

    ax.set_xticks(range(len(month_labels)))
    ax.set_xticklabels([f"'25-{m}" for m in month_labels], fontsize=12)
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands))
    ax.set_ylabel("Cases / month")
    ax.set_title(
        "Flagship SKU in-flight  ·  KNR MEX BOUIL CHK 6 2 LB  ·  1.18M cases/yr  ·  15% moved",
        pad=20,
    )
    ax.legend(loc="upper left", frameon=False, fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "05_flagship_monthly")


# --- Main ----------------------------------------------------------------
def main():
    print("Loading data…")
    sku = load_sku_master()
    monthly = load_monthly()

    print("Building charts…")
    chart_one_network(sku)
    chart_three_systems(sku)
    chart_format_complexity(sku)
    chart_s1_s2_divide()
    chart_flagship_monthly(monthly)
    print("Done.")


if __name__ == "__main__":
    main()
