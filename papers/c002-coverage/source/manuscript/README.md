# Build and scope

This is the manuscript of the accepted, unchanged resolution-paper claim.
It uses the unmodified official ACM acmart 2.20 input copied from the
user-designated CTAN distribution into `vendor/acmart.cls`. The class
remains byte-identical. No city or ORCID is invented. Malaysia is the
institution's country; the sole author, institution, and email match
`authors.json`.

The current STOC 2027 submission CFP, checked on 2026-11-01 Asia/Shanghai,
requires named authors, an initial title page, 11-point single-column
single-spaced text, Letter paper and one-inch margins. The submission has
no conference page limit; the user's stricter cap is twelve total pages.
The proceedings sigconf rule applies at a different stage. This local
format and local mathematical acceptance imply no conference acceptance.
See https://acm-stoc.org/stoc2027/stoc2027-cfp.html .

For the complete clean build, run from the project directory:

```
python3 manuscript/build.py
```

The script uses the installed TeX Live engine and BibTeX, with project-local
copies of the unmodified class and standard `alpha.bst`. It places the final draft at
`output/pdf/sparse-coverage-discrepancy.pdf`. A separate citation/build/visual
release review is required after the manuscript freeze. No external action
is authorized. The finite diagnostic programs are supplementary and are
not needed to verify the mathematical proof.
