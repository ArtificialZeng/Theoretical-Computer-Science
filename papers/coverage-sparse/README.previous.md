# Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

How much does testing only selected pairs for independence reduce the best attainable coverage value? For k-colorable graphs and graphs of maximum degree at most k−1, the manuscript gives the exact worst-case ratio 1/[1−(1−1/k)^k]. Disjoint cliques give tight examples. A collision inequality also provides finite-instance and measurement-error bounds. The statement concerns suprema over graph classes.

Scope: **resolution of the stated target**. 8 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper coverage-sparse
python3 scripts/build_pdfs.py --paper coverage-sparse
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/reproduce.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
