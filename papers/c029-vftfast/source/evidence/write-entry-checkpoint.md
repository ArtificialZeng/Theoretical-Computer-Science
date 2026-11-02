# Research checkpoint — pass 3 (final permitted research pass)

Job: c029-vftfast-research-9df2f29ab673; 2026-11-02 UTC.
Decision: candidate; kind resolution-paper; proposed original_status proved.
This requests fresh review; no acceptance, STOC assessment, manuscript/PDF or
readiness label is created. Assigned accumulated pass 3 of at most 3. No
counters, usage entries, scheduling, earlier evidence or reviews were reset.
The prior checkpoint is preserved in evidence/research3-entry-checkpoint.md.
Immutable source SHA-256 remains
45828a099cc88bde52aee6450b298c8b73397e4367d3911585521595f94657b8.

The NEW complete argument is evidence/research3-resolution.md. It combines
exact Vandermonde exterior-basis path representatives with DR2020's known
multiplicative constructor. For eta=min(delta/2,1/4), d=floor(sqrt k), use
DR when f^(eta*d)>=n. In the complementary regime the representative DP's
(f+d+1)^O(d+1) cost is uniformly polynomial after the logarithmic k cap.
The representative list is scanned once with protected gap-cut tests.
Every rejection excludes any original-fault-budget protected cut; every
insertion has an actual compatible witness of size <=(r-1)f.

The previously pending PPT packing transfer is now written explicitly for
arbitrary insertion-witness sequences. Its analytical path-system induction
requires no omitted paths or endpoint scan order. The center probability is
tracked before suppressing factors: 10C'sq/D <= (5/(6s^2)) q^(-eta) N^(-1/k).
Thus its center-set upper bound has only polylogarithmic positive prefactors,
including when the probability is capped at one. The robust CLFT theorem
then gives q exponent <=1 and N exponent <=1 for the global insertions.
The proof credits PPT's park/spread/sunflower theorems as dependencies; it
does not independently certify them or assert greedy-output containment.
Pendant constructions cover every shorter distance, with the original fault
set unchanged. Boundary cases include f=0 via counting budget q=1, n<=2,
k<=3 via DR with max(1,f), and large binary f/k by valid caps. Constants
have no dependence on f or k. The algorithm is deterministic on every run.

NEW exact tests: 3,160 complete mixed constructions on every labeled graph
of n=2,3,4 and 10 fixed masks each at n=5,6; d<=3, f<=min(2,n-2), radii
d,d+1,2d+1,48d^2. Largest pendant graph N=18. Results: 6,248 d-to-r runs,
23,909 insertion-witness checks, 809,892 exact rejection-cut checks,
560,240 d-to-r and 57,856 final mixed-distance comparisons, all passing.
DR implementation: 1,848 runs / 33,763 comparisons, all passing. Separately
20,465 rational parameter cases, k=4..4096 and five eta values, passed
seven packing-constant/exponent inequalities each. These finite observations
do not establish the infinite theorem, asymptotic size or novelty; those
claims rest on the supplied proof and exact primary dependencies.

Current primary comparison is evidence/research3-sources.md. PPT v1 still
lists its running-time improvement as open. No equivalent combined method
was identified in bounded current searches; that is not priority certification.
The proposed contribution is the full uniform polynomial-time realization
of the immutable tradeoff, not a new exterior-algebra primitive or improved
size/stretch bound. Its independent innovation and theoretical significance
must be critically judged by the fresh referee. No venue decision is inferred.
Prior separator/history barriers remain limited method diagnostics. The new
f-dependent separator does not contradict their arbitrary-f FPT obstruction.

Known remaining mathematical gaps in the proposed proof: none identified
by this researcher. This is not a truth certificate. One decisive NEXT TEST:
fresh referee review of the frozen original-scope claim, especially Section 4's
packing transfer and positive uniform factors, every parameter/boundary case,
and whether the combined algorithm is new and substantively nonroutine versus
PPT, DR and representative-family literature. Require the actual separate
innovation/STOC assessment records before any accepted writing phase. No
additional research pass is requested or authorized by this checkpoint.
