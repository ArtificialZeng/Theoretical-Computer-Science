# Reproduce the revised note

From this directory, run `python3 -B reproduce.py` (standard Python 3 library only;
do not use `-O`, because assertions check certificates). It prints JSON. The
default run is offline, reads only bundled data and owned algorithms, and does
not require source papers or the original authors' software. All newly generated
full-model optimizer queries use `max_chord_probes=0`, as in Algorithms 1–2.
The saved certificate corpus also records earlier executions; checking a
certificate is independent of which search produced it.

The output checks the saved primal/dual witnesses, signed-cost normalization,
new pure-bisection queries, all uniform segments and their shared endpoints
for b=2 through 22 plus 41 and 64, support sharpness at segment interiors,
the three distinct costs 39/20, 11/5 and 12/5, and the expected-cost versus
expected-per-horizon-ratio separation. The unbounded-domain and quantified
claims are established by the manuscript proofs. Finite checks test the
implementation and exact witnesses; they do not replace those proofs.

The uniform frontier at b=3 has breakpoints R=27/19,3/2,5/3,2 and values
54/19,21/8,7/3,2. Figure 3 is drawn from these proved values. The underlying
capped-geometric law overlaps Kim–Fan's one-hot-b construction; the paper
credits that structure. The default program evaluates the observed software
law exactly; that is separate from rerunning external software.

## Optional original-software execution

Publisher: https://proceedings.mlr.press/v306/kim26l.html
Software: https://github.com/JihwanKim4689/distributional-ski-rental
Pinned commit: `0a86125f31e9e1b1abbba5bd4fde32a332860124`.
The two original files are not redistributed (no repository license was found).
Obtain that checkout independently, then run:

```
python3 -B reproduce_author_code.py /path/to/pinned/checkout
```

The wrapper verifies the full SHA-256 of both source files and executes only
the unchanged `SkiRentalOptimizer` AST class, skipping top-level experiments,
plots and imports. It makes the six specified calls: constructor arguments
`(3,1.5,[1,2],[.4,.6])`, tolerances 1e-5,1e-9,1e-12, in both Figure-1 and
Table-2 optimizer files. Saved output is `data/kf26-software-observations.json`.
All calls returned (1/4,3/8,3/8), true J=12/5, moment=9/8. The construction
at h=3 temporarily adds 9/16 at day 3, reaching F=19/16, before its existing
correction yields final mass 3/8. Internal moment/mass variables do not
certify the returned law. The manuscript computes the true model quantities.
These are six finite floating-point observations, not an all-version,
all-tolerance or convergence theorem. The theoretical minimum-support-level
law costs 11/5 and must not be described as the observed software output.

## Build

Run `make` (TeX Live 2026, latexmk, pdfLaTeX, BibTeX; TikZ, algorithm and
needspace are standard installed packages). `make clean` removes auxiliary
build files. The official unmodified acmart v2.20 is bundled with its source
and README; provenance is recorded in SOURCE_PROVENANCE.json. The document
uses single-column 11pt, single spacing, US Letter and one-inch margins.
The alpha bibliography lists full author names, with metadata drawn from
publisher/official exports. Long abstract fields were omitted from the
compilation copy; see BIBLIOGRAPHY_PROVENANCE.md. Full third-party papers,
HTML, source extracts and unlicensed software are not part of this package.

## Scope and review limits

The accepted contribution is one result-note: general certifying optimization,
complete uniform expected-cost frontier, uniqueness and sharp support, objective
separations, and the narrowly pinned published/software application. A direct structural description of the complete frontier for arbitrary
forecasts is left for future work. A fresh model
context checked the mathematics; this is AI verification, not human peer review
or statistically independent evidence. Local build and writing checks do not
certify priority, venue significance, author consent or conference acceptance.
