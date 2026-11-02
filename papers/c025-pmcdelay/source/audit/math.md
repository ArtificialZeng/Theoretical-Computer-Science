# Fresh mathematical referee report

Job: `c025-pmcdelay-referee-6970e98c3a2b`.
Frozen mathematical snapshot: `9e18afcb85b19f266e11aab420e78596f90e785921128737257fbdd42a21cfbc`.
Review performed 2026-11-01 UTC (2026-11-02 Asia/Shanghai).

**Verdict: accept the frozen resolution-paper scope.** The proposed algorithm
settles the immutable positive assertion: every finite simple graph, all
nonempty PMCs once, one input-polynomial bound on initial, successive and final
delay, with exponential storage allowed. This is an internal mathematical and
innovation judgment. The separate venue assessment is **working_paper**.

## Inputs and integrity

I read the original statement, precise interpretation, claim, snapshot and its
listed mathematical evidence, together with the required project/publication
instructions and STOC standard. I did not read checkpoint/state files, earlier
reviews or job transcripts. The required supervisor note was treated as an
unverified pointer; its optional unlisted proof aids were not used. Assertions
of confidence or finite success were not accepted as proofs.

All 18 frozen file hashes and the canonical snapshot digest were recomputed
and matched. In particular source.md remains byte-identical, SHA-256
`30ba523462232346f8c2d671825d32d790edcd9362f00b8eec84a58e11d4e5cc`.
The argument audited is research/streaming_proof.md, with its primitive contracts.
No claim, proof or source input was repaired or rewritten during this review.

## Reconstructed proof and adversarial checks

**1. The helper is a genuine polynomial-time construction with a prefix-useful
fiber bound.** For a minimal separator S choose distinct full components C,D.
Saturate S and minimally triangulate each block S union C_i independently.
The union T is chordal because its pieces meet in the clique S and there are
no edges between different original components.

To check inclusion-minimality, consider any chordal G <= H <= T. If an edge
xy within S is missing from H, full components C,D supply two x-y paths with
interiors on different sides. Shortest paths on each side are induced; they
have no internal cross edges. Their union is a chordless cycle. Thus every
saturation edge is forced in H. Each restriction H[S union C_i] then contains
the saturated base block and equals its chosen minimal triangulation. Hence
H=T. This checks inclusion-minimality, rather than minimum fill size.

In the selected block, a maximal clique properly extending S exists. The
clique-tree subtrees for s in S pairwise intersect. Their intersections with
the connected union of subtrees meeting C are nonempty, since C is full.
Tree Helly gives a clique containing S and a vertex of C. It is maximal in
the union T because no other block has an edge to that vertex of C. Its vertex
set Gamma is therefore a PMC of the ORIGINAL graph. The other full component
D survives as a whole component of G-Gamma with neighborhood exactly S.
For fixed Gamma, distinct preimage separators are distinct neighborhoods of
components of G-Gamma, so there are at most n. This is the needed bound on
the actual helper map, not merely a comparison of final output counts.

MCS-M, maximal-clique listing in a chordal graph, graph searches and a fixed
choice of labels implement the helper in polynomial time. Paths in MCS-M
are tested in the original saturated block; fill edges do not alter its search
graph. The primary pseudocode and Theorem 4.4 support this interpretation.

**2. The endpoint-safe graph searches retain the structural preimages.**
I checked the statements and constructed witnesses in BLS Theorems 8--10,
not just the informal neighborhood description. For an a-nice target Omega,
write C_a=C(a,Omega), S_0=N(C_a), and T_0=Omega-S_0. The cited constructions
give W and u in W intersect C_a such that

    Omega subseteq X = W union N(u) subseteq Omega union C_a,

and retain T_0 in W. In Theorem 9, u=a and every deleted S_0 vertex is adjacent
to a. In Theorem 10, u is in the shutter D and every deleted vertex is fully
adjacent to D. These facts establish both containments independently of the
source's inconsistent endpoint wording in Definitions 12 and 20.

Fix b in T_0. Lemma 10 puts T_0 into a full component C_T of G-S_0 distinct
from C_a. The b-component A after deleting X-{b} stays in C_T. Each s in S_0
is adjacent to A: PMC pair visibility gives either edge bs or a b-s path
with interior outside Omega. Such an interior cannot use C_a, since b has
no neighbor there, and avoids X. Thus S_0 subseteq N(A) while N(A) is disjoint
from C_a. The endpoint guard consequently keeps this pair, and the u-component
after deleting N(A) is exactly C_a. The computed separator is S_0 and the
retained set is exactly Omega. There is no undefined component query or
unproved extension of the source definition in this argument.

