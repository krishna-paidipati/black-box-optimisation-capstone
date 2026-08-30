# Model Card — BBO Sequential Optimisation Approach

**Version:** Final round (confirmed observations through Week 12)

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
- Final round: RL-informed reward-feedback interpretation

## Reinforcement-learning interpretation

The final activity uses MAB, Q-learning and MDP concepts to interpret how the
query policy changed as observations accumulated. These concepts are not
presented as a newly trained RL agent. Instead, returned objective values are
viewed as reward feedback that changes confidence in local search policies.
Exploration is reduced where repeated improvements support exploitation and is
retained selectively where deterioration, flatness or possible noise makes the
current value estimate less reliable.

The overall workflow therefore combines trial-and-error black-box feedback with
model-based planning from the GP surrogate and acquisition logic.

## Evidence status

Confirmed Week 12 outputs are stored in
`weeks/week_13/week_12_outputs.json`. The submitted final-round queries are
stored in `weeks/week_13/queries.json`. Final-round outputs are not included
until the portal returns them.

## Limitations

Sparse coverage, adaptive sampling bias, possible evaluation noise and the lack
of any global-optimality guarantee remain important limitations. PCA is
unsupervised, clustering is descriptive, feature-importance diagnostics are not
causal, and RL terminology in the final reflection is an analogy for the
feedback-driven decision process rather than evidence that a separate RL policy
was trained.
