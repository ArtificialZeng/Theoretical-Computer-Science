# Research pass 2: progress record

Job: c037-msthalf-research-d9c4fc8e3237; pass 2 of at most 3.
Original remains unresolved; no candidate/manuscript/PDF.

Assigned kernel: weighted-order inequality (K) for arbitrary ultrametrics,
nonuniform q-weights, arbitrary hierarchy depth and heights. Previous exact
uniform-weight/two-level checks will not be rerun as new evidence.

Proof/disproof split: seek a hierarchy-sensitive interval charging proof;
attack it on balanced, comb and unbalanced hierarchies with unequal heights
and nonuniform order weights. A counterexample to this sufficient kernel
would not negate the immutable all-algorithm source question.

Current observations: one-scale crossing control is inherited from pass 1.
Applying it separately and integrating W/s can add log(aspect ratio), so
that argument is insufficient. In an ultrametric, a connected graph of
true-distance-at-most-s edges lies within one s-cluster; this closure has
no general-metric analogue. No complete multiscale charge established yet.

Primary source refresh: https://arxiv.org/abs/2610.40594 inspected fresh;
only v1 (2026-10-29) appears. Primary full text and Lemma 3.2 inspected;
quarter upper and half lower bounds persist. Exact-title/id searches did
not identify a full-gap resolution. This is bounded search, not exhaustive
open-status or novelty certification.

Exact finite attack completed: ultrametric_nonuniform_check.py checked 180
sampled hierarchy/order/rectangle-density configurations, n in 8,12,16,24,32;
balanced, comb and random merge shapes; height increments 1, {1,2,7}, and
{1,3,27,81}; nonuniform integer weights reduced by two coordinate sweeps.
17,224 exact feasibility calls, then a separate direct rectangle-density
calculation for every saved witness. Largest cost/[r(W+MST)] = 1053/1177.
This is no counterexample and no optimization/completeness certificate.
All metrics and optimized weights are saved in ultrametric-nonuniform-check.json.
