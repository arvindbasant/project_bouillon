"""Generate charts for the Week-1 deck  —  TONNES-FIRST edition.

Run from repo root:  python3 deliverable/build_charts.py
Outputs PNGs into deliverable/charts/ at 16:9 (1600×900 @ dpi=160).
"""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# --- Style -------------------------------------------------------------------
mpl.rcParams.update({
    "font.family":       "DejaVu Sans",
    "font.size":         14,
    "axes.titlesize":    20,
    "axes.titleweight":  "bold",
    "axes.labelsize":    14,
    "axes.edgecolor":    "#333333",
    "axes.linewidth":    0.8,
    "axes.grid":         True,
    "grid.color":        "#EEEEEE",
    "grid.linewidth":    0.6,
    "xtick.color":       "#333333",
    "ytick.color":       "#333333",
    "figure.facecolor":  "white",
    "axes.facecolor":    "white",
    "savefig.dpi":       160,
    "savefig.bbox":      "tight",
    "savefig.facecolor": "white",
})

C_LERMA   = "#2F5A8A"
C_INDY    = "#2E8B57"
C_BATAVIA = "#C97B1F"
C_S1      = "#2E8B57"
C_S2      = "#B03030"
C_AT_INDY = "#4A90D9"
C_TEXT    = "#222222"
C_MUTED   = "#888888"

FIG_W, FIG_H = 16, 9

CHARTS = Path(__file__).parent / "charts"
CHARTS.mkdir(exist_ok=True)
DATA   = Path(__file__).parent.parent / "data"


# --- Helpers -----------------------------------------------------------------
def save(fig, name):
    path = CHARTS / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    print(f"  wrote {path.relative_to(Path.cwd())}")


def fmt_t(t):
    """Format tonnes with K suffix."""
    if t >= 1_000:
        return f"{t/1_000:.1f}K t"
    return f"{t:.0f} t"


def thousands_t(x, pos):
    if x >= 1_000:
        return f"{x/1_000:.0f}K"
    return f"{int(x)}"


# --- Data load ---------------------------------------------------------------
def load_sku_master():
    rows = []
    with open(DATA / "sku_master.csv") as f:
        for r in csv.DictReader(f):
            r["total_cases_2025"]  = float(r["total_cases_2025"]  or 0)
            r["total_tonnes_2025"] = float(r["total_tonnes_2025"] or 0)
            r["country"]           = (r["country"] or "").strip()
            rows.append(r)
    return rows


def load_monthly():
    rows = []
    with open(DATA / "monthly_volume.csv") as f:
        for r in csv.DictReader(f):
            r["cases"]  = float(r["cases"]  or 0)
            r["tonnes"] = float(r["tonnes"] or 0)
            rows.append(r)
    return rows


# --- Chart 1: Site × channel — TONNES primary --------------------------------
def chart_one_network(sku):
    sites    = ["Lerma", "Indy", "Batavia"]
    channels = ["US Retail", "UFS", "CDA Retail", "UI"]
    mat_t = {s: {c: 0.0 for c in channels} for s in sites}
    mat_c = {s: {c: 0.0 for c in channels} for s in sites}
    for r in sku:
        su = r["sourcing_unit"]
        cn = r["country"]
        mat_t[su][cn] += r["total_tonnes_2025"]
        mat_c[su][cn] += r["total_cases_2025"]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    x = np.arange(len(sites))
    bottoms = np.zeros(len(sites))
    colors = {
        "US Retail":  "#4A90D9",
        "UFS":        "#C97B1F",
        "CDA Retail": "#8A8AA0",
        "UI":         "#D0D0D0",
    }
    for c in channels:
        vals = np.array([mat_t[s][c] for s in sites])
        ax.bar(x, vals, bottom=bottoms, color=colors[c], label=c,
               edgecolor="white", linewidth=1.2, width=0.55)
        for i, v in enumerate(vals):
            if v > 400:
                ax.text(x[i], bottoms[i] + v / 2,
                        fmt_t(v),
                        ha="center", va="center",
                        color="white", fontsize=12, fontweight="bold")
        bottoms += vals

    # Site totals + cases annotation on top
    net_t = sum(sum(mat_t[s].values()) for s in sites)
    for i, s in enumerate(sites):
        tot_t = sum(mat_t[s].values())
        tot_c = sum(mat_c[s].values())
        ax.text(x[i], tot_t + 300,
                f"{fmt_t(tot_t)}  ·  {tot_t/net_t:.0%}\n({tot_c/1_000:.0f}K cases)",
                ha="center", va="bottom",
                color=C_TEXT, fontsize=13, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels([
        "LERMA  (MX)\n3 lines · 6 formats",
        "INDY\n1 line · 2 formats",
        "BATAVIA\n2 lines · 7 formats",
    ], fontsize=14)
    ax.set_ylabel("2025 tonnes (directional)")
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands_t))
    ax.set_ylim(0, 35_000)
    ax.set_title("NA Bouillon network · 2025 · volume in tonnes", pad=20)
    ax.legend(loc="upper right", frameon=False, fontsize=13)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "01_one_network")


