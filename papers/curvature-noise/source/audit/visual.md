# Fresh rendered-page visual audit

Job: `curvature-noise-release-132a90b124b3`. Date: 2026-10-31.
**Verdict: accept.** I freshly rendered the current frozen PDF with Poppler:

`pdftoppm -scale-to 1800 -png manuscript/main.pdf audit/release-pages/page`

Each of the six full-page PNGs was actually opened and visually inspected in
this context, individually, in physical page order. Text extraction was a
supplement, not the visual audit. Image hashes are in
`audit/release-checks.json`; the current PDF digest is bound in `visual.json`.

| Physical page | Actual observations |
|---|---|
| 1 | Separate cover. Two-line title, five authors and institutions in the required order, concise positive abstract and all five contact emails are legible. Fractions, subscripts, floor symbols and limits render clearly. No cover folio, overlap, clipping or copyright strip. The open space separates abstract and contact block naturally. |
| 2 | Body folio 1. Model, curvature definition, finite theorem, explicit pair, sparse corollary and example fit the text region. The long max expression, exponent and equation numbers are contained. Citation SVW14 is resolved and colored. No collision at the theorem/corollary transitions. |
| 3 | Body folio 2. Related-work citations show resolved alpha labels. Construction, baseline, Table 1, oracle validity and c inequalities are readable. Table column labels and all parameter values match the formulas; rules and caption do not overlap text. |
| 4 | Body folio 3. Uniform-shift comparison, all-size tail chain, adaptive-query proof and final QED are entirely visible. Long multiline inequalities are aligned. The logged underfull vertical box produces modest spacing, with no clipping or other substantive defect. |
| 5 | Body folio 4. Singleton proof, corollary proof, asymptotic equations and exact-tail definitions are legible. Summation limits, square-root ceiling, rho subscripts and the hypergeometric term render correctly. Page break after beta's explanation is coherent. |
| 6 | Body folio 5. Exact-tail lemma, finite fractions and open directions appear before the two-sentence factual AI paragraph. References follow as the final content, with four alphabetic labels and full author lists. No trailing appendix/disclosure after references, clipping, overlap or unresolved citation glyphs. |

All pages have readable body text, equations, table and folios. No missing glyphs,
unreadable figure, clipped equation, overlapping element or unexpected blank
page was found. Single-column composition, nominal one-inch text margins,
11pt body/caption/reference settings and single spacing agree with the sources
and build evidence. There are six total pages, below the user's limit of twelve.
Info/XMP authors, emails, institutions, title and embedded-font checks are
recorded in the build audit. The AI paragraph is before the final bibliography;
the abstract presents the precise positive result without a closing task-status
disclaimer. The original problem's unresolved status remains accurate in the
claim/publication/dossier and the closing research directions.

The PDF was not changed. No rebuild/refreeze cycle was needed. This report
certifies only the inspection actually described, not mathematical correctness
or conference acceptance. `pages_reviewed` is exactly `[1,2,3,4,5,6]`.
