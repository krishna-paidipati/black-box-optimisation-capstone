"""Gaussian Process hyperparameter tuning used for Week 7.

This module tunes two model choices that materially affect the BBO surrogate:

1. kernel family: RBF or Matérn with several smoothness assumptions;
2. ``alpha``: the observation-noise / numerical-stability parameter.

Candidate configurations are compared with shuffled K-fold cross-validation.
The winning configuration is then refitted on all observations.

The function is intentionally small and explicit instead of introducing a
large AutoML dependency. The capstone datasets remain small, and keeping the
search inspectable makes the modelling decisions easier to justify.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import (
    ConstantKernel,
    Matern,
    RBF,
)
from sklearn.model_selection import KFold


@dataclass(frozen=True)
class GPTuningResult:
    """Selected GP configuration and its cross-validation score."""

    kernel_name: str
    alpha: float
    normalised_rmse: float


def _kernel(kernel_name: str, n_dims: int):
    """Construct an ARD kernel for the requested kernel family."""
    length_scale = np.full(n_dims, 0.2, dtype=float)
    bounds = (1e-2, 10.0)

    if kernel_name == "rbf":
        base = RBF(
            length_scale=length_scale,
            length_scale_bounds=bounds,
        )
    elif kernel_name == "matern_0.5":
        base = Matern(
            length_scale=length_scale,
            length_scale_bounds=bounds,
            nu=0.5,
        )
    elif kernel_name == "matern_1.5":
        base = Matern(
            length_scale=length_scale,
            length_scale_bounds=bounds,
            nu=1.5,
        )
    elif kernel_name == "matern_2.5":
        base = Matern(
            length_scale=length_scale,
            length_scale_bounds=bounds,
            nu=2.5,
        )
    else:
        raise ValueError(f"Unsupported kernel: {kernel_name}")

    return ConstantKernel(
        constant_value=1.0,
        constant_value_bounds=(1e-3, 1e3),
    ) * base


def _normalised_rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Return RMSE divided by target standard deviation."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    rmse = float(np.sqrt(np.mean((y_true - y_pred) ** 2)))
    scale = float(np.std(y_true) + 1e-12)
    return rmse / scale


def tune_gp(
    X: np.ndarray,
    y: np.ndarray,
    *,
    random_state: int = 42,
) -> tuple[GaussianProcessRegressor, GPTuningResult, list[GPTuningResult]]:
    """Tune kernel family and alpha using shuffled K-fold validation.

    The returned GP is refitted on the complete supplied data using the best
    cross-validation configuration.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)

    kernel_names = (
        "rbf",
        "matern_0.5",
        "matern_1.5",
        "matern_2.5",
    )
    alpha_values = (
        1e-8,
        1e-6,
        1e-4,
        1e-3,
        1e-2,
    )

    folds = KFold(
        n_splits=min(5, len(y)),
        shuffle=True,
        random_state=random_state,
    )

    results: list[GPTuningResult] = []

    for kernel_name in kernel_names:
        for alpha in alpha_values:
            prediction = np.empty_like(y, dtype=float)

            for train_index, valid_index in folds.split(X):
                gp = GaussianProcessRegressor(
                    kernel=_kernel(kernel_name, X.shape[1]),
                    alpha=alpha,
                    normalize_y=True,
                    n_restarts_optimizer=1,
                    random_state=random_state,
                )
                gp.fit(X[train_index], y[train_index])
                prediction[valid_index] = gp.predict(X[valid_index])

            results.append(
                GPTuningResult(
                    kernel_name=kernel_name,
                    alpha=alpha,
                    normalised_rmse=_normalised_rmse(y, prediction),
                )
            )

    results.sort(key=lambda item: item.normalised_rmse)
    best = results[0]

    fitted = GaussianProcessRegressor(
        kernel=_kernel(best.kernel_name, X.shape[1]),
        alpha=best.alpha,
        normalize_y=True,
        n_restarts_optimizer=10,
        random_state=random_state,
    )
    fitted.fit(X, y)

    return fitted, best, results
