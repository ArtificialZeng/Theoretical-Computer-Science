# Mandatory Excursions in Privacy-Constrained Probability Paths

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Can a privacy-constrained probability path stay between its endpoint probabilities? For swapped three-outcome distributions, the manuscript determines optimal budgets and the smallest unavoidable peak of the unchanged coordinate. It also derives sharp costs for monotone or endpoint-bounded paths and excursion certificates for general endpoints. This is a legacy partial-result note; the original general problem remains unresolved.

Scope: **legacy partial result; original broader question unresolved**. 7 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper privacy-interpolation
python3 scripts/build_pdfs.py --paper privacy-interpolation
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/reproduce.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
