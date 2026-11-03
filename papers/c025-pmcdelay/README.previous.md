# Polynomial-Delay Enumeration of All Potential Maximal Cliques

**working_paper** · 9 total pages.

[PDF](c025-pmcdelay_working_paper.pdf) · [Unified index](../../README.md)

Enumerates every potential maximal clique of any finite simple undirected graph exactly once, with polynomial delay before the first answer, between answers, and after the last answer. Helper outputs charge minimal-separator prefixes to actual cliques; suspended recursion and buffering turn prefix bounds into worst-case delay. Exponential storage is allowed: no polynomial-space guarantee or faster treewidth exponent is claimed.

Classification basis: fresh_internal_stoc_assessment

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c025-pmcdelay
python3 scripts/build_pdfs.py --paper c025-pmcdelay
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