# --- Chart 2: Site density — Batavia punches above weight --------------------
def chart_site_density(sku):
    """Tonnes vs cases bubble — shows Batavia's weight concentration."""
    sites = ["Lerma", "Indy", "Batavia"]
    colors = [C_LERMA, C_INDY, C_BATAVIA]
    tot_c = {s: 0.0 for s in sites}
    tot_t = {s: 0.0 for s in sites}
    for r in sku:
        su = r["sourcing_unit"]
        if su in sites:
            tot_c[su] += r["total_cases_2025"]
            tot_t[su] += r["total_tonnes_2025"]

    net_c = sum(tot_c.values())
    net_t = sum(tot_t.values())

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    for i, s in enumerate(sites):
        ax.scatter(tot_c[s] / 1_000, tot_t[s], s=max(tot_t[s] * 0.8, 200),
                   color=colors[i], alpha=0.85, zorder=3, edgecolors="white", linewidth=2)
        density = tot_t[s] / tot_c[s] * 1_000  # kg/case
        ax.annotate(
            f"{s}\n"
            f"{tot_t[s]/1_000:.1f}K t  ({tot_t[s]/net_t:.0%} of tonnes)\n"
            f"{tot_c[s]/1_000:.0f}K cases ({tot_c[s]/net_c:.0%} of cases)\n"
            f"density: {density:.1f} kg/case",
            xy=(tot_c[s] / 1_000, tot_t[s]),
            xytext=(tot_c[s] / 1_000 + (-600 if s == "Batavia" else 80),
                    tot_t[s] + (500 if s != "Indy" else -1_500)),
            fontsize=14, color=colors[i],
            arrowprops=dict(arrowstyle="->", color=colors[i], lw=1.5),
        )

    # Reference line y = mean density × x
    mean_density = net_t / net_c  # tonnes/case
    xs = np.array([0, net_c / 1_000 * 1.05])
    ax.plot(xs, xs * mean_density * 1_000, "--", color="#AAAAAA", lw=1.5,
            label=f"Network avg density  ({mean_density*1_000:.1f} kg/case)")

    ax.set_xlabel("2025 cases (thousands)", fontsize=14)
    ax.set_ylabel("2025 tonnes", fontsize=14)
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands_t))
    ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: f"{x:.0f}K"))
    ax.set_title(
        "Batavia makes 11% of cases but 23% of tonnes  ·  UFS formats are heavy",
        pad=20,
    )
    ax.legend(loc="upper left", frameon=False, fontsize=13)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "02_site_density")


