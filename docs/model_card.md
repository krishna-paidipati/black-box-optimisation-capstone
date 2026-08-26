# Model Card — BBO Sequential Optimisation Approach

## 1. Overview

**Name:** BBO Sequential Surrogate Optimisation Approach  
**Project:** Black-Box Optimisation Capstone  
**Version:** Week 10  
**Task:** Maximisation of eight unknown black-box functions  
**Dimensions:** 2D to 8D

This project implements an iterative optimisation workflow rather than one fixed predictive model. Gaussian Process surrogate modelling and acquisition reasoning form the primary numerical foundation, supplemented by diagnostic models and function-specific heuristics.

## 2. Intended Use

The approach is designed for educational black-box optimisation problems where:

- objective functions are unknown;
- function evaluations are limited or expensive;
- observations accumulate sequentially;
- uncertainty is important;
- exploration must be balanced against exploitation.

It is not intended to establish mathematically guaranteed global optima.

The implementation should not be transferred directly to safety-critical, medical, financial or other high-stakes optimisation tasks without appropriate domain validation, uncertainty analysis and governance.

## 3. Technical Approach and Evolution

### Week 1
I established the initial workflow using exploratory analysis, Gaussian Process surrogate modelling, acquisition-function reasoning and space-filling heuristics.

### Week 2
The first returned outputs allowed the strategy to become function-specific. Exploration and exploitation were adjusted according to observed performance.

### Week 3
RBF soft-margin SVM diagnostics were introduced to examine whether observations could help distinguish relatively high- and low-performance regions.

### Week 4
A compact PyTorch neural-network surrogate and input-gradient analysis were introduced as secondary diagnostics. They did not replace the primary uncertainty-aware optimisation workflow.

### Week 5
Candidate selection was refined using coarse-to-fine Expected Improvement analysis.

### Week 6
Feature-importance diagnostics and feature-guided local refinement were added to investigate which dimensions appeared most influential.

### Week 7
Gaussian Process hyperparameters and modelling assumptions were examined more explicitly as the dataset grew.

### Week 8
Structured prompting was introduced as a decision-support layer. LLM reasoning was deliberately separated from the numerical optimiser and was not treated as ground truth.

### Week 9
Scaling-aware diagnostics examined best-so-far improvement and diminishing returns. Search effort could therefore shift between local exploitation and broader exploration according to recent evidence.

### Week 10
Transparency and interpretability became explicit components of the implementation. Each function's proposed query records its search intent, empirical evidence and underlying assumption.

## 4. Performance

Performance is assessed primarily through:

- objective value returned by the portal;
- best objective value observed for each function;
- improvement relative to previous rounds;
- best-so-far progression across evaluations.

Because all eight functions are maximisation problems, larger objective values represent better observed performance.

Confirmed Week 9 outputs were:

| Function | Week 9 output |
|---|---:|
| Function 1 | 0.0000021011876927792272 |
| Function 2 | 0.5284601272802701 |
| Function 3 | -0.014269124103300751 |
| Function 4 | 0.44938062714098637 |
| Function 5 | 4440.481244076172 |
| Function 6 | -0.3692565596073361 |
| Function 7 | 1.6972383579136083 |
| Function 8 | 9.9429751999995 |

These values should not all be interpreted as the overall best values obtained during the project because some functions performed better in earlier rounds.

Week 10 queries have been submitted, but their outputs were not available when this model card was prepared.

## 5. Assumptions and Limitations

A central assumption is that observations near previously successful points provide useful information about neighbouring regions.

This assumption can fail for discontinuous, noisy or strongly multimodal functions.

Additional limitations include:

- a very small evaluation budget;
- increasingly sparse coverage as dimensionality increases;
- exploitation bias around successful regions;
- sensitivity of surrogate models to kernel and hyperparameter choices;
- possible overconfidence in sparsely sampled regions;
- inability to verify whether a discovered maximum is global;
- limited evidence for estimating complex feature interactions.

Diagnostic models are therefore treated as decision-support tools rather than proof of the hidden function structure.

## 6. Transparency and Reproducibility

The repository preserves the optimisation process round by round.

Weekly directories record confirmed preceding outputs, selected queries, implementation notes and reflections. Later iterations additionally record the reasoning and assumptions behind query selection.

This makes it possible to distinguish:

1. observed evidence;
2. model-generated diagnostics;
3. heuristic judgement;
4. final submitted queries.

This separation is important because reproducibility requires more than recording the final objective values. It requires documenting how each decision was reached.

## 7. Ethical Considerations

The synthetic BBO challenge does not directly involve personal or sensitive data. Nevertheless, the project demonstrates practices relevant to responsible ML.

Transparent documentation reduces the risk of presenting model predictions as facts, hiding unsuccessful experiments or overstating optimisation performance.

In a real-world adaptation, additional considerations would depend on the application and could include fairness, privacy, safety, environmental cost, human oversight and the consequences of optimisation errors.

## 8. Current Status

This model card describes the implementation through the Week 10 submission.

It should be treated as a living document and updated when new portal outputs or material changes to the optimisation strategy are introduced.
