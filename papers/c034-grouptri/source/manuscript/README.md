# Bounded-exponent Exact Triangle

This source package accompanies *Truly Subcubic Exact Triangle over
Bounded-Exponent Abelian Groups*, by Zijian Zeng, UCSI University,
1002266693@ucsiuniversity.edu.my.

The artifact classification is `working_paper`. It is an internal assessment,
not an external venue decision. No submission or public upload is authorized.

## Build

With TeX Live (including acmart dependencies), latexmk and BibTeX installed,
run `make` in this directory. The result is `main.pdf`. Alternatively run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main.bbl` is also supplied as a generated bibliography input. `acmart.cls`
and `ACM-Reference-Format.bst` are unmodified official distribution files.
No custom class, font installation, or network access is required to build.
The manuscript uses the one-column review-submission format, with identified
authors, rather than the two-column proceedings format. The compiled paper
has eight total pages, including the title page and references. An affiliation
city was not supplied; the remaining acmart city warning is disclosed rather
than filled with an assumed author campus.

## Finite semantic checks

The `verification` directory contains an exact copy of the separate finite
verifier and its recorded coverage. These checks use brute-force detectors;
they do not implement or benchmark the asymptotically fast prime backend.
They check the capped-listing semantics, local potential/kernel identities,
absence markers, graph partition and exact exponent inequalities.

Run it in a new isolated directory so that its historically named output
cannot overwrite any review records:

```sh
mkdir -p verification/run/audit
cd verification/run
python3 ../independent_verifier.py
```

The script prints its count/coverage record and writes
`audit/independent-checks.json` inside that new run directory. Its embedded
provenance identifies the original internal review, not a new review or
acceptance conferred by rerunning code. The expected counts and limitations
are in `verification/recorded-checks.json`.

The paper discloses substantial OpenAI Codex assistance. Neither these finite
checks nor the internal model review constitutes formal verification or
external peer review. The full proof depends explicitly on the stated
elementary-group algorithm in the cited primary paper.
