# Model Card - BBO Sequential Optimisation Approach

**Version:** Final - confirmed observations through Week 13

## Primary approach

Gaussian Process surrogate modelling and acquisition reasoning remain the
primary uncertainty-aware numerical foundation for the project. The objective
is maximisation for all eight hidden functions.

## Technical evolution

- Week 1: GP/acquisition baseline
- Week 2: function-specific exploration/exploitation
- Week 3: RBF SVM diagnostics
- Week 4: neural surrogate and gradients
- Week 5: coarse-to-fine Expected Improvement
- Week 6: feature-guided refinement
- Week 7: GP hyperparameter tuning
- Week 8: structured prompt decision support
- Week 9: scale-aware diagnostics
- Week 10: transparent decision tracing
- Week 11: clustering diagnostics
- Week 12: PCA variance/redundancy diagnostics
- Week 13: RL-informed reward-feedback interpretation and final query selection

## Reinforcement-learning interpretation

The final activity uses MAB, Q-learning and MDP concepts to interpret how the
query policy changed as observations accumulated. These concepts are not
presented as a newly trained RL agent. Instead, returned objective values are
viewed as reward feedback that changes confidence in local search policies.

Exploration was reduced where repeated improvements supported exploitation and
retained selectively where deterioration, flatness or possible noise made the
current value estimate less reliable.

The overall workflow therefore combines trial-and-error black-box feedback with
model-based planning from the Gaussian Process surrogate and acquisition logic.

## Final evidence

Confirmed Week 12 outputs used for the final decision are stored in
`weeks/week_13/week_12_outputs.json`. The submitted Week 13 queries are stored
in `weeks/week_13/queries.json`, and their confirmed portal responses are stored
in `weeks/week_13/week_13_outputs.json`.

The final round produced new observed best values for Functions 3, 4, 5, 7 and
8. Functions 1 and 2 improved relative to Week 12 but remained below earlier
historical best observations. Function 6 deteriorated relative to its Week 12
best.

These outcomes are consistent with the project's central optimisation lesson:
increasing confidence in a promising local region can justify exploitation,
but sparse black-box feedback does not remove uncertainty or guarantee that a
local perturbation will improve the objective.

## Limitations

Sparse coverage, adaptive sampling bias, possible evaluation noise and the lack
of any global-optimality guarantee remain important limitations. PCA is
unsupervised, clustering is descriptive, feature-importance diagnostics are not
causal, and RL terminology in the final reflection is an analogy for the
feedback-driven decision process rather than evidence that a separate RL policy
was trained.