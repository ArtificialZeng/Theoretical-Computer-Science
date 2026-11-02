# Uniform parameters, time, faults, and guarantee

For every fixed rational delta in (0,1), seek constants C_delta,b_delta and
an algorithm polynomial in the explicit input length (its polynomial exponent
may depend on delta). On EVERY undirected unweighted simple n-vertex input,
integers k>=1 and f>=0, return H subset G with at most
C_delta*(f+1)^(1+delta)*n^(1+1/k)*log(n+2)^b_delta edges, such that for ALL
F subset V of size<=f and ALL u,v outside F with finite G-F distance,

 dist_(H-F)(u,v) <= C_delta*sqrt(k)*dist_(G-F)(u,v)+C_delta*k.

A deterministic procedure suffices. A randomized procedure must have the
whole simultaneous size/stretch guarantee with probability>=1-(n+2)^(-3)
on each input, with polynomial running time on every run (capping a bounded
expected-time algorithm is allowed only with its actual proof). No external
failure-query oracle or readable output history is free. Source asks a
time improvement; the complete target here is uniform polynomial time, not
just polynomial for each fixed k or f. Favorable constants may depend on
delta but not on n,f,k. Proving every rational delta suffices for real delta
by monotonicity with a smaller rational exponent.

Trivial n<=2 and f=0 cases can use known constructions or G. Cap f at n-2
for surviving pairs. k>ceil(ln(n+2)) can use that cap, whose n^(1+1/k)
factor is O(n), with smaller stretch/additive terms. This charges every
poly(k) factor as polylogn, but does not absorb a worse polynomial f exponent.
No weighted/directed/hypergraph faults, emulator edges, extra failure budget,
or omitted fault sets change the target. Classical (2k-1,0) VFT algorithms
are prior, since their multiplicative stretch is not O(sqrt(k)).

First decisive positive test: reconstruct the path-greedy separation task
in source Section2.3 and its DR2020/BDR2021 relaxed fault-cut tests. Determine
whether short-path color-coding or representative families can select the
violating path without n^sqrt(k) enumeration while preserving the source
packing/size analysis. Produce a complete separation lemma or its precise
method failure; do not merely replace the hard exact length-bounded-cut
oracle and claim all path enumeration disappeared. A length-bounded-cut
hardness or failure of one greedy verifier does not rule out all algorithms
for the frozen tradeoff. A negative original answer needs appropriate
complexity hardness for the full uniform construction problem.

## Triage clarification, 2026-11-02

This is a uniform algorithmic existence question: for each fixed delta there
must be one algorithm for all graph inputs and all f,k; there is no restriction
to fixed k or fixed f. An original negative answer must exclude the full
construction target under explicitly stated complexity assumptions, rather than
refute an intermediate separation lemma. The permitted randomization convention
above specifies one sufficient success model; it is not attributed verbatim to
the source's informal running-time challenge. The original source.md is unchanged.

For boundary handling, using G is justified only where its edge count satisfies
the stated bound (for example k=1 or n<=2). In particular, f=0 alone does not
justify returning a dense G; use a qualifying nonfaulty spanner instead. For
n>=2, cap f at n-2 because every surviving distinct pair excludes its endpoints;
n<=1 is vacuous. For k>K=ceil(ln(n+2)), a construction at K has smaller stretch
parameters and n^(1+1/K)<=e*n, so a constant loss suffices. Constants cannot
depend on f or k. These are reductions, not a resolution of the main target.

Nearest verified primary statements are Parter--Popova--Tzalik, arXiv:2610.33934v1,
Theorem 1.4 and printed pp.4--5 (the target size/stretch with inefficient path
enumeration), and Corollary 3.20 (different polynomial fault overhead).
Dinitz--Robelle, arXiv:2002.10889v2, Theorems 2 and 4, give a polynomial
multiplicative construction and a length-bounded-cut gap test. Bodwin--Dinitz--
Robelle, arXiv:2007.08401v3, Theorem 1.3, gives optimal-size polynomial-time
purely multiplicative spanners. None of these statements supplies the frozen
uniform O(sqrt(k)),O(k) tradeoff with f^(1+delta) dependence.

