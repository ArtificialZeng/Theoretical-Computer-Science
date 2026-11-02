# Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

What consistency–robustness tradeoff is possible for online bipartite matching with potentially wrong matching advice? For unweighted degree-two graphs, the exact frontier is min{3/4, 3/2−c}; on cycles it is min{7/8, 7/4−c}. An algorithm prioritizing previously exposed offline neighbors reaches the endpoints, and indistinguishable small inputs give matching upper bounds. The adversary is oblivious and advice may list absent edges.

Scope: **resolution of the stated target**. 6 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper advice-matching
python3 scripts/build_pdfs.py --paper advice-matching
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/reproduce.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
