# Model Card — BBO Sequential Optimisation Approach

## Overview
**Version:** Week 11  
**Task:** maximise eight unknown 2D–8D black-box functions.

Gaussian Process surrogate modelling and acquisition reasoning remain the
primary numerical foundation. Supporting diagnostics are added only when they
serve a specific purpose.

## Intended use
Educational sequential black-box optimisation with limited evaluations and
uncertainty. Not a guarantee of global optimality and not intended for direct
safety-critical deployment.

## Technical evolution
- Week 1: GP/acquisition baseline and exploration.
- Week 2: function-specific exploration/exploitation.
- Week 3: RBF SVM diagnostics.
- Week 4: PyTorch neural surrogate and gradients.
- Week 5: coarse-to-fine Expected Improvement.
- Week 6: Extra Trees feature-guided refinement.
- Week 7: GP hyperparameter tuning.
- Week 8: structured prompt decision support.
- Week 9: scaling/diminishing-return diagnostics.
- Week 10: transparent decision tracing.
- Week 11: KMeans and nearest-neighbour cluster diagnostics.

## Performance
Confirmed Week 10 outputs:

| Function | Week 10 output |
|---|---:|
| F1 | 0.000020579299197814755 |
| F2 | 0.6548301209141953 |
| F3 | -0.024715336576968623 |
| F4 | 0.45411365194265985 |
| F5 | 4440.482959868813 |
| F6 | -0.31712068337721777 |
| F7 | 1.7449602475404162 |
| F8 | 9.94581999875 |

These are round-specific, not necessarily all-time best values.

## Assumptions and limitations
Local improvement is assumed to provide useful nearby information, which can
fail for noisy, discontinuous or multimodal functions. Function 3 has shown
different outputs for an identical repeated input, supporting non-zero noise
modelling. Coverage is sparse, especially in higher dimensions. Clusters may
reflect adaptive sampling bias. Global optimality cannot be proven.

## Transparency and ethics
The repository separates observed evidence, diagnostics, assumptions and final
queries. This reduces the risk of presenting model outputs as facts or hiding
failed experiments. Real-world adaptation would require domain-specific safety,
privacy, fairness and oversight.
