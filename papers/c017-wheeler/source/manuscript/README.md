# Local manuscript build

This is the single combined paper for the accepted full membership theorem,
the O(S^13) bound, pumped failure certificates, and equivalent realizability.
It is a local manuscript awaiting the separate release review. It has not
been submitted, uploaded, or accepted by a conference.

From this directory, build with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The original official acmart.cls and ACM-Reference-Format.bst were copied
unchanged from the user-specified ACM distribution. The acmsmall/nonacm option
selects a single-column, single-spaced base; the main file sets US Letter,
one-inch margins, 11pt, a separate title page, and named authors. The current
STOC 2027 CFP specifies this submission geometry; its sigconf rule is for
the accepted proceedings version. The user's stricter total-page cap is 12.
The final draft has 10 pages including title and references.

The complete TeX inputs, including the generated main.bbl, are listed in
../publication.json. No project-local dependency installation was needed.
The mathematical evidence remains unchanged under ../audit/snapshot.json.

Reproducibility records (not manuscript build inputs):
- ../evidence/check_membership.py and membership-check.json implement and
  document the finite membership controls.
- ../evidence/check_exact_certificates.py and exact-certificates.json replay
  exact serialized pump families on specified finite indices.
- ../evidence/research-2-check-realizability.py and
  research-2-realizability-check.json implement and document the automatic
  quotient and end-to-end controls; their project-relative intake imports
  are retained in this project.
- ../audit/referee-a6cac210b41e-verify.py and its checks report record the
  separate-context internal checks, without asserting external peer review.

Finite tests are supplementary. The paper contains the all-input mathematical
arguments. Primary bibliography basis and the absence of a designated Excel
list are recorded in ../literature/user_bibliography_check.md.
