# Checkpoint

## Research pass 2 — c022-spe-memory-research-776ae007899c

**Decision:** candidate, resolution-paper, original status proved as a research
proof claim. This requests fresh review; it creates no mathematical acceptance,
manuscript, PDF, release, or submission-ready classification. It is the SAME
paper's revised scope. The old conditional v1 packet and its working_paper
assessment remain unchanged under `history/conditional-v1/`; that acceptance
does not certify this combined scope.

**Original scope retained:** source.md is still SHA-256
`9dd4ff19af8a2996db2a11e18b2a4caa65426f62647822995c446c31dd0899fe`.
The full exact-payoff compression, with n*3^n VERTEX-update states, arbitrary
set-sized/branching arenas, every legal history, prefix targets and every
required winner subset allowing extra winners, is unchanged in
`evidence/promise-reset-proof.md`. No hidden previous vertex is introduced.
All twelve historical mathematical frozen files were verified at entry;
old claims, reviews and manuscripts were not edited. problem.md is unchanged.

**New evidence:** `evidence/research-pass2/combined-theorem.md` checks the
actual Flesch et al. 2010 primary hypotheses: arbitrary nonempty action sets,
whole-history feasible actions, pure strategies, prefix-retaining subgames,
and bounded lower-semicontinuous payoffs. Boolean Reach qualifies;
epsilon=1/2 makes its SPE exact. Compression gives unconditional n*3^n-memory
SPE existence on the full arena scope. Unrestricted existence is OLD; this
corollary adds no independent new technique or algorithmic FPT claim. The
finite-arena constrained-SPE FPT baseline is also already known.

**Decisive polynomial-bound test:**
`evidence/research-pass2/exponential-lower-bound.md` gives a complete family
with n=k+2 players, O(k^2) vertices, outdegree at most two and required set
S={E}. An E-winning pure SPE exists, but EVERY such SPE requires at least
binomial(k,floor(k/2)) >= 2^k/(k+1) states for E, regardless of other players'
memory. A chooses an r-subset, E must supply its complement, and credible
checkers make failure profitable to A. At the common first E vertex all
r-subsets need distinct incoming states. This rules out the proposed
polynomial strengthening in the actual all-SPE scope. It does not refute the
original positive question or establish the exact optimal exponential base.

**Verification:** `python3 code/check_subset_memory.py` checks the canonical
SPE after ALL legal histories for k=1..7 (15,787 product positions), and all
allowed subset/response pairs for k=1..12. A forgetful E control is rejected
with a serialized profitable A deviation despite its E-winning initial
outcome. Exact results are `evidence/research-pass2/subset-memory-checks.json`.
The infinite family follows from the proof, not extrapolation. The subtle
false assertion that every unsatisfied checker immediately exits was avoided;
only the proved terminal-outcome lemma is used.

**Prior work/value limits:** fresh primary comparison is
`evidence/research-pass2/literature.md`. The 2023 primary survey already
establishes exponential SPE branching-memory necessity; the lower bound here
is supporting sharpness evidence, not an independent qualitative novelty.
No equivalent full-scope upper theorem was found in this bounded search;
priority remains for fresh review. Two optional shell downloads failed;
web access supplied actual primary PDF text. This is operational evidence,
not a mathematical obstruction. No numerical acceptance chance is asserted.

**Preservation:** new `claim.json` uses kind/statement and the actual proposer
job ID, includes source.md and problem.md, and binds decisive evidence.
`evidence/research-pass2/integrity.json` records this pass. Entry checkpoint
is preserved beside it. Runner research_passes=2 was observed; counters,
state.json, scheduling, failed routes and usage were not reset or edited.
No agent, other Codex process, background worker or external contact was used.
The preceding triage timeout remains an operational historical fact.

**One next test:** freeze this exact combined claim for a genuinely fresh
REFEREE to check full original-scope compression, the arbitrary-action
Flesch application, the ALL-SPE binomial lower bound, current novelty and
actual STOC value against cited primary results. New acceptance and required
innovation/STOC records must precede writing; retain working_paper unless the
actual fresh venue assessment supports otherwise. No automatic third
research pass is requested.
