# Precise frozen target: deterministic 2D range LIS

The immutable statement is `source.md`; this file interprets it without replacing it.

For every positive integer n, every nonnegative integer m, every sequence
(a_1,...,a_n) of arbitrary real values, and every supplied family of m query
rectangles, let P={(i,a_i):1<=i<=n}. A query is the product of an index interval
and a value interval. Closed intervals can be used as a normal form, retaining
all points on their boundaries; other specified boundary conventions are
normalized by comparisons, without altering point membership. For each query
q, report indices i_1<...<i_l of maximum possible cardinality such that all
(i_j,a_i_j) lie in q and a_i_1<...<a_i_l. Empty intersections return an empty
sequence. Repeated values cannot occur together in a strictly increasing chain.
Let k be the sum of the lengths of all reported answers.

The assertion to resolve is existence of universal constants epsilon>0, C>0,
B>=0 and one uniform deterministic algorithm, valid for every such input, with
worst-case cost at most

C (n+m) n^(1-epsilon) log(n+m+2)^B + O(k).

Constants, algorithm and exponent saving are independent of input values,
queries, LIS lengths and n,m. Input real comparisons and operations on
O(log(n+m+2))-bit words have unit cost. Larger exact integers require charged
multiword operations. Queries may be processed offline; any optimal witness
is allowed. All overlaps, repeated values, sparse/dense instances and all
optimum lengths remain in scope. For m=Theta(n), the overhead must have a fixed
polynomial saving over n^2; n^2/log n does not qualify. A stronger square-root
bound is optional. Neither length-only answers, an explicit input set system,
1D queries nor a restriction on LIS lengths resolves this target. Failure of
a subsidiary algorithm does not negate the existence assertion.

## Source status and nearest comparisons

Status at triage, 2026-11-02: **open-supported**, provisionally. This is bounded
literature evidence, not a priority or completeness certificate.

Karthik C. S. and Saladi Rahul, *Range Longest Increasing Subsequence and its
Relatives*, [arXiv:2404.04795v2](https://arxiv.org/abs/2404.04795v2), revised
2025-12-01: Problem-I and Theorem 1 give randomized 2D reporting with
O-tilde((n+m)sqrt(n))+O(k); Section 7 explicitly asks for deterministic
subquadratic time and efficient stitching-set derandomization. Theorem 5
provides the small-LIS routine; Definition 2 and Section 3.2 give stitching
semantics. It suffices to hit a suitable maximum chain for each long query;
requiring every long chain to be hit is a stronger task.

Korogi's [arXiv:2610.20983v1](https://arxiv.org/abs/2610.20983v1), Theorem 1.1,
claims near-linear deterministic preprocessing for weighted **index-interval**
queries. Its Introduction defines that scope. A value query there returns
an optimum weight, rather than imposing a second geometric range on every
internal chain element. This inspected claim alone does not settle our 2D
question. Its full correctness was not reviewed in triage.

Bagchi, Chaudhary, Eppstein and Goodrich, SCG 2004, *Deterministic Sampling
and Range Counting in Geometric Data Streams*, Section 2, Lemma 2.2 and
Observations 2.3--2.4 already provide deterministic approximation and
merge/reduce machinery under a subset-only subsystem-oracle hypothesis.
The supplied proposal's possible delta is computing canonical-path traces
using disjoint original interval backgrounds, with a subquadratic total
charge. Generic sampling is prior art. Additional supplied comparisons with
SIGMOD 2011 path covers, ICALP 2019 explicit critical-path hitting and SPAA
2026 MPC hitting sets are indexed in the evidence. Their full implications
for localization and novelty remain to be audited.

## Admission and next test

A full deterministic polynomial exponent saving would address the actual
randomization gap in an established range-query problem. The supplied A--E
proposal makes that payoff concrete, but is neither an accepted proof nor an
established substantive innovation. Current evidence supports one research
pass, not a candidate or a manuscript. No STOC readiness assessment is made.

In the first bounded RESEARCH pass, validate or refute the localized merge-reduce stitching claim in intake/root-localized-net-proof.md: for t=Theta(n^(15/16)), deterministically construct O(n^(1/8) polylog n) points hitting a canonical maximum chain of every rectangle with optimum at least t, in O(n^(7/4) polylog n) charged word operations. Check the full-original-background trace oracle, multiset error induction and exact binomial arithmetic, then verify the supplied small-LIS/stitching integration yields the frozen full reporting bound; compare the localization step against known implicit path-cover/sampling theorems.

## Triage revalidation — c031-detlis-triage-2f01817be384

On 2026-11-02, the current primary records and local source statements were rechecked; the precise statement and all quantifiers above remain unchanged. The current weighted 1D claim does not itself provide 2D internal value filtering. Source status remains provisionally open-supported; no full deterministic equivalent was identified in the bounded check. This is admission evidence only. See evidence/triage-2f01817be384.md and evidence/triage-integrity-2f01817be384.json.
