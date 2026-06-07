# Computational layer — *The Birth of Morphotopy*

Two exact analyses behind §8. Neither measures history or mind; each turns one
structural claim of the genealogy into something reproducible.

```
cd simulation
uv run run_all.py        # writes output/results.json + output/figures/*.png
```

- **`stratigraphy()`** — the sixteen strata of geometric reason dated by a
  representative work (earth-measure ~1800 BCE → Levin's TAME 2022 → morphotopy
  2026). Computes order, span (3,826 yr), the largest gap (the 1,937-year
  Euclid→Descartes plateau), and the acceleration, now quantified: 12 of 16 strata
  fall in the 197 years after the 1829 rupture; half the strata exist by 1895; the
  mean interval between consecutive strata is ~1,146 yr before 1829 and ~18 yr
  after, a 64× contraction. Backs §8.1 + Figure 1 (timeline + cumulative-count inset).
- **`frustration()`** — exact enumeration of antiferromagnetic Ising systems. The
  triangle (odd cycle) is frustrated: global minimum $-1$ sits above the summed
  local minima $-3$, so $\min\sum_i E_i > \sum_i \min E_i$ holds; the ground state
  is sixfold degenerate with one third of bonds unsatisfied. The square (bipartite)
  is the unfrustrated control (degeneracy 2). The triangle is then **scaled up** to
  a periodic triangular-lattice antiferromagnet (`_triangular_ground`, N = 9, 12,
  16): the frustrated-bond fraction stays exactly 1/3 at every size, the
  ground-state degeneracy is extensive (6 → 42 → 68), and the residual entropy per
  spin scatters around Wannier's (1950) exact thermodynamic value 0.3231 — so the
  single triangle is the seed of a macroscopic fact, not a small-system artifact.
  Backs §8.2 + Figure 2 (spin cartoons + the lattice scaling).

Both analyses are deterministic (exact enumeration, no seed). The largest lattice
is $2^{16}$ states, enumerated in seconds. Every number cited in §8 is a key in
`output/results.json`; the two figures are written to `output/figures/` and
embedded in the paper.
