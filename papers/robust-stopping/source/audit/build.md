# Fresh affected build audit

Job: robust-stopping-release-ff035ab58689.
Current snapshot c70f1a41d2a4a68c3ad3f996323997e58e2b037484d8e4d79a5f9e8327bd3f3d; manuscript 2947c811f73b90b79c82634fc3909aad696aa457956ffd61ec1744834d8f8da1; final PDF 750891c12b44b7761c1c8c96968e8005e68e4b8b7f3f4299a8a5fe80fd96ce84.

Verdict: accept. All23publication inputs match the current snapshot and were
copied into audit/release-ff035ab58689/clean-source without auxiliary outputs.
Ran the declared latexmk -pdf -interaction=nonstopmode -halt-on-error
-file-line-error -recorder main.tex command there. It succeeded. The actual
final compiler log is clean-source/main.log; console trace is clean-build.log.
BibTeX regenerated the identical BBL. Compiler log inspected: no fatal error,
undefined citation/reference, overfull box, package/LaTeX warning or rerun request.
One underfull vbox remains; all final pages were inspected and it causes no
clipping, overlap or illegibility. BibTeX reports zero warnings/errors.

Rebuilt PDF and final PDF both have11physicalLetterpages, identical extracted
text and pixel-identical page renders at105dpi. The isolated rebuild has only
normal creation metadata/ID differences; the unchanged frozen final PDF remains
the delivery target. No source/PDF edit or new manuscript freeze was needed.

Official acmart.cls hash matches template/acmart.cls unchanged. Source declares
single-column11pt/single spacing/Letter/1in,11ptcaptions/references and separate
cover. Exact5authors/affiliations/emails and ordered PDFInfo/XMP confirmed;
all19fonts embedded. Bibliography is last and AI disclosure precedes it.
Recorded input closure and all16keys pass; all23current source inputs staged.
No third-party fulltexts or unlicensed code are among publication inputs.

Offline reproduction passed758saved certificates,216signed/tie queries,
36new pure-bisection cases,1071uniform certificates,334endpoint agreements,
support sharpness and exact separation/objective values. Six optional
unchanged-class runs on frozen third-party inputs also agree with the accepted
finite observation. All output records are under this audit directory.
Root will package and test the actual final delivered archive after the gate.
These checks do not independently prove the quantified mathematics.
