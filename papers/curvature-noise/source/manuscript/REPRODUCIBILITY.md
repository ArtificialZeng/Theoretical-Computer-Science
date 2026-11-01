# Reproducing the manuscript and finite checks

This package is self-contained. It requires no research-source PDF, network
access, frozen project dossier, or third-party Python package.

## Build

Use a standard TeX Live installation containing the dependencies of the official
ACM `acmart` class, plus pdfLaTeX, BibTeX, and latexmk. The tested installation
is TeX Live 2026, acmart 2.20, and latexmk 4.88. From this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
```

For a clean rebuild:

```sh
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
```

The generated `main.bbl` is supplied for inspection and portability. BibTeX
regenerates it from `references.bib` and the supplied unmodified `alpha.bst`.
The unmodified official `acmart.cls` is included. Its original source and
license text are in `vendor/acmart.dtx`; `vendor/README-acmart` is the upstream
README. The distribution came from CTAN, not directly from the ACM publisher
endpoint; see `SOURCE-PROVENANCE.json`.

The submission uses manuscript single-column 11pt US Letter, single spacing,
a separate cover, and nominal one-inch margins. The `onehalfspacing` command
AFTER the final `clearpage` restores the class default only after all content
has shipped, to satisfy acmart's end-of-document guard; no printed page uses
that restoration. Publisher metadata identifies the authors and an unpublished
report, rather than implying ACM publication. There is no submission ID,
article DOI, copyright strip or acceptance assertion.

## Exact checks

```sh
python3 reproduce.py
```

Python 3.9 or later, standard library only. The program prints JSON to stdout,
does not write files, and stops with a nonzero exit on a failed assertion.
Assertions must remain enabled (do not use Python's `-O` option).

Four finite cases directly check 151,552 set-pair submodularity inequalities,
normalization, monotonicity, positive singletons, exact curvature and OPT.
Across all hidden sets and all query subsets they check 38,016 oracle entries,
including infeasibly large queries and the leakage threshold. Symmetry permits
one full submodularity table per parameter choice. The baseline objective's
curvature is checked separately.

For n=6, k=3, r=2, epsilon=1/2, kappa=1/3, the program exactly enumerates the
best output for every depth-zero, one and two deterministic adaptive decision
policy under the uniform prior over hidden sets. The optima are 359/540,
7/10, and 13/18, respectively. The baseline beta is 359/540 and p is 1/20.
Randomized policies are mixtures and have the same best prior optimum.

Four count-based cases check every query size for n=128, 257, 89 and 512.
They use integer binomial coefficients and fractions. They verify cn>3k
and the stronger bound with e replaced by 8/3 using integer powers, avoiding
floating exponentiation. The elementary bounds 8/3<e<3 justify this check.

The verifier is adapted from the separate fresh AI mathematical-review pass's
verifier. Running it again is reproducibility, not another independent review.
The finite cases are supplemental observations; the analytic proofs in the
manuscript establish the quantified theorem and asymptotic corollary. None
of these checks certifies novelty, exhaustive literature coverage, or venue
acceptance.

## Scope

The proved contribution is the exact-curvature/noise calibrated finite
expected query bound and its sparse-cardinality corollary for fixed
0<=kappa<1, k=floor(n^alpha), 0<alpha<1/2, and epsilon*k tending to infinity.
Matching is additive and is relative only if rho stays bounded away from zero.
The known singleton algorithm and standard construction/transcript methods
are credited in the paper. The full original joint-parameter question remains
unresolved; no curvature-one, zero-noise, bounded-epsilon*k, high-probability
hardness or finite minimax characterization is claimed.

No authoritative user Excel bibliography was supplied. Metadata was refreshed
from primary pages for the four cited records. The adjacent unavailable fulltext
comparison is documented in the project citation map and is not used to support
an unsupported claim. No external source fulltexts are distributed here.
