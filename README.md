# Black-Box Optimisation Capstone

This repository documents my iterative solution to an eight-function Black-Box Optimisation challenge. Each hidden function accepts a vector in the unit hypercube and returns one scalar objective value. Every function is a maximisation problem, and only one new query per function is available in each round.

## Current technical strategy

The implementation has evolved with the evidence returned by the portal:

- **Week 1:** initial-data analysis, Gaussian Process surrogate modelling, acquisition-function reasoning and space-filling heuristics.
- **Week 2:** function-specific exploration/exploitation updates using the first returned outputs.
- **Week 3:** RBF soft-margin SVM used as a diagnostic for high- versus low-performance regions.
- **Week 4:** compact PyTorch neural-network ensemble added as a secondary surrogate. Backpropagation is used to inspect local input gradients, while Gaussian Process uncertainty remains the primary guide for query selection.

The project intentionally does not claim that any single model reveals the hidden function. Candidate points are selected by combining model predictions, uncertainty, observed performance, dimensionality and problem-specific evidence.

## Query format

Portal submissions use six-decimal coordinates separated by hyphens, for example:

`0.699642-0.145615`

All coordinates lie in `[0, 1)`.

## Repository structure

- `src/bbo/` — reusable Bayesian-optimisation utilities.
- `weeks/week_XX/` — confirmed outputs, selected queries, implementation notes and reflections for each round.
- `scripts/` — submission validation utilities.
- `data/raw/` — local-only course data instructions; raw course datasets are not committed publicly.
- `CHANGELOG.md` — cumulative record of strategy changes.

The repository will continue to evolve as each new portal response is received.
