# Rendered-page visual audit

Job: c034-grouptri-release-98d1e823492f. PDF SHA256: e9b3d5055ad93f76865143de8acab7b3c4dc6c1f3cd1fe3b20482eb99d68cfa4. Manuscript digest: a40f8840ae0d14f65c4af83e804cb282ac08f663f3e89dfedb04cd0efadea7ba.

Accept. Rendered the final PDF with pdftoppm -r 120 -png, and actually opened and inspected every individual page image using view_image. PDF text extraction supplemented, rather than replaced, this visual review. Pages reviewed exactly: 1,2,3,4,5,6,7,8.

| Page | Actual observation |
|---|---|
| 1 | Correct title, sole author/institution and contact footer; full abstract and saving formula legible. Generous title-page whitespace is intentional. |
| 2 | Theorem 1.1, group presentation, prior-work comparison and coordinate-cost sentence fit margins. Body AI disclosure begins at bottom and continues normally on page 3. |
| 3 | Body AI disclosure completes; elementary backend, equations (1)--(2), signs and three-marker explanation legible. Lemma 3.1 continues onto page 4 without clipping. |
| 4 | Capped lemma completes; proof, superscripts, cutoff inequality, bound and parameters (3) clear; no overlap at transition to Section 4. |
| 5 | Hitting/frequency formulas (4)--(7), complete piece predicates and Lemma 4.1 proof legible; right equation numbers and proof box fit. |
| 6 | Attribution, carry cancellation, kernel map and complete-instance explanation readable. Recurrence (10) fits; proof continues normally onto page 7. |
| 7 | Five-row charged cost table has clear rules and labels; savings and induction readable. Finite coverage numbers legible; prose continues on page 8. |
| 8 | Finite-check qualification, distinct closing AI statement and all three bibliographic records visible; author names, dates, IDs and DOI links wrap without overflow. |

All eight final pages have legible symbols/fonts, consistent headers/page numbers, intact margins and no clipping, overlap, black glyph boxes or unreadable references. The only visual table is the cost ledger; its five entries match the TeX and accepted proof charges. There are no plotted data, figures, image-only claims or visual axes to audit. Rendered images are tmp/release-build/review-page-1.png through review-page-8.png; their hashes and exact matches to all independently rebuilt ZIP pages are in audit/reproduction.json. The eight total pages meet the user cap of twelve. The working_paper label in filename/metadata retains the actual venue assessment.
