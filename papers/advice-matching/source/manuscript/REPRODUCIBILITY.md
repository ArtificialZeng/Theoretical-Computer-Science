# Build and exact finite checks

The complete analytic proof is in `main.tex` and `body.tex`. Finite checks are
supporting evidence and do not prove the statements for arbitrary graph size.
The source bundle needs no research fulltexts, network connection, or project
files outside this directory.

## Requirements and commands

Use TeX Live 2026 (pdfLaTeX, BibTeX, latexmk and the standard packages required
by acmart) and Python 3.10 or later. No Python packages are required.

From this directory:

```sh
sh build.sh
python3 reproduce.py
```

`build.sh` removes old compilation outputs and builds `main.pdf`. The official
`acmart.cls` is included unchanged with its upstream source and README; the
BibTeX style `alpha.bst` is also included. `template-provenance.json` records
the original CTAN download. The class was not downloaded directly from ACM;
the ACM endpoints were inaccessible. No extra system packages are installed.

For a machine with pdfLaTeX but without latexmk, the equivalent build is:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## What the checker covers

`reproduce.py` prints JSON to standard output, reads no fulltexts, and writes
no files. It checks all 265 labelled bipartite graphs with equal parts of size
three and both maximum-degree bounds, all six online orders (1,590 inputs),
all 2,652 maximum-advice cases, and all 54,060 arbitrary-advice cases. The
regular subclass contributes 1,224 arbitrary-advice cases. It also tests
3,490 component orders through six online vertices, 3,552 cycle root
orientations, three Z prefixes, and nine cycle-gadget prefixes. All arithmetic
is integral or uses Python's `Fraction`.

Expected output has `ok: true` and `minimum_E_ratio_n3: "3/4"`.
The tests include partial maximum tables, absent advised edges, isolates,
disconnected graphs, and the exact common table `(0,2,3,1)` for the cycle
upper bound. Only the advised pair with online index 2 and offline index 3
is absent in world 0 (zero-based indices).

The research dossier also contains larger finite runs and a fresh model-context
mathematical review. This bundle deliberately provides a short standalone
reproduction run; it does not silently rerun or overwrite those frozen files.
A separate AI context is an additional verification pass, not human peer review
or statistically independent evidence.

## Scope and status

The accepted theorem concerns simple unweighted graphs, irrevocable integral
vertex-by-vertex decisions, fixed graph/order/advice independent of random
coins, and an injective partial matching table with possible absent edges.
Consistency is for every realized maximum matching table. The theorem holds
uniformly for every finite size with no additive error. It resolves the
original problem under that precise interpretation. Adaptive adversaries,
weights and one-side-only degree bounds are separate questions.

This is a local writing-stage artifact. A fresh citation/build/every-page
visual release review and the actual release gate remain required. Preparing
this bundle does not establish journal or conference acceptance, author
agreement, or permission for external submission.
