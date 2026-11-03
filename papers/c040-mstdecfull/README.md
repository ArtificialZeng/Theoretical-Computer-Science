# Deterministic Quasipolynomial MST Approximation under Decrease-Only Corruption

**working_paper** · 8 total pages.

[PDF](c040-mstdecfull_working_paper.pdf) · [Unified index](../../README.md)

Gives a deterministic quasipolynomial algorithm for metric MST approximation under decrease-only corruption, for every fixed marking probability p<1. An adversary knows both the metric and the independently sampled mask; the algorithm uses only the corrupted observations and returns a spanning path with expected true cost O_p(log^2 n) times the MST optimum. Its n^{O_p(log n)} arithmetic/comparison bound is independent of aspect ratio. The proof combines quantile-based hidden-core carving with a depth-first leaf-order bound charged to actual outlier mass.

Classification basis: fresh_internal_stoc_assessment

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c040-mstdecfull
python3 scripts/build_pdfs.py --paper c040-mstdecfull
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
