# Verification Report

**Mode:** Search, with accepted-proof scope checking for original mathematical assertions.
**Document:** manuscript/main.tex, manuscript/references.bib and final six-page PDF.
**Generated:** 2026-11-01. **Job:** c009-cycle2-release-70b6b8b76475.

## Summary

21 fixed extracted claims; 21 verified at the stated scope; 0 numerical errors, hallucinations, misleading attributions or unresolved citation records. Overall citation status: PASS. This is a local release audit, not a new mathematical referee verdict or exhaustive priority certification.

The explicitly invoked $citation-check-skill was used as an advisory two-pass method. The extraction was saved first in audit/release-claim-extraction.md. Verification then proceeded against that fixed list. The user expressly authorized the bounded autonomous release audit, overriding an extra advisory confirmation pause. Mathematical assertions were checked against the accepted claim and analytic text, rather than misattributed to external literature. Definitions and methodology descriptions were excluded by the extraction rules.

## Sequential verification of fixed claims

| ID | Status | Evidence and finding | Confidence class |
|---|---|---|---|
| C01 | Verified | Accepted full-scope claim; theorem and all analytic proofs agree. Every ell,n and all weighted hosts retained. | interpretation |
| C02 | Verified | HMNTW25 Definition3.1 and Problem3.23; frozen original and actual primary passages read. | paraphrase |
| C03 | Verified | HMNTW25 subdivision convention preceding Corollary3.21; (++--) orientation checked directly. | interpretation |
| C04 | Verified | GIKK23 Theorem12 and proof; coefficient values for4,8,12 yield nonnegative criterion, as already independently recomputed by referee. | interpretation |
| C05 | Verified | FHMZ24 Definition4.9 and Lemmas4.10-4.11; vertex and edge structure checked. | paraphrase |
| C06 | Verified | FHMZ22 Theorem1.5 and FHMZ24 Theorem4.2 explicitly require an edge homomorphism; mixed vertex obstructs it. | paraphrase |
| C07 | Verified | MPT04 Equation(3.2), p272, actual author-uploaded text. | paraphrase |
| C08 | Verified | MPT04 Theorem3.7(i), pp277-278, sigma1(A)>=delta(A). | paraphrase |
| C09 | Verified | Direct multiplication gives T^2 symmetric part diag(3/16,-1/16); norm submultiplicativity has the stated direction. | exact |
| C10 | Verified | Real skew matrix is normal with imaginary eigenvalues; singular values are their moduli. | exact |
| C11 | Verified | Indicator-vector operator bound and taking the4ell-th root of theorem constant give exactly factor2. | exact |
| C12 | Verified | Manuscript residual, adapted vector, Rayleigh quotient and n=1 handling match accepted proof. | exact |
| C13 | Verified | Every cyclic index expansion has4ell factors A/n and includes coincident maps. | exact |
| C14 | Verified | Skew top eigenspace has dimension>=2; Cauchy-Schwarz then min-max. No invalid squaring of Loewner order. | exact |
| C15 | Verified | Entry/Frobenius bound and beta<=d+sqrt(a) imply two-case forcing with accepted constant. | exact |
| C16 | Verified | K0 eigenvalues, beta=r/sqrt(3), Q eigenvalues and ratio argument give exactly2 beta^(4ell). | exact |
| C17 | Verified | FHMZ22 live arXiv primary metadata. | exact |
| C18 | Verified | FHMZ24 live arXiv primary metadata. | exact |
| C19 | Verified | GIKK23 live arXiv v3 metadata; year2023 is the identified version year. | exact |
| C20 | Verified | HMNTW25 live arXiv v1 metadata. | exact |
| C21 | Verified | MPT04 author-uploaded primary article record and first page; author institution publication list agrees. | exact |

## Primary sources and exact attribution scope

