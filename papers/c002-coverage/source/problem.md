# Precise frozen problem

Job: `c002-coverage-triage-beb2748f534b` (triage), 2026-11-01 Asia/Shanghai.
Immutable input: `source.md`, SHA-256
`b79ed29f77420ec62a957e727b934deb6b9435b41ed86deaa2c8d77c01b66f9d`.

For every positive integer n,m,t and integer k>=2, take finite feature-index
sets U_i, i in [m]. Each tagged occurrence (i,u), u in U_i, has a nonempty
incidence subset S_(i,u) of [n]. The hypothesis is

    for every j in [n], sum_i sum_(u in U_i) 1[j in S_(i,u)] <= t.

Equal incidence subsets at distinct tags remain distinct in this sum, even
within one function. Empty occurrences may be discarded. Define, for every
T subseteq [n],

    f_i(T) = sum_(u in U_i) 1[S_(i,u) intersects T].

A coloring is an arbitrary map chi:[n]->[k]; empty color classes are allowed.
Put T_c=chi^(-1)(c) and

    disc_chi(F,k) = max_(i in [m], c,c' in [k]) |f_i(T_c)-f_i(T_c')|.

The question is whether there exists ONE fixed polynomial P in two variables
such that, for EVERY such n,m,t,k and incidence family, SOME chi satisfies
disc_chi(F,k)<=P(t,k). P must be independent of n,m, the number of occurrences,
and their sizes. This is an existence question; an algorithm for explicitly
listed incidences would strengthen a positive answer. A negative answer must
exclude every polynomial, not just one proposed bound. No restriction on
rank, t, k, or the incidence family is part of the frozen target.

## Source, normalization, and present status

Nearest inspected result: Avila, Rohwedder, Wennmann, *Non-Additive
Discrepancy: Coverage Functions in a Beck-Fiala Setting*, ESA 2026,
DOI 10.4230/LIPIcs.ESA.2026.139, Theorem 3 and Definition 4, printed p.139:4;
Section 1.3, printed p.139:5, discusses removing the logarithmic size factor
from O(sqrt(t^3 k) log(ntk)). Current arXiv landing page still identifies v3
(2026-07-01); the official proceedings paper was published 2026-08-25.
The frozen question permits worse polynomial t,k dependence than deleting
that logarithm while retaining the source's exponents.

Definition 4's set-union notation could be read as deduplicating equal
incidence subsets. Here the explicit covering-universe interpretation in
source.md controls: occurrences are tagged. The paper's singleton lower
bound and classical additive specialization support this reading. The
literal deduplicated model would be a different problem. Arbitrary feature
weights, weaker influence-counted sparsity, and arbitrary Lipschitz functions
(including Hollender et al., Question 14) are outside the target.

Source status at triage: **open-supported direction**, with the precise
qualitative formulation frozen by this project. Bounded current searches
found no inspected equivalent size-independent bound; this is not priority
certification or proof that no such result exists. See the dated triage
evidence record for sources, searches, and access limits.

## Proposed delta and decisive test

Nearest prior result X is the above logarithmic bound, together with its
independent interaction classes and dropped-row rounding (Section 5,
Lemma 23, pp.139:12-13). Proposed delta Y is deterministic protection of
large occurrences using disjoint Hall rainbow blocks, then categorical
block rounding, potentially giving 4kt(kt-1)^2 for all parameters.
Hall's theorem and floating-variable rounding are standard separately;
substantive novelty of their combination is unverified.

Verification route Z: independently reconstruct the all-parameter categorical
extension and multiple-choice rounding lemma, checking occurrence
multiplicity, multiple items of a feature inside one block, and cumulative
error. Search symmetrically for a counterexample to each lemma or the bound.
The supplied route and preliminary native challenge are research inputs,
not a frozen candidate, acceptance, or resolution of this job.

## Research pass 1 submission (2026-11-01 Asia/Shanghai)

`research/proof.md` now supplies a complete proposed positive resolution
of the exact quantified problem above, with P(t,k)=4kt(kt-1)^2 and a
deterministic polynomial-time construction for explicitly listed incidences.
This is the same original scope, not a bounded-rank or fixed-parameter
replacement. Candidate status requests fresh review; it is not acceptance.

The all-parameter proof establishes the categorical coefficient bound,
the 2kt per-class error, and telescoping across <=(kt-1)^2 classes.
The exact multiple-choice lemma is known: Doerr--Srivastav (2003), as
explicitly stated in Glaßer--Reitwießner--Witek, FSTTCS 2011, Theorem 2,
p.58, DOI 10.4230/LIPIcs.FSTTCS.2011.55. It is credited as a dependency,
not submitted as an innovation. The proposed new reduction and its current
primary comparison are specified in `literature/research-primary-comparison.md`.
Full independent correctness, novelty and substantive-value review is pending.
