# Fresh mathematical review

Job: `c022-spe-memory-referee-af2ba8807d2f`.
Frozen snapshot: `8167ae363386355fe869e8109b82155be5da309379f81a3f7216041bf9acf52f`.
Review date: 2026-11-02 Asia/Shanghai (2026-11-01 UTC).

**Verdict: accept the exact combined resolution-paper claim.** The immutable
original question is proved, with F(n)=n*3^n. The unconditional existence
corollary and the stated binomial lower-bound family also pass. The separate
STOC assessment is **working_paper**, not submission_ready. This is an actual
internal review, not external peer review or a mathematical truth certificate.

The review used source.md, problem.md, claim.json, the frozen snapshot and its
listed inputs, together with primary literature checked directly. Earlier
acceptances, confidence statements and supervisor descriptions were not used
as evidence of correctness. No checkpoint, scheduling state or earlier job
transcript was consulted. No frozen input was edited. All 22 frozen file hashes
and the canonical snapshot digest match; the source hash is unchanged
(`audit/referee-integrity.json`).

## Reconstruction of the compression proof

Fix the given pure SPE sigma. At each reachable augmented vertex x=(v,W),
P(x) is the set of full payoff sets of sigma after all legal histories ending
at x. This is a nonempty finite set of subsets of the n players, even for
arbitrary vertex and branching cardinalities. Its elements contain W.

For every p in P(x), successor y, and owner i of v, some q in P(y) satisfies
q_i <= p_i. To verify this, choose an actual history witnessing p. Moving to
y once and then following sigma is an admissible unilateral deviation after
that history. The SPE inequality supplies q; for the prescribed successor
the two full payoffs coincide. This holds after off-profile histories too.

For a fixed p, any witness continuation stays in X_p={x:p in P(x)}. Because
p has only finitely many targets, that continuation reaches an augmented
vertex with W=p after finitely many edges. Thus the distance d_p to the
completed set inside X_p is a finite natural number at every x in X_p.
Choosing a rank-decreasing successor when d_p>0, and an X_p successor when
d_p=0, gives one table f_p realizing p from every x in X_p. At rank zero,
W cannot grow outside p. No compactness, finite branching or uniform bound
on d_p is required. Ordinary set-theoretic choice fixes these tables.

The explicit machine stores (A,p,j), A subset p, j a player, so its state
count is n*3^n. A is the visited set before the current vertex. At v both
next and up use the same incoming memory, form B=A union t(v), and normalize
the promise at (v,B). An available p is retained. Otherwise the new promise
minimizes the payoff bit of j, the previous vertex's owner. Up stores
(B,new promise,owner(v)); next chooses the corresponding f-table move.
The next function therefore has exactly the source's pre-current-vertex
memory convention. Neither function stores a vertex, edge, expected move,
witness history or rank.

Induction over every legal history gives the correct prefix visited set
and a normalized promise in P(x), independently of compliance. Following
the constructed profile thereafter retains that promise at every step and
realizes it through f_p. In particular these are actual continuation payoffs,
not merely feasible labels.

For a player whose current promise bit is zero, consider an arbitrary
unilateral strategy change. At other players' moves the promise is retained.
At the deviator's moves it is either retained, or the previous-owner
minimizer selects a new promise whose deviator bit is still zero, by the
local inequality. All promises contain all targets already visited, so
the deviator never visits its target at any finite time. This proves the
full deviation inequality directly, including infinitely many changes.
A player with promised bit one cannot improve its Boolean payoff.

These arguments establish SPE after every legal history. The initial
promise is the given sigma's full payoff and is retained at v0. Hence the
exact payoff is preserved. This entails the original required-winner
implication for every S, including S empty, without fixing the other winners.

## Existence corollary

