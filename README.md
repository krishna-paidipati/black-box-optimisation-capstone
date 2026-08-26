# Black-Box Optimisation Capstone

This repository documents my iterative solution to eight unknown maximisation
functions under a strict query budget.

## Current technical strategy
- Week 1: GP/acquisition baseline.
- Week 2: function-specific exploration/exploitation.
- Week 3: RBF SVM diagnostics.
- Week 4: neural-surrogate and gradient diagnostics.
- Week 5: coarse-to-fine EI refinement.
- Week 6: feature-guided multi-resolution refinement.
- Week 7: GP hyperparameter tuning.
- Week 8: structured prompt decision support.
- Week 9: scaling-aware diagnostics.
- Week 10: transparent decision tracing.
- Week 11: clustering and nearest-neighbour diagnostics.

Gaussian Process modelling remains the primary uncertainty-aware numerical
foundation.

## Project documentation
- [`Technical Foundations`](docs/technical_foundations.md)
- [`Datasheet`](docs/datasheet.md)
- [`Model Card`](docs/model_card.md)

## Repository structure
- `src/bbo/` — reusable optimisation utilities.
- `weeks/week_XX/` — weekly queries, outputs, analyses and reflections.
- `scripts/` — validation utilities.
- `data/raw/` — local-only course data instructions.
- `docs/` — technical and governance documentation.
- `CHANGELOG.md` — cumulative project history.

## Current status
The repository documents the **Week 11 submission**, with confirmed portal
outputs through **Week 10**.
