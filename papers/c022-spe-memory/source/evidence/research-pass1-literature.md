# Current primary-source comparison for the proposed full resolution

Job: c022-spe-memory-research-5979be48ad66. Checked 2026-11-02 Asia/Shanghai
(2026-11-01 UTC). This is the researcher's bounded comparison, not a fresh
referee verdict, exhaustive priority certificate or journal-quality judgment.
The precise proposed theorem is in `evidence/promise-reset-proof.md`.

1. **Main, Automata Exchange 25.26 (2025-07-01).** The live original
   [author question](https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/)
   was reopened. Its numbered question 3 still asks for arena-independent
   bounds for SPEs satisfying a required subset; it retains the finite-arena
   baseline m^3*n*2^(3n). No resolution is announced on the page. This is
   source-status evidence, not proof that no later resolution exists.

2. **Brihaye--Bruyere--Goeminne--Raskin, Constrained existence problem for weak
   subgame perfect equilibria with omega-regular Boolean objectives.**
   [arXiv:1806.05544v2](https://arxiv.org/abs/1806.05544v2), 2018-08-15;
   related journal publication I&C 278 (2021), 104594,
   [DOI 10.1016/j.ic.2020.104594](https://doi.org/10.1016/j.ic.2020.104594).
   The live arXiv record lists v2 as latest. Re-read cached text
   `intake/weak-spe-full.txt`: memory definition p.5, Proposition 9 p.6,
   Definitions 16/17 and Proposition 19 pp.10-12, Corollary 21 and its
   reachability proof p.19. These establish weak SPE=SPE for Reach and a
   finite-arena reconstruction storing continuation and lasso information.
   The published finite-arena bound depends on arena size. The proposed
   proof uses related payoff-credibility reasoning but replaces continuation
   identity by promise compatibility, previous-owner normalization and a
   rank-selected continuation table. The older bound alone does not yield
   either this memory bound or the arbitrary infinite-arena transformation.
   Theorem numbers above refer to the inspected 2018 full version.

3. **Main, Arena-independent memory bounds for Nash equilibria in reachability
   games, I&C 309 (2026), 105425.**
   [Publisher](https://www.sciencedirect.com/science/article/pii/S0890540126000234),
   [DOI](https://doi.org/10.1016/j.ic.2026.105425),
   [author full text](https://orbi.umons.ac.be/bitstream/20.500.12907/55655/1/main.pdf).
   Rechecked publisher statement and cached `intake/main-NE-2026.txt`,
   memory definition and Remark 1 p.5, Examples 3 and 17, Example 34
   pp.32-34. Its arena-independent reachability bounds are for NE. Remark 1
   distinguishes vertex and edge memory; the proposed proof supplies
   up(M,v) explicitly and stores only the previous owner's identity.
   Existing NE punishment tables do not establish credible continuation
   equilibria after every history. Its Buchi lower-bound example does not
   refute the Reach construction, which relies on irreversible finite
   target completion. No general omega-regular theorem is proposed.

4. **Bruyere--Raskin--Reynouard--Van Den Bogaard, CONCUR 2025, paper 12.**
   [Primary full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol348-concur2025/html/LIPIcs.CONCUR.2025.12/LIPIcs.CONCUR.2025.12.html),
   [DOI](https://doi.org/10.4230/LIPIcs.CONCUR.2025.12).
   Reopened abstract, reachability discussion, Remark 21 and conclusion.
   A system commits a strategy and must handle all rational environment
   responses, a different strategy-quantifier problem. Its construction
   does not state the proposed pure, exact-payoff-preserving memory
   transformation for every player on arbitrary arenas.

5. **Alluwaym--Main--Schewe, Simple Nash Equilibria for Qualitative Multiplayer
   Games, arXiv:2607.07151v1 (2026-07-08).**
   [Primary full text](https://arxiv.org/html/2607.07151v1).
   Re-read finite-arena definition, Section 4 including Theorem 7's proof,
   Theorem 10 and conclusion. The general SPE result is randomized
   stationary on finite graphs. The pure positional special case assumes
   absorbing targets/unsafe states. It does not preserve an arbitrary
   pure SPE payoff or cover arbitrary infinite arenas. The conclusion's
   positional existence question differs from the present finite-memory
   constrained transformation; the proposed theorem does not answer that
   positional question.

6. **Goeminne--Monmege, Permissive Equilibria in Multiplayer Reachability Games,
   arXiv:2411.13296v1 (2024-11-20).**
   [Primary full text](https://arxiv.org/html/2411.13296v1),
   [version record](https://arxiv.org/abs/2411.13296).
   Newly checked finite-arena definition, Section 5 symbolic forests,
   Corollary 13, Theorem 15 and conclusion. This studies penalties and
   multi-strategies all of whose refinements are equilibria. Its finite
   symbolic trees have height depending on the number of vertices and
   penalty bounds. These statements supply neither the proposed
   arena-independent vertex-memory bound nor its arbitrary-arena scope.

7. **Brihaye--Goeminne--Main--Randour, Reachability Games and Friends,
   FSTTCS 2023, paper 1.**
   [Primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol284-fsttcs2023/LIPIcs.FSTTCS.2023.1/LIPIcs.FSTTCS.2023.1.pdf),
   DOI 10.4230/LIPIcs.FSTTCS.2023.1. Inspected pp.1:11-1:12, which discuss
   branching memory for constrained SPEs and recover a bound polynomial in
   arena size and exponential in the number of players from the prior
   symbolic representation. The survey uses edge updates and warns that
   vertex-update bounds can differ. It does not give the proposed bound.

## Search coverage and proposed substantive delta

Fresh queries included combinations of reachability, pure SPE, subgame
perfect equilibria, arena-independent, memory bounds, 2026, Main, and payoff
promises. Search results were leads only; the comparisons above use primary
text. No equivalent full-scope resolution was found in this bounded search.
There is no claim of complete bibliographic or historical-registry coverage.

The proposed delta is an explicit n*3^n vertex-update bound preserving the
EXACT payoff of every given pure SPE on every set-sized, arbitrarily
branching arena. It removes arena-size dependence from the stated older
finite-arena bound and establishes the conditional infinite-arena statement.
The new step is the rule that preserves any still-available promise and
otherwise selects a credible payoff minimizing the previous owner's bit;
no expected edge or continuation vertex is tested or stored. Cooperative
finite target completion makes globally selected progress tables possible.
This is a new strategy uniformization argument relative to the inspected
results, rather than a numerical substitution into their stated bounds.
Its correctness, novelty and theoretical significance remain for the fresh
referee to assess independently. No STOC suitability or acceptance is asserted.