I checked Flesch et al., *Perfect-Information Games with Lower-Semicontinuous
Payoffs*, MOR 35(4), 742-755 (2010), Definitions 2.1-2.5, footnote 2,
Remark 2.1 and Theorem 2.3, in the frozen publisher text and the
[university-hosted primary PDF](https://cris.maastrichtuniversity.nl/ws/files/72810748/flesch_2010_perfect_information_games_with_lower.pdf).
The model permits infinite action sets and history-dependent feasible actions;
pure strategies have no measurability restriction and subgame payoffs retain
the prefix. Thus the legal-history unfolding with successors as actions fits.

The Boolean target payoff has an open one-set: a finite target visit witnesses
victory. It is bounded and lower semicontinuous, also with an uncountable
discrete alphabet. A pure subgame-perfect 1/2-equilibrium is exact because
any strict improvement is one. Applying the verified compression proves the
unconditional finite-memory assertion. Unrestricted existence and the
minimizing-deviator-payoff construction in that paper's Section 3.3 are old;
the corollary supplies no independent new existence method.

## Lower-bound proof

The quota decisions and markers define O(k^2) vertices, legal successors
everywhere, and outdegree at most two. The case k=1, with first quota zero,
also satisfies the construction; its numerical lower bound is simply one.

At a checking history with a missing index, an SPE cannot end at e: the
missing checker, on that purported e-continuation, can instead move to a
and win. This only forces the eventual terminal a; it does not force the
first unsatisfied checker to exit immediately.

The canonical profile is an SPE at all histories. A can choose any r-subset
and E subsequently chooses its complement. A wrong earlier E choice makes
coverage impossible under the fixed response quota, so E has no profitable
repair in such a subgame. At checks, a player either already won or can
exit and win; a player whose sole decision is past cannot change it in a
later subgame. Off-profile checker continuations and terminals are covered.

Now fix any E-winning SPE. Its initial outcome is e and A loses. Every
r-subset W can be selected by A unilaterally. After each such history, E
must select exactly the complement: otherwise the credible-check argument
forces a and gives A a profitable initial deviation. Distinct W must give
distinct incoming memory states of E at the same first response vertex.
Equal states there would force identical response paths, since only E has
non-forced choices during that phase. Other players' memory cannot signal
through forced moves. Thus every encoding of E's strategy has at least
binomial(k,floor(k/2)) states. The central coefficient is at least
2^k/(k+1). This is the claimed all-SPE, single-required-winner lower bound,
not a counterexample merely to the compression's chosen registers.

## Independent finite checks and scope limits

`audit/referee-checks.py` is a fresh implementation, with no imports of the
proposer's programs. It computes actual continuation payoffs on all reachable
history-product states and searches forward for arbitrary profitable
deviations at each state. It extracts P from verified original profiles,
rather than assuming a label-elimination procedure enumerates SPE payoffs.

It exhausts 1,024 positional profiles over all labelled two-vertex,
two-player arenas and targets, plus 2,000 seeded finite-machine inputs.
Of these, 2,827 are SPEs and all 2,827 recompress correctly: 11,199 original
and 10,532 compressed product positions, including seven cases with multiple
payoff labels at an augmented vertex. Initial exact payoffs and all normalized
promises are checked. Independent lower-family profiles for k=1,...,6 pass
at 4,963 legal-history product positions, and the covering response is
uniquely the complement. Explicit owner-omission and progress-omission
controls both fail as expected (`audit/referee-checks.json`).

These finite checks are supplementary falsification evidence. The general
upper theorem, infinite-arena scope, and all-k lower bound rest on the
arguments above. No formal proof assistant certification is asserted.

Other boundary checks: initial target visits are included on normalization;
empty targets and empty/full payoff sets are valid; finitely many players
is essential to finite completion; unreachable machine arguments can be
completed arbitrarily using no-dead-endness and choice. The strategy tables
are arbitrary vertex-dependent functions as the source allows. Their
computability on an infinite arena is not claimed. No quantitative,
Buchi, stochastic or general omega-regular extension is accepted.

## Current prior work and substantive value

The live [original author question](https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/)
still lists the three questions. This is page-status evidence only.

The nearest finite-arena baseline is Brihaye--Bruyere--Goeminne--Raskin,
[arXiv:1806.05544v2](https://arxiv.org/abs/1806.05544v2), related I&C 278
(2021), 104594. Proposition 9, Proposition 19 and Corollary 21 give the
Reach weak-SPE equivalence and arena-dependent lasso reconstruction;
Theorem 34 already gives constrained-existence FPT. The new theorem removes
all arena dependence and supplies the infinite-arena transformation.
The DOI refresh failed, but the actual frozen full text was available and
read; theorem numbers here refer to that full version.

A close antecedent missing from the proposer's comparison is Bruyere--Le
Roux--Pauly--Raskin, *On the existence of weak subgame perfect equilibria*,
I&C 276 (2021), 104553, DOI 10.1016/j.ic.2020.104553. In the
[author postprint](https://orbi.umons.ac.be/bitstream/20.500.12907/2750/1/ICArticleWSPEFinalVersion.pdf),
Theorem 7 uses finitely many leaf outcomes and outcome-indexed positional
paths. Its reachable absorbing-leaf hypotheses do not cover general Reach
arenas; completing the promised targets does not absorb future deviations.
Theorem 16 gives finite-range weak-SPE existence, without the general
finite-memory conclusion. This antecedent must be credited in writing.

The candidate's remaining advance is the compatibility/previous-owner
normalization for all-history SPE labels, together with finite-target
progress on a continuing arena. This supplies an explicit source-model
machine while preserving any prescribed SPE payoff. It is a substantive
extension, rather than a numerical substitution into either prior theorem.
Outcome labels, positional path selection and payoff-minimizing punishments
themselves must not be marketed as new.

[Main, I&C 309 (2026), 105425](https://doi.org/10.1016/j.ic.2026.105425),
and the frozen author text (Theorem 23, Remark 1), supply quadratic
player-dependent NE memory and the vertex/edge distinction. NE stability
does not give credible continuations. The compatibility idea has an
antecedent in his relaxation of punishment; the substantive issue here is
preserving subgame perfection.

[Reachability Games and Friends, FSTTCS 2023, Section 3.1.3](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.1)
already explains exponential SPE branching memory and clause checkers.
[Fijalkow--Horn, arXiv:1010.2420v2, Lemmas 1-2](https://arxiv.org/pdf/1010.2420v2)
gives generalized-reachability memory bounds. Consequently the new finite
family is supporting sharpness evidence, with no accepted priority claim
for exponential necessity or its precise constants.

[Alluwaym--Main--Schewe, arXiv:2607.07151v1, Theorems 7 and 10](https://arxiv.org/html/2607.07151v1)
concerns finite graphs, stationary randomized SPEs, and a pure special case
with absorbing targets. It does not give this exact-payoff-preserving pure
transformation. The inspected CONCUR 2025 paper 12 has different rational
synthesis quantifiers; the permissive-equilibrium paper arXiv:2411.13296v1
uses finite symbolic forests with arena-dependent heights and penalties.

Current searches combined Reach, SPE, infinite arenas, memory bounds,
arena independence, payoff labels and 2026 developments. No equivalent
full-scope theorem was found in this bounded primary-source review.
This is a reasoned novelty assessment, not an exhaustive priority certificate.

## Final assessment and limits

There is no identified mathematical gap in the exact frozen claim. The
uniform upper bound resolves the immutable question with substantive new
value: it separates finite internal memory from the size and branching of
the arena while keeping credible continuations at every history. The lower
bound and existence application belong coherently in the same contribution.

The record does not establish a competitive STOC case. Its new mechanism
is compact and closely related to older label/punishment constructions;
no new finite-arena FPT classification, effective infinite-arena algorithm,
broader objective class, or optimal exponential base is established.
The positive infinite-arena result is meaningful, but broad impact and
technical depth remain uncertain. See `audit/stoc-assessment.json`.
No manuscript, PDF, external submission or additional research pass was
performed by this referee.
