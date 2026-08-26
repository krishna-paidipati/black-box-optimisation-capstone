# Datasheet — BBO Capstone Query and Evaluation Dataset

## 1. Motivation

This dataset was developed as part of my Black-Box Optimisation (BBO) capstone project. The challenge consists of eight unknown objective functions with increasing dimensionality. Each function is a maximisation problem.

The dataset supports sequential optimisation under a restricted evaluation budget. Its purpose is to preserve the evidence available at each round, support surrogate modelling and acquisition-based query selection, and provide a reproducible record of how the optimisation strategy evolved.

## 2. Composition

The project contains observations for eight black-box functions with input dimensions ranging from 2 to 8.

Each observation consists of:

- a function identifier;
- an input vector x;
- one scalar objective value y;
- the round in which the query was submitted.

The course supplied the initial observations. Each subsequent round adds one new query and one returned objective value per function.

At the time of this datasheet, confirmed portal responses are available through Week 9. Week 10 queries have been selected and submitted, but their outputs are not yet included as confirmed observations.

All input coordinates lie within the challenge's unit-hypercube domain. Portal submissions are stored using six-decimal coordinates.

The dataset is intentionally sparse, particularly for the higher-dimensional functions. Later observations are also concentrated around promising regions rather than being uniformly distributed.

## 3. Collection Process

The initial observations were supplied by the capstone challenge.

Additional observations were collected sequentially. Only one new query per function could be submitted in each round. The corresponding objective value was returned by the capstone portal and incorporated into the next round's analysis.

The query strategy evolved during the project and included:

- initial space exploration;
- Gaussian Process surrogate modelling;
- Expected Improvement and uncertainty-aware reasoning;
- function-specific exploration/exploitation decisions;
- SVM diagnostics for high- and low-performance regions;
- neural-network and gradient diagnostics;
- feature-importance analysis;
- coarse-to-fine and local candidate refinement;
- hyperparameter tuning;
- structured prompt decision support;
- scaling and diminishing-return diagnostics;
- explicit decision tracing and interpretability.

Queries were therefore generated adaptively rather than through independent random sampling.

## 4. Preprocessing and Uses

Inputs are represented numerically and portal queries are standardised to the required six-decimal format.

For most functions, objective values are modelled directly. Function 1 has produced extremely small positive values across parts of the search, so a logarithmic transformation may be used for numerical modelling where explicitly documented.

No synthetic portal responses are added to the historical dataset. Returned objective values are stored as received.

### Intended uses

The dataset is intended for:

- black-box optimisation experiments;
- surrogate-model evaluation;
- exploration/exploitation analysis;
- sequential decision-making demonstrations;
- educational analysis of optimisation under limited observations;
- reproducibility of this capstone project.

### Inappropriate uses

The dataset should not be interpreted as:

- a comprehensive sample of the complete function surfaces;
- proof that a global optimum has been found;
- a benchmark for safety-critical optimisation;
- representative real-world population data;
- evidence for causal relationships between individual coordinates and output.

## 5. Distribution and Maintenance

The project documentation and permitted derived artefacts are maintained in the public GitHub repository `krishna-paidipati/black-box-optimisation-capstone`.

Course-provided raw data is not intentionally redistributed where redistribution rights have not been established. The repository documents how the local raw data is expected to be organised.

I maintain the project repository and update the query/result history after each confirmed capstone round.

## 6. Known Gaps and Biases

The primary limitation is sparse sampling.

As optimisation progressed, queries increasingly concentrated around high-performing regions. This creates exploitation bias and leaves substantial parts of the search space unexplored.

The problem becomes increasingly important from Functions 6 to 8 because dimensionality grows while the evaluation budget remains small.

Boundary-heavy observations, particularly for Function 5, also provide limited information about interactions within the interior of the search space.

These limitations are documented so that surrogate predictions are not mistaken for complete knowledge of the hidden functions.
