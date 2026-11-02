# Exponential memory is necessary for constrained pure SPEs

Job: `c022-spe-memory-research-776ae007899c`, research pass 2.
This is a mathematical research argument submitted for fresh review, not an
acceptance report. It refutes the proposed polynomial strengthening, not the
immutable original question, whose arena-independent upper bound is retained.

## Statement

For every integer k >= 1 there is a finite (k+2)-player Boolean reachability
game G_k, with O(k^2) vertices, maximum outdegree two, and no cycles except
absorbing terminal loops, with the following properties:

1. There is a pure SPE whose outcome wins for player E.
2. In EVERY pure SPE whose outcome wins for E, player E's strategy requires
   at least binomial(k, floor(k/2)) vertex-update memory states.

There is no restriction on the other players' memories or extra winners.
In particular a polynomial-in-n bound cannot replace n*3^n in the original
required-winner implication or in the stronger exact-payoff transformation.
Indeed binomial(k,floor(k/2)) >= 2^k/(k+1).
This is an all-SPE lower bound with required set S={E}, not a state-count
obstruction for the promise-reset proof.

The construction uses familiar generalized-reachability subset memory and
credible clause-checking from prior work. It is supporting sharpness evidence
for the same upper-bound result, with no claim of an independent new method
or of priority for exponential necessity; see literature.md.

## Exact arena

Players are A, E, C_1,...,C_k. Put r=floor(k/2). A play first passes through
an A-controlled selection phase selecting exactly r indices from [k], then
an E-controlled selection phase selecting exactly k-r indices. The selected
sets are denoted W and U. Both phases examine indices 1,...,k in order,
include or exclude each index, and merge all histories at the end of the
phase. Thus every r-subset W leads to the SAME first E decision vertex.

For completeness, a selection phase with quota b uses decision vertices
q(i,c), where 0 <= i < k indices have been examined and c selected, and
0 <= c <= i, c <= b <= c+k-i. For d in {0,1} allow the choice d exactly
when c+d <= b <= c+d+k-i-1. The corresponding edge leads to a marker
z(i,c,d), then to q(i+1,c+d), or to the next phase if i+1=k.
All decisions in the phase belong to its selecting player; marker ownership
is immaterial because markers have one successor. If d=1 the marker belongs
to target C_(i+1); if d=0 it belongs to no target. The two phases have
disjoint vertices. Their initial count is zero. Every decision has at least
one and at most two successors. The counter is part of the actual arena
vertex, not a strategy register. There are O(k^2) such vertices.

After E's phase, play visits c_1,...,c_k in order. At c_i, player C_i may
continue to c_(i+1) (or to terminal e when i=k), or go to terminal a.
Both terminals have only a self-loop. Player A's target is {a}; E's target
is {e}; C_i's target consists of a and all inclusion markers of index i in
either selection phase. No other vertex belongs to any target. Initial
vertex is the first A decision. Ownership of terminals may be assigned to A.

This specifies a finite no-dead-end turn-based game in exactly source.md's
Boolean target and vertex-update model. The exact generator is family(k)
in `code/check_subset_memory.py` (zero-based indices there).

## Credible-check lemma

Fix any pure SPE sigma and any legal history entering the checking chain,
after selections W,U. If W union U != [k], its sigma continuation ends at a.

Proof: If instead it ended at e, all checking nodes would have been visited
and every C_i outside W union U would receive zero. At the actual history
ending at c_i that player can move directly to a and receive one. This
contradicts SPE after that history. The checking chain is finite, so its only
other outcome is a. This does not assume that an unsatisfied checker always
exits immediately: it may also get one from a later exit. The conclusion is
about the terminal outcome. The lemma applies to every legal checking
history, including those reached by an A deviation.

## Existence of an E-winning SPE, with all-history verification

Use these strategies. A selects any fixed legal choices. E remembers W.
At its index i decision E tries to include i iff i is outside W; if that
choice is illegal because of previous off-profile choices, E chooses any
legal choice. At c_i, C_i continues if its target was already visited and
otherwise exits to a. Terminals and markers have forced moves.

