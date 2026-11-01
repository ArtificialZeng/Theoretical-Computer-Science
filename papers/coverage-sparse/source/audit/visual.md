# Fresh every-page visual audit

Verdict: accept. Job `coverage-sparse-release-baf234409c0d`.

Rendered the current output/pdf/main.pdf with system pdftoppm at 110 dpi to
`evidence/release/baf234409c0d/page-1.png` through page-8.png. Each of the eight
full-page images was actually opened and inspected in this fresh context.
Text extraction, bbox checks and font checks supplemented the image review.
Current digest bindings and exact pages_reviewed=[1,2,3,4,5,6,7,8] are in visual.json.

| Physical PDF page | Actual observations |
|---|---|
| 1 | New modest title wraps cleanly to two lines. All five ordered names and institutions, abstract equations and five contact emails are readable. Separate cover has no folio or invented publication data. Contact block fits comfortably. |
| 2 | The motivating introduction is first. Model displays, alpha_k definition and Theorem 1.1 are legible. Table 1 follows its definition and callout at the bottom; it no longer precedes Section 1. All 15 exact rational entries and rules fit. |
| 3 | Contribution roadmap, related-work discussion and coloring proof are readable. Citation labels and equations resolve. Complete six-author attribution is present; no label or text overlap. |
| 4 | Normalized Cartesian construction, product formula and scientific TikZ figure are clear. Triangle edges, orange transversal, shaded block and T/C roadmap are distinct. Caption is accurate. Collision proof and start of the finite theorem are readable; the removed process clause is absent. |
| 5 | Natural continuation of the finite theorem, its proof, both inclusion chains and exact matching theorem/coupling are clear. Equations (4)–(8), parameters and limits fit. The error-scale paragraph continues normally to the next page. |
| 6 | Finite orbit argument and Proposition 4.2 fit. Table 2's five primal/dual rows have readable rational masses and values. Reproduction filenames and portable entry point are clear. The next section and t-wise definition introduce the corollary. |
| 7 | Table 3's complete 20-profile slack certificate is readable. Corollary 5.1's sandwich, finite rate and proof are clear, followed by attribution and open questions. Final AI disclosure consists of two factual sentences. |
| 8 | References are last. Seven alpha entries show complete author lists, correct years, venue/page details and functioning DOI/arXiv links without duplicate identifier fragments. No clipping or awkward unbroken URL exceeds the page. |

All pages use the same single-column typography, normal single spacing and
nominal one-inch Letter geometry. Normal math scripts are smaller than body
text. Bbox measurements show ordinary glyph/microtype protrusion of at most
about 1.85 PDF points horizontally and 2.57 points vertically beyond the nominal
text rectangle; no content is clipped or collides with the folios. The cover's
white space is appropriate for the required separate cover. No unreadable
glyph, black box, overlapping float, missing symbol or substantive layout defect
was found. Page count eight satisfies the user's twelve-page total cap.

The separate source-package clean build was also rendered on all eight pages.
Its PNGs are byte-identical to the eight images inspected above, as recorded in
archive-build-comparison.json. The inspected visual content therefore covers
both builds without relying on pdftotext alone.

The final-style checklist was applied to the actual images. Title, first-table
position, redundant collision-proof clause and AI disclosure were repaired;
response-to-review stage language now reports the actual completed audits.
No frozen mathematical evidence or accepted theorem was edited.
