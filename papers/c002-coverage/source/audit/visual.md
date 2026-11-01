# Fresh rendered-page visual audit

Job: `c002-coverage-release-c84ac066553a`. Reviewed: 2026-10-31T22:05:01.069857+00:00.

Research snapshot: `26d2a64f317984b35b49212bdc46529ccb7f19bc1be1b5e471d28d308d18456e`.
Manuscript snapshot: `cbd9e040f4147d3e60fc3daafd59dcd1d2dfe965798be52063afe7345dcd085f`.
PDF: `b2dac13ca628fb6c3b7495516ee0acbdd390a90b0942127ada2935401ba873db`.

**Verdict: accept.** The canonical PDF was rendered in this job with `pdftoppm -r 120 -png output/pdf/sparse-coverage-discrepancy.pdf tmp/pdfs/release/page`. Each complete PNG was actually opened with the image-viewing tool, pages 1–4 together and pages 5–7 together, and inspected individually. Text extraction was used only as a complementary content check. No prior writer's visual report was substituted for this review.

| Page | Image inspected | Actual observations |
|---:|---|---|
| 1 | tmp/pdfs/release/page-1.png | Two-line title, sole author/affiliation, full abstract, author email footnote and folio are readable. The sparse lower title-page area is intentional. No collision or clipping. |
| 2 | tmp/pdfs/release/page-2.png | Model equations (1)–(2), Theorem 1.1 and bound (3) are clear. Prior bound's radical and logarithm are distinct. Multiplicity qualification and introductory prose fit within margins. |
| 3 | tmp/pdfs/release/page-3.png | Prior attribution continues normally; Lemma 2.1, bound (4), nested sums and final absolute-value display are legible and separated from prose. Proof-ending square is clear. |
| 4 | tmp/pdfs/release/page-4.png | Hall union/cardinality signs, Lemmas 3.1–3.2, modular states (5), symmetry (6), and hit probability (7) render correctly. Bottom display is above the folio; no overlap. |
| 5 | tmp/pdfs/release/page-5.png | Multi-index affine matrix (8) and column estimate (9) remain readable. Equation (10), telescoping bound and construction section fit. Page break in algorithm prose is normal. |
| 6 | tmp/pdfs/release/page-6.png | Fractional miss factor, powers/bit-length formulas and LP proof text are clear. Limits and substantial-AI-use paragraph are present, readable and within margins. |
| 7 | tmp/pdfs/release/page-7.png | All five bibliography labels and records are readable, with correct diacritics, years, page ranges, DOI/arXiv identifiers. Hanging indents and line wraps do not collide or clip. |

Exactly pages [1,2,3,4,5,6,7] were reviewed. There are no charts, figures or data tables. Mathematical glyphs, proof squares, primes, subscripts, radicals and displayed equations have no missing-glyph boxes. No text overlaps, truncated formulas, stray material outside the page, illegible bibliography or substantive spacing defect was observed. All pages have consistent typography, text width and folios. Seven total pages, including title and bibliography, satisfy the twelve-page user limit. The title page correctly names Zijian Zeng/UCSI University and the supplied email; the paper is not anonymous, consistent with the current CFP.

This is actual presentation review of the unchanged frozen PDF, not a mathematical truth or external acceptance certificate. No source/PDF repair was necessary.