# --- Chart 3: Format × site heatmap — TONNES ---------------------------------
def chart_format_complexity(sku):
    def _chan(r):
        return (r["country"] or "").strip()

    format_rules = [
        ("7.9 oz",                 lambda r: r["size"] == "7.9oz"),
        ("3.5 oz",                 lambda r: r["size"] == "3.5oz"),
        ("15.9 oz",                lambda r: r["size"] == "15.9oz"),
        ("2 lb",                   lambda r: r["size"] == "2lb"),
        ("2.5 lb",                 lambda r: r["size"] == "2.5lb"),
        ("2.6 oz",                 lambda r: r["size"] == "2.6oz"),
        ("40.5 oz",                lambda r: r["size"] == "40.5oz"),
        ("4.4 lb (UFS)",           lambda r: r["size"] == "4.4lb"),
        ("7.9 lb (UFS)",           lambda r: r["size"] == "7.9lb"),
        ("25 lb bulk Caldo (UFS)", lambda r: r["size"] in ("25 lb", "0") and _chan(r) == "UFS"),
        ("160 g Zero Salt (CDA)",  lambda r: r["size"] == "0" and _chan(r) == "CDA Retail"),
    ]
    sites = ["Indy", "Lerma", "Batavia"]
    mat   = np.zeros((len(format_rules), len(sites)))
    for r in sku:
        su = r["sourcing_unit"]
        if su not in sites:
            continue
        for i, (_, rule) in enumerate(format_rules):
            if rule(r):
                mat[i][sites.index(su)] += r["total_tonnes_2025"]
                break

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    color_vals = np.sqrt(mat)
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        "network", ["#F6F6F6", "#D6E8F5", "#4A90D9", "#1F4E79"],
    )
    ax.imshow(color_vals, cmap=cmap, aspect="auto")

    for i in range(len(format_rules)):
        for j in range(len(sites)):
            v = mat[i][j]
            if v == 0:
                txt, color = "—", "#BBBBBB"
            else:
                txt   = fmt_t(v)
                color = "white" if color_vals[i][j] > color_vals.max() * 0.45 else C_TEXT
            ax.text(j, i, txt, ha="center", va="center",
                    color=color, fontsize=13, fontweight="bold")

    ax.set_xticks(range(len(sites)))
    ax.set_xticklabels(sites, fontsize=16, fontweight="bold")
    ax.set_yticks(range(len(format_rules)))
    ax.set_yticklabels([r[0] for r in format_rules], fontsize=13)
    ax.set_title(
        "Indy runs 2 of 11 formats  ·  values in tonnes  ·  every other format is somewhere else",
        pad=20,
    )
    ax.set_xticks(np.arange(-.5, len(sites), 1),    minor=True)
    ax.set_yticks(np.arange(-.5, len(format_rules), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "03_format_complexity")


# --- Chart 4: S1 vs S2 divide — TONNES computed from data -------------------
def chart_s1_s2_divide(sku):
    indy_t  = sum(r["total_tonnes_2025"] for r in sku if r["sourcing_unit"] == "Indy")

    s1_formats = {"2lb", "15.9oz"}
    s1_t = sum(
        r["total_tonnes_2025"] for r in sku
        if r["sourcing_unit"] == "Lerma" and r["size"] in s1_formats
    )

    s1_c = sum(
        r["total_cases_2025"] for r in sku
        if r["sourcing_unit"] == "Lerma" and r["size"] in s1_formats
    )
    indy_c = sum(r["total_cases_2025"] for r in sku if r["sourcing_unit"] == "Indy")

    # S2 = everything not at Indy and not in the S1 pool
    s2_t = sum(
        r["total_tonnes_2025"] for r in sku
        if r["sourcing_unit"] != "Indy"
        and not (r["sourcing_unit"] == "Lerma" and r["size"] in s1_formats)
    )
    s2_c = sum(
        r["total_cases_2025"] for r in sku
        if r["sourcing_unit"] != "Indy"
        and not (r["sourcing_unit"] == "Lerma" and r["size"] in s1_formats)
    )

    segments = [
        ("Already at Indy",    indy_t, C_AT_INDY,
         f"Indy's 2025 output\n{fmt_t(indy_t)}  ·  {indy_c/1_000:.0f}K cases"),
        ("S1 addressable",     s1_t,   C_S1,
         f"Lerma 2 lb + 15.9 oz\n{fmt_t(s1_t)}  ·  {s1_c/1_000:.0f}K cases\nCapacity question, not capability"),
        ("S2 capability build",s2_t,   C_S2,
         f"6 new formats · 4+ new techs · UFS from scratch\n{fmt_t(s2_t)}  ·  {s2_c/1_000:.0f}K cases\nCapex + R&D harmonization required"),
    ]
    total_t = sum(s[1] for s in segments)

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    left = 0
    y = 0.5
    for label, val, color, caption in segments:
        ax.barh(y, val, left=left, color=color, height=0.45,
                edgecolor="white", linewidth=2)
        pct = val / total_t
        ax.text(left + val / 2, y,
                f"{label}\n{fmt_t(val)}  ·  {pct:.0%}",
                ha="center", va="center",
                color="white", fontsize=15, fontweight="bold",
                linespacing=1.4)
        left += val

    left = 0
    for label, val, color, caption in segments:
        ax.text(left + val / 2, -0.18, caption,
                ha="center", va="top",
                color=C_TEXT, fontsize=12, linespacing=1.4)
        left += val

    ax.set_xlim(0, total_t * 1.02)
    ax.set_ylim(-0.7, 1.1)
    ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands_t))
    ax.set_xlabel("2025 tonnes")
    ax.set_yticks([])
    ax.set_title(
        "The whole project in one bar  ·  S1 = capacity question  ·  S2 = capability build",
        pad=20,
    )
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.grid(axis="x", color="#EEEEEE", linewidth=0.6)
    plt.subplots_adjust(bottom=0.22)
    save(fig, "04_s1_s2_divide")


