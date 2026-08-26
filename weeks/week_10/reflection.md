# Week 10 Reflection — Transparency and Interpretability

## What reasoning guided the tenth-round submission?

I used a function-specific strategy rather than applying one rule to all eight
functions. F1 continues a direction that has improved the objective by orders
of magnitude. F7 receives tight local exploitation after Week 9 produced a
clear new best. F3, F4, F6 and F8 move back toward stronger recent basins after
less successful perturbations. F2 uses controlled interpolation between recent
and historically stronger regions. F5 is treated as a one-dimensional
sensitivity test because x2-x4 have repeatedly saturated near their upper
boundary.

## How transparent is the decision-making process?

The process is intentionally auditable. The repository stores each submitted
query, the confirmed response from the preceding round and a decision record
describing search intent, evidence and assumptions. A researcher would also
need the course-provided initial observations and all previous weekly query /
response files to reconstruct the full trajectory. Random seeds and modelling
configuration are retained where stochastic algorithms are used.

## What assumptions are being made?

A key assumption is that repeated local improvement provides useful evidence
about nearby points. This supports local exploitation, but it may fail for
discontinuous, highly multimodal or noisy functions. I also assume that the
observed outputs are sufficiently reliable to compare across rounds. These
assumptions can bias the search toward an apparent local optimum.

## Where are the gaps or potential biases?

The observations are not uniformly distributed. Later rounds deliberately
cluster around promising regions, so large portions of the unit hypercube
remain sparsely sampled, especially for the higher-dimensional functions.
This exploitation bias improves short-term optimisation efficiency but weakens
claims about the global response surface. Boundary-heavy functions such as F5
also provide limited information about interior interactions.

## What is one significant limitation?

The largest limitation is the very small evaluation budget relative to the
dimensionality and possible complexity of the hidden functions. A surrogate can
appear confident because observations cluster locally even though distant
regions remain unexplored. I therefore treat GP predictions, feature
importance and other diagnostics as decision aids rather than proof of the
global optimum. The final results should be interpreted as the outcome of a
documented sequential search under a strict query budget, not as exhaustive
optimisation.
