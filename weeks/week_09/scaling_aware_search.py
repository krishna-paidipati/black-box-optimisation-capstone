"""Scaling-aware search diagnostics for Week 9.

The challenge does not have a model-size scaling law in the LLM sense, so this
module measures *optimisation scaling* instead: how quickly best-so-far
performance improves as additional black-box evaluations are added.

That trajectory is used to decide whether candidate generation should favour
local exploitation or reserve more budget for global exploration.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from bbo.acquisition import expected_improvement


@dataclass(frozen=True)
class ScalingDiagnostics:
    """Summary of recent best-so-far progress."""

    recent_improvement: float
    previous_improvement: float
    improvement_ratio: float
    local_fraction: float


def best_so_far(y: np.ndarray) -> np.ndarray:
    """Return the cumulative maximum objective sequence."""
    return np.maximum.accumulate(np.asarray(y, dtype=float).reshape(-1))


def scaling_diagnostics(y: np.ndarray) -> ScalingDiagnostics:
    """Estimate diminishing returns and an exploitation allocation.

    A high recent improvement relative to the preceding improvement favours
    local refinement. A plateau reserves more of the candidate budget for
    exploration.
    """
    best = best_so_far(y)

    if len(best) < 3:
        return ScalingDiagnostics(0.0, 0.0, 1.0, 0.60)

    recent = float(best[-1] - best[-2])
    previous = float(best[-2] - best[-3])

    scale = float(np.std(y) + 1e-12)
    recent_norm = max(recent, 0.0) / scale
    previous_norm = max(previous, 0.0) / scale

    ratio = (recent_norm + 1e-6) / (previous_norm + 1e-6)

    # Plateau -> more global exploration; sustained improvement -> more local.
    if recent_norm < 1e-4:
        local_fraction = 0.55
    elif ratio >= 0.75:
        local_fraction = 0.85
    else:
        local_fraction = 0.70

    return ScalingDiagnostics(
        recent_improvement=recent,
        previous_improvement=previous,
        improvement_ratio=ratio,
        local_fraction=local_fraction,
    )


def scaled_candidate_search(
    gp,
    X: np.ndarray,
    y: np.ndarray,
    *,
    n_candidates: int = 100_000,
    local_scale: float = 0.05,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray, ScalingDiagnostics]:
    """Generate an adaptive mixture of local and global candidates."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    rng = np.random.default_rng(random_state)

    diag = scaling_diagnostics(y)
    n_local = int(n_candidates * diag.local_fraction)
    n_global = n_candidates - n_local

    centre = X[int(np.argmax(y))]
    local = np.clip(
        centre + rng.normal(0.0, local_scale, size=(n_local, X.shape[1])),
        0.000001,
        0.999999,
    )
    global_points = rng.uniform(
        0.000001, 0.999999, size=(n_global, X.shape[1])
    )

    candidates = np.vstack([local, global_points])
    mean, std = gp.predict(candidates, return_std=True)
    score = expected_improvement(
        mean,
        std,
        best_y=float(np.max(y)),
        xi=0.01 * float(np.std(y) + 1e-12),
    )

    order = np.argsort(score)[::-1]
    return candidates[order], score[order], diag
