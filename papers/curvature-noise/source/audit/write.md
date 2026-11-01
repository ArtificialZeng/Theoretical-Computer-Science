# Writing handoff

Job `curvature-noise-write-cf9542198fc2`, 2026-10-31. Writing phase only.
The original source and every frozen mathematical evidence hash remain unchanged.
The accepted mathematical scope is `claim.json`, as reviewed in `audit/math.md`;
`check-math` succeeded before manuscript creation and again before freezing.
The original full joint-parameter question remains unresolved.

## Manuscript and package

`manuscript/main.pdf` has **6 total pages** (separate cover plus five numbered
content/reference pages), within the user's 12-page limit. The article states
and proves the accepted finite randomized query bound, sparse-cardinality
corollary, credited singleton baseline, and ancillary exact-tail lemma. It
preserves the fixed all-set oracle model, exact curvature, per-family polynomial
query quantifier, expected-value criterion, additive matching and endpoint limits.
The manuscript credits the capped-rank construction, modular tuning, transcript
method and singleton algorithm, and ends with the required two-sentence AI
assistance disclosure. No priority guarantee or full-problem resolution is claimed.

The official unmodified acmart class is copied locally and its source/license
is included. Manuscript mode is single-column, nominal 11pt body/captions/references,
normal single spacing, US Letter and nominal one-inch margins. The separate cover
contains the five exact requested authors, institutions and emails. PDF Info and
XMP author order and title agree; inferred ACM publisher/journal metadata were
replaced by the authors/unpublished-report metadata. All fonts are embedded.

`publication.json` enumerates eleven complete source/package inputs, including
the class, alpha style, generated bbl and portable exact verifier.
`manuscript/curvature-noise-source.zip` contains those inputs with no external
research fulltexts. Its isolated build and standard-library verifier both pass.
`manuscript/REPRODUCIBILITY.md` gives precise coverage and commands;
`manuscript/README-ZH.md` gives the Chinese scope and handoff.

## Authoring checks actually performed

- Clean pdfLaTeX/BibTeX/latexmk build and actual main.log read. No unresolved
  citations/references, overfull boxes, class/package warnings or errors remain.
  One underfull vertical-box diagnostic is harmless and visually inspected.
- All six final pages rendered and inspected individually, including the cover,
  table, every displayed proof equation and full-author alpha bibliography.
  No clipping, overlap, missing glyphs or illegible content found. Caption size
  was independently checked as 11pt in pdftohtml font output.
- Isolated ZIP compilation contains no project fulltext dependencies and yields
  the same six-page text/source inputs. The recorder's local authored dependency
  closure agrees with publication.json; generated aux/out files are rebuild products.
- The portable verifier reproduces all accepted referee finite cases and exact
  policy optima. The isolated environment exposed Python 3.9's lack of bit_count;
  using a compatible popcount fixed this packaging issue. The final verifier
  passed on Python 3.9.6 and matches the accepted saved finite results.
- The required PDF skill was read and its artifact marker ran successfully once
  immediately before first authoring. No subagents/background/model workers or
  external submission/upload/contact actions were used.

`audit/write-checks.json` and `audit/write_check.py` record authoring checks;
these are not a fresh release audit. Actual gate outputs are saved in
`audit/write-math-gate.json` and `audit/write-freeze-gate.json`.

## Citations and remaining limit

`literature/user_bibliography_check.md` was read before creating the PDF and
records that no authoritative user workbook/BibTeX list was supplied. No such
records were fabricated. Four relevant primary records were refreshed and
conservative bibliographic entries retained. The writing citation map is
`audit/write-citation-map.md`. The accepted evidence's bounded novelty screen
and adjacent Gong--Liu--Geng--Fang fulltext access limitation remain disclosed
in the dossier, without attaching unsupported prose to that source.

## One next test

A separate fresh release context must audit the frozen manuscript/PDF against
primary citation passages, inspect all six pages, check build/metadata/fonts,
and run the actual release gate. No citation/visual release verdict or local
publication success flag has been fabricated by this writer.
