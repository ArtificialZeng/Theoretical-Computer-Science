# Research checkpoint — pass 2

Job: c029-vftfast-research-36ff17e1eeb1; 2026-11-02 UTC.
Decision: continue; candidate_kind none; original_status unresolved.
Assigned accumulated pass 2 of at most 3; one remaining pass is subject to
runner enforcement. No counters, scheduling state, failure records, frozen
files or reviews were reset or overwritten. Prior checkpoint is preserved in
evidence/research2-entry-checkpoint.md. Source SHA-256 is unchanged:
45828a099cc88bde52aee6450b298c8b73397e4367d3911585521595f94657b8.
No candidate, audit acceptance, manuscript/PDF, or readiness label is created.

The supplied all-endpoint CLIQUE separator reduction was read critically;
it remains a conditional method barrier, not original construction hardness.
New evidence/research2-history.md strengthens the diagnosis: every private-
internal subdivision with chain lengths L>d can be built by valid length-d
insertions, each with a singleton fault witness and G-F distance exactly d.
Delete the far core endpoint during prefix windows and the initial endpoint
for the final window. Hence merely supplying a valid adaptive geodesic
history does not avoid the barrier. This does NOT prove reachability under
the source's exact fully prescribed scan, or exclude a more disciplined
constructor. New direct BFS tests checked 24,982 insertions / 49,964 distances,
including the two full expanded root graphs; zero failures. Prior exhaustive
root and pass-1 checks were not rerun.

The principal NEW POSITIVE route is evidence/research2-positive-kernel.md.
An explicit Vandermonde exterior-basis DP computes fault-representative lists
of length-d paths per endpoint pair in n^O(1)*(f+d+1)^O(d+1) time. Its support
basis preserves disjointness against remaining extension vertices and f faults;
the protected cut subroutine then supplies an O(r*f)-budget joint separator.
This is established representative-family machinery, not claimed novel alone.

A parameter switch makes that cost usable: for eta=min(delta/2,1/4),
d=floor(sqrt(k)), use the known multiplicative (2d-1) VFT construction when
f>=n^(1/(eta*d)). It already has the frozen size/stretch tradeoff there.
Below that threshold, f^O(d) and d^O(d) are polynomial in n under k<=log(n+2).
DR2020 v2 Theorems 2/9 were explicitly checked: deterministic size
O(d*f^(1-1/d)*n^(1+1/d)), runtime O(m*d*f^(2-1/d)*n^(1+1/d)). The remaining
branch applies source packing to insertion witnesses q=O(r*f), r=O_eta(k),
and the pass-1 pendant-path reduction for all scales. No quantifier is narrowed.

New exact representative-DP tests passed 106,424 disjointness comparisons /
4,024 DP configurations on 110 graphs: all labeled n=2..4 graphs, 18 fixed
masks each at n=5,6, d<=min(n-1,4), all relevant f and endpoints. This does
not verify the complete spanner or the source's long packing argument.
Code and coverage JSON are retained. Current primary versions and comparisons
are in evidence/research2-sources.md; no complete equivalent was found in a
bounded search, which is not a novelty certificate. The full original theorem
and STOC significance are not yet established.

ONE NEXT TEST (final permitted research pass): assemble and adversarially
validate the complete deterministic TWO-BRANCH construction in
research2-positive-kernel.md. Verify the source Theorem 5.4 packing bound for
the representative-list adaptive witness sequence with q=O(r*f), including
pendant scales and uniform constants; implement the complete small-f branch
and exhaustively compare size/stretch against all faults on a bounded domain;
recheck primary literature for this exact parameter-switch combination. This
single end-to-end test can close or refute the proposed full-scope algorithm.
Only after all actual gaps close may a full-resolution claim be proposed.
If that final pass fails, preserve evidence and park; no subsidiary manuscript.
