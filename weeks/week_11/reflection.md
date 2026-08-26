# Week 11 Reflection — Clustering and Local Structure

## 1. How have patterns in your past queries influenced your latest choices?

My Week 11 strategy uses recurring high-performing regions rather than treating
each observation independently. Function 1 has improved through repeated moves
towards lower coordinates, while Function 7 improved from around 1.60 to 1.70
and then 1.745. I therefore continued local refinement for these functions.
Functions 2, 5, 6 and 8 also improved in Week 10, so I reduced the next step
rather than starting unrelated global searches.

## 2. Have you identified clusters or recurring promising regions?

Yes. I treat a cluster as a neighbourhood containing nearby observations with
relatively strong outputs. Function 7 has a clear high-performing local region,
while Function 8 has a stable region producing values around 9.94–9.95.
Function 5 shows a boundary cluster where x2, x3 and x4 repeatedly perform
strongly near one. These clusters indicate promising regions but do not prove
global optimality.

## 3. Which strategies have proven less effective?

Large moves away from established regions sometimes reduced performance.
Function 8, for example, weakened after a larger move and recovered after
returning locally. Function 3 also showed that the same input can return
different outputs, so I no longer treat every observation as exact evidence of
a deterministic surface.

## 4. How do these refinements parallel clustering algorithms?

I use input-space distance to identify neighbourhoods and objective values to
judge whether those neighbourhoods matter. Repeated strong observations raise
confidence in a region; isolated results receive less weight. Unlike ordinary
unsupervised clustering, objective performance directly affects how I interpret
each cluster.

## 5. What might plotted trends show?

Low-dimensional plots should show concentrations around promising regions and
directional trajectories such as Function 1. Higher-dimensional projections may
show local concentrations but can hide interactions. In future rounds I would
compare cluster membership, nearest-neighbour distance and objective
performance: improving clusters justify tighter refinement, while plateaus or
inconsistent clusters justify more exploration.
