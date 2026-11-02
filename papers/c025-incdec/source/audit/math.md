# Fresh mathematical review

Job: `c025-incdec-referee-2ab23be91f58`.
Frozen snapshot: `2b34def4196da89c592b17665c39fbf7b0b04e44c40aeac720bf40cd52fb35b4`.
Review date: 2026-11-01 UTC (2026-11-02 Asia/Shanghai).

The reviewed candidate is exactly the resolution-paper in frozen `claim.json`:
endpoint-oriented greedy for the actual objective gives a deterministic
polynomial-oracle 2-competitive permutation for every pair of nonnegative
monotone submodular functions. Together with the existing structural lower
bound, the sharp unrestricted and polynomial-oracle constants both equal 2.
This report does not revise or restrict that candidate.

## Reconstructed universal argument

Write F(S)=h(S)+g(E\S), H=h(E), and G=g(E), initially with normalized inputs.
Complementation preserves submodularity, so F is submodular. Monotonicity and
nonnegativity of the two summands give, for arbitrary O,P,

    F(O) <= H+G,
    F(O)-F(O union P) <= G.

For the second inequality, h(O)-h(O union P)<=0, whereas
g(E\O)-g(E\(O union P))<=g(E)=G. Neither inequality supposes that F is
monotone. This is the exact decomposition property used by the proof.

Assume H>=G and greedily add an available element of maximum F marginal until
all elements have been used, even after these marginals become negative.
For any allowed tie choices the gains a_i form a nonincreasing sequence:
each surviving element's marginal decreases when the current set grows,
and it was no larger than the preceding chosen maximum.

Fix an internal cardinality 1<=k<n, put P=P_k, d=a_(k+1), and take any
O of size k. If d>=0, diminishing returns and greedy maximality give

    F(O union P)-F(P) <= sum_(e in O\P) F(e|P)
                         <= |O\P| d <= k d.

Also k d <= sum_(i=1)^k a_i = F(P)-G. Therefore

    F(O) <= F(P)+G+k d <= 2F(P).

All terms and inequalities remain valid at d=0 and when O intersects P.
In particular the positive initial value G is retained, rather than discarded
by normalizing the combined nonmonotone objective.

If d<0, nonincreasing gains make every subsequent gain negative, hence
H=F(E)<=F(P). Thus F(O)<=H+G<=2H<=2F(P). The direction comparison H>=G
is essential at this step. No denominator or positive optimum is required.

If H<G, apply the established argument to F'(A)=g(A)+h(E\A) and reverse its
greedy order. The returned prefix of size k is E\Q_(n-k), where Q_j is the
swapped greedy prefix. F'(Q_(n-k)) equals the original objective there, and
complementation maps all original size-k comparators bijectively onto swapped
size-(n-k) comparators. This proves the identical guarantee for every k on
one returned permutation. The endpoint cardinalities are exact automatically;
the empty ground set and singleton ground set cause no exceptional step.

These steps establish the universal claim, rather than extrapolating a finite
search. They also validate the proof dossier's nonnegative-summand identities:
in the nonnegative-d branch their sum telescopes to 2F(P)-F(O); in the negative-d
branch the three terms are H+G-F(O), H-G, and 2(F(P)-H).

