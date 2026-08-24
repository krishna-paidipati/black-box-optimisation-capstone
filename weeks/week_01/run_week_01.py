"""Week 1 baseline analysis for the Stage 2 BBO capstone.

This script summarises the course-provided initial observations and demonstrates
how a Gaussian Process + acquisition workflow can be used to rank candidate
points. The exact portal submissions are preserved separately in queries.json,
which is the authoritative record of what was submitted.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from bbo.acquisition import expected_improvement, upper_confidence_bound  # noqa: E402
from bbo.candidates import min_distance_to_observations, random_candidates  # noqa: E402
from bbo.data import best_observation, load_function_data  # noqa: E402
from bbo.surrogate import fit_gp  # noqa: E402

DATA_ROOT = ROOT / "data" / "raw" / "initial_data"


def analyse_function(function_id: int, n_candidates: int = 50_000) -> None:
    """Print a compact surrogate-based diagnostic for one function."""
    X, y = load_function_data(DATA_ROOT, function_id)
    best_x, best_y, best_idx = best_observation(X, y)

    print(f"\nFunction {function_id}")
    print("-" * 50)
    print(f"Samples: {len(y)} | Dimensions: {X.shape[1]}")
    print(f"Current best row: {best_idx}")
    print(f"Current best y: {best_y:.6f}")
    print(f"Current best x: {np.array2string(best_x, precision=6)}")

    gp = fit_gp(X, y)
    candidates = random_candidates(n_candidates, X.shape[1], seed=42 + function_id)
    mean, std = gp.predict(candidates, return_std=True)

    ei = expected_improvement(mean, std, best_y=best_y, xi=0.01)
    ucb = upper_confidence_bound(mean, std, kappa=1.96)
    nearest = min_distance_to_observations(candidates, X)

    ei_idx = int(np.argmax(ei))
    ucb_idx = int(np.argmax(ucb))
    explore_idx = int(np.argmax(nearest))

    print(f"Top EI candidate:      {np.array2string(candidates[ei_idx], precision=6)}")
    print(f"Top UCB candidate:     {np.array2string(candidates[ucb_idx], precision=6)}")
    print(f"Maximin exploration:   {np.array2string(candidates[explore_idx], precision=6)}")


def main() -> None:
    if not DATA_ROOT.exists():
        raise SystemExit(
            "Initial data not found. Place the course-provided initial_data directory at "
            f"{DATA_ROOT}"
        )

    for function_id in range(1, 9):
        analyse_function(function_id)


if __name__ == "__main__":
    main()
