# Reproduction

The article proves three subsidiary results: the all-budget minimum-reservoir-peak frontier for every positive swapped triplet, the sharp coordinate-monotonicity and endpoint-box penalty in each dimension, and exact evaluation of general necessary excursion certificates. The original general interpolation-family comparison remains unresolved.

From the project or extracted source-archive root:

```sh
python3 manuscript/reproduce.py
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript/main.tex
```

The checker needs Python 3 and only its standard library. It reads bundled files, prints JSON, and does not overwrite any research or audit evidence. Expected totals are 867 paths, 1,824 half-cells, 5,472 coordinate cells, 79 degenerate cells, and 3,483 envelope comparisons on 233 endpoint pairs and 699 budget instances. Path coordinates on a half-cell have the form A*u+B/u+C, with u=exp(s). Scaling the derivative and cap conditions by u reduces them to quadratics; endpoint and vertex/discriminant checks certify the entire cell. Reflection in time and exchange of the two changing coordinates certify the second half. The sweep is compared with direct reconstruction of all cells on a fixed seeded test set.

The bundled checker adapts the actual separate-context mathematical referee's finite verification, removing its project-snapshot writer and changing input paths. This is reproducibility of that verification, not another independent audit. `checks/provenance.json` identifies the original files and hashes. Finite checks do not replace the analytic proofs, prove novelty, or certify arbitrary cap feasibility. The necessary certificates have no asserted bit-complexity bound.

The build uses TeX Live 2026 (pdfLaTeX/BibTeX), latexmk, the unchanged official acmart 2.20 class, its standard installed packages, and the unchanged alpha bibliography style. All project-local compile inputs, including the generated main.bbl, are listed in the root publication.json. Poppler supplies pdfinfo, pdffonts and pdftoppm for inspection. There are no external fulltext, network, Python-package or figure dependencies. No system packages were installed.

The class's original acmart.dtx and distribution README are included under `manuscript/template/` to preserve the official source and license terms; they are not compile dependencies. Download provenance records CTAN and its redirect, not a successful direct ACM download. The bibliography cites inspected preprint versions where appropriate and includes all authors. `REFERENCE_NOTES.md` maps the six references to the passages used. No user-designated Excel workbook was supplied in this project.

The final PDF is configured as an English, non-anonymous manuscript with a separate title/abstract/contact cover, 11pt body/caption/reference text, single spacing, Letter paper, nominal one-inch text margins, no review line numbers, and references as its last material. A short factual AI-assistance paragraph precedes the bibliography. The five supplied authors, affiliations and emails are retained in order; Info/XMP author fields and XMP contact/affiliation metadata agree.

The WRITE job creates and freezes local artifacts. A separate fresh release job must still inspect all pages and citations, verify build/dependency closure, bind its reports to the final manuscript/PDF digests, and pass the real release gate. Mathematical acceptance is a separate AI-context review, not human peer review. No submission, upload or external contact is authorized or performed.
