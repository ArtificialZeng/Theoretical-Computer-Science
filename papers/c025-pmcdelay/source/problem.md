# Precise original target and triage reading

The immutable question is `source.md`; its SHA-256 is
`30ba523462232346f8c2d671825d32d790edcd9362f00b8eec84a58e11d4e5cc`.
Source status at triage: **open-supported**. Research pass 1 now proposes a full positive resolution for fresh review; no mathematical acceptance or venue assessment exists.

## Objects and quantifiers

For every finite simple undirected labelled graph G=(V,E), let n=|V| and
m=|E|. A chordal graph has no induced cycle of length at least four. A minimal
chordal completion is a chordal graph H on V with E contained in E(H) such
that no proper subset of its added edges still gives a chordal supergraph of
G. Minimal means inclusion-minimal, not minimum-cardinality. A nonempty set
Omega is a potential maximal clique (PMC) of G exactly when it is a maximal
clique of at least one such H. Let PMC(G) be the family of these sets.

The positive assertion is: there exist ONE algorithm A and ONE fixed polynomial
p, independent of G and its output count, such that A on EVERY such G emits
exactly the elements of PMC(G), each once, and halts. Time to the first output,
each interval between successive outputs, and time from the last output to
halting are each at most p(n+m+1). If no output exists, the whole computation
must halt within this bound. In particular the empty graph on zero vertices
has no nonempty output and must terminate promptly. Disconnected graphs,
isolated vertices and complete graphs are included. No output ordering is
required; exponential storage is allowed. No bound on PMC size, graph class,
width, preprocessing advice or supplied completion/list is available.

A complete negative answer must rule out this assertion under explicitly
stated justified complexity assumptions. Neither an intermediate method
counterexample nor constrained-search hardness alone does so. Total
output-polynomial time alone does not provide this delay bound.

## Nearest results and actual scope delta

Berge--Limouzy--Schivre, arXiv:2610.19850v3, Theorem 1 (printed pp.6,43),
gives total O(n^4 m |PMC(G)|) enumeration; Section 1.4, printed p.8,
explicitly leaves polynomial delay open. The current arXiv page still lists
v3, revised 20 October 2026. Its connected-input convention is handled in
our target only by a proved component reduction, not an implicit restriction.
Kenig, arXiv:2610.24856v1, Theorem 1.1, p.2, gives delay
2^{O(k^3)} n^4 log n for PMCs of size at most k. Taking k=n does not yield
polynomial delay. Grigoriev--Kobayashi--Tamaki--van der Zanden,
IPEC 2025 article 21, gives polynomial delay on triconnected planar graphs.
These do not settle the all-graph, all-size assertion. See the dated source
check in `evidence/triage-validation.md` for links and search limitations.

Proposed delta: a full all-input polynomial-delay algorithm obtained by
streaming recursive lifts and the source's complete seed/neighborhood
traversal, with polynomial-fiber separator helper outputs and an additive
simultaneous emission/termination induction. The full original resolution is
the research objective. The separator-extension idea overlaps IPEC 2025
Proposition 29 (p.21:14); it must not be sold independently as new mathematics.
The technical and novelty burden is the complete conversion and its proof.

## Supplied evidence, failed route and unresolved kernel

`intake/pmc-streaming-proposal.md` and
`intake/pmc-streaming-induction-v2.md` are unreviewed proposals. Their source
seed dependencies match the inspected statements of Lemmas 11/12,
Algorithm 3 and Theorem 11/Corollary 3; this is not an audit of those proofs or
of the new algorithm. Source Definition 20 and the close-separator endpoint
conditions must be implemented exactly. Arbitrary single-seed strong
connectivity is not supplied by those results.

Preserved root diagnostics: the earlier atom-neighborhood route has 18
reported failures including atlas198. Later `intake/root-positive-finite-check.md`
and its JSON/code report full output and charging checks on 1036 graphs,
including literal minimal-completion comparison on 31 graphs. This supersedes
the older handoff's statement that no finite generator check had run. This
triage did not rerun those exhaustive tests. Their subset separator oracle
is exponential and establishes no asymptotic delay theorem.

Next decisive test: produce a dependency-complete proof or exact obstruction
to the proposed simultaneous bounds E(j)<=Q(n)j and T<=Q(n)|PMC(G)|, with
Q(n)=Q(n-1)+poly(n). First justify the polynomial helper Gamma(S) and its
outside-component witness/fiber at most n, then trace all source seeds,
recursive pause points, phase boundaries and buffered final waiting. Verify
the actual polynomial-delay separator and minimal-triangulation primitives;
no exponential subset oracle may enter the complexity proof. An obstruction
to this route does not disprove the original assertion.

## Payoff and gates

A successful full conversion would replace a total-time guarantee by a
worst-case streaming guarantee for a central exact graph-algorithm primitive.
It implies neither polynomial space nor a smaller exponential PMC count or
an improved worst-case treewidth exponent. Its actual novelty, depth and STOC
significance remain unassessed. Bounded research admission is justified;
there is no authorization for a manuscript/PDF until full innovative original
resolution and the required fresh reviews. Three research passes remain in
the recorded cap; this triage consumes no research pass.

## Research pass 1: proposed full resolution, not acceptance

`research/streaming_proof.md` gives a full all-input algorithm and proof with no
known remaining gap beyond its explicitly named standard theorem dependencies.
It proves a witnessed polynomial separator-helper fiber, transfers the source
preimages to an explicit endpoint-safe graph-search neighborhood, and proves
emission-rank and full-termination bounds simultaneously with an additive
polynomial recurrence. Standard FIFO buffering then gives polynomial initial,
inter-output and final delay; empty/disconnected cases are proved separately.

The literal endpoint wording inconsistency between source Definition 12 and
Definition 20 is disclosed and handled by the transfer proof; it is not hidden
by an implementation assumption. `research/polynomial_primitives.md` specifies
the actual graph-search separator queue primitive, trie replacement and MCS-M
contracts. A new 29-case targeted test uses polynomial primitives inside the
generator and exhaustive subsets only in its finite expected-output oracle.
All complete output sets and helper/lift/queue checks passed. This is finite
transcription evidence, not a universal theorem or independent review.

Nearest sources and current limits are in `evidence/pass1-literature.md`,
including Capelli–Strozecki STACS 2023 / Computational Complexity 2026: the
buffering transformation is known and is not the contribution. The proposed
new delta is the full streaming conversion of PMC enumeration, especially
constructive separator charging and the recursive simultaneous time invariant.
The fresh referee must assess whether this is correct, current, substantively
innovative and valuable enough; STOC competitiveness remains unassessed.
No manuscript/PDF or audit acceptance has been created.
