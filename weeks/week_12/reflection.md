# Week 12 Reflection — PCA-Informed Simplification

My optimisation strategy has become much more structured than it was in the
first few rounds. Initially I relied more on broad exploration, Gaussian
Process uncertainty and manual interpretation of very limited observations.
With 21 observations now available per function, I can compare historical best
regions, local boundaries, repeated trajectories, dimensional sensitivity and
recent improvement rates before deciding how far to move.

The PCA concept helped me think about which dimensions and behaviours account
for most of the useful variation. I do not use PCA itself to predict the
objective because PCA is unsupervised. Instead, I use it to inspect the
standardised input observations and the higher-performing subset. Principal
component loadings show directions in which the submitted queries vary most,
while feature/objective correlations provide a separate diagnostic of which
original coordinates appear associated with performance.

I now simplify parts of the strategy where repeated evidence shows redundancy.
Function 5 is a clear example: x2, x3 and x4 repeatedly remain near their upper
boundaries, so I continue a controlled change in x1 instead of perturbing all
four dimensions. Function 8 is also showing diminishing returns from very small
local movements, suggesting that further microscopic refinement may soon add
less information.

Week 11 demonstrated why simplification must not become blind extrapolation.
Function 1 had improved dramatically for several rounds, but the next movement
crossed into a sharply worse region. For Week 12 I therefore tighten the
boundary between the successful Week 10 point and unsuccessful Week 11 point.
Function 2 is treated similarly around the stronger x2≈0.40 region, while
Function 6 moves back toward its stronger Week 10 neighbourhood.

This round will strongly influence the final Week 13 submission. Where Week 12
confirms an improving local direction, the final round can use a very small
exploitation step. Where the result shows a plateau, noise or another boundary
crossing, the final query should test the most informative remaining
alternative rather than simply repeating the current best point.

The main PCA lesson I apply to BBO is therefore not simply dimensionality
reduction. It is the idea of preserving informative structure while removing
redundant movement. As the evaluation budget becomes nearly exhausted, each
query should concentrate on dimensions and directions that the accumulated
evidence suggests matter most while retaining enough exploration to avoid
mistaking a locally dense region for the global optimum.