The source preimage either contains a or strictly decreases C(a,W). Repeating
preimages therefore reaches a non-a-nice PMC. Reversing gives reachability
from the complete seed family. The argument does not assume strong
connectivity from one arbitrary PMC. The substantial structural existence
theory is credited to BLS, not reproved or claimed as this candidate's work.

**3. All and only the required PMCs are generated.** A child PMC has a valid
lift X or X+{a}. Deleting a from a lift recovers X, so different child outputs
give different root outputs. Lemmas 11/12 supply all seeds: PMCs surviving
deletion of a and PMCs containing a. The separator phase tests S+{a} and
additionally emits its valid helper PMC. Extra seeds cannot destroy
reachability. Recognition on every insertion and a trie exclude invalid sets
and duplicates. The queue already receives each discovery at insertion and
is expanded once per PMC, so there is no exponential transition copying a
completed seed list. Choosing a spanning-tree leaf keeps recursive inputs
connected. Complete graphs are direct base cases.

**4. Both prefix time and termination have a fixed polynomial bound.** Let
K=|PMC(H)| and K_c=|PMC(H-a)|. Let p(n) bound all local primitive operations,
including one entire neighborhood expansion, one separator gap plus helper,
and suspension/dictionary/serialization costs. Such a fixed polynomial exists
for the specified finite implementations. Binary tries avoid dependence on
the number of stored outputs; all addresses and counters have polynomial bit
length because at most exponentially many vertex subsets are stored.

Set Q(n)=Q(n-1)+(n+10)p(n). Its growth is O(n^2 p(n)) after making p
nondecreasing. I checked simultaneous induction for E(j)<=Q(n)j and
T<=Q(n)K. For termination, K_c<=K, D<=nK, and at most K queue expansions
give child cost Q(n-1)K_c plus at most (n+7)p(n)K local work.

For an output in phase I, the child rank r is at most the root output rank j;
the child is paused at that exact emission. For phase II, the first r-1
separator helpers have all already been emitted. Since every helper fiber
has at most n separators, r-1<=n(j-1), and completed child work is charged to
K_c<=j existing root outputs. In phase III, all helpers are already emitted,
so D<=n(j-1); every queue entry popped so far corresponds to a different
earlier output, so at most j expansions have begun. The displayed local
constants in the candidate fit the additive slack (n+10)p(n) in all cases.
No recursive coefficient greater than one multiplies Q(n-1). In particular
the child's final tail is covered by its T invariant, rather than inferred
from its last emission time.

**5. Buffering covers all three kinds of delay.** With q=Q(n), after qj
simulated steps at least j outputs exist when j<=K. Only j-1 have been
returned, so a FIFO output is available. A running simulation cannot survive
past block K because T<=qK. If it halts inside a block, all remaining outputs
are buffered. Thus the K-th returned output has no exponential simulation
tail. Buffer bookkeeping/serialization change only the fixed polynomial.
Halting does not require traversing and deallocating exponential storage.
This is a self-contained use of known amortization, not a novelty claim.

**6. Boundary scope is complete.** Inclusion-minimal triangulations have no
edges crossing original connected components: deleting all such edges leaves
a chordal disjoint union containing G. Conversely unions of componentwise
minimal triangulations are minimal. Hence nonempty PMCs partition by original
component. Sequential component enumerators preserve polynomial boundary
delay; isolated vertices and complete components are covered. The zero-vertex
graph is detected and halts without output. All domain restrictions in the
original question are respected; polynomial space is not asserted.

## Independent finite verification

audit/referee_verify.py uses only Python's standard library and imports no
owner implementation. It independently lists all chordal supergraphs and
filters inclusion-minimal completions, then lists their maximal cliques, on
ALL 1,100 labelled graphs of orders zero through five. These literal PMC
families agree with a fresh component/pair-witness recognition implementation.
There are 1,341 minimal completions across these inputs.

Among 772 connected inputs, five complete graphs are base cases. On the
remaining inputs it checked 1,605 literal separator helpers, their glued
minimal triangulations, outside-component witnesses and fibers; 3,792
all-vertex seed closures; and 902 strong preimages with the containment and
strict-decrease conditions used in step 2. It also independently checked the
complete distinct output sets of all 29 frozen serialized cases (up to order
ten) using the fresh global criterion. audit/referee-verification.json records
coverage and a digest. These are exact finite diagnostics, not asymptotic
evidence or a proof of the unbounded theorem.

The first version of my verifier incorrectly applied recursive seed obligations
to the singleton complete base case and failed an assertion. That operational
verifier error is preserved in audit/referee-verification-initial.json. I made
the complete base case explicit and corrected the removed vertex's adjacency
in its child oracle before the successful run. Neither defect concerned the
candidate proof, and the frozen packet was not changed.

## Current prior work, novelty and value

