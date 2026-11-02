# Fresh mathematical review

Job: `c032-dspdag-referee-56b0105494de` (referee).
Snapshot: `df4def35c3d991745cbd37b3e8238b49c3edeedc07c6350a8a195b3092c3ad02`.
Reviewed on 2026-11-02 UTC. **Verdict: accept the frozen resolution-paper claim.**
This is an actual fresh internal review, not external peer review or a truth
certificate. The separate venue assessment is `working_paper`.

## Scope and materials

The immutable question asks whether some fixed k>=3 admits a uniform
O(n^(k+1-delta)) algorithm for prescribed disjoint shortest paths on every
source-model weighted DAG, or whether a standard hypothesis excludes every
such improvement. The frozen candidate gives a positive answer: deterministic
O_k(m+n+n^(k+0.3)) detection for every fixed k>=3, hence k=3 and delta=0.7.
I accept that stronger stated bound, not merely the slower Strassen fallback.
I also accept the claimed primitive-dependent schedule and fallback bound.

I read source.md, problem.md, claim.json, the current snapshot and its listed
proof, code, finite evidence and primary source texts. I did not use checkpoint,
state, prior verdicts or proposer confidence as evidence. The phase-entry note
is procedural context; its older snapshot pointer is superseded by the actual
current snapshot. Fresh primary-literature checks are recorded in
[the literature report](fresh-56b0105494de/literature.md). All 21 frozen files
and the canonical snapshot digest matched in
[the integrity check](fresh-56b0105494de/integrity.json).

The source does not fully fix arbitrary input-weight bit encoding. Acceptance
uses its original addition/comparison model, exactly as the frozen question and
candidate state. For B-bit integer weights, their actual preprocessing bit cost
must be added. The candidate does not impose bounded weights or give arbitrary
precision for free. For arbitrary parallel-arc encodings the O(m) input scan
remains necessary. With the source's ordinary O(n^2)-arc convention the asserted
n-only exponent follows. These are retained model qualifications, not scope
reductions made by this review.

## Reconstruction of correctness

**Original shortestness.** Compute each distance map in the original DAG and
retain precisely its tight edges, excluding unreachable tails. A retained path
telescopes to the original designated distance; every shortest path consists
of retained edges. This is done once, before conflicts or deletions, in
O_k(m+n) original-weight operations. Labelled edge graphs share the same
topological order, so shortest-path filtering satisfies the algorithm's actual
common-order hypothesis. Unreachable pairs give NO.

**Terminals and completion.** Under strict disjointness, cross-label repeated
endpoints give NO; s_i=t_i gives the trivial original path. Appending a distinct
private sink after all original vertices lets a finished token wait while
earlier tokens advance. Passing its target without completing cannot lead to a
successful later return in a DAG. Endpoint-only sharing is separated into
label-private terminal copies; labels not entitled to an endpoint cannot visit
it. For the internal/internal-only convention an additional shared internal
copy enforces precisely that collision rule. Copies of one original vertex
are consecutive, and no original edge joins equal original ranks, preserving
a common acyclic order. Mapping to and from copies retains exactly the allowed
sharing and changes the vertex count by O_k(1). Shortestness is never recomputed
after normalization. Thus neither terminal ambiguity in the source nor early
completion hides a distinct-terminal restriction in the theorem.

**Frontier semantics.** For a distinct-coordinate tuple q only its unique
least coordinate u moves. After a legal move every abandoned vertex is smaller
than every current coordinate: the old minimum is abandoned and both its
replacement and all unchanged coordinates are larger. A later destination
therefore cannot hit an abandoned vertex; masking current collisions suffices.
Conversely, for any fixed feasible family to the private sinks, advance the
least token along that family's path. Every unfinished token precedes every
completed sink, so a least unfinished token has a next edge. Disjointness makes
each move legal, and the finite remaining edge count decreases. This proves
soundness and completeness for the final sink tuple.

