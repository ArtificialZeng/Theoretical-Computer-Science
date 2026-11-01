# Deciding Membership and Realizability for Wheeler Transducers

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Can one decide Wheeler membership when the number of output-monotonicity pieces is unspecified? The manuscript gives a polynomial-time algorithm for finite trimmed deterministic subsequential transducers, allowing partial transitions and erasing outputs; a conservative bit bound is O(S^13). Branching recurrence and simple cycles require different structural tests. Equivalent Wheeler realizability is also decidable and constructive, with no polynomial-time or minimality claim for that construction.

Scope: **resolution of the stated target**. 10 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c017-wheeler
python3 scripts/build_pdfs.py --paper c017-wheeler
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 evidence/check_membership.py
python3 evidence/check_exact_certificates.py
python3 evidence/research-2-check-realizability.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
