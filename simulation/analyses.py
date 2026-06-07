"""Two computational analyses for *The Birth of Morphotopy*.

Neither measures history or mind. Each turns one structural claim of the
genealogy into something reproducible.

  1. stratigraphy — the strata of geometric reason dated by a representative
                    work and ordered by emergence; the paper's claim that the
                    abstraction *accelerates* (millennia between the early
                    strata, decades between the late ones) is computed, not
                    asserted.
  2. frustration  — the one technical invariant the final stratum carries:
                    geometric frustration. On a triangle, antiferromagnetic
                    bonds cannot all be satisfied at once; the global minimum
                    sits strictly above the sum of the local minima
                    (min sum E > sum of min E), the ground state is
                    macroscopically degenerate, and a residual fraction of bonds
                    stays frustrated. On a square (bipartite) it does not. This
                    is the fact the morphotopy stratum generalizes; the paper
                    does not extend it to psychology.
"""
from __future__ import annotations

import itertools
import math

# ----------------------------------------------------------------------------
# 1. Stratigraphy of geometric reason. Year = a representative work (negative =
# BCE). Dates are onsets, not precise events; the early strata are deliberately
# coarse (the earth-measure stratum has no single date).
# ----------------------------------------------------------------------------
STRATA = [
    ("earth-measure (geodesy)", -1800, "Egyptian/Babylonian land survey"),
    ("Euclidean ideality", -300, "Euclid, Elements"),
    ("coordinate capture", 1637, "Descartes, La Géométrie"),
    ("projective space", 1639, "Desargues"),
    ("non-Euclidean rupture", 1829, "Lobachevsky"),
    ("Riemannian internalization", 1854, "Riemann, Habilitationsvortrag"),
    ("transformation regime", 1872, "Klein, Erlangen Program"),
    ("topological continuity", 1895, "Poincaré, Analysis Situs"),
    ("phase-space / dynamics", 1902, "Gibbs"),
    ("space without points (topos)", 1963, "Grothendieck"),
    ("biological morphospace", 1966, "Raup"),
    ("information geometry", 1985, "Amari"),
    ("conceptual spaces", 2000, "Gärdenfors"),
    ("semantic embeddings", 2013, "Mikolov et al."),
    ("problem-space (basal cognition)", 2022, "Levin, TAME"),
    ("morphotopy", 2026, "this paper"),
]


