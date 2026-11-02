# Adversarial checks and failed variants, research pass 1

Job: c022-spe-memory-research-5979be48ad66. All results below are research
records, not a referee verdict. The original question was never narrowed.

## Proof/counterexample split

The positive attack compresses the old continuation indices. The negative
attack starts with merging histories that demand different punishments at a
common vertex. Such a collision can refute a proposed compressed machine;
it is not an all-SPE lower bound for the source question. The constructed
collision below separates the identities of only two previous owners and
is handled by the proposed finite owner component. No fixed-player family
with unbounded required memory, and no original-question disproof, is claimed.
After a full positive argument emerged, attacks concentrated on its universal
claims and exact memory implementation rather than on unrelated variants.

## Exact counterexample: deleting the previous-owner component

A six-vertex three-player Reach game has initial root r and edges

    r -> a,b;  a -> a,w;  b -> b,w;
    w -> t1,t2;  t1 -> t1;  t2 -> t2.

P1 controls a, P2 controls b, and P3 controls all other vertices.
T1={t1}, T2={t2}, T3=empty. The intended initial payoff is 000.
At a, payoff 000 is supported by choosing its loop and, after entering w,
choosing t2; this makes a deviation by P1 unprofitable. At b, the analogous
continuation from w must choose t1 to deter P2. P3 is indifferent, so both
punishments are credible. An SPE using the previous owner's identity chooses
these continuations after ALL corresponding legal histories.

The labels A=empty and p=000 coincide after leaving a and b for w. There is
no continuation payoff 000 at w. Always using the same minimizer at w
therefore makes one of a->w or b->w profitable. This is an
**exact-counterexample** to the owner-free reset variant with identical
remaining mode, not to the original question and not to all alternative
memory encodings. The implemented owner-free control fixes j=P1; the
all-history verifier finds the profitable P2 deviation after root->b,
including when that history is off the prescribed initial outcome.

## Exact counterexample: deleting the progress rule

One player has a non-target v with edges to itself and to a target t,
and t has only a self-loop. The promise p=1 is feasible at both vertices.
Retaining every feasible promise and selecting an arbitrary compatible
successor can choose v->v forever, so the actual payoff is 0 although
the promise remains 1. This is an **exact-counterexample** to the
rank-free selector variant, not to the original question. Choosing a
successor that decreases distance to completed visited bits repairs this
specific failure. Rank values are in vertex-dependent tables, not memory.

## Independent all-history finite verifier

Reproduce with:

    python3 code/check_promise_reset.py --random-games 1000

Results: `evidence/promise-reset-finite-checks.json`.
All 576 labelled two-vertex, two-player no-dead-end directed games are
covered: 3^2 nonempty successor-set assignments, 2^2 ownership assignments,
4^2 target-membership assignments, initial vertex 0. No symmetry reduction
is used. A separate seeded sample covers 1,000 games with 1-4 players and
3-8 vertices; this range is sampled, not exhaustive.

The script first constructs finite payoff label sets by local-credibility
elimination and labelled-path filtering. It explicitly checks local label
inequalities and constructs finite progress selectors. It does NOT rely
on a claim that its labels enumerate all SPE payoffs. For every generated
initial label it builds the stated vertex-update machine and checks its
actual behavior independently. Across 1,576 games it checks 1,848 profiles
and 21,187 reachable product positions counted across those profiles.

Every legal successor is explored when forming the product; the common
memory update reads the source vertex and the SAME incoming state used
by the next-move function. The shared update means the machines' memories
are synchronized by observed vertices even if a player deviates. At every
reachable product position, the verifier follows the prescribed functional
graph to obtain the actual full reachability payoff. For each player it
then computes reverse reachability to that player's target with opponents'
actions fixed and ALL of that player's edges available. This checks all
unilateral strategies after every legal history, not just one-shot changes
or the prescribed outcome. Arithmetic and reachability are exact.

Controls correctly reject: (i) owner omission in the merging arena;
(ii) rank omission in the self-loop arena; (iii) a noncredible punishment
at a vertex lying off the initial outcome, even though the prescribed
profile is a Nash equilibrium at the initial vertex. The repaired merging
profile has 13 reachable legal-history product positions and passes.

Finite computation is a falsification and implementation check. It is not
a proof about larger or infinite arenas; those quantifiers are addressed
only by the mathematical proof packet.

## Targeted mathematical checks of universal scope

- **Hidden edge memory:** up((A,p,j),v) stores only A union t(v), the
  normalized payoff r and o(v). It never tests an edge or saves v. At a
  successor it can minimize the previous owner's payoff using j alone.
- **Merging histories:** when the same actual machine memory and current
  vertex coincide, normalization and progress choices are identical. The
  credibility lemma applies to every label at that augmented vertex, so
  no original witness history must be recovered.
- **Every legal history:** P is built from ALL original-profile subgame
  outcomes. New-machine reachability of its visited bits is proved along
  all legal edges, independently of compliance.
- **Targets in the prefix:** P(v,W) consists of full payoffs containing W.
  Machine A excludes the current vertex; normalization includes it exactly
  once through union. Empty and full payoff sets are included.
- **Arbitrary deviations:** the proof follows any deviating path. A losing
  player's normalized bit stays zero at opponent moves and at every one
  of its own arbitrary moves, precluding a finite target visit.
- **Infinite arenas/branching:** each promised finite set of targets has a
  finite completion time in its witness continuation. Shortest distances
  are minima of nonempty subsets of natural numbers; no finite-branching
  or compactness argument, lasso, or finite-state termination is used.
  Distances can be unbounded over the arena without increasing memory.
- **Buchi control:** Main's Example 34 is not covered by the proof. For
  Buchi payoff labels, visited-target bits need not be contained in the
  eventual payoff, and visiting each promised target once does not create
  a completed objective. Both irreversible completion and the losing-bit
  invariant used here fail to establish the needed Buchi conclusions.
  Thus the proof does not purport to contradict that lower bound.

No failed audit, timeout, confidence estimate or finite negative search was
used as mathematical evidence. The preceding triage timeout and unknown
usage remain recorded in their existing files. The researcher has found
no remaining gap in the full positive argument; an actual fresh referee
is still required before any acceptance or manuscript/PDF.
