# Same-paper combined scope for a fresh mathematical review

Proposer: `c022-spe-memory-research-776ae007899c`, research pass 2.
The immutable statement and its interpretation remain `source.md` and
`problem.md`, byte-unchanged. No prior acceptance is extended by this file.

## Primary theorem: exact-payoff compression

For every n >= 1, every set-sized no-dead-end turn-based n-player arena,
with arbitrary branching, initial vertex and Boolean reachability targets,
every pure SPE has an exact-payoff-equivalent pure SPE using at most n*3^n
VERTEX-update states per player. SPE is required after every legal history,
and prefix target visits are retained. The strategy convention is precisely
next_i(up*(m0,h),v) at history hv; arbitrary vertex-dependent tables are
allowed. This fully resolves the required-winner implication for every S
in source.md, with no finiteness or extra-winner restriction.

The complete argument is the unchanged `evidence/promise-reset-proof.md`:
SPE continuation payoffs supply finite labels P(v,W); every label has locally
credible successor labels and a finite path to fulfilling all promised
targets. Natural-number distance to that completed visited set gives uniform
progress without storing a rank. A promise is retained whenever available;
otherwise a credible label minimizing the previous owner's payoff is chosen.
The machine stores (previously visited set A, promised payoff p, previous
owner j), with A subset p, giving n*3^n states. A losing deviator's bit stays
zero along any unilateral deviation, and every normalized continuation
realizes its exact promise. No hidden vertex or expected edge is stored.

The complete compression argument is included in the proposed evidence
packet without alteration. This combined claim requires a genuinely fresh
review of the actual proof and of each added assertion.

## Verified existence consequence from Flesch et al. (2010)

Primary source: J. Flesch, J. Kuipers, A. Mashiah-Yaakovi, G. Schoenmakers,
E. Solan and K. Vrieze, *Perfect-Information Games with Lower-Semicontinuous
Payoffs*, Mathematics of Operations Research 35(4), 742-755 (2010),
DOI [10.1287/moor.1100.0469](https://doi.org/10.1287/moor.1100.0469).
The actual publisher-version input and extracted text are in
`intake/flesch-existence/`; the PDF hash is
70cb24306f70a0bdc4690f527f54d9184c82d9ed347335e8c5d5342ebbd93572.

Their Definition 2.1 and footnote 2 allow a nonempty action set of arbitrary
cardinality and finitely many players. Remark 2.1 permits feasible actions
depending on the entire history. Definition 2.2 imposes no measurability
condition on pure strategies. Definition 2.4 evaluates a subgame with its
actual prefix retained. Theorem 2.3 supplies a pure subgame-perfect epsilon
equilibrium for every epsilon>0 for bounded lower-semicontinuous payoffs.

Unfold the given arena into the set of its legal histories from v0. The
active player at a history ending in v is its arena owner and the feasible
action set is Succ(v), a nonempty set. These are precisely the histories
and pure strategies of the original game. If desired use V as a common
action alphabet with the legal successor restriction of Remark 2.1; no
countability or finite-branching hypothesis is introduced. For each player,
the payoff is the indicator of visiting its target in the full play,
including v0. Its one-set is open in the discrete-alphabet product topology:
one finite target visit witnesses membership, and every legal extension
keeps that payoff. Therefore the payoff is lower semicontinuous and bounded.
This covers empty targets, initial visits and arbitrary target cardinality.

Apply Theorem 2.3 with epsilon=1/2. In every subgame a profitable Boolean
deviation would change zero to one, an improvement greater than epsilon,
contradicting that theorem's inequality. The obtained profile is thus an
EXACT pure SPE after every legal history. Apply the compression theorem to
this profile. It follows that EVERY arena in the full above scope admits a
pure SPE using at most n*3^n vertex-update states per player.

The unrestricted existence theorem is OLD; the finite-memory conclusion is
a direct corollary of it and the proposed new compression. This corollary
answers question 1 in the author's list, while exact-payoff compression
answers questions 2 and 3. It supplies neither a new existence technique nor
an effective infinite-arena algorithm. No claim of algorithmic FPT novelty
is made: the finite-arena constrained-SPE FPT baseline is already prior work.

## Quantitative limitation: polynomial memory is impossible

For n=k+2, k>=1, the finite bounded-degree family in
`evidence/research-pass2/exponential-lower-bound.md` admits an E-winning pure
SPE, but EVERY E-winning pure SPE requires at least
binomial(k,floor(k/2)) >= 2^k/(k+1) states for player E, without restricting
the other players' memories. Thus exponential dependence on n is necessary
even for a singleton required winner set and finite arenas of O(n^2) size.
This resolves the supervisor's proposed polynomial strengthening negatively
by a genuine strategy lower bound, not only a failure of the present proof.

The subset-memory and credible-checking ideas are standard antecedents.
This supporting lower bound is not marketed as a standalone novelty. The
main proposed substantive innovation remains the full arena-independent
upper-bound construction. The two bounds match at the level 2^{Theta(n)},
not in the exponential base or the exact optimal function.

## Dependencies, gaps and significance limits

Dependencies: the unchanged complete compression proof; ordinary choice for
set-sized vertex tables; Flesch et al.'s actual Theorem 2.3 with its stated
arbitrary-action and history-dependent-action scope; and the complete finite
lower-bound construction and injectivity proof. Known mathematical gaps in
this combined argument: none identified by the proposer. This is a proposed
resolution, subject to fresh scrutiny, not mathematical acceptance.

All original quantifiers, the memory model and negative-answer scope remain
unchanged. No optimal exponential base, positional existence, randomized
bound, quantitative objective, or general omega-regular extension is claimed.
Current primary-source comparison is in `evidence/research-pass2/literature.md`.
The routine existence corollary and standard-type lower-bound evidence do
not independently establish venue-level significance. A fresh referee must
separately assess correctness, substantive innovation and actual STOC
importance/depth/breadth. No manuscript or PDF is created during this
research phase.
