"""Week 3 query validation and SVM diagnostic helpers.

This script does not evaluate the hidden black-box functions. It validates the
portal-ready queries and provides a small reusable helper for classifying
observations into high- and low-performance regions with an RBF SVM.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


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


def parse_query(query: str) -> np.ndarray:
    """Convert the portal's hyphen-delimited query format to a numeric vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def validate_queries(queries: dict[str, str]) -> None:
    """Validate dimensions, bounds and fixed six-decimal formatting."""
    for function_name, expected_dim in EXPECTED_DIMS.items():
        query = queries[function_name]
        parts = query.split("-")

        if len(parts) != expected_dim:
            raise ValueError(
                f"{function_name}: expected {expected_dim} coordinates, got {len(parts)}"
            )

        for part in parts:
            if not part.startswith("0.") or len(part.split(".")[1]) != 6:
                raise ValueError(
                    f"{function_name}: coordinate {part!r} is not in six-decimal portal format"
                )

        values = parse_query(query)
        if np.any(values < 0.0) or np.any(values >= 1.0):
            raise ValueError(f"{function_name}: all coordinates must lie in [0, 1).")


def fit_high_performance_svm(
    X: np.ndarray,
    y: np.ndarray,
    quantile: float = 0.70,
) -> tuple[object, float]:
    """Fit an RBF soft-margin SVM to classify the highest-performing observations.

    The classifier is only a diagnostic aid. The BBO objective remains continuous,
    so final query selection should still consider surrogate predictions and
    uncertainty rather than treating this classifier as the optimiser.
    """
    threshold = float(np.quantile(y, quantile))
    labels = (y >= threshold).astype(int)

    classifier = make_pipeline(
        StandardScaler(),
        SVC(
            kernel="rbf",
            C=5.0,
            gamma="scale",
            class_weight="balanced",
            probability=True,
            random_state=42,
        ),
    )
    classifier.fit(X, labels)
    return classifier, threshold


if __name__ == "__main__":
    path = Path(__file__).with_name("queries.json")
    queries = json.loads(path.read_text())
    validate_queries(queries)
    print("All Week 3 queries have valid dimensions and six-decimal portal formatting.")
