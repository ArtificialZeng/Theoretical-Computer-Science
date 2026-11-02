# A Size-Independent Discrepancy Bound for Sparse Coverage Functions

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Can sparse coverage functions be balanced with an error independent of the number of items? If each item belongs to at most t feature occurrences across the family, a deterministic polynomial-time partition into k≥2 classes achieves pairwise discrepancy at most 4kt(kt−1)². Hall witnesses balance large features, and multiple-choice Beck–Fiala rounding handles the remaining interactions. The result gives a polynomial bound depending only on t and k.

Scope: **resolution of the stated target**. 7 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c002-coverage
python3 scripts/build_pdfs.py --paper c002-coverage
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 evidence/research_rounding_check.py
python3 audit/referee_verify.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
