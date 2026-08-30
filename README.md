# Black-Box Optimisation Capstone

This repository documents my iterative solution to eight unknown maximisation
functions under a strict sequential query budget.

## Strategy evolution

- Week 1: GP/acquisition baseline
- Week 2: function-specific exploration/exploitation
- Week 3: RBF SVM diagnostics
- Week 4: neural-surrogate and gradient diagnostics
- Week 5: coarse-to-fine Expected Improvement refinement
- Week 6: feature-guided refinement
- Week 7: GP hyperparameter tuning
- Week 8: structured prompt decision support
- Week 9: scale-aware diagnostics
- Week 10: transparent decision tracing
- Week 11: clustering diagnostics
- Week 12: PCA variance and redundancy diagnostics
- Week 13: final-round RL-informed feedback interpretation and predominantly local exploitation

Gaussian Process modelling remains the primary uncertainty-aware numerical
foundation. The later diagnostic methods support interpretation and query
selection; they do not replace the core optimiser.

## Repository structure

- `src/bbo/` contains reusable optimisation utilities for data loading,
  surrogate modelling, acquisition functions, candidate generation and
  query formatting.
- `weeks/week_01/` through `weeks/week_13/` preserve the sequential
  optimisation history, submitted queries, returned outputs and weekly
  reflections.
- `docs/` contains the technical foundations, dataset documentation and
  model card.
- `scripts/validate_submission.py` validates portal query formatting.
- `data/raw/` is intentionally excluded from version control because the
  course-provided data are not redistributed.

## Running the project

Create an environment and install the dependencies:

```bash
pip install -r requirements.txt

## Week 13 - Final-round perspective

The final iteration connects the accumulated BBO evidence to reinforcement
learning ideas. Early rounds placed greater value on exploration, whereas the
larger data set allowed the final policy to concentrate on proven local regions.

Returned objective values were treated as feedback that strengthened or weakened
confidence in each search direction, analogous to updating reward expectations.
This informed whether the next query should exploit a promising neighbourhood,
tighten around a boundary, or retain limited exploration where uncertainty
remained important.

The implementation remains best described as a hybrid of trial-and-error
feedback and model-based planning. The hidden functions supply black-box reward
signals, while Gaussian Process surrogate modelling and acquisition reasoning
anticipate where future evaluations may be valuable.

## Documentation

- [`Technical Foundations`](docs/technical_foundations.md)
- [`Datasheet`](docs/datasheet.md)
- [`Model Card`](docs/model_card.md)
- [`Week 13 - Final Round`](weeks/week_13/README.md)

## Current status

The repository records the **submitted Week 13 final-round queries** and
**confirmed portal outputs through Week 12**. Week 13 outputs are intentionally
left unrecorded until they are returned by the portal.