* **HMNTW25**: [v1, 12 December 2025](https://arxiv.org/abs/2512.11222v1). Actual text: https://arxiv.org/html/2512.11222v1. Locations: Definition3.1, printed p7; subdivision convention and Problem3.23, printed p17. Authors/title/year/version agree. The entire all-ell local family and weighted definition agree; this source is not represented as proving the new global result.

* **GIKK23**: [v3, 13 July 2023](https://arxiv.org/abs/2212.09343v3). Actual text: https://arxiv.org/html/2212.09343v3. Locations: Theorem12, printed p13, with coefficient expansion and proof. Metadata agree. Criterion and positive residual in its proof cover lengths4,8,12. Coefficient evidence read in audit/referee-prior-criterion.json and frozen theorem12 results. Failure at16 concerns only the criterion; manuscript makes no negative mathematical or exhaustive-priority inference.

* **FHMZ22**: [v1, 30 October 2022](https://arxiv.org/abs/2210.16971v1). Actual text: https://arxiv.org/html/2210.16971v1. Locations: Theorem1.5. Authors/title/year/version agree. Transfer requires a homomorphism to a directed edge; each current cycle has a mixed vertex, excluding that hypothesis.

* **FHMZ24**: [v1, 13 February 2024](https://arxiv.org/abs/2402.08418v1). Actual text: https://arxiv.org/html/2402.08418v1. Locations: Theorem4.2; Definition4.9; Lemmas4.10-4.11, printed pp16-18. Metadata agree. Edge-homomorphism hypothesis verified. D2 is precisely the two-parallel-two-edge-path four-cycle; Dk for k>2 has different degree/size structure from the serial family.

* **MPT04**: [Rocky Mountain Journal of Mathematics34(1),269-288,2004; DOI10.1216/rmjm/1181069905](https://www.researchgate.net/publication/38371363_Almost_Skew-Symmetric_Matrices). Actual text: author-uploaded full primary text at same URL. Locations: Equation(3.2), printed p272; Theorem3.7, printed pp277-278. Authors/title/journal/pages/year and DOI agree with author-uploaded record. Read actual block formula and sigma1(A)>=delta(A) statement. These concern the first power. DOI resolver failed and CiteSeer returned403, but the actual author-uploaded text and metadata were accessible; no citation remains unverified on that basis.

## Bibliography authority, current search and limitations

literature/user_bibliography_check.md was inspected. No Excel workbook or user-designated authoritative bibliography exists in this task. None was invented and no irrelevant citation was added. The five references are all substantively used. Metadata basis is accessible primary arXiv records and the author-uploaded primary MPT04 record/text, with institutional author-list corroboration. The optional publisher resolver and CiteSeer failures do not establish nonexistence or leave the accessible primary text unverified.

All applicable academic query templates were run: author/year/title fragment, full title with index/arXiv domain, author/year/venue, each available arXiv ID, and the MPT04 DOI. The exact queries and source findings are recorded in evidence/release-literature-check.json. Search date is2026-11-01. The latest displayed He record remains v1; Chen-Clemen-Noel v2 concerns paths/spiders; the current regular-tournament paper restricts both targets and hosts. No inspected statement contradicts the accepted comparison or supplies a known full-family implication. This is a bounded comparison, not proof of priority. Older operator leads remain subject to the limits disclosed by the accepted referee. No manuscript claim asserts exhaustive priority or venue acceptance.

## Complete dependency and PDF check

The exact dependency scope is the sorted source_files list in publication.json: manuscript/acmart.cls, manuscript/alphaurl.bst, manuscript/build.sh, manuscript/build/main.bbl, manuscript/main.tex, manuscript/references.bib. The TeX recorder, source imports, bibliography commands and BibTeX log were inspected. They identify main.tex, local acmart.cls, generated bbl, references.bib and alphaurl.bst; the build script is additionally included. main.aux and main.out are generated state regenerated by the clean build. All other TeX packages/fonts are system inputs. No external authored imports or figures are used; the orientation is shown in native TeX. The official class hash matches the designated unmodified distribution.

All five citation keys are defined, used and rendered with readable alphanumeric labels. The .bib, rebuilt .bbl, extracted PDF and page6 image agree. No unresolved citation or cross-reference appears in the clean compiler log or final pages. The density includes every vertex map; hypotheses, global scope, equality and exponent claims stay within the actual accepted claim. Known lengths4,8,12 are credited in abstract and prior work. Substantive Codex use is disclosed at the end. No unsupported strengthening or irrelevant citation was found. No prose or mathematical source was edited in this release job.
