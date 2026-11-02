# Checkpoint

## Research pass 1 — c022-spe-memory-research-5979be48ad66

Decision: **candidate**, kind **resolution-paper**. Researcher's proposed
original status: **proved**, subject to actual fresh referee review. No
acceptance, manuscript/PDF, or release record was created. The immutable
`source.md` remains byte-for-byte unchanged (SHA-256
`9dd4ff19af8a2996db2a11e18b2a4caa65426f62647822995c446c31dd0899fe`).

**Claim:** Every given pure SPE in an arbitrary no-dead-end n-player Boolean
reachability arena has an exact-payoff-equivalent pure SPE using at most
n*3^n VERTEX-update states per player. This covers possibly infinite,
arbitrarily branching arenas and every required winner subset, allowing
extra winners. SPE is checked after every legal history and includes
targets visited before the subgame. No quantifier has been narrowed.

**New decisive artifact:** `evidence/promise-reset-proof.md` supplies the
complete argument and explicit up/next functions. From the given SPE, label
each augmented vertex (v,visited targets) by all full subgame payoffs seen
after legal histories. These finite nonempty sets satisfy local credibility.
A promise is retained whenever available; otherwise the new promise minimizes
the previous owner's payoff bit. Memory stores only visited bits, promise,
and previous owner. Vertex-dependent selectors decrease natural-number
distance to completion of the promised finite target set. No vertex, edge,
continuation position or rank value is stored. A losing-bit invariant rules
out arbitrary unilateral deviations after every legal history. Known
mathematical gaps: none found by the researcher; independent review pending.

**Exact checks:** `code/check_promise_reset.py` and
`evidence/promise-reset-finite-checks.json` cover all 576 labelled
2-vertex/2-player arenas and 1,000 seeded games with 1-4 players and
3-8 vertices. They check 1,848 constructed profiles over 21,187 legal-history
product positions, with opponents fixed in each best-response search. These
are finite falsification checks; the infinite theorem depends on the proof.
`evidence/research-pass1-adversarial.md` records exact failures of the
owner-free reset and rank-free selector variants, plus correct rejection
of an off-path noncredible NE threat. None is a disproof of the original.

**Current prior-work check:** `evidence/research-pass1-literature.md`
rechecks the original author question, the old symbolic witness result,
Main 2026 NE bounds, CONCUR 2025 synthesis, the July 2026 randomized-SPE
paper, permissive equilibria, and the FSTTCS 2023 survey. No equivalent
full resolution was found in this bounded primary-source inspection.
The proposed substantive delta is removal of all arena dependence, with
explicit vertex updates and credible continuations on arbitrary arenas.
Novelty/significance must still pass the fresh referee; no STOC judgment.

**Counters and operational history:** The runner's state was observed with
research_passes=1; the worker did not edit it or any scheduling state. At most
three accumulated research passes are authorized; this job uses the first.
Triage `c022-spe-memory-triage-3c055ee6378d` advanced after recovering the
incomplete timeout job `c022-spe-memory-triage-7aa11f697acb`; its unknown
usage was not reset. The prior checkpoint is preserved at
`evidence/checkpoint-at-research-entry.md`; original triage evidence and
`triage-recovery.md` remain. No agents or background workers were used.

**One next test:** A fresh referee should try to falsify the promise-reset
uniformization lemma in `evidence/promise-reset-proof.md`, especially the
local-label inequality and source-only update at merging histories, and
check current novelty and substantive significance before any acceptance.
The runner owns freezing, actual check-math and subsequent gates.
