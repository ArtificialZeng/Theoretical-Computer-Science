# Frozen original: full-range quasipolynomial MST under decreasing corruptions

Status: NEW-QUESTION / computational refinement of a primary source theorem.
This precise extension is formulated here, not falsely quoted as an authored
conjecture. It was already deferred as c038-screen-08 before research; it has
never received a queue RESEARCH pass. Do not rename or resume c038-mstqp:
that exhausted original permits arbitrary increases/decreases for p<1/2,
and remains unresolved. This original is the full decrease-only range p<1.

Primary: Anand–Gupta–Jayaram–Lee–Vakilian, *Approximating Minimum Spanning
Trees in Metrics under Semi-Random Corruptions*, arXiv:2610.40594v1,
Theorems1.2/1.3 and Section6, especially Definitions6.4–6.6 and Algorithm2/3.
The inspected current record on 2026-11-02 shows v1 only. The source already
has an inefficient logarithmic approximation for every fixed p<1 and an
n^O(log n)-time O(log^4 n) approximation for p<=0.1. These are prior, not
contributions of this project. Bounded follow-up/equivalence searches found
no stated full-range computational theorem; this is not a priority certificate.

## Exact full original

For EVERY fixed real 0<=p<1, construct an explicit zero-true-query classical
algorithm with constants a_p,C_p>0 such that for every n>=2, every genuine
n-point finite metric d, and EVERY omniscient decrease-only adversary, it
returns a spanning tree T satisfying

    E[sum_(uv in T) d(u,v)] <= C_p * max(1,log_2 n)^4 * MST(d).

The mask marks each unordered pair independently with probability p. The
adversary sees d, the full mask and the algorithm, and chooses a symmetric
finite nonnegative observation D_uv<=d(u,v) on each marked pair; unmarked
pairs retain their true distance. It chooses D before seeing the algorithm's
private random bits. Only D is observed; no true distance or hidden label
queries are allowed. The expectation includes the mask and the algorithm's
private bits, and is uniform over adversary strategies of this kind.

On EVERY observed input and EVERY private-bit execution, the number of exact
arithmetic/comparison operations and private bit operations is at most
n^(a_p max(1,log_2 n)), independently of the true or observed aspect ratio.
Use the source's exact-distance arithmetic/comparison model, not a claim of
unit-bit cost for arbitrary reals. For rational inputs, any claimed bit-model
strengthening must separately charge input precision. The algorithm may
hardwire a fixed rational lower bound 0<q<=1-p; constants may depend on it,
but never on n or aspect ratio. p=0 and small n must have literal valid cases.
Witness/output correctness and finite-bit random leader selection are required.

A complete conditional negative answer must refute this exact assertion under
an explicitly supported standard hypothesis; failure of one hierarchy does
not do so. A local quantile fact, a bounded-aspect-only result, a success-only
runtime, a p<1/2 theorem, or merely a logarithmic finite exhaustive algorithm
does not resolve the original. Full scope and substantive innovation are
required before a manuscript, then actual fresh correctness/novelty/value and
five-criterion STOC assessment. If the extension is a routine adjustment to
the existing method, keep Markdown/code only even if correct.

## Decisive first test and value risk

Read intake/full-range-upper-quantile-program.md. The proposed new route
concentrates observed clique seeds using uniform uncorrupted rectangles,
uses high quantiles for seed comparisons at every p<1, and tests ALL future
seeds including overlapping ones. The first test is a complete proof of
nonaccumulating outliers and the weighted hierarchy bound with all runtime,
aspect normalization, bad-mask expectation and finite randomness charged.
Do not replace that test by another small counterexample or parameter table.

The full computation/noise range would be a concrete improvement, but venue
value is unestablished: the prior hierarchy framework and extraction lemma
are inherited, and the prior p<=0.1 cutoff may be technical. TRIAGE/referee
must assess this risk candidly; do not grant novelty/depth merely because the
noise range is wider. No implication for the exhausted general-corruption
original is asserted.
