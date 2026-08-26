# Week 8 Reflection — Prompting and Decoding Strategies

The submitted reflection treats structured prompting as decision support around
the existing numerical BBO workflow rather than claiming that an LLM replaces
the Gaussian Process/acquisition strategy.

Key design choices were structured function-specific context, conservative
decoding for reproducibility, strict six-decimal output constraints, separation
of the eight functions, and reliance on observed numerical evidence to guard
against hallucinated objective values or hidden-function assumptions.
