# Deterministic Truly Subquadratic Two-Dimensional Range-LIS Reporting

**working_paper** · 9 total pages.

[PDF](c031-detlis_working_paper.pdf) · [Unified index](../../README.md)

Reports a longest strictly increasing subsequence inside every index–value rectangle of a sequence, deterministically in O((n+m)n^(2/3)log^30(n+m+2))+O(K) operations. Repeated values, arbitrary overlapping queries and witness output are included. A background-sensitive trace oracle and exact conditional scores implement deterministic relative sampling for canonical chains. The result removes randomness from the full reporting model, while remaining slower than the prior randomized square-root-overhead bound.

Classification basis: fresh_internal_stoc_assessment

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c031-detlis
python3 scripts/build_pdfs.py --paper c031-detlis
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
