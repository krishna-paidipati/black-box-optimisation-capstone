"""Acquisition functions for balancing exploration and exploitation."""

from __future__ import annotations

import numpy as np
from scipy.stats import norm


def upper_confidence_bound(mean: np.ndarray, std: np.ndarray, kappa: float = 1.96) -> np.ndarray:
    """Return UCB scores for a maximisation problem."""
    return mean + kappa * std


def expected_improvement(
    mean: np.ndarray,
    std: np.ndarray,
    best_y: float,
    xi: float = 0.01,
) -> np.ndarray:
    """Return Expected Improvement scores for a maximisation problem."""
    std = np.asarray(std, dtype=float)
    improvement = np.asarray(mean, dtype=float) - float(best_y) - float(xi)

    scores = np.zeros_like(improvement)
    mask = std > 1e-12
    z = improvement[mask] / std[mask]
    scores[mask] = improvement[mask] * norm.cdf(z) + std[mask] * norm.pdf(z)
    return scores