At a history in A's phase, every continuation of A's choices yields some
r-subset W, and E subsequently selects its complement. Thus all checkers
are satisfied and continue to e; A gets zero regardless of a unilateral
deviation, while every other player gets one. At a history in E's phase,
if E's earlier selections agree with the complement of W, the strategy
continues to its unique complementary completion, which is legal, and E
gets one. If an earlier E decision disagreed, no legal completion can cover
all indices: a complement index already omitted cannot be recovered, or an
index of W already included consumes one of the exactly k-r slots. Under
the specified checker strategies a missing index causes exit to a. Hence
E cannot gain by any strategy change from such a history. A has no further
choices in E's phase. At every checking history, a satisfied checker already
gets one, and an unsatisfied checker exits to a and gets one. A checker
whose node is past cannot affect the future; E and A have no further
nontrivial moves. The same assertions cover histories after arbitrary
previous checking deviations and both terminals.

Therefore no player has a profitable unilateral strategy change after ANY
legal history. Initially E and all C_i win, while A loses. E's strategy is
implementable with at most 2^k vertex-update states storing W, setting or
clearing bit i upon processing an A marker of index i. Its next move uses
only the incoming memory and the current E decision vertex. Each C_i needs
only its own visited-target bit (two states); A is positional. The current
decision vertices have no target bits, so the source convention that memory
omits the current vertex causes no discrepancy. No previous vertex is stored.

## Lower bound for every E-winning SPE

Fix any pure SPE sigma initially winning for E. Its initial outcome reaches
e and gives A zero. Freeze all strategies except A's. Player A can select
ANY r-subset W during its phase. This unilateral deviation must still give
A zero, since sigma is an NE at the initial history. After any such W,
E's prescribed response selects exactly k-r indices U. If W union U were
not [k], the credible-check lemma at that legal history would give terminal
a, a profitable deviation for A. Thus for EVERY W, E's prescribed response
must be U=[k] minus W. All quantifiers here refer to the single fixed sigma,
and its credibility after the off-profile histories reached by A's choices.

Let m(W) be the incoming state of any finite vertex-update machine encoding
sigma_E at the common first E decision vertex, after the A history selecting
W has been processed. If m(W)=m(W') for distinct r-subsets W,W', determinism
forces E to produce exactly the same subsequent vertex sequence in its
phase: the current vertex is identical, next uses the same state and vertex,
and up also processes the same vertex at each step. All other moves in
that phase are forced. The selected set U is consequently identical. But
it would have to equal both [k] minus W and [k] minus W', impossible.
Thus W -> m(W) is injective and the machine has at least binomial(k,r)
states. Other players' memories cannot transmit information during E's
selection phase, where they have no nontrivial moves. Arbitrary
vertex-dependent tables do not evade a collision at the SAME actual vertex.

The central binomial coefficient is the maximum of k+1 coefficients whose
sum is 2^k, so it is at least 2^k/(k+1). With n=k+2 this is exponential
in n and rules out every polynomial bound on the original required-winner
problem. It leaves n*3^n valid and does not prove its exact base or optimal
constant. A generic transfer of stronger generalized-reachability lower
bounds involving infinite nontermination would need a separate argument:
failure of E to terminate need not make A win. No such transfer is used.

## Exact finite checks and limits

Run `python3 code/check_subset_memory.py`. The serialized result is
`evidence/research-pass2/subset-memory-checks.json`. For k=1,...,7 the
canonical profiles pass exact best-response reachability after every legal
history, exploring 15,787 product positions in total. All legal edges are
used to reach history states. With opponents fixed, every deviator's edge
remains available; reverse target reachability tests arbitrary unilateral
strategies, not only one-shot moves. For k=1,...,12 all pairs of allowed
W,U are checked and the sole covering response is the complement.

A deliberately forgetful E control is rejected already at k=2: its
initial outcome still wins for E, but A can choose W={1} and make E repeat
that selection, leaving index 2 missing and inducing terminal a. The exact
vertex witness is serialized. Finite checks validate the implementation and
falsify that control; the all-k injectivity proof above establishes the
lower bound. Neither arbitrary strategies nor all machines are exhaustively
enumerated by the finite program. Fresh proof/novelty review remains required.