# --- Chart 5: Flagship monthly — TONNES primary ------------------------------
def chart_flagship_monthly(monthly):
    target = "KNR MEX BOUIL CHK 6 2 LB"
    prof_t = defaultdict(lambda: defaultdict(float))
    prof_c = defaultdict(lambda: defaultdict(float))
    for r in monthly:
        if r.get("product_du") == target:
            su = r["sourcing_unit"]
            m  = r["month"]
            prof_t[su][m] += r["tonnes"]
            prof_c[su][m] += r["cases"]

    months      = sorted({m for s in prof_t.values() for m in s})
    month_lbls  = [m[-2:] for m in months]
    lerma_t     = [prof_t["Lerma"].get(m, 0) for m in months]
    indy_t      = [prof_t["Indy"].get(m, 0)  for m in months]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.plot(month_lbls, lerma_t, marker="o", markersize=10, linewidth=3,
            color=C_LERMA, label="Lerma")
    ax.plot(month_lbls, indy_t,  marker="o", markersize=10, linewidth=3,
            color=C_INDY,  label="Indy")
    ax.fill_between(month_lbls, 0, lerma_t, color=C_LERMA, alpha=0.08)
    ax.fill_between(month_lbls, 0, indy_t,  color=C_INDY,  alpha=0.08)

    # Annotations: find the Indy ramp start and Lerma peak
    indy_peak_idx = int(np.argmax(indy_t))
    lerma_peak_idx = int(np.argmax(lerma_t))
    ax.annotate(
        "Indy ramp\nstarts mid-year",
        xy=(indy_peak_idx, indy_t[indy_peak_idx]),
        xytext=(indy_peak_idx - 1.5, max(indy_t) * 0.85),
        fontsize=13, color=C_INDY,
        arrowprops=dict(arrowstyle="->", color=C_INDY, lw=1.5),
    )
    ax.annotate(
        "Lerma still carries\n85% of tonnage",
        xy=(lerma_peak_idx, lerma_t[lerma_peak_idx]),
        xytext=(lerma_peak_idx + 0.5, lerma_t[lerma_peak_idx] * 0.85),
        fontsize=13, color=C_LERMA,
        arrowprops=dict(arrowstyle="->", color=C_LERMA, lw=1.5),
    )

    ax.set_xticks(range(len(month_lbls)))
    ax.set_xticklabels([f"'25-{m}" for m in month_lbls], fontsize=12)
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(thousands_t))
    ax.set_ylabel("Tonnes / month")
    tot_t = sum(lerma_t) + sum(indy_t)
    ax.set_title(
        f"Flagship SKU in-flight  ·  KNR MEX BOUIL CHK 6 2 LB  ·  {fmt_t(tot_t)}/yr  ·  Lerma→Indy transfer live",
        pad=20,
    )
    ax.legend(loc="upper left", frameon=False, fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "05_flagship_monthly")


# --- Main --------------------------------------------------------------------
def main():
    print("Loading data…")
    sku     = load_sku_master()
    monthly = load_monthly()

    print("Building charts…")
    chart_one_network(sku)
    chart_site_density(sku)
    chart_format_complexity(sku)
    chart_s1_s2_divide(sku)
    chart_flagship_monthly(monthly)
    print("Done.")


if __name__ == "__main__":
    main()
