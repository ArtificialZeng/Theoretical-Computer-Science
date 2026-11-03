# Rectangular Batching for Disjoint Shortest Paths on DAGs

**working_paper** · 8 total pages.

[PDF](c032-dspdag_working_paper.pdf) · [Unified index](../../README.md)

Detects k prescribed mutually vertex-disjoint shortest paths in a positive-weight directed acyclic graph, for every fixed k≥3, in deterministic O_k(m+n+n^(k+0.3)) time. Rectangular Boolean products batch transitions of the established minimum-coordinate frontier recurrence, with packing, preprocessing and exact arithmetic charged. A Strassen-based alternative gives exponent k−2+log₂7. The same method handles label-specific allowed edges with a common acyclic order.

Classification basis: fresh_internal_stoc_assessment

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c032-dspdag
python3 scripts/build_pdfs.py --paper c032-dspdag
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
