# Datasheet — BBO Capstone Query and Evaluation Dataset

## Motivation
The dataset supports sequential optimisation of eight unknown maximisation
functions under a restricted evaluation budget and preserves the evidence used
at each round.

## Composition
Each record contains a function identifier, input vector, scalar output and
query round. Functions range from 2D to 8D. Initial observations were supplied
by the course; each round adds one query/output pair per function.

Confirmed portal responses are available through **Week 10**. Week 11 queries
have been selected but their outputs are not yet confirmed.

## Collection process
Queries were generated adaptively using Gaussian Processes, acquisition
reasoning, local/global exploration, SVM diagnostics, neural and gradient
diagnostics, feature importance, hyperparameter tuning, structured prompting,
scaling diagnostics, decision tracing and Week 11 clustering diagnostics.

## Preprocessing and uses
Portal inputs use six decimals. Function 1 may be modelled in log-output space
where documented because its positive responses span many orders of magnitude.
Function 3 has produced different outputs for an identical repeated input,
providing evidence of possible evaluation noise or variability.

Intended uses include educational BBO, surrogate analysis, sequential
decision-making and reproducibility. The data should not be treated as complete
coverage, proof of global optimality, causal evidence or a safety-critical
benchmark.

## Distribution and maintenance
Project documentation is maintained in the public repository
`krishna-paidipati/black-box-optimisation-capstone`. Course raw data are not
intentionally redistributed where rights are unclear. I maintain the query and
result history after each processed round.

## Known gaps and biases
Sampling is sparse and increasingly concentrated around strong regions.
Higher-dimensional functions remain poorly covered, and Function 5 contains
many boundary observations. Cluster structure may partly reflect the adaptive
sampling policy rather than intrinsic global structure.
