# A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

How does persistent multiplicative oracle noise affect submodular maximization when curvature is known? In the sparse-cardinality regime k=⌊n^α⌋, 0<α<1/2, with εk→∞, a hidden-set construction gives an asymptotic lower bound matching noisy-singleton selection. For vanishing noise the limiting factor is 1−κ, rather than the exact-oracle benchmark 1−κ/e. This legacy note resolves that regime, not the original unrestricted problem.

Scope: **legacy partial result; original broader question unresolved**. 6 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper curvature-noise
python3 scripts/build_pdfs.py --paper curvature-noise
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/reproduce.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
