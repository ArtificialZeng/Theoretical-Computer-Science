# Fresh primary-source comparison

Job: `c002-coverage-referee-3e90f78a9294`.
Checked 2026-10-31 UTC / 2026-11-01 Asia/Shanghai, during this referee job.
This is a bounded novelty screen, not exhaustive priority certification.

The referee read only the authorized frozen packet, policy/instruction files,
and the actual primary sources needed for review. No earlier audit, checkpoint,
state file, research handoff, transcript or owner verdict was consulted.

## Sources actually inspected

1. Avila, Rohwedder and Wennmann, *Non-Additive Discrepancy: Coverage Functions
   in a Beck-Fiala Setting*, ESA 2026, DOI
   [10.4230/LIPIcs.ESA.2026.139](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.139).
   The live publisher record gives 2026-08-25; the
   [live arXiv history](https://arxiv.org/abs/2602.09948) still lists v3,
   2026-07-01. Inspected the frozen full texts of both versions and the
   [official live PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol388-esa2026/LIPIcs.ESA.2026.139/LIPIcs.ESA.2026.139.pdf).
   Theorem 3 retains `O(sqrt(t^3 k) log(ntk))`; Section 5/Lemma 23 already
   supplies interaction classes and linear rounding. Definition 4 and the
   covering-universe introduction were checked for the occurrence convention.
   The selected arXiv and proceedings statements agree; pagination differs.

2. Glaßer, Reitwießner and Witek, *Applications of Discrepancy Theory in
   Multiobjective Approximation*, FSTTCS 2011, DOI
   [10.4230/LIPIcs.FSTTCS.2011.55](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2011.55).
   Inspected the [official full PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol013-fsttcs2011/LIPIcs.FSTTCS.2011.55/LIPIcs.FSTTCS.2011.55.pdf),
   Section 3, Theorem 2, printed p.58. Its rational one-choice-per-group
   theorem has error `2 max_column sum_row |A_entry|` and a polynomial-time
   algorithm. This is exactly the submitted dependency, not a new lemma.

3. Doerr and Srivastav, *Multicolour Discrepancies*, CPC 12(4):365--399
   (2003), DOI
   [10.1017/S0963548303005662](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/multicolour-discrepancies/B3B9E2D4477711A2B29A197DCA886EDE).
   Verified publisher metadata/abstract. The original full text was not read;
   the precise theorem above was verified in the primary 2011 paper and
   independently rederived from the submitted self-contained proof. An
   initially attempted incorrect Cambridge URL was inaccessible; the DOI
   search then located the correct publisher record linked here.

4. Hollender, Manurangsi, Meka and Suksompong, *Discrepancy Beyond Additive
   Functions with Applications to Fair Division*,
   [arXiv:2509.09252](https://arxiv.org/abs/2509.09252).
   The live history remains v2 (2025-09-29). Read the frozen full text,
   Definition 13, Question 14 and Theorem 15, printed p.10. Its sparsity
   counts influenced functions, and its general Lipschitz question is broader
   than tagged coverage. Its sparse bound retains item-count dependence.
   The present candidate does not resolve that broader question.

5. Dupré la Tour and Fujii, *Discrepancy And Fair Division For Non-Additive
   Valuations*, [arXiv:2509.16802](https://arxiv.org/abs/2509.16802).
   The live history still lists the original 2025-09-20 submission. Read the
   frozen full text, Theorem 1, printed pp.2--3. Its general valuation bound
   depends on the number of functions and restricts the color count to prime
   powers. It does not imply the candidate's occurrence-degree-only bound.

6. [Wennmann's own publication list](https://leo-wennmann.github.io/) was
   checked for a named follow-up. None resolving this target was displayed.
   Its last-update label is May 15, 2026, so it is weak supplementary evidence.

## Independent search coverage

The following queries were issued in this fresh job, in addition to opening
the source records above. Domain exclusions only suppressed aggregators;
aggregator, problem-catalogue and AI summary results were not theorem evidence.

- `"Non-Additive Discrepancy" "Coverage Functions"`
- `"coverage functions" discrepancy "size-independent"`
- `"Multicolour discrepancies" Doerr Srivastav`
- `"Applications of Discrepancy Theory in Multiobjective Approximation"`
- `"coverage" "discrepancy" "rainbow" "Hall"`
- `"Non-Additive Discrepancy" "bound"`
- `"coverage functions" "discrepancy" "independent"`
- `"non-additive" "discrepancy" "polynomial" "sparse"`
- `"coverage" "Beck-Fiala" "Hall"`
- `"coverage" "discrepancy" "cyclic"`
- `"coverage functions" "discrepancy" "constant"`
- `"non-additive discrepancy"`
- `"coverage functions" "discrepancy" "bound" 2026`
- `"coverage functions" "size independent" Beck Fiala`
- `"coverage discrepancy" "polynomial"`
- `"non-additive" "discrepancy" "rainbow blocks"`
- `"Beck-Fiala" "coverage" "polynomial"`
- `"nonadditive discrepancy" "sparse"`
- `"coverage functions" "discrepancy" "Hall's"`
- `"discrepancy" "disjunctions" "sparse"`
- `"discrepancy" "submodular" "Beck-Fiala"`
- `"nonlinear discrepancy" "bounded"`
- `"coverage functions" "discrepancy" "O(t"`
- `"10.1017/S0963548303005662"`
- `"polychromatic" "Hall" "hypergraph"`
- `"coverage" "discrepancy" "block states"`

No inspected equivalent supplied the full rainbow-witness/categorical
reduction or a polynomial bound independent of both size parameters for
this exact model. The absence of such a hit does not exclude unindexed,
inaccessible, differently named or very recent work. The substantive novelty
assessment in `audit/math.md` rests on the precise structural delta against
the inspected nearest theorems, not on a claim of exhaustive search.