For nonnegative unnormalized inputs use h'=h-h(empty), g'=g-g(empty), and
B=h(empty)+g(empty)>=0. Both normalized functions retain the hypotheses.
The normalized algorithm satisfies 2F'(P)>=OPT'_k, implying
2(F'(P)+B)>=OPT'_k+B. The endpoint orientation is taken after this subtraction.
This covers the additional original variant without any negative baseline.

The procedure queries H,G and at most n(n+1)/2 candidate objective values,
each using two summand queries, plus cached-current-value bookkeeping.
There are polynomially many exact arithmetic operations and comparisons.
The claim uses the exact-value unit-cost model explicitly fixed in problem.md;
it makes no unsupported bit-complexity assertion for arbitrary real oracles.

## Matching impossibility and scope

For n>=2 take E={a,b_1,...,b_(n-1)} and h=g=q, where a covers all n-1 unit
features and each b_i covers only feature i. These are normalized nonnegative
monotone coverage functions. At cardinalities 1 and n-1 the optimum equals
2(n-1). If a is not first, the size-1 prefix has value n. If a is first, the
size-(n-1) prefix has value n. Consequently every permutation has ratio at
least 2(n-1)/n. For each r<2 an integer n>2/(2-r) refutes a uniform r guarantee,
independently of computational restrictions. This reproduces prior work;
it is not a new lower bound. The new upper algorithm attains 2, so both infima
in the immutable problem equal 2. There is no unattained-infimum loophole.

All pairs, arbitrary unequal totals, zero functions, all cardinalities, and
deterministic tie choices are covered. This is a full original resolution,
not a fixed-cardinality, equal-total, randomized, or gross-substitutes restriction.

## Checks actually performed

Every listed snapshot input was hashed without modification. All 24 file
hashes and the canonical mapping digest match. No checkpoint, state, previous
audit, owner session, job transcript, or progress-summary contents were read.
The listed research-progress.md was deliberately not used. The decisive proof,
the relevant listed source texts, selected frozen code and exact certificates
were inspected; the old numerical LP screen was treated only as finite
numerical evidence, not as a proof or a novelty assessment.

The new `audit/referee_checks.py` imports no proposer implementation. It checks
normalization, nonnegativity, edge monotonicity, every elementary submodular
square, the algorithm and reversal, every comparator at internal prefixes,
both exact proof identities and their signs, and nonnegative baseline transfer.
There were 625 exact instances, 4,318 completed greedy orders, 83,003 comparator
checks, 706 negative-d branch visits, and 3,636 zero-d visits. All greedy ties
were enumerated in 148 designated instances (ground size at most 6); other
instances used a fixed deterministic tie order. Generated instances were sums
of capped nonnegative modular functions with a recorded seed; four frozen
rational adversaries were also checked. These families do not exhaust general
submodular functions. All permutations of the lower-bound family were checked
for n=2,...,8 (46,232 permutations total), attaining the stated finite formula.
The exact output and limits are in `audit/referee-checks.json`. Every frozen
hash still matched after these tests. The universal derivation above supplies
what these finite checks cannot establish.

## Primary literature and contribution assessment

The direct comparison is Disser, Klimm, Lutz and Strubberg, *Incremental–
decremental maximization*, Acta Informatica 63:31 (2026),
[DOI 10.1007/s00236-026-00546-x](https://link.springer.com/article/10.1007/s00236-026-00546-x).
Its model, Section 1.1/Table 1, Corollary 2, Proposition 11, Proposition 17,
Section 5 and Appendix B were checked in the frozen journal text and compared
with the current publisher record. Its upper bound is 1+e/(e-1); the lower
bound is 2; its equal-total result already attains 2. Proposition 19 and
Corollary 20 make its unchanged double-greedy algorithm's larger constant tight.
The reviewed procedure instead selects actual-objective marginals and fixes
one orientation from the endpoints. The source's infimum is unrestricted;
its algorithmic results are polynomial-time. The new result satisfies both
readings. The publisher explicitly leaves the general submodular gap open.
The [arXiv record](https://arxiv.org/abs/2508.14516) still lists only v1.

Bienkowski et al., [ESA 2026, Theorems 1.1 and 1.2](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.134),
were checked in the frozen introduction and current official record: their
monotone incremental upper 1.373 uses optimum-set access and sacrifices
efficiency; their lower is 1.25. They concern the one-function subcase, so they
do not imply this arbitrary-pair upper theorem.

Chen and Kuhnle, [arXiv:2605.07902v1, Section 2 and Theorem 1](https://arxiv.org/html/2605.07902v1),
were independently inspected beyond the abstract. Their curvature-dependent
guarantee uses normalized combined objectives and greedy with pruning for a
fixed |S|<=k constraint. Active sets may lose previously selected elements.
That theorem does not supply a nested permutation at all exact cardinalities,
nor the unconditional pair-class factor proved here. This is a comparison of
the stated theorem, not a certification of all claims in that preprint.

The primary [Ohsaka--Matsuoka reconfiguration abstract](https://arxiv.org/abs/2111.14030)
was additionally screened. Its path-threshold objective between input
solutions differs from simultaneous cardinality-wise comparison. No transfer
or consequence from its approximation constants is asserted.

Fresh searches covered the exact model/title, ratio 2, actual/net marginal
greedy, endpoint/permutation greedy, additive nonmonotonicity, and submodular
reconfiguration. No equivalent full theorem was located in these checked
primary results as of this review date. This bounded search cannot certify
priority over all possible formulations or unpublished work.

The substantive advance is the complete sharp deterministic polynomial-oracle
upper bound on the full pair class, improving 2.582... to 2. The independent
idea is to retain the initial endpoint budget in the union comparison and
use endpoint orientation to certify the entire decreasing tail. The classical
monotone greedy theorem cannot be invoked on this nonmonotone combined
objective, and the source's equal-total theorem or tight double-greedy analysis
cannot be substituted for this argument. Thus this is a new algorithmic
resolution with substantive value relative to the verified prior work,
although its proof is elementary and its broader consequences remain limited.

## Verdict and limits

**Accept** the exact frozen resolution-paper and original_status **proved**.
No mathematical or original-scope gap remains in this review. The literature
screen found no duplicate; priority language must remain bounded to checked
sources. This is an actual fresh internal review, not external peer review or
a mathematical truth certificate. No original or decisive evidence was changed.

The separate venue assessment is **working_paper**. Resolving this focused
gap is worthwhile, but the record does not establish exceptional importance,
depth, or consequences across TCS sufficient for a confident competitive STOC
case. Acceptance here must not be promoted to submission_ready. No manuscript
or PDF was authored in this referee job.