For a valid target p, an incoming transition moving label i has the complete
predecessor p[i:=u] with u<min(p), and contribution
F(p[i:=u]) AND A_i(u,p_i). This uses one compatible predecessor family. No
independently chosen path witnesses are combined. Invalid source entries remain
zero and invalid targets are masked. The seed is retained in addition to these
incoming contributions.

**Chronology and output partition.** The least coordinate strictly increases.
Every transition is assigned to its unique dyadic split separating its source
and target minima. Solving the left half, applying its cross transitions, then
solving the right half is therefore a valid finalization order, including a
seed whose minimum is not the first vertex. At a cross step all inputs have
minimum in L and are final; all writes have minimum in R. No cross-step product
can depend on another cross-step output.

Put S=R union the tail T. When label i moves to x, target minimum in R is
equivalent to exactly one of: x is in R and all context coordinates are in S;
or x is in T and the first context coordinate in R is coordinate j, all
earlier context coordinates being in T. These k classes are disjoint and
exhaustive. In particular x may lie beyond the current interval. Fixing an
entire labelled context gives a genuine contraction only over u in L.
Consequently the product (targets by u) times (u by contexts), followed by
collision masking and OR, implements exactly the scalar recurrence.

## Reconstruction of the global running time

For half-width b, batch at most b targets and b^(k-1) contexts. Class 0 needs
at most (N/b)^(k-1) products per label. Each other class has at most
b N^(k-2) contexts and at most N/b target batches, giving the same product
bound. The ceiling is controlled because (N/b)^(k-2) is an integer after
power-of-two padding. Empty tails generate no calls. All k labels and k
classes cost O_k((N/b)^(k-1)) products per node.

Each product repacks b^2+b^k entries and scatters b^k entries. This remains
charged when the same context array is reused with different target batches.
Context-list generation is bounded by the same O_k(N^(k-1)b) node charge;
there is no whole N^k scan per node. There are N/(2b) nodes at this width.
Thus data movement is O_k(N^k) per level and multiplication cost is
O_k((N/b)^k B_k(b)). Initialization and all levels give exactly the displayed
primitive-dependent bound. For any fixed multiplication exponent tau>k, the
dyadic sum is O_k(N^tau), absorbing N^k log N. The proof's O_k(N^k) space
claim for the explicit fallback includes the table and streamed square products;
the primitive-dependent theorem correctly leaves unspecified primitive workspace
additional. I found no omitted factor of N or uncharged large output array.

**Explicit fallback.** There are b^(k-2) square products per rectangular
product. Strassen gives exponent k-2+log_2(7), strictly between k and k+1.
Signed intermediate integers have polynomial magnitude: at depth d inputs
have magnitude at most 2^d, and at most four terms recombine per return level,
giving the claimed conservative O(b^4) bound. Arithmetic uses O(log N)-bit
operands; its elementary bit overhead is at most O(log^2 N). The word bound
and the separately stated bit-cost bound follow. This fallback is valid but
is not being substituted for the stronger candidate.

## The stronger exact rectangular primitive

Le Gall--Urrutia's Section 2.2 defines degenerations with polynomial maps over
an arbitrary field F; Q is an admissible specialization. Their Table 3 bound
3.251640, with the slack in the candidate, gives a fixed q0 and a rational
polynomial degeneration of rank r0<q0^3.26. The exponent is an infimum; choosing
an intermediate exponent strictly below 3.26 and then sufficiently large q0
justifies the strict inequality without assuming the infimum is attained.

If the image has lowest nonzero term lambda^s times the target tensor and
degree at most D, its t-th tensor power has coefficient at degree st exactly
the t-th target power and degree at most Dt. Interpolating that coefficient
from Dt+1 distinct rational evaluations bounds exact rank by
(Dt+1)r0^t. A sufficiently large *fixed* t gives a finite rational base identity
of rank r<q^3.27, q=q0^t. Permuting tensor variable groups turns dimensions
(q,q^2,q) into (q,q,q^2), preserving rank; the resulting bilinear algorithm
has the needed target-by-context orientation. All these conversion principles
are prior algebraic tools, not a new multiplication theorem.

