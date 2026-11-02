# Certified Expected-Cost Optimization for Robust Ski Rental

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

How should a ski-rental policy use a finite rational forecast while satisfying an expected competitive-ratio bound at every horizon? The manuscript gives exact expected-cost optimization with primal and dual certificates on unbounded buy-day and horizon domains, a support bound of b+1 days, and an explicit uniform-forecast frontier. Its running time is polynomial in numerical b and input bit length. The broader original question remains unresolved.

Scope: **legacy partial result; original broader question unresolved**. 11 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper robust-stopping
python3 scripts/build_pdfs.py --paper robust-stopping
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/reproduce.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
