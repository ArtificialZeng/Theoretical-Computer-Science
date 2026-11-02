# Pass 1 initial exact result

Job c025-incdec-research-393eb62fad16. Entry clock 2026-11-01 23:05:54 UTC;
dispatch 23:03:51; main-test cutoff 23:20:50.999992; finalization cutoff
23:23:50.999990. No agents or background workers used.

`python3 code/chain_dp.py` completed 255 exact rational tests: 35 scaled
Proposition 11 curvature-one cases (n=2..8, g scales 1/4,1/2,1,2,4), 20
Proposition 19 cases (k=2,3, the same scales and both function roles), and
200 seeded weighted coverage pairs (n=1..8, universe <=12, weights 1..5,
including zero functions). Every tested instance has a complete 2-good chain.
195 instances also have full permutation enumeration at n<=6, agreeing with
the reachability result. All elementary monotonicity/submodularity inequalities
of both tabulated functions were checked exactly. These tests are exhaustive
over subsets/permutations of their explicit inputs, not over function classes.

Reachable local dead ends occur in 10 inputs, including scaled Prop.11 at n=4
and a random n=3 input. Thus every-reachable-good-set extension is false.
This is a diagnostic against an intermediate claim, not the original problem.
Full values, thresholds, reachability, backward viability, parent pointers and
complete chain certificates are in chain-tables.json; counts/hash in
chain-summary.json. The original remains unresolved; no candidate or PDF.

Implementation scope detail: the Prop.19 construction uses distinct labeled
items A_k and B_k even though their coverage sets coincide. This is a valid
coverage valuation and is the labeled reading needed for the source's 2k-item
construction and distinct modular values. The source family's universe has
k^k atoms (27 for k=3); the random-universe <=12 cap does not apply to it.

Next immediate work within this pass: verify a minimal local-dead-end witness
without using DP, then test a changed constructive invariant. Preserve every
failed method as diagnostic only. Full theorem and polynomial extraction both
remain missing.
