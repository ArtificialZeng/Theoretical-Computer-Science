# A Universal Partial Cycle with Three Wildcards per Window

**working_paper** · 5 total pages.

[PDF](c012-upcycles_working_paper.pdf) · [Unified index](../../README.md)

Does a nontrivial universal partial cycle exist with more than one wildcard per window? An explicit binary cycle of length 512 has length-12 windows containing exactly three wildcards. Its windows partition all 4096 binary 12-words into groups of eight completions. The entire cycle is encoded by 128 octal digits and checked by a short solver-free Python program, giving a finite existence proof.

Classification basis: Conservative classification: no explicit fresh review under the new STOC standard.

Mathematical scope: proved

From the repository root:

```sh
python3 scripts/reproduce.py --paper c012-upcycles
python3 scripts/build_pdfs.py --paper c012-upcycles
```

The original archive and expanded source are linked in the unified index. Checks run on disposable copies. Finite checks are not a full proof, formal verification, new novelty review or external peer review. Original author lists and archived files remain unchanged.
