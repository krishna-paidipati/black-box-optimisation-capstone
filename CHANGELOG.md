# Changelog

## Documentation update — technical foundations

- Added `docs/technical_foundations.md`.
- Documented the research basis for Gaussian Process surrogate modelling and Expected Improvement.
- Distinguished primary optimisation methods from SVM, neural-network and Extra Trees diagnostic analyses.
- Documented NumPy, scikit-learn and PyTorch responsibilities in the current implementation.
- Added explicit limitations and future technical investigations.
- Added a reproducibility note explaining why stored portal queries remain the authoritative historical record.

## Week 6

- Added the eight confirmed Week 5 outputs.
- Added Extra Trees feature-importance diagnostics.
- Added feature-guided multi-resolution local candidate refinement.
- Retained Gaussian Process Expected Improvement as the primary ranking signal.
- Added Week 6 portal queries and reflection.

## Repository maintenance

- Standardised Week 4 and Week 5 with executable `run_week_04.py` and `run_week_05.py` entry points.
- Kept specialised modelling logic separate from weekly runners.

## Week 5

- Added the eight confirmed Week 4 outputs.
- Added coarse-to-fine Expected Improvement refinement.
- Kept the neural ensemble as a secondary diagnostic.

## Week 4

- Added the eight confirmed Week 3 outputs.
- Added a compact PyTorch neural-network ensemble and input-gradient analysis.

## Week 3

- Added Week 2 outputs and RBF SVM high/low-performance diagnostics.

## Week 2

- Added Week 1 outputs and function-specific exploration/exploitation updates.

## Week 1

- Initialised the repository and baseline Gaussian Process workflow.