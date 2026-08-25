# Week 3 — SVM diagnostics and adaptive Bayesian optimisation

Week 3 incorporates the outputs returned from the second query round and refines the search strategy independently for each black-box function.

## Main changes

- Added Week 2 outputs to the cumulative evidence.
- Retained Gaussian Process / acquisition reasoning for continuous optimisation.
- Used SVM-style high-vs-low performance classification as a diagnostic rather than as the sole optimiser.
- Increased local exploitation for functions with repeated strong observations.
- Kept Function 1 strongly exploratory because observed outputs remain effectively zero.

## Week 3 portal queries

| Function | Query |
|---|---|
| F1 | `0.000100-0.000100` |
| F2 | `0.699642-0.145615` |
| F3 | `0.475344-0.452698-0.404406` |
| F4 | `0.385928-0.412267-0.392461-0.415681` |
| F5 | `0.015000-0.930000-0.999900-0.999900` |
| F6 | `0.500000-0.280000-0.580000-0.900000-0.050000` |
| F7 | `0.006169-0.293390-0.228844-0.069686-0.379744-0.864278` |
| F8 | `0.085267-0.032034-0.084852-0.052881-0.999900-0.500994-0.214072-0.237489` |

The returned outputs are intentionally not included until the portal processes this round.