def stratigraphy() -> dict:
    dates = sorted(y for _, y, _ in STRATA)
    n = len(dates)
    span = dates[-1] - dates[0]
    gaps = [(dates[i + 1] - dates[i]) for i in range(n - 1)]
    max_gap = max(gaps)
    gi = gaps.index(max_gap)
    modern_onset = 1829  # the non-Euclidean rupture
    pre_modern_span = modern_onset - dates[0]
    modern_window = dates[-1] - modern_onset
    in_modern = sum(1 for y in dates if y >= modern_onset)

    # acceleration, made quantitative: the year by which half the strata exist,
    # and the mean interval between consecutive strata within each era (both
    # endpoints on the same side of the 1829 threshold; the one transition gap
    # 1639->1829 is excluded from both so each mean is within-era).
    median_year = dates[n // 2 - 1]                       # 8th of 16: half exist by here
    pre = [d for d in dates if d < modern_onset]
    mod = [d for d in dates if d >= modern_onset]
    pre_gaps = [pre[i + 1] - pre[i] for i in range(len(pre) - 1)]
    mod_gaps = [mod[i + 1] - mod[i] for i in range(len(mod) - 1)]
    mean_pre = sum(pre_gaps) / len(pre_gaps)
    mean_mod = sum(mod_gaps) / len(mod_gaps)

    return {
        "n_strata": n,
        "order_by_date": [s for s, _, _ in sorted(STRATA, key=lambda s: s[1])],
        "span_years": span,
        "largest_gap_years": max_gap,
        "largest_gap_between": [dates[gi], dates[gi + 1]],
        "pre_modern_span_years": pre_modern_span,         # earth-measure -> 1829
        "modern_window_years": modern_window,             # 1829 -> morphotopy
        "strata_in_modern_window": in_modern,
        "modern_window_fraction_of_span": round(modern_window / span, 4),
        "median_emergence_year": median_year,             # half the strata exist by here
        "mean_gap_premodern_years": round(mean_pre),      # within the pre-1829 era
        "mean_gap_modern_years": round(mean_mod),         # within the post-1829 era
        "acceleration_ratio": round(mean_pre / mean_mod),  # how much faster, modern vs pre
        "strata": [{"stratum": s, "year": y, "work": w} for s, y, w in STRATA],
    }


# ----------------------------------------------------------------------------
# 2. Geometric frustration by exact enumeration of antiferromagnetic Ising
# plaquettes. Spins s_i in {-1,+1}; bond energy = +J s_i s_j (so an
# antiferromagnet, J>0, wants s_i s_j = -1, energy -J per satisfied bond).
# ----------------------------------------------------------------------------
def _plaquette(edges: list[tuple[int, int]], n: int, J: float = 1.0) -> dict:
    energies = {}
    for s in itertools.product((-1, 1), repeat=n):
        e = J * sum(s[i] * s[j] for i, j in edges)
        energies[s] = e
    e_ground = min(energies.values())
    ground = [s for s, e in energies.items() if math.isclose(e, e_ground)]
    degeneracy = len(ground)
    # frustrated bonds in a ground state: bonds with s_i s_j = +1 (unsatisfied
    # for an antiferromagnet). Count in the first ground state (all equivalent).
    g0 = ground[0]
    frustrated = sum(1 for i, j in edges if g0[i] * g0[j] > 0)
    n_bonds = len(edges)
    # sum of independent local minima: each bond alone can reach -J
    sum_local_min = -J * n_bonds
    return {
        "n_spins": n,
        "n_bonds": n_bonds,
        "ground_energy": e_ground,
        "sum_of_local_minima": sum_local_min,
        "global_minus_local": round(e_ground - sum_local_min, 6),   # >0 iff frustrated
        "is_frustrated": e_ground > sum_local_min + 1e-9,
        "ground_degeneracy": degeneracy,
        "frustrated_bond_fraction": round(frustrated / n_bonds, 4),
        "residual_entropy_per_spin": round(math.log(degeneracy) / n, 4),
    }


# ----------------------------------------------------------------------------
# Triangular-lattice antiferromagnet on an L1 x L2 torus. Each site has six
# neighbours; taking the three forward offsets {(1,0),(0,1),(1,-1)} gives 3N
# distinct bonds. Exact ground-state enumeration: in one pass over the 2^N spin
# configurations, track the minimum energy, its degeneracy, and one ground
# configuration (to read off the frustrated-bond fraction). The single triangle
# is the L1=L2 -> small limit; as N grows the per-spin ground-state entropy
# climbs toward Wannier's exact thermodynamic value S/N ~ 0.3231.
# ----------------------------------------------------------------------------
WANNIER_ENTROPY_PER_SPIN = 0.3231  # Wannier (1950, corr. 1973), triangular Ising AF


def _triangular_edges(L1: int, L2: int) -> tuple[list[tuple[int, int]], int]:
    def idx(i, j):
        return (i % L1) * L2 + (j % L2)
    edges = []
    for i in range(L1):
        for j in range(L2):
            a = idx(i, j)
            for di, dj in ((1, 0), (0, 1), (1, -1)):
                edges.append((a, idx(i + di, j + dj)))
    return edges, L1 * L2


def _triangular_ground(L1: int, L2: int, J: float = 1.0) -> dict:
    edges, n = _triangular_edges(L1, L2)
    n_bonds = len(edges)
    e_min, deg, g0 = None, 0, None
    for bits in range(1 << n):
        s = [1 if (bits >> k) & 1 else -1 for k in range(n)]
        e = J * sum(s[i] * s[j] for i, j in edges)
        if e_min is None or e < e_min:
            e_min, deg, g0 = e, 1, s
        elif e == e_min:
            deg += 1
    frustrated = sum(1 for i, j in edges if g0[i] * g0[j] > 0)
    return {
        "L": [L1, L2], "n_spins": n, "n_bonds": n_bonds,
        "ground_energy_per_bond": round(e_min / n_bonds, 4),
        "ground_degeneracy": deg,
        "frustrated_bond_fraction": round(frustrated / n_bonds, 4),
        "residual_entropy_per_spin": round(math.log(deg) / n, 4),
    }


def frustration() -> dict:
    triangle = _plaquette([(0, 1), (1, 2), (0, 2)], 3)   # 3-cycle (odd) -> frustrated
    square = _plaquette([(0, 1), (1, 2), (2, 3), (0, 3)], 4)  # 4-cycle (bipartite) -> not
    # scale the triangle up: periodic triangular-lattice antiferromagnet
    lattices = [_triangular_ground(L1, L2) for L1, L2 in ((3, 3), (3, 4), (4, 4))]
    return {
        "coupling_J": 1.0,   # energy unit; bond energy = +J s_i s_j
        "triangle": triangle,
        "square": square,
        "triangular_lattices": lattices,
        "wannier_entropy_per_spin": WANNIER_ENTROPY_PER_SPIN,
        # headline contrasts, pulled to the top level
        "triangle_global_minus_local": triangle["global_minus_local"],
        "square_global_minus_local": square["global_minus_local"],
        "triangle_frustrated_fraction": triangle["frustrated_bond_fraction"],
        "triangle_degeneracy": triangle["ground_degeneracy"],
        "square_degeneracy": square["ground_degeneracy"],
        "degeneracy_ratio": round(triangle["ground_degeneracy"] / square["ground_degeneracy"], 4),
        "lattice_frustrated_fraction": lattices[-1]["frustrated_bond_fraction"],
        "lattice_entropy_per_spin": lattices[-1]["residual_entropy_per_spin"],
    }


def run() -> dict:
    return {"stratigraphy": stratigraphy(), "frustration": frustration()}