The current primary records still show BLS v3 (20 October 2026) and Kenig v1
(17 October 2026). The exact local theorems were inspected. BLS Theorem 1
guarantees total O(n^4 m K) time and Section 1.4 explicitly leaves worst-case
polynomial delay open. Its structural neighborhood, lifts and reachability
are essential dependencies of the present argument. [Primary record](https://arxiv.org/abs/2610.19850v3).

Kenig Theorem 1.1 supplies delay 2^{O(k^3)} n^4 log n for size-at-most-k
PMCs (also with constraints). Setting k=n does not give polynomial delay.
The candidate does not supply Kenig's parameterized or constrained guarantee.
[Primary record](https://arxiv.org/abs/2610.24856v1).

IPEC 2025 Theorem 32 gives polynomial delay for triconnected plane graphs.
Proposition 29 already uses a separator-saturating triangulation and an
extending clique; that extension idea must not be advertised as new.
The candidate removes the graph-class restriction through its full conversion.
[Primary article](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2025.21).

I additionally checked Brosse--Conte--Limouzy--Punzi--Rucci,
arXiv:2402.18265v1 / IWOCA 2024: Proposition 1 already establishes unique
child extension, and Lemma 4 gives output-polynomial time
O(n^9 m^2 K^4) with O(n^3) space. It gives neither the claimed all-size delay
bound nor the new prefix-time invariant. The present result does not dominate
its polynomial-space guarantee. [Primary full text](https://arxiv.org/html/2402.18265v1).

Capelli--Strozecki STACS 2023 expressly describes FIFO conversion of
incremental-linear enumeration with exponential storage as folklore. Their
2026 journal development remains current. Buffering is therefore prior work;
the burden here is establishing the stronger input-polynomial prefix bound.
[STACS primary record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2023.18),
[journal primary record](https://link.springer.com/article/10.1007/s00037-026-00287-w).

The known separator primitive is directly stated in BLS Lemma 1 and supported
by the Berry--Bordat--Cogis WG 1999 publisher record. Its complete historical
chapter text was not obtained in this review. I compared the candidate queue
recipe with the initialization/generation loops in official igraph source;
its list-wide duplicate search must be replaced by the specified trie.
MCS-M's local primary Theorem 4.4 and pseudocode give minimal triangulation;
the optimized O(nm) bound is unnecessary because naive path tests are polynomial.
[BBC record](https://link.springer.com/chapter/10.1007/3-540-46784-X_17),
[official code](https://raw.githubusercontent.com/igraph/igraph/main/src/connectivity/separators.c),
[MCS-M record](https://doi.org/10.1007/s00453-004-1084-3).

Quoted searches combining PMCs, polynomial delay, incremental and the source
title found no equivalent general all-size result in the checked primary
sources. This bounded search is not a priority certificate. A mistaken v2
HTML request for the Brosse paper returned 404; the actual current v1 full text
was then successfully inspected. That access error has no mathematical import.

The substantive delta is an algorithmic modification plus an invariant:
emit actual bounded-fiber helper solutions while consuming separator seeds,
pause recursive enumeration exactly at injectively lifted outputs, and couple
prefix and termination estimates additively. A global D<=nK inequality alone
does not bound a separator prefix, and applying FIFO to BLS's total-time bound
alone is invalid. The added emissions and simultaneous induction overcome
those two concrete obstacles. This is a complete improvement in enumeration
complexity for an expressly open general-graph question, not a routine
restricted example or a subsidiary-method counterexample. I judge this a
substantive mathematical algorithmic contribution despite its heavy, explicit
dependence on existing structural theory.

The STOC case is more uncertain. The result improves time to ANY prescribed
number of distinct PMCs and supplies a general streaming guarantee, but does
not improve treewidth's known total-time exponent, reduce space, or supply a
new structural characterization. The hardest graph-structural arguments are
from BLS. Whether the new scheduling/charging idea has the depth and breadth
needed for competitive STOC submission is not established by the reviewed
packet. audit/stoc-assessment.json therefore retains working_paper.

## Disposition

No unresolved mathematical or original-scope gap was found in the frozen
argument. Accept resolution-paper, original_status proved, subject to the
normal structural provenance gate. audit/innovation.json records this actual
review. No manuscript/PDF, submission, upload or contact was performed.
Any substantive later change to the frozen evidence requires a new snapshot
and fresh review. This report is neither external peer review nor formal
verification, and its venue label is not a conference decision.

The required `release_gate.py check-math PROJECT_DIR` was run after these fresh
audits were written and returned exit code 0 with `ok: true`, the exact snapshot
digest above and this referee job ID. Its actual result is recorded in
audit/referee-check-math.json. This passes the structural/provenance check only;
the mathematical judgment is the reconstructed review above.
