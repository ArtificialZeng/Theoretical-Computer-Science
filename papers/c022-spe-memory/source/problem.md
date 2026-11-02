# Precise original problem

Triage job: `c022-spe-memory-triage-3c055ee6378d`.
The immutable statement is `source.md`, SHA-256
`9dd4ff19af8a2996db2a11e18b2a4caa65426f62647822995c446c31dd0899fe`.
This file interprets that statement; it does not replace or narrow it.

## Objects and quantifiers

Let n >= 1 and P = {1,...,n}. An arena is a directed graph (V,E), a
partition (V_i) indexed by P, and an initial vertex v0. Every vertex has a
successor. V and successor sets may be infinite; no countability, finite
branching, or bounded-degree assumption is imposed. Each player i has a
target T_i contained in V. A play is an infinite legal path. Its Boolean
payoff for i is 1 exactly when some vertex of the play belongs to T_i.

A pure strategy selects a legal successor at every finite legal history
from v0 ending in a vertex controlled by that player. A profile is an SPE
if, after EVERY legal history from v0, no player has a unilateral strategy
change giving a strictly higher Boolean payoff. Histories need not be
consistent with the profile. The payoff in a subgame is evaluated on the
prefix followed by the continuation: any target already visited stays won.

A strategy has at most b memory states if there are a nonempty finite set
M with |M| <= b, initial state m0, and functions
`up: M x V -> M`, `next_i: M x V_i -> V`, with legal outputs, such that
at history h v its move is `next_i(up*(m0,h),v)`. Here h omits the current
vertex v, and up* is iteration over the vertices of h. Each player may
have its own machine. Arbitrary vertex-dependent functions are allowed;
the bound measures states, not table encoding or computability.

The question is whether there exists a function F from positive integers
to positive integers such that, for every n, every such arena and targets,
and every required set S contained in P (including the empty set):

> If some pure SPE from v0 has an outcome winning for every i in S,
> then some pure SPE from v0 has an outcome winning for every i in S
> and every player's strategy has at most F(n) states.

Other players may also win. A positive answer must cover infinite arenas
with arbitrary branching. A negative answer may use a fixed n and finite
arenas indexed by b, each admitting an S-winning SPE but admitting none
whose players all use at most b states. Ruling out one profile, one exact
payoff vector, or a proposed intermediate lemma is insufficient.

## Nearest results and proposed substantive delta

The original author question is Automata Exchange 25.26, question 3,
posted 2025-07-01. Its finite-arena baseline depends cubically on arena
size. The cached Brihaye--Bruyere--Goeminne--Raskin full version
arXiv:1806.05544v2 has vertex-update memory (p.5), weak SPE = SPE for
Boolean reachability (Proposition 9, p.6), and finite-arena bound
O(|V|^3 n 2^(3n)) (Corollary 21, p.13; proof p.19).
Main's 2026 I&C paper concerns NASH equilibria. Its author version's
Remark 1 explicitly warns that edge-update memory cannot be substituted
at the same bound. CONCUR 2025 paper 12 treats rational synthesis with
different strategy quantifiers. Alluwaym--Main--Schewe, arXiv:2607.07151v1,
treats randomized stationary SPEs on finite graphs; its restricted pure
result assumes absorbing targets. These do not supply the target theorem.
Precise inspected passages and limitations are in
`evidence/triage-assessment.md`.

Source status: **open-supported within this bounded primary-source check**;
original mathematical status: **unresolved**. No exhaustive novelty or
historical-registry clearance is asserted.

Proposed delta: remove all arena-size dependence for pure constrained SPEs
in the full above scope, or refute it by an all-SPE lower bound. Either
would address the stated source question and have plausible substantive
value beyond the known finite-arena and NE results.

## Bounded first test

Test a reachability-specific compression of the old symbolic-witness
construction: replace stored continuation vertex/lasso position by modes
containing visited-target bits, a promised Boolean payoff, last-deviator
identity, and a next promised target. Attempt to define actual vertex-update
functions and verify (a) one-shot incentive inequalities at every legal
history and (b) eventual fulfillment of promised, not-yet-won targets.
The finite-witness argument behind Proposition 9 motivates this test;
it does not prove the compression. First seek a small exact finite-arena
collision of modes that invalidates the compression, or an explicit
uniform selection/progress argument that survives it. A failure concerns
this route only. Keep infinite-arena selection and progress as explicit
obligations; finite testing cannot prove the positive statement.


## Research pass 1 proposal (not fresh acceptance)

Job `c022-spe-memory-research-5979be48ad66` proposes a complete positive
resolution with F(n)=n*3^n, preserving the exact payoff of any given pure
SPE. The quantifiers and memory model above are unchanged. The full proof
is `evidence/promise-reset-proof.md`; source comparison and verification
limits are `evidence/research-pass1-literature.md` and
`evidence/research-pass1-adversarial.md`. This supersedes the triage's
unresolved working status only as a research proof claim submitted for
fresh review; it is not mathematical acceptance or a publication verdict.
