# Bounded source and suitability assessment

Job: `c022-spe-memory-triage-3c055ee6378d`.
Inspection date: 2026-11-02 Asia/Shanghai (2026-11-01 UTC).
Decision: **advance to bounded research**, not acceptance or a candidate.

## Recovery integrity

Contrary to the launch description of a completed preserved triage, the
actual `triage-recovery.md` says the preceding job was incomplete and
records `problem_file_exists=false`. On entry `problem.md` was absent and
`checkpoint.md` contained only the initial no-research instruction.
Source and checkpoint matched the recorded hashes exactly. Thus there was
no completed scope/decision packet to validate. This job fills that gap;
it neither resets usage nor repeats retrieval of the unchanged cached PDFs.
The preceding timeout remains an operational failure, not mathematics.

## Primary material actually inspected

1. [Main, Automata Exchange 25.26, 2025-07-01](https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/).
   The live page's introduction and three questions were read. Question 3
   asks for arena-independent memory for SPEs satisfying required
   objectives. The page retains the arena-dependent finite-arena baseline;
   it does not announce a resolution. This supports the lead's status,
   rather than proving absence of later work.

2. [Brihaye, Bruyere, Goeminne, Raskin, arXiv:1806.05544v2](https://arxiv.org/abs/1806.05544v2),
   cached `intake/weak-spe-full.pdf` and `.txt`. Read Definition 1 (p.3:
   finite graph), memory definition (p.5), Definitions 4/6 and Propositions
   7/9 (pp.5-6), Proposition 19 construction (p.12), Corollary 21 (p.13),
   and its reachability reduction proof (p.19). The construction remembers
   a deviating player and continuation vertex plus a lasso position.
   Reachability is converted using visited-target bits. Its established
   bound remains O(|V|^3 n 2^(3n)). The finite-witness proof of Proposition
   9 truncates a profitable deviation at its first target visit; it supplies
   a useful credibility test, not an arena-independent construction.
   These theorem numbers belong to the inspected 2018 full version,
   related to I&C 278 (2021), 104594, not an assertion of identical numbering.

3. [Main, Arena-independent memory bounds for Nash equilibria in reachability games, I&C 309 (2026), 105425](https://www.sciencedirect.com/science/article/pii/S0890540126000234),
   DOI 10.1016/j.ic.2026.105425. Read publisher abstract/introduction and
   cached author full text `intake/main-NE-2026.txt`, Table 1 (p.3), memory
   definition/Remark 1 (p.5), and Example 34 (pp.32-33).
   [Cached author-version origin](https://orbi.umons.ac.be/bitstream/20.500.12907/55655/1/main.pdf).
   The author-version reachability upper bound n^2 is for NE, not SPE.
   Its vertex/edge-memory distinction matters on infinite arenas and for
   size bounds. The Buchi/coBuchi lower-bound control uses different
   objectives and does not refute this reachability question.

4. [Bruyere, Raskin, Reynouard, Van Den Bogaard, CONCUR 2025 paper 12](https://drops.dagstuhl.de/storage/00lipics/lipics-vol348-concur2025/html/LIPIcs.CONCUR.2025.12/LIPIcs.CONCUR.2025.12.html),
   DOI 10.4230/LIPIcs.CONCUR.2025.12. Read abstract/introduction,
   reachability discussion before Remark 21, Remark 21 and conclusion.
   A system commits a strategy and faces all rational environment responses;
   this differs from existential constrained SPE-profile selection here.
   The stated finite-memory system solution and complexity results do not
   give an arena-independent bound for all players' pure SPE strategies.

5. NEW comparison: [Alluwaym, Main, Schewe, Simple Nash Equilibria for Qualitative Multiplayer Games, arXiv:2607.07151v1](https://arxiv.org/html/2607.07151v1),
   submitted 2026-07-08; the inspected abstract page lists only v1 and calls
   it an MFCS 2026 preprint. Read abstract, introduction, related work,
   Theorem 10 and conclusion. The arena is finite and the general SPE
   construction is randomized stationary. Theorem 10 gives a pure
   memoryless existence result with absorbing targets/unsafe vertices.
   The paper discusses constrained pure equilibria separately. Neither
   randomization nor the absorbing-target restriction resolves the frozen
   pure, arbitrary-target, prescribed-winner, infinite-arena statement.
   Its conclusion leaves positional existence in all-reachability games
   open, a related but different question.

## Search coverage and duplicate limitation

Fresh web queries were `"subgame-perfect" "arena-independent" reachability
memory 2026` and `"Memory Requirements" "Subgame" "Reachability" Main`.
They surfaced the 2026 randomized result, which was checked in primary full
text. No equivalent full resolution was found in this bounded check.
Search results alone were not treated as theorem evidence. Cached primary
PDFs were reused rather than downloaded again. No historical registry was
provided within this project; no global duplicate clearance is asserted.
The immutable normalized scope is recorded for supervisor comparison.

## Cheapest discriminating test and next test

Definition/scope comparison passes: the live author question is the intended
question 3, the finite-arena bound retains |V|, and the newer NE/randomized
SPE/synthesis results have materially different conclusions or quantifiers.
Thus the target is not an immediate corollary of those inspected results.
The all-history condition and the vertex-update convention eliminate two
plausible but unsound shortcuts. No new original theorem or counterexample
was proved in triage.

One bounded research test: attempt a vertex-update compression of
Proposition 19's continuation indices using visited targets, promised payoff,
last deviator and next target; check both one-shot incentives and actual
target progress. Inspect a small finite merging-history example first for
incompatible required continuation moves in the same proposed mode. An
exact collision falsifies the proposed compression, not the original
question. If it survives, write explicit up/next and address arbitrary
branching and infinite arenas before claiming any upper bound.

The expected payoff is substantive: resolve the full arena-independent
question, positively or by an all-SPE lower-bound family. The finite-witness
property and existing symbolic-witness construction give a concrete first
attack rather than mere confidence. Research remains limited to three
accumulated 25-minute passes; no pass has been consumed here. No manuscript,
PDF, acceptance record, or scheduler edit was created.
