# Current primary-source comparison for combined scope

Job `c022-spe-memory-research-776ae007899c`; checked 2026-11-02 Asia/Shanghai
(2026-11-01 UTC). This is the researcher's bounded literature check, not
an independent novelty verdict or exhaustive priority claim. The decisive
mathematics is in combined-theorem.md and exponential-lower-bound.md.

1. **Original question.** James C. A. Main's
   [Automata Exchange 25.26](https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/)
   was reopened live. The page still lists infinite-arena finite-memory
   existence, preservation of a given SPE's objectives, and arena-independent
   bounds as its three questions. No resolution notice appears. This is
   evidence about that page, not a universal claim of open status.

2. **Known finite-arena SPE baseline.** Brihaye, Bruyere, Goeminne and Raskin,
   [arXiv:1806.05544](https://arxiv.org/abs/1806.05544), current record v2,
   2018-08-15; journal I&C 278 (2021), 104594,
   [DOI](https://doi.org/10.1016/j.ic.2020.104594).
   Actual cached text `intake/weak-spe-full.txt`: p.5 has vertex updates;
   Proposition 9 identifies weak SPE and SPE for Boolean Reach; Corollary 21
   has arena-dependent memory. Proposition 27, pp.16-18, supplies the QBF
   clause-player checking mechanism, a direct antecedent of the lower-bound
   checks. Theorem 34 already proves finite-arena constrained-existence FPT
   in player count. Our proposed new contribution is the explicit uniform
   n*3^n vertex-memory upper bound on arbitrary set-sized arenas, not FPT,
   weak-SPE equivalence, or credible clause checks.

3. **Known exponential necessity.** Brihaye, Goeminne, Main and Randour,
   *Reachability Games and Friends*, FSTTCS 2023, paper 1,
   [primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol284-fsttcs2023/LIPIcs.FSTTCS.2023.1/LIPIcs.FSTTCS.2023.1.pdf),
   DOI 10.4230/LIPIcs.FSTTCS.2023.1. Live full text Section 3.1.3,
   printed pp.1:10-1:12, explicitly describes exponential branching memory
   for SPEs and its generalized-reachability origin. Its formula (1) forces
   complementary bit strings; its QBF2 construction uses clause checkers.
   Therefore merely refuting polynomial constrained-SPE memory is NOT a new
   qualitative discovery. The O(k^2), degree-two family and binomial(k,k/2)
   lower bound in this pass are a self-contained supporting specialization;
   their exact constant/base priority is not established. They cannot serve
   as an independent innovation claim or automatic STOC upgrade.

4. **Generalized reachability antecedent.** Fijalkow and Horn,
   *The surprising complexity of generalized reachability games*,
   [arXiv:1010.2420v2](https://arxiv.org/pdf/1010.2420v2), 2012-02-03,
   actual full text Section 3.4, Lemmas 1-2, printed pp.8-10. This proves
   exponential memory bounds in the zero-sum conjunction-of-targets model;
   it uses edge updates. The present lower bound directly proves a vertex-
   update collision at one common vertex and establishes existence and
   necessity for ALL SPEs with a SINGLE required winner. It does not claim
   that arbitrary generalized-reachability lower bounds transfer through
   a verifier: nonterminating plays are a separate obstacle.

5. **Existence is old.** Flesch et al., MOR 35(4) (2010), 742-755,
   [DOI](https://doi.org/10.1287/moor.1100.0469),
   [university-hosted publisher PDF](https://cris.maastrichtuniversity.nl/ws/files/72810748/flesch_2010_perfect_information_games_with_lower.pdf).
   Reopened the actual 16-page PDF and reread cached Definitions 2.1-2.5,
   footnote 2, Remark 2.1 and Theorem 2.3 (printed pp.743-744).
   The arbitrary-action and history-dependent-action scope is explicit.
   The Boolean epsilon=1/2 deduction is given in combined-theorem.md.
   No new unrestricted existence result is claimed; the new assertion for
   review is its finite-memory consequence via the compression theorem.

6. **Current NE and randomized comparisons.** Main,
   [I&C 309 (2026),105425](https://www.sciencedirect.com/science/article/pii/S0890540126000234),
   DOI 10.1016/j.ic.2026.105425, concerns arena-independent NASH memory;
   the cached primary full text and model distinctions remain in
   `intake/main-NE-2026.txt`. Its abstract/scope were refreshed live.
   Alluwaym, Main and Schewe,
   [arXiv:2607.07151v1](https://arxiv.org/html/2607.07151v1), 2026-07-08,
   current record still v1, considers finite graphs and randomized stationary
   SPEs. These are not the full pure exact-payoff transformation on arbitrary
   arenas. The lower bound's prescribed winner constraint is also essential;
   it asserts neither that every unconstrained SPE needs exponential memory
   nor that a randomized stationary theorem fails.

7. **Different synthesis quantifiers.** Bruyere, Raskin, Reynouard and
   Van Den Bogaard, [CONCUR 2025, paper 12](https://drops.dagstuhl.de/storage/00lipics/lipics-vol348-concur2025/html/LIPIcs.CONCUR.2025.12/LIPIcs.CONCUR.2025.12.html),
   DOI 10.4230/LIPIcs.CONCUR.2025.12. The primary reachability discussion
   and Remark 21 concern a committed system strategy and rational environment
   responses. Its stated memory lower bounds for the synthesis problem do
   not replace the all-player pure SPE transformation in source.md.

Queries during this pass combined reachability, SPE/subgame perfection,
arena-independent memory, 2026, polynomial memory and exponential lower
bounds. No equivalent full-scope upper theorem was found in this bounded
check. Unsearched literature and priority uncertainty remain; the next fresh
review must assess actual novelty and value against these precise sources.

Two optional direct local downloads (2023 survey, Fijalkow-Horn v2) failed
with URLError in the restricted shell; `intake/research-pass2/sources.json`
records that operational fact. Their actual primary PDF texts WERE available
and inspected through the web tool. No local copy is represented as existing.
The Flesch, 2018 and Main primary PDF/text inputs already exist locally.
