"""Gaussian Process surrogate models used in the BBO capstone."""

from __future__ import annotations

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel


def fit_gp(X: np.ndarray, y: np.ndarray, *, noise_level: float = 1e-6) -> GaussianProcessRegressor:
    """Fit a flexible GP surrogate suitable for small black-box datasets.

    The Matérn-5/2 kernel is a practical default for functions that may be
    smooth without being infinitely differentiable. A WhiteKernel allows the
    surrogate to represent observation noise when present.
    """
    n_dims = X.shape[1]
    kernel = (
        ConstantKernel(1.0, (1e-3, 1e3))
        * Matern(length_scale=np.ones(n_dims), length_scale_bounds=(1e-2, 1e2), nu=2.5)
        + WhiteKernel(noise_level=noise_level, noise_level_bounds=(1e-10, 1e1))
    )
    gp = GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        n_restarts_optimizer=8,
        random_state=42,
    )
    gp.fit(X, y)
    return gp
