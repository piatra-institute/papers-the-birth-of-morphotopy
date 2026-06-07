"""Figures for the morphotopy analyses (publication quality, embedded in §8)."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import STRATA, stratigraphy, frustration


def plot_stratigraphy(path: str) -> None:
    s = stratigraphy()
    strata = sorted(STRATA, key=lambda t: t[1])
    names = [n for n, _, _ in strata]
    years = [y for _, y, _ in strata]
    fig, ax = plt.subplots(figsize=(9, 6))
    yi = list(range(len(strata)))
    ax.grid(axis="y", color="#eee", lw=0.8, zorder=0)
    ax.scatter(years, yi, s=55, color="#1b5e20", zorder=3)
    ax.axvline(1829, ls="--", lw=1, color="#b71c1c", zorder=2)
    ax.text(1829, len(strata) - 0.4, "1829", color="#b71c1c", fontsize=8, ha="right")
    ax.set_yticks(yi); ax.set_yticklabels(names, fontsize=8)
    ax.set_ylim(-0.6, len(strata) - 0.4)
    ax.set_xscale("symlog")
    ax.set_xlabel("year of emergence (symlog; BCE negative)")
    ax.set_title("The strata of geometric reason accelerate toward the present")

    # inset: cumulative count vs (linear) year, in the empty lower-right
    ins = ax.inset_axes([0.42, 0.12, 0.40, 0.34])
    xs = sorted(years)
    ins.step(xs + [2026], list(range(1, len(xs) + 1)) + [len(xs)], where="post",
             color="#1b5e20", lw=1.3)
    ins.axvline(1829, ls="--", lw=0.8, color="#b71c1c")
    ins.set_xlim(-2100, 2100)
    ins.set_title("cumulative strata vs year", fontsize=7)
    ins.tick_params(labelsize=6)
    ins.text(-1950, 14.5, f"mean gap {s['mean_gap_premodern_years']} yr → "
             f"{s['mean_gap_modern_years']} yr\n({s['acceleration_ratio']}× faster after 1829)",
             fontsize=6.5, va="top")
    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)


def _draw_spins(ax, pts, spins, edges, frustrated):
    """Draw a small spin graph: vertices with up/down arrows, bonds coloured by
    whether they are satisfied (antiferromagnet: neighbours disagree)."""
    for (i, j) in edges:
        col = "#b71c1c" if (i, j) in frustrated or (j, i) in frustrated else "#2e7d32"
        ax.plot([pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]], color=col, lw=2.2, zorder=1)
    for k, (x, y) in enumerate(pts):
        ax.scatter([x], [y], s=240, color="white", edgecolor="#333", zorder=2)
        ax.annotate("", xy=(x, y + (0.14 if spins[k] > 0 else -0.14)),
                    xytext=(x, y - (0.14 if spins[k] > 0 else -0.14)),
                    arrowprops=dict(arrowstyle="-|>", color="#333", lw=1.6), zorder=3)
    ax.set_aspect("equal"); ax.axis("off")


def plot_frustration(path: str) -> None:
    f = frustration()
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6),
                             gridspec_kw={"width_ratios": [1, 1, 1.5]})

    # (a) triangle, a ground state [+,+,-]: bond 0-1 is frustrated
    tri = [(0.0, 0.0), (1.0, 0.0), (0.5, 0.87)]
    _draw_spins(axes[0], tri, [1, 1, -1], [(0, 1), (1, 2), (0, 2)], {(0, 1)})
    axes[0].set_title("triangle: 1 of 3\nbonds frustrated", fontsize=9)

    # (b) square, checkerboard [+,-,+,-]: every bond satisfied
    sq = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]
    _draw_spins(axes[1], sq, [1, -1, 1, -1], [(0, 1), (1, 2), (2, 3), (0, 3)], set())
    axes[1].set_title("square: every\nbond satisfied", fontsize=9)

    # (c) triangular-lattice scaling
    ns = [f["triangle"]["n_spins"]] + [L["n_spins"] for L in f["triangular_lattices"]]
    frac = [f["triangle"]["frustrated_bond_fraction"]] + \
           [L["frustrated_bond_fraction"] for L in f["triangular_lattices"]]
    ent = [f["triangle"]["residual_entropy_per_spin"]] + \
          [L["residual_entropy_per_spin"] for L in f["triangular_lattices"]]
    ax = axes[2]
    ax.plot(ns, frac, "o-", color="#b71c1c", label="frustrated-bond fraction")
    ax.plot(ns, ent, "s-", color="#1565c0", label="residual entropy / spin")
    ax.axhline(f["wannier_entropy_per_spin"], ls="--", lw=1, color="#555")
    ax.text(ns[-1], f["wannier_entropy_per_spin"] + 0.015,
            f"Wannier {f['wannier_entropy_per_spin']}", fontsize=7, ha="right", color="#555")
    ax.axhline(1 / 3, ls=":", lw=0.8, color="#b71c1c", alpha=0.5)
    ax.set_xlabel("spins $N$ (triangular lattice)"); ax.set_ylim(0, 0.7)
    ax.set_title("the triangle's signatures persist", fontsize=9)
    ax.legend(fontsize=7, loc="upper right")

    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)
