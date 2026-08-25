"""Week 4 neural-surrogate diagnostics for the BBO capstone.

This module complements the Gaussian Process workflow with a small PyTorch
ensemble.  The neural network is deliberately treated as a secondary
diagnostic because each black-box function still has relatively few
observations.

The code supports:
1. fitting several compact MLP regressors;
2. estimating predictive disagreement across the ensemble; and
3. computing gradients of predicted output with respect to the input.

The hidden black-box functions are never evaluated locally.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import torch
from torch import nn


class SmallMLP(nn.Module):
    """Compact surrogate suitable for the small tabular BBO datasets."""

    def __init__(self, input_dim: int) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.Tanh(),
            nn.Linear(32, 32),
            nn.Tanh(),
            nn.Linear(32, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


@dataclass
class NeuralEnsemble:
    models: list[SmallMLP]
    y_mean: float
    y_std: float


def fit_neural_ensemble(
    X: np.ndarray,
    y: np.ndarray,
    *,
    n_models: int = 10,
    epochs: int = 800,
    learning_rate: float = 0.01,
    weight_decay: float = 1e-3,
) -> NeuralEnsemble:
    """Fit a deterministic ensemble of compact MLP surrogate models."""
    X = np.asarray(X, dtype=np.float32)
    y = np.asarray(y, dtype=np.float32)

    y_mean = float(y.mean())
    y_std = float(y.std() + 1e-12)
    y_scaled = (y - y_mean) / y_std

    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y_scaled[:, None], dtype=torch.float32)

    models: list[SmallMLP] = []
    for model_index in range(n_models):
        torch.manual_seed(100 + model_index)
        model = SmallMLP(X.shape[1])
        optimizer = torch.optim.Adam(
            model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay,
        )

        for _ in range(epochs):
            optimizer.zero_grad()
            prediction = model(X_tensor)
            loss = torch.mean((prediction - y_tensor) ** 2)
            loss.backward()
            optimizer.step()

        model.eval()
        models.append(model)

    return NeuralEnsemble(models=models, y_mean=y_mean, y_std=y_std)


def predict_ensemble(
    ensemble: NeuralEnsemble,
    X: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return ensemble mean prediction and model-to-model disagreement."""
    X_tensor = torch.tensor(np.asarray(X, dtype=np.float32))

    predictions = []
    with torch.no_grad():
        for model in ensemble.models:
            scaled = model(X_tensor).numpy().ravel()
            predictions.append(scaled * ensemble.y_std + ensemble.y_mean)

    stacked = np.vstack(predictions)
    return stacked.mean(axis=0), stacked.std(axis=0)


def mean_input_gradient(
    ensemble: NeuralEnsemble,
    x: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Estimate the mean and standard deviation of input gradients.

    The returned gradient is in the original output scale.  For this capstone
    every function is maximised, so a positive component indicates a local
    direction in which the neural surrogate predicts increasing output.
    """
    gradients = []

    for model in ensemble.models:
        x_tensor = torch.tensor(
            np.asarray(x, dtype=np.float32)[None, :],
            requires_grad=True,
        )
        prediction = model(x_tensor).sum()
        prediction.backward()
        gradients.append(
            x_tensor.grad.detach().numpy().ravel() * ensemble.y_std
        )

    stacked = np.vstack(gradients)
    return stacked.mean(axis=0), stacked.std(axis=0)
