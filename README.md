# Black-Box Optimisation Capstone

This repository documents my iterative solution to an eight-function Black-Box Optimisation (BBO) challenge. Each hidden function accepts a vector in the unit hypercube and returns one scalar objective value. Every function is a maximisation problem, and only one new query per function is available in each round.

## Current technical strategy

The implementation has evolved as new observations have been returned by the capstone portal:

- **Week 1:** Initial-data analysis, Gaussian Process surrogate modelling, acquisition-function reasoning and space-filling heuristics.

- **Week 2:** Function-specific exploration/exploitation updates using the first returned outputs.

- **Week 3:** RBF soft-margin SVM introduced as a diagnostic for identifying high- versus low-performance regions.

- **Week 4:** Compact PyTorch neural-network ensemble added as a secondary surrogate. Backpropagation was used to inspect local input gradients, while Gaussian Process uncertainty remained the primary guide for query selection.

- **Week 5:** Coarse-to-fine candidate refinement was introduced to concentrate the search around promising regions while retaining Expected Improvement as the uncertainty-aware ranking criterion.

- **Week 6:** Feature-guided multi-resolution refinement was introduced using Extra Trees feature importance. Influential dimensions are refined more tightly while other dimensions retain greater exploratory movement. Gaussian Process modelling remains the primary surrogate.

The project intentionally does not assume that any single model reveals the hidden functions. Candidate points are selected by combining model predictions, predictive uncertainty, observed performance, dimensionality and evidence accumulated across rounds.

## Query format

Portal submissions use six-decimal coordinates separated by hyphens, for example:

`0.699642-0.145615`

All query coordinates lie within the permitted unit-hypercube search space.

## Repository structure

- `src/bbo/` — reusable Bayesian optimisation and acquisition-function utilities.
- `weeks/week_XX/` — weekly queries, confirmed outputs, executable analysis, implementation notes and reflections.
- `scripts/` — submission validation and supporting utilities.
- `data/raw/` — local-only course data instructions; raw course datasets are not committed publicly.
- `docs/` — technical design and research justification.
- `CHANGELOG.md` — cumulative record of strategy changes across the project.

Each weekly directory preserves the evidence and methodology available at that stage. The stored `queries.json` file is treated as the authoritative record of the actual portal submission.

## Technical foundations

The optimisation strategy is grounded in established surrogate-based and Bayesian optimisation methods. Gaussian Process regression remains the primary uncertainty-aware surrogate, with Expected Improvement used to balance exploration and exploitation.

SVM, neural-network, gradient and tree-based analyses are introduced only as supporting diagnostics where they provide additional information. This distinction helps prevent unnecessary model complexity while the number of available observations remains small.

A detailed explanation of the research foundations, software choices, implemented methods, limitations and planned technical investigation is available in [`docs/technical_foundations.md`](docs/technical_foundations.md).

## Core technologies

The current implementation primarily uses:

- **Python** for the optimisation workflow.
- **NumPy** for numerical operations and candidate generation.
- **scikit-learn** for Gaussian Process regression, SVM analysis and Extra Trees feature-importance diagnostics.
- **PyTorch** for the Week 4 neural-network surrogate and gradient analysis.

## Reproducibility

Each weekly analysis can be reproduced through its corresponding entry point:

```bash
python weeks/week_01/run_week_01.py
python weeks/week_02/run_week_02.py
python weeks/week_03/run_week_03.py
python weeks/week_04/run_week_04.py
python weeks/week_05/run_week_05.py
python weeks/week_06/run_week_06.py