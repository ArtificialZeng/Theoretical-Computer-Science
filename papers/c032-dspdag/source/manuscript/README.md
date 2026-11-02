# Local working paper

Build from the project root with:

```sh
python3 manuscript/build.py
```

Requires installed Python 3, pdflatex and BibTeX with the standard acmart
dependencies. No installation or network access is used by the build.
The script copies the four TeX inputs into a clean project-local directory,
runs pdflatex, BibTeX and two final pdflatex passes, and writes
`output/pdf/dspdag-working_paper.pdf`. It also retains the generated `main.bbl`
and build logs. A fixed source timestamp makes local rebuilds reproducible.

The official acmart v2.20 class and ACM Reference Format BST are unmodified
copies from the user-designated official template distribution. The acmlarge
option supplies single-column, single-spaced text; the document selects 11pt,
letter paper and one-inch margins for the current initial-submission format.
This is a local working paper, with one requested author, not an ACM publication
or conference submission. The internal venue assessment remains working_paper.

No figures or external TeX inputs are required. `references.bib` has nine
relevant primary references. No user Excel bibliography was designated.
The paper includes substantive AI disclosure and does not assert human
verification or external peer review. Fresh citation/build/every-page review
and the final delivered-source archive reproduction remain separate release
requirements. Writing completion does not authorize publication or upload.
