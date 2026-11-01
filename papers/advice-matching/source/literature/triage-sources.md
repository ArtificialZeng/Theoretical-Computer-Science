# Primary-source triage record

Inspected 2026-10-31 Asia/Shanghai (2026-10-30 UTC).
Job: advice-matching-triage-5cc2f73291d9. No novelty or verified-open-status claim.

1. Davin Choo, Themistoklis Gouleakis, Chun Kai Ling, Arnab Bhattacharyya,
   *Online bipartite matching with imperfect advice*.
   https://arxiv.org/html/2405.09784v3#S3 and
   https://arxiv.org/html/2405.09784v3#A1 .
   Inspected the cached full Section 3 and Appendix A (HTML elements S3, A1),
   and checked the live Section 3. Theorem 3.1 gives the exact-consistency
   obstruction; its stated extension gives the linear inequality. Inspection
   of the displayed edge sets shows disjoint Z graphs, not a high-degree
   construction. The table-only specialization was verified directly in
   evidence/known-obstruction.md. Appendix A's deterministic paragraph has an
   apparent sign typo; our derivation does not use that line.

2. Billy Jin and Will Ma, *Online Bipartite Matching with Advice: Tight
   Robustness-Consistency Tradeoffs for the Two-Stage Model*.
   https://arxiv.org/html/2206.11397#S3.SS1 .
   Inspected Section 2 (Definition 2.1), Section 3.1, Figure 3, and Proposition
   3.1 with its proof. The unweighted tradeoff is linear; the commonly cited
   curved tradeoff concerns vertex-weighted matching. Its Z graph satisfies
   both degree bounds. Its batched achievability and stronger advice-value
   consistency benchmark are distinct from this project's model.
   The source's Columbia-hosted PDF could not be fetched by the web tool
   (content-length fetch failure); arXiv HTML supplied the inspected primary
   text. The earlier cache manifest reports an HTTP 403 for that PDF.

3. Amey Bhangale, Arghya Chakraborty, Prahladh Harsha,
   *Optimal Online Bipartite Matching in Degree-2 Graphs*, ISAAC 2025.
   https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.13/LIPIcs.ISAAC.2025.13.html
   DOI: 10.4230/LIPIcs.ISAAC.2025.13.
   Inspected Theorems 1 and 2, Section 2's explicit notation G(d1,d2), and
   Section 4.1's phased hardness graph. The integral theorem is for G(n,2);
   the fractional 3/4 theorem is not an integral achievability result. The
   stated hardness family uses increasing offline degree across phases, so
   it cannot certify tightness on G(2,2) without a new argument.

Searches used exact titles, randomized degree-two online matching, both-side
degree bounds, and consistency/robustness prediction equivalents. Advice-bit
complexity and random-arrival papers surfaced as leads; they were not used
as proof of any statement here. No exhaustive literature survey is claimed.
The project-local selection.md was checked: this was the independently
admitted structural matching lead, and general two-stage matching was already
parked there as known. No historical cross-project registry was present within
this project's files; none was modified or assumed screened.

Decision: the lower-bound restriction is a rediscovery. The full sequential
G(2,2) achievable frontier remains status-uncertain in this triage. Park under
the source's explicit overlap instruction. The outstanding algorithmic
question is recorded only as a possible reopening test, not a new claim.
