# Uniform Pumping Does Not Characterize Copyless Cost Register Automata

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Does the uniform pumping condition characterize functions computed by copyless polynomial cost register automata? This manuscript proves that it does not, even among rational weighted-automaton functions: summing the positions of the 1s in a binary word satisfies the condition with one pumping exponent and one finitely generated subsemiring, but no finite-state copyless polynomial cost register automaton computes it. A minimum-image retraction and a polynomial spectral projection yield a commutation obstruction; return words remove finite control. This is the released nine-page separation, not the later extended revision.

Scope: **resolution of the stated target**. 9 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c021-ccrapumping
python3 scripts/build_pdfs.py --paper c021-ccrapumping
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 evidence/research_checks.py
python3 audit/referee-check.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
