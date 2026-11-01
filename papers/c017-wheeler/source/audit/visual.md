# Fresh rendered-page visual audit

Job: c017-wheeler-release-bce62e5f5c55. Date: 2026-11-01. Verdict: accept.
PDF: manuscript/main.pdf. Actual pages reviewed: 1,2,3,4,5,6,7,8,9,10, each once.

The frozen PDF was freshly rendered with pdftoppm -r 110 -png into
 tmp/pdfs/release-bce62e5f5c55-page-01.png through -10.png.
Each full page image was actually opened in this context using view_image.
This assessment is based on the rendered pages, not just text extraction or
prior writer confidence. The clean rebuild's corresponding ten PNGs are
byte-identical to these inspected images (release-rebuild.json), so its page
content is also the exact imagery inspected. This is image-equality evidence,
not a claim of an additional independent review.

| Page | Direct observation |
|---|---|
| 1 | Two-line title, sole author, abstract and bottom contact footnote are legible and inside the page. Blank lower space belongs to the separate title-page layout. Email is complete. |
| 2 | Introduction, numerical citations, model display and Theorem 1.1 fit the margins. The theorem's final line is visible above the page number; no clipped colex subscripts. |
| 3 | Theorem 1.2, Sections 2 and Lemmas 2.1–2.3 are readable. Equation 1 and proof boxes have clear spacing; the final lemma continues naturally on the next page. |
| 4 | Global-monotonicity proof, branching lemma, pump display and shell equation fit. Powers, reversed-word notation and equation numbers are legible. |
| 5 | Level decomposition, two-side lemma/proof, example transitions and algorithm fit. Displayed Equation 5 and small transition labels are legible with no collisions. |
| 6 | Complexity exponents and all quantified certificate inequalities are readable. The underfull-box whitespace around the corollary is visible but does not clip, overlap or hide content. Presburger paragraph ends above the footer. |
| 7 | Normalization and canonical-color section fits. Equations 6–8, lambda subscripts and arrow-output labels are legible. Convex-quotient subsection begins cleanly. |
| 8 | Padding discussion, representative equation and right-invariance/necessity arguments fit. Long Equation 9 stays within margins; no symbols collide. |
| 9 | Realizability completion, exact finite-coverage counts and AI methodology are readable. The shorter page ends naturally after the disclosure, before the explicit bibliography page break. |
| 10 | All six references are readable, with correctly numbered entries, accented names, versions and wrapped URLs. No dangling marker, overlap or text beyond the margins. |

No clipping, overlap, missing glyph, illegible equation or broken reference was
seen. There are no charts, tables or data figures requiring a separate visual-data
comparison. All pages retain consistent typography, clear hierarchy and page
numbers. Ten total pages satisfy the user's cap. This visual acceptance concerns
presentation of the bound PDF only, not mathematical truth or STOC acceptance.
