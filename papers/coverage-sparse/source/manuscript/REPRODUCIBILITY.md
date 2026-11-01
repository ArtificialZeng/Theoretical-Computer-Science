# Source and exact verification

Build from the package root with an installed TeX Live including acmart's
standard dependencies, TikZ, BibTeX, latexmk and pdfLaTeX:

```sh
cd manuscript
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex
```

The local official `acmart.cls` is unmodified. Template sources and CTAN
provenance accompany it. The article uses alpha bibliography labels and the
STOC submission layout configured in main.tex.

Run the finite exact checks from the package root:

```sh
python3 manuscript/reproduce.py
```

This read-only launcher imports the verifier's functions without invoking its
historical main function, and prints exact JSON results to stdout. It needs
only Python's standard library. It never overwrites the frozen research output.
The inputs and the separate discovery program are in
`evidence/revision-research/`. `finite-certificates.json` contains the five
primal orbit mixtures and dual coefficients. `verify_revision.py` reconstructs
all labeled subsets and checks each marginal, tested pair, objective and
pointwise dual. `discover_finite.py` is an exact rational profile search, not
an LP solver dependency.

Checks cover the five optima 7/8, 5/6, 5/6, 65/81, 73/81, 137 rational
matching cases (m=1..12), 11,397 occupancy profiles (k=2..8,m=1..6), local
collision inequalities for k=2..40, and 11 product-law enumerations with n<=12.
Finite checks supplement the complete analytic proofs in the article; they do
not establish the infinite-parameter statements by extrapolation.

The point-by-point Chinese response and local handoff document are separate
from the article. No external submission is performed by any of these commands.
