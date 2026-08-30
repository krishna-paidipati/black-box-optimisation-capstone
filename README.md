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
- Final round: RL-informed feedback interpretation and predominantly local exploitation

Gaussian Process modelling remains the primary uncertainty-aware numerical
foundation. The later diagnostic methods support interpretation and query
selection; they do not replace the core optimiser.

## Final-round perspective

The final iteration connects the accumulated BBO evidence to reinforcement
learning ideas. Early rounds placed greater value on exploration, whereas the
larger data set allowed the final policy to concentrate on proven local regions.
Returned objective values were treated as feedback that strengthened or weakened
confidence in each search direction, analogous to updating reward expectations.

The implementation remains best described as a hybrid of trial-and-error
feedback and model-based planning: the hidden functions supply black-box reward
signals, while GP surrogate modelling and acquisition reasoning anticipate where
future evaluations may be valuable.

## Documentation

- [`Technical Foundations`](docs/technical_foundations.md)
- [`Datasheet`](docs/datasheet.md)
- [`Model Card`](docs/model_card.md)
- [`Final Round`](weeks/final_round/README.md)

## Current status

The repository records the **submitted final-round queries** and **confirmed
portal outputs through Week 12**. Final-round outputs are intentionally left
unrecorded until they are returned by the portal.
