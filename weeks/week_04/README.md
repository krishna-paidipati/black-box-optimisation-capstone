# Week 4 — Neural-surrogate and gradient diagnostics

Week 4 adds a compact neural-network surrogate as a secondary diagnostic while retaining Gaussian Process reasoning as the primary optimisation method.

## Confirmed Week 3 results

| Function | Week 3 output |
|---|---:|
| F1 | 3.0778671018359276e-248 |
| F2 | 0.6240751182000498 |
| F3 | -0.015678114213233098 |
| F4 | 0.42217637988277845 |
| F5 | 3605.87049298965 |
| F6 | -0.4274173033893786 |
| F7 | 0.999980409900096 |
| F8 | 9.9365843164769 |

## Week 4 query rationale

- **F1:** local search around the only initially informative positive region rather than another domain corner.
- **F2:** conservative exploitation near the stable high-performing first-coordinate region.
- **F3:** model-supported exploration of a different high-potential region.
- **F4:** local Expected-Improvement refinement near the best observed basin.
- **F5:** strong exploitation at the boundary direction repeatedly supported by observations and both surrogates.
- **F6:** GP/NN-consensus refinement after Week 3 improved the objective.
- **F7:** return towards the Week 2 high-performing region after the Week 3 deterioration.
- **F8:** local high-dimensional refinement supported by both GP predictions and neural input gradients.

The neural model is not used as a standalone optimiser because the available samples remain small.
