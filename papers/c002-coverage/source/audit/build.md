# Fresh build audit

Job: `c002-coverage-release-c84ac066553a`. Reviewed: 2026-10-31T22:05:01.069857+00:00.

Research snapshot: `26d2a64f317984b35b49212bdc46529ccb7f19bc1be1b5e471d28d308d18456e`.
Manuscript snapshot: `cbd9e040f4147d3e60fc3daafd59dcd1d2dfe965798be52063afe7345dcd085f`.
PDF: `b2dac13ca628fb6c3b7495516ee0acbdd390a90b0942127ada2935401ba873db`.

**Verdict: accept.** This release context inspected the existing actual clean-build evidence and current compiler outputs. It did not claim or perform a new compilation, edit source, generate another PDF or change the frozen manuscript.

`manuscript/build.py` documents a clean foreground run of `latexmk -C main.tex` followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, with project vendor paths for the official class and bibliography style. `evidence/write-build.log` records that actual run and BibTeX convergence; its initial missing references are ordinary first-pass diagnostics, resolved by the final pass. The separately bound log is **manuscript/main.log**, the actual final TeX compiler log, not a filtered or rewritten transcript.

Fresh inspection found no final warning, undefined reference/citation, overfull/underfull box, fatal error or emergency stop. The log records seven pages and 395202 bytes. BibTeX's main.blg has no reported problem. `main.bbl` contains all and only the five cited keys; final extracted text and rendered references confirm resolution. `manuscript/main.pdf` and the canonical output PDF are byte-identical and match the frozen digest.

`evidence/release-verification.json` independently reconciles the recorder inputs with publication.json; only generated aux/out and system TeX files fall outside the listed local inputs. The official acmart 2.20 class matches the supplied official distribution byte-for-byte. No modified class, omitted figure or extra imported authored source was found.

Fresh pdfinfo and pdffonts outputs are saved in `evidence/release-pdfinfo.txt` and `evidence/release-fonts.txt`. The PDF has a valid header, seven Letter pages, no encryption, no JavaScript, and nonempty extractable text. All sixteen reported font resources are embedded Type 1 subsets; no Type 3 fallback is reported. The PDF title is correct. The visible sole author, affiliation and email match authors.json; PDF metadata does not add another author. Main prose, abstract and bibliography use the configured 11-point size. Source formatting and actual rendered pages were compared with the current [STOC 2027 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html): named title page, single column/single spacing, Letter page and one-inch text margins. The manuscript's substantial-AI-use disclosure is present. The user's twelve-total-page cap is met. This is a local artifact-format check and implies no submission or conference acceptance.

No PDF authoring operation occurred in this release context; under the read-only exception in the PDF skill, no artifact-authoring marker was required. Rendering existing pages is the visual review documented separately.
