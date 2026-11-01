# A Universal Partial Cycle with Three Wildcards per Window

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Does a nontrivial universal partial cycle exist with more than one wildcard per window? An explicit binary cycle of length 512 has length-12 windows containing exactly three wildcards. Its windows partition all 4096 binary 12-words into groups of eight completions. The entire cycle is encoded by 128 octal digits and checked by a short solver-free Python program, giving a finite existence proof.

Scope: **resolution of the stated target**. 5 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c012-upcycles
python3 scripts/build_pdfs.py --paper c012-upcycles
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 manuscript/verify.py
python3 evidence/research2-witness/minimal_check.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
