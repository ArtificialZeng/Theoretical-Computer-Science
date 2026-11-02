# Precise original problem and triage reading

Job: c034-group3sum-triage-7cb7e5c1a226. Phase: TRIAGE.
The immutable source.md, not this interpretation, controls scope.
Source SHA256: f3507a3e5b20d6707750b7e703d5d1c0764d4d5b13ef6b7a4f0001d940c8e8cf.

## Quantified target

For every fixed integer M >= 2, construct one uniform classical algorithm A_M
and a constant delta_M > 0 such that, for every fixed real c > 0, every integer
n >= 2, every finite abelian group G = product_i Z_(m_i) with m_i >= 2,
m_i dividing M and |G| <= n^c, and every three lists S_i of at most n elements
of G, A_M returns x_i in S_i with x_1+x_2+x_3=0, or correctly reports absence,
in O_(M,c)(n^(2-delta_M) polylog(n)) total charged operations. Empty lists are
negative instances; duplicates can be removed. The bounded n cases are constant
work for fixed parameters. delta_M must be independent of c and n.

The input contains the cyclic factors and residue vectors, not an arbitrary
Cayley table or a black-box group. The word RAM has Theta(log n)-bit words;
arithmetic on longer encodings and every reduction, count, hash construction,
query, scan and witness recovery are charged. There are O_(M,c)(log n) factors.
A bit-operation implementation may pay polylogarithmic overhead. Randomized
algorithms must have a stated bounded error on each fixed input and an honest
total running-time cap. A deterministic algorithm suffices.

The target includes all mixed-prime and higher prime-power factors. An
injective homomorphism sends coordinate x in Z_m to (M/m)x in Z_M, preserving
and reflecting zero sums. Its ambient order is at most |G|^(log_2 M), so this
normalization preserves a polynomial order bound for fixed M; it does not
solve 3SUM. A Z_8-only theorem remains partial. No new unproved counting or
matrix oracle may be substituted for an algorithm.

## Primary position and nearest prior

Ruhollah Majdoddin, arXiv:2610.17420v1, Section 19 Model (printed p.66),
Theorem 19.17 and Section 19.6 (pp.76-82), Open Problem 19.26 (pp.82-83).
The frozen primary PDF and its text are in intake/primary/.

Theorem 19.17 gives the full exponent-dividing-p^2 class for each fixed prime,
conditionally on its specified sparse-triangle primitive; Corollary 19.25
instantiates a prior primitive. Its explicit embedding already includes
Z_4^d x F_2^d. That example in the subsequent open-problem list is erroneous;
the general bounded-exponent target itself is unambiguous and remains larger.
Theorem 19.11 and Proposition 19.10 cover elementary groups and boundedly many
cyclic factors. The source's proposed layer induction is prior, not our novelty.

The precise proposed delta is a fully charged algorithm for every fixed M,
with positive saving independent of c, beyond these existing scopes. A
successful generic layer-composition method could also extend the algorithms
for representable coordinatewise relations (Remark 20.6). This is a plausible
substantive payoff, not a completed contribution or venue-readiness assessment.

## Admission and first research test

Source status: open-supported in the inspected primary version, with bounded
current searches finding no full resolution. Suitability: admit one bounded
research pass; no theorem or candidate exists. See evidence/triage.md.

First test: formulate and attempt a generic extension invariant for the source's
light/heavy algorithm, checking the first new p^3 layer with p=2 diagnostically.
For each branch account for the number of blocks and compatible class triples,
all hash-counting groups and scans, and witnesses. Seek polylogarithmically many
calls whose aggregate costs are O_M(n^(2-delta_M) polylog(n)); each source-style
call needs middle group size D, O_M(n/sigma) blocks, Z(pi)=O_M(sigma*n^2), and
F=O_M(sigma*n^2/D). Derive computable potentials for every nonzero valuation
layer and carry-dependent target. Test whether the invariant composes across
both prime-power extensions and CRT factors, without hiding enumeration costs.
Failure of these sufficient conditions refutes that proposed induction, not
the original algorithm-existence statement. Keep the full target unchanged.
