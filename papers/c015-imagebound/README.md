# Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Is the known mortality upper bound for k-image-bounded nondeterministic automata tight? For every fixed k≥2, the manuscript proves that the maximum shortest mortal-word length is Θk(n^(k+1)). The lower bound holds for all sufficiently large n even over a binary alphabet with strongly connected automata. A queue-and-clocks construction supplies the delay, while a global image invariant preserves the restriction under every word.

Scope: **resolution of the stated target**. 6 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c015-imagebound
python3 scripts/build_pdfs.py --paper c015-imagebound
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 evidence/portable-check.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