The base has finitely many rational coefficients. Choosing p above both N
and a fixed constant exceeding the product of their denominators permits exact
reduction of the identity modulo p. Deterministic sieving and Bertrand's
theorem provide such a prime at negligible asymptotic cost; large base constants
are fixed independently of the instance. Recursive padded multiplication obeys
T(M)<=r T(M/q)+O_q(M^3), including dense linear maps and all output entries.
Since r>q^3 may be ensured, T(M)=O_q(M^3.27). The base dimensions and constants
are fixed: hardwiring this finite rational identity defines a uniform algorithm,
not size-dependent advice. An explicit coefficient implementation is unnecessary
for this existence theorem, and the finite verifier does not pretend to supply
or test one.

For the original 0/1 factors each true output is an integer in [0,b], even
after padding. Since p>N>=b, nonzero residue is equivalent to positive integer
output. There is no characteristic-two cancellation or random error. Residues
occupy O(log(N+2)) bits, and elementary modular multiplication/reduction has
the stated conservative log-squared overhead. For k=3 the global sum is
O(N^3.27 log^2 N)=O(N^3.3). For k>3, split the context columns into b^(k-3)
blocks of b^2 columns. The sum becomes O_k(N^(k+0.27) log^2 N), bounded by
O_k(N^(k+0.3)). Original preprocessing and N=O_k(n) give the frozen claim.

## Independent finite checks and their limits

I inspected the frozen verifier without running its main function, which would
overwrite frozen validation.json. I wrote a separate
[verifier](fresh-56b0105494de/independent_verify.py), importing no proposer code.
It uses bit-mask contractions and immutable cross-step source snapshots, and
compares the entire reached set against an ascending-minimum scalar recurrence.
It exhausted all triples of labelled DAGs on three ordered vertices and all
ordered seeds (3,072 cases), all common-edge DAGs on four vertices and ordered
three-token seeds (1,536 cases), and 110 further labelled k=2,3,4,5 cases.
All 4,718 full-state comparisons passed, including the per-node batch-count
bound. Separately 120 weighted original DAG instances, including 181-bit
weights, tied path lengths, unreachable/reversed/repeated/trivial endpoints,
were compared under three disjointness conventions against direct enumeration
of original globally shortest path families. All 360 comparisons passed;
strict, endpoint-only and internal-only conventions produced respectively
7, 12 and 29 YES cases. Results are in
[verification.json](fresh-56b0105494de/verification.json).

These are bounded bug checks. They neither prove all-instance correctness nor
benchmark or implement the fast rectangular algorithm. The preceding invariants,
charging argument and cited multiplication theorem establish those parts.

## Novelty, value and final decision

The detailed primary comparisons are in the linked literature report. The
established tuple graph, shortest-path filtering, terminal devices, generic
chronological recursion, Strassen and rectangular exponents are prior work.
The new part is the k-way target-minimum partition with entire labelled-context
packing and a globally valid dyadic charge. A direct generic closure of N^k
states or a claim to multiply all transitions at every node would not give its
bound. The proof supplies the missing dependency and data-movement analysis.

Against the inspected FHW/Berczi--Kobayashi/AVW baseline and Eppstein's actual
tuple-graph results, this is a substantive algorithmic improvement, not a routine
restatement, a graph-family restriction or a subsidiary counterexample. It
answers the exact existential original and also applies to ordinary prescribed
disjoint paths and arbitrary label-specific forward-edge graphs. No equivalent
full theorem was found in the bounded fresh primary search. This supports the
innovation judgment while retaining ordinary priority-search limitations.

No mathematical gap or necessary scope repair remains identified in this
frozen claim. Acceptance covers correctness, full original scope and substantive
innovation. STOC competitiveness is a separate judgment: the breadth of further
consequences and whether this compact combination constitutes sufficient new
technical depth for that venue remain uncertain. Accordingly the separate
assessment is `working_paper`; this does not change mathematical acceptance.
No manuscript, PDF or external communication was produced in this referee job.
