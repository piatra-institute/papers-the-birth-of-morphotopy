"""Orchestrator: reproduces every number in the paper's modelled section (§8).

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in §8
is a key in the JSON file. Both analyses are deterministic (exact enumeration);
there is no seed.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_stratigraphy, plot_frustration

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_stratigraphy(str(OUT / "figures" / "stratigraphy.png"))
    plot_frustration(str(OUT / "figures" / "frustration.png"))

    s, f = results["stratigraphy"], results["frustration"]
    print(f"stratigraphy: {s['n_strata']} strata, span {s['span_years']} yr, "
          f"largest gap {s['largest_gap_years']} yr {s['largest_gap_between']}; "
          f"half by {s['median_emergence_year']}; mean gap "
          f"{s['mean_gap_premodern_years']}→{s['mean_gap_modern_years']} yr "
          f"({s['acceleration_ratio']}x faster after 1829)")
    print(f"frustration: triangle global-minus-local {f['triangle_global_minus_local']} (>0), "
          f"square {f['square_global_minus_local']}; degeneracy {f['triangle_degeneracy']} vs "
          f"{f['square_degeneracy']}; frustrated fraction {f['triangle_frustrated_fraction']}")
    print("  triangular lattice: " + ", ".join(
        f"N{L['n_spins']} deg{L['ground_degeneracy']} frac{L['frustrated_bond_fraction']} "
        f"S/N{L['residual_entropy_per_spin']}" for L in f["triangular_lattices"])
        + f"  (Wannier {f['wannier_entropy_per_spin']})")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