A concrete first research test is the following *unproved sufficient separator*.
Given H subset G, d<=floor(sqrt(k)), r=O_delta(k), and f>=1, either output a
length-d path P in G and F disjoint from V(P) with |F|<=c*r*f and
dist_(H-F)(endpoints(P))>r, or correctly certify that no such pair exists with
|F|<=f. Seek running time 2^O(d)*poly(n,f,r), with absolute constants in the
exponents (or a polynomial bound outright). Because k can be capped at O(log n),
this time would be polynomial. The gap permits a polylogarithmic fault inflation,
which would preserve the desired size expression if the source's size proof
applies to the resulting sequence with fault parameter c*r*f. That transfer and
all scales required by Appendix B must also be proved. Color-coding alone does
not establish this joint property. A failure of this sufficient separator is
only a route diagnosis. Details and source-status limits are in
evidence/triage-sources.md.

## Research pass 1: refined sufficient separator, original scope unchanged

The original question and all its quantifiers remain unchanged. The earlier
all-path separator is sufficient but stronger than necessary. It is enough to
certify absence of pairs with |F|<=f, dist_(G-F)(x,y)=d and
dist_(H-F)(x,y)>r; a returned witness may still be ANY simple length-d path P
with a compatible cut C of size O(r*f). Iterating such a separator gives an
f-VFT d->r spanner. The conditional packing-transfer and pendant-path proofs
for all Appendix B scales are in evidence/research1-separator.md, Section 2.
They apply the cited source analysis and leave the separator unproved.

The protected fixed-path cut subroutine is proved there and exactly tested.
An H-oblivious explicit list of exact-length paths can require
binomial(f+d-1,d-1) different supports, even with arbitrary output fault
inflation. This diagnoses that particular path-compression route. Its witness
is nongeodesic when d>=3, so it does not rule out the refined separator.
Shortest witnesses must be induced paths in G, but generic induced-path
detection itself has conditional hardness comparisons; no black-box shortcut
or original lower bound follows from that fact.

Next bounded test: prove or diagnose an H-dependent shortest-violation gap
separator with output budget O(r*f), complete path protection, and time
2^O(r+d*log(d+2))*poly(n,f,r) with fixed polynomial exponents. Here
d=floor(sqrt(k)), r=O_delta(k), and k<=ceil(ln(n+2)). This time would be uniform
polynomial and would preserve the original size bound via the recorded
reduction. A counterexample must defeat the proposed rule on a genuine
shortest-distance-d violation; the nongeodesic list obstruction does not do so.

## Research pass 2: parameter-dependent positive route

Original source and quantifiers are unchanged. A valid adaptive geodesic
singleton-fault history alone does not avoid the root separator barrier
(evidence/research2-history.md). This is a method diagnosis, not original
hardness. A different sufficient separator in time
n^O(1)*(f+d+1)^O(d+1) is now constructed using Vandermonde exterior bases
and fault-representative path DP. Its f dependence is essential.

For eta=min(delta/2,1/4), d=floor(sqrt(k)), split at f>=n^(1/(eta*d)).
Above this threshold, known polynomial multiplicative (2d-1)-spanners
already meet the frozen size/stretch requirements. Below it, the new
representative separator's f^O(d) cost is polynomial. The conditional size
transfer remains the source witness-sequence packing bound with q=O(r*f),
and the previously recorded pendant-path all-scale reduction. Details and
precise unresolved final validation obligations are in
evidence/research2-positive-kernel.md. This is a promising full-scope
algorithm program, not yet a candidate or certified resolution.

## Research pass 3: proposed complete resolution, subject to fresh review

The immutable source and every original quantifier remain unchanged.
evidence/research3-resolution.md gives the proposed complete deterministic
algorithm: exact fault-representative path DP in the small-f regime, DR2020
multiplicative spanners in the complementary large-f regime, explicit PPT
witness-sequence packing transfer, and all pendant scales. It includes f=0,
bounded k, binary-encoded large f/k, and simultaneous surviving-pair guarantees.
The computational cap ceil(log_2(n+2)) differs harmlessly from the possible
natural-log cap above; its final size loss is at most two.

New full-construction and exact parameter checks are recorded in
evidence/research3-full-checks.json and
evidence/research3-parameter-checks.json. They verify the stated finite
domains, not the infinite theorem or novelty. The researcher proposes
resolution-paper / proved in claim.json, requesting a fresh audit; no
acceptance or STOC assessment is prepopulated. Primary comparisons and the
proposed innovation are in evidence/research3-sources.md. Earlier unresolved
statuses describe the actual earlier passes and remain preserved.
