# Technical Foundations and Design Justification

## Current optimisation architecture

The Stage 2 Black-Box Optimisation (BBO) capstone contains eight unknown
maximisation functions with input dimensionality increasing from 2D to 8D.
Only a small number of objective evaluations are available, so each weekly
query must use the accumulated evidence efficiently.

The project's primary optimisation architecture is:

1. reconstruct all observations available before the current weekly query;
2. fit a Gaussian Process (GP) surrogate to each function;
3. use predictive mean and uncertainty through acquisition functions such as
   Expected Improvement (EI) and, where useful, Upper Confidence Bound (UCB);
4. compare acquisition recommendations with the best observed regions;
5. use secondary models only as diagnostics when they add information that the
   GP alone does not provide;
6. store the exact submitted query separately from exploratory model outputs so
   that the repository remains an accurate historical record.

This architecture is appropriate for the capstone because objective evaluations
are scarce and the underlying response surfaces are unknown. A GP is
particularly useful because it provides both a prediction and an uncertainty
estimate, allowing the search to balance exploitation of promising regions with
exploration of uncertain regions.

## Research foundations

### Efficient Global Optimization

Jones, Schonlau and Welch (1998), *Efficient Global Optimization of Expensive
Black-Box Functions*, is the principal research foundation for this project.
The paper addresses optimisation when objective evaluations are expensive or
severely limited and develops a response-surface approach for deciding where to
evaluate next.

That setting closely matches this capstone: the hidden functions cannot be
evaluated freely, and only one new query per function is submitted in each
round. The project's use of a surrogate plus Expected Improvement therefore
follows an established sequential black-box optimisation principle rather than
blind or exhaustive search.

### Practical Bayesian optimisation

Snoek, Larochelle and Adams (2012), *Practical Bayesian Optimization of Machine
Learning Algorithms*, provides a second important foundation. The work models
an unknown objective with a Gaussian Process and shows that GP design choices,
including kernels and hyperparameter treatment, can materially affect
optimisation performance.

This supports the project's decision to keep the GP as the primary
uncertainty-aware surrogate while treating more flexible models as supporting
diagnostics, particularly while the number of observations remains small.

## Implemented supporting methods

The weekly strategy has deliberately evolved without claiming that every method
introduced by the programme is equally suitable for the data.

- **Gaussian Process regression** is the primary surrogate.
- **Expected Improvement** is the main acquisition mechanism for combining
  predicted performance with uncertainty.
- **UCB** has been used as an additional acquisition diagnostic.
- **RBF SVM analysis** was introduced in Week 3 to examine high- versus
  low-performing regions.
- **PyTorch neural-network ensembles and input gradients** were introduced in
  Week 4 as secondary non-linear and sensitivity diagnostics. They did not
  replace the GP because the available data are still small.
- **Coarse-to-fine GP refinement** was used in Week 5 to concentrate candidate
  generation around promising regions without abandoning uncertainty-aware
  ranking.
- **Extra Trees feature importance** was added in Week 6 to support
  feature-guided, multi-resolution refinement. This translated the module's
  hierarchical-refinement idea into a method appropriate for tabular BBO data;
  a CNN was not fitted because these observations are not image or spatial
  tensors.

## Software choices

### NumPy

NumPy is used for array operations, candidate generation, reproducible random
sampling and manipulation of the accumulated observations. It provides a
lightweight numerical foundation for the project.

### scikit-learn

scikit-learn is central to the current approach because it provides
`GaussianProcessRegressor`, kernel implementations, SVMs and Extra Trees within
a consistent API. `GaussianProcessRegressor` can return predictive standard
deviations, which are required by the acquisition functions used in this
project.

For the present capstone scale, scikit-learn is preferable to introducing a
larger Bayesian-optimisation framework because the project intentionally keeps
the acquisition logic explicit and inspectable.

### PyTorch

PyTorch is used only where neural-network functionality is genuinely relevant:
the Week 4 neural surrogate ensemble and backpropagation-based input-gradient
diagnostics. It is not the primary optimisation framework.

## Reproducibility and repository design

Each weekly directory is intended to preserve the state of the project at that
round. The standard pattern is:

```text
weeks/week_XX/
├── README.md
├── queries.json
├── reflection.md
├── run_week_XX.py
└── week_previous_outputs.json
```

Specialised implementation modules are retained alongside the runner when
needed, for example `neural_surrogate.py`, `coarse_to_fine.py` and
`feature_guided_refinement.py`.

The `queries.json` file is the authoritative record of the portal submission.
Re-running a later or refined model is not treated as evidence that the model
originally generated a historical query. This separation is intentional and
keeps the project documentation reproducible and defensible.

## Current limitations

The project has very few observations relative to the complexity that an
unknown non-linear response surface may contain. Consequently:

- GP kernel estimates can be sensitive to individual observations;
- high-dimensional functions remain difficult with such small samples;
- neural networks can overfit easily;
- feature-importance estimates should be interpreted as diagnostics rather than
  causal effects;
- a high acquisition score does not guarantee a high black-box response.

These limitations are why model complexity is being increased cautiously.

## Planned technical investigation

As additional weekly observations become available, useful extensions include:

1. comparing EI, UCB and Probability of Improvement under the same historical
   data;
2. evaluating kernel sensitivity and GP calibration;
3. examining automatic relevance determination or other dimension-sensitive
   kernels for the higher-dimensional functions;
4. comparing local refinement against deliberately exploratory candidates;
5. tracking regret-style and best-so-far performance across rounds;
6. testing whether secondary surrogate agreement provides a useful query
   confidence diagnostic.

The objective is not to add complexity for its own sake. New methods should be
introduced only when they address a limitation visible in the accumulated BBO
evidence.

## References

1. Jones, D. R., Schonlau, M., & Welch, W. J. (1998). *Efficient Global
   Optimization of Expensive Black-Box Functions*. Journal of Global
   Optimization, 13, 455–492. DOI: 10.1023/A:1008306431147.

2. Snoek, J., Larochelle, H., & Adams, R. P. (2012). *Practical Bayesian
   Optimization of Machine Learning Algorithms*. Advances in Neural Information
   Processing Systems 25.

3. scikit-learn documentation. *Gaussian Processes*. Used as the implementation
   reference for `GaussianProcessRegressor` and kernel behaviour.
