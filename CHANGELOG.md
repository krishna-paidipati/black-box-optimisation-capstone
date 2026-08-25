# Changelog

## Repository maintenance
- Standardised Week 4 and Week 5 with `run_week_04.py` and `run_week_05.py`
  executable entry points, matching the Week 1–3 repository convention.
- Kept specialised modelling logic in `neural_surrogate.py` and
  `coarse_to_fine.py`.
- Corrected the Week 5 Expected Improvement helper to use the implemented
  `best_y` API.

## Week 5
- Added the eight confirmed Week 4 outputs.
- Added a coarse-to-fine Expected Improvement candidate-refinement helper.
- Kept the neural ensemble as a secondary diagnostic rather than increasing
  network depth.
- Refined query selection around empirically supported basins.
- Added Week 5 queries and submission reflection.

## Week 4
- Added the eight confirmed Week 3 outputs.
- Added a compact PyTorch neural-network ensemble as a secondary surrogate
  diagnostic.
- Added backpropagation-based input-gradient analysis.
- Kept Gaussian Process uncertainty as the primary optimisation signal.

## Week 3
- Added Week 2 outputs and RBF SVM high/low-performance diagnostics.

## Week 2
- Added Week 1 outputs and function-specific exploration/exploitation updates.

## Week 1
- Initialised the BBO repository and baseline Gaussian Process workflow.
