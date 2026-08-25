"""Week 5 analysis runner for the BBO capstone.

This entry point reconstructs all observations available before the Week 5
submission. It then applies the Week 5 coarse-to-fine Gaussian Process
candidate search and uses the Week 4 neural ensemble as a secondary consistency
check.

The exact Week 5 portal submissions are stored in ``queries.json`` and printed
as the authoritative historical record. The hidden black-box functions are
never evaluated locally.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
WEEK_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(WEEK_DIR))
sys.path.insert(0, str(ROOT / "weeks" / "week_04"))

from bbo.data import best_observation, load_function_data  # noqa: E402
from bbo.surrogate import fit_gp  # noqa: E402
from coarse_to_fine import coarse_to_fine_candidates  # noqa: E402
from neural_surrogate import fit_neural_ensemble, predict_ensemble  # noqa: E402

DATA_ROOT = ROOT / "data" / "raw" / "initial_data"

EXPECTED_DIMS = {
    "function_1": 2,
    "function_2": 2,
    "function_3": 3,
    "function_4": 4,
    "function_5": 4,
    "function_6": 5,
    "function_7": 6,
    "function_8": 8,
}


def load_json(path: Path) -> dict:
    """Load a JSON file and fail clearly when a historical record is missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return json.loads(path.read_text())


def parse_query(query: str) -> np.ndarray:
    """Convert a portal query string into a NumPy vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def build_history(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    """Build initial data plus confirmed Week 1 through Week 4 observations."""
    X, y = load_function_data(DATA_ROOT, function_id)
    key = f"function_{function_id}"

    historical_rounds = [
        (
            ROOT / "weeks" / "week_01" / "queries.json",
            ROOT / "weeks" / "week_02" / "week_01_outputs.json",
        ),
        (
            ROOT / "weeks" / "week_02" / "queries.json",
            ROOT / "weeks" / "week_03" / "week_02_outputs.json",
        ),
        (
            ROOT / "weeks" / "week_03" / "queries.json",
            ROOT / "weeks" / "week_04" / "week_03_outputs.json",
        ),
        (
            ROOT / "weeks" / "week_04" / "queries.json",
            ROOT / "weeks" / "week_05" / "week_04_outputs.json",
        ),
    ]

    for query_path, output_path in historical_rounds:
        query = parse_query(load_json(query_path)[key])
        output = float(load_json(output_path)[key])

        if query.size != X.shape[1]:
            raise ValueError(
                f"{key}: historical query has {query.size} coordinates; "
                f"expected {X.shape[1]}"
            )

        X = np.vstack([X, query])
        y = np.concatenate([y, [output]])

    return X, y


def analyse_function(function_id: int) -> None:
    """Print Week 5 coarse-to-fine and neural-consistency diagnostics."""
    X, y = build_history(function_id)
    best_x, best_y, best_idx = best_observation(X, y)

    gp = fit_gp(X, y)
    refined, ei_scores = coarse_to_fine_candidates(
        gp,
        y,
        n_dims=X.shape[1],
        n_coarse=20_000,
        n_elite=10,
        local_per_elite=500,
        local_scale=0.04,
        random_state=500 + function_id,
    )

    # The neural ensemble is a secondary check only. It does not replace the
    # uncertainty-aware Gaussian Process ranking.
    ensemble = fit_neural_ensemble(
        X,
        y,
        n_models=5,
        epochs=400,
    )

    top_candidates = refined[:100]
    nn_mean, nn_disagreement = predict_ensemble(ensemble, top_candidates)

    # Among the highest-EI candidates, highlight the point with the strongest
    # neural mean as a consistency diagnostic.
    nn_idx = int(np.argmax(nn_mean))

    print(f"\nFunction {function_id}")
    print("-" * 72)
    print(f"Observations available for Week 5: {len(y)}")
    print(f"Dimensions: {X.shape[1]}")
    print(f"Best observed row: {best_idx}")
    print(f"Best observed y: {best_y:.12g}")
    print(f"Best observed x: {np.array2string(best_x, precision=6)}")
    print(
        "Top coarse-to-fine EI point: "
        f"{np.array2string(refined[0], precision=6)}"
    )
    print(f"Top EI score:                {ei_scores[0]:.6g}")
    print(
        "NN-supported top-100 point:   "
        f"{np.array2string(top_candidates[nn_idx], precision=6)}"
    )
    print(f"Neural disagreement:         {nn_disagreement[nn_idx]:.6g}")


def print_submitted_queries() -> None:
    """Print the exact Week 5 portal queries stored in the repository."""
    queries = load_json(WEEK_DIR / "queries.json")

    print("\nAuthoritative Week 5 portal submissions")
    print("=" * 72)
    for function_id in range(1, 9):
        key = f"function_{function_id}"
        query = queries[key]
        expected_dim = EXPECTED_DIMS[key]

        if len(query.split("-")) != expected_dim:
            raise ValueError(
                f"{key}: stored query does not have {expected_dim} coordinates"
            )

        print(f"F{function_id}: {query}")


def main() -> None:
    """Run the complete Week 5 diagnostic workflow."""
    if not DATA_ROOT.exists():
        raise SystemExit(
            "Initial data not found. Place the course-provided initial_data "
            f"directory at {DATA_ROOT}"
        )

    for function_id in range(1, 9):
        analyse_function(function_id)

    print_submitted_queries()


if __name__ == "__main__":
    main()
