# Model Card — BBO Sequential Optimisation Approach

**Version:** Week 12

Gaussian Process surrogate modelling and acquisition reasoning remain the
primary numerical foundation.

Technical evolution:
- Week 1: GP/acquisition baseline
- Week 2: function-specific exploration/exploitation
- Week 3: RBF SVM diagnostics
- Week 4: neural surrogate and gradients
- Week 5: coarse-to-fine Expected Improvement
- Week 6: feature-guided refinement
- Week 7: GP hyperparameter tuning
- Week 8: structured prompt decision support
- Week 9: scaling diagnostics
- Week 10: transparent decision tracing
- Week 11: clustering diagnostics
- Week 12: PCA variance/redundancy diagnostics

Confirmed Week 11 outputs are stored in `weeks/week_12/week_11_outputs.json`.

PCA is unsupervised and is therefore not treated as an objective optimiser.
Sparse coverage, adaptive sampling bias, possible evaluation noise and the lack
of any global-optimality guarantee remain key limitations.
