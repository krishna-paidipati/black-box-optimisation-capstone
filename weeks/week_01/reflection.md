# Week 1 Reflection

For my first round of the BBO challenge, I used a combination of exploration, exploitation and Bayesian optimisation principles rather than applying the same rule to all eight functions. I first examined the initial input and output data for each function, identified the current best observations and considered the information supplied about each function's expected behaviour. I then used surrogate modelling and acquisition-based reasoning, particularly Expected Improvement and uncertainty, to identify promising new query points.

For Function 1, I favoured exploration because the initial outputs provided very little information about the location of narrow peaks. For Functions 2–4, I used a more balanced exploration/exploitation strategy. Function 2 is described as noisy with multiple local optima, so I avoided relying entirely on its current maximum. Functions 3 and 4 provided more structure for surrogate-guided selection.

For Function 5, I used stronger exploitation. Its current best observation was substantially higher than the others, and the supplied description states that the function is typically unimodal. This made local refinement around the promising region more defensible than broad exploration in the first round.

Functions 6–8 became progressively more challenging because dimensionality increased while the observations remained sparse. Function 8 was particularly difficult because even 40 samples provide limited coverage of an eight-dimensional unit hypercube. In such settings, surrogate uncertainty and careful candidate selection become more important than visual inspection.

The additional information that would help most is knowledge of the functions' noise levels, smoothness and effective dimensionality. It would also be useful to know whether some coordinates have little influence on the objective.

In future rounds, I will compare each returned output with the previous best observation and with the surrogate's expectation. Strong improvements will justify increased local exploitation, while poor or surprising outcomes will motivate greater exploration or changes to the surrogate assumptions. Each function will continue to receive its own strategy rather than a fixed acquisition rule throughout the challenge.
