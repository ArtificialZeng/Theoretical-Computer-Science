# Verification Report

**Mode:** Search verification, with frozen-proof/record checks for authored mathematics and finite-check descriptions.
**Document:** manuscript/main.tex and the complete seven-page frozen PDF.
**Generated:** 2026-11-02 UTC.

| Metric | Count |
|---|---:|
| Fixed extracted claims | 32 |
| Verified against primary text or accepted frozen records | 32 |
| Numerical errors | 0 |
| Unverified citations | 0 |
| Contradicted or misleading attributions | 0 |

**Overall status: PASS for release citation and scope review.** This is neither fresh mathematical certification nor an exhaustive novelty guarantee.

Job: `c037-msthalf-release-aff0d39d4223`. Date: 2026-11-02 UTC.

Mathematical snapshot: `d0a2fbd366a632f17366053e75f1a37a1254cc80a92e14c60a7d14734548277b`. Manuscript: `21d0504817983aa84f21573d2ff6560239183353573fc2cc1d767e3501675427`. PDF: `67321fa41524b5de24e7bfa5125e659333f1c58a51427d0fa0ef1d1ab378bba4`.

$citation-check-skill was explicitly invoked as an advisory aid. Pass 1 is saved in evidence/release/citation-extraction.md and .json; pass 2 uses that unchanged list in order below. The user's bounded autonomous JSON-only release instruction supersedes the advisory skill's interactive confirmation step. The two passes were kept separate.

No Excel workbook or authoritative user BibTeX record was designated; literature/user_bibliography_check.md was read. Both genuinely relevant primary papers already appear in the bibliography. No unrelated reference was inserted. All applicable academic search templates were run; exact queries and primary URLs are in evidence/release/citation-search-log.json. Search hits were used for discovery only, and no secondary hit establishes a theorem. Both cited sources and original theorem passages were accessible through the web tool. Optional direct local downloads failed DNS resolution; this operational limitation has no mathematical or bibliographic implication.

## Claim-to-source check, in fixed extraction order

| Claim | Source and location | Finding |
|---|---|---|
| C01 | accepted frozen original and full proof; manuscript Theorem 1.1 | Verified: Same all-n, all-metric, all-post-mask-adversary scope, with explicit finite no-query procedure. No efficiency claim added. |
| C02 | Anand et al. v1, Theorems 1.4/5.3 | Verified: The arbitrary-increase/decrease upper bound has p<1/4 and expected O_p(log n) true cost. |
| C03 | Anand et al. v1, Theorem 1.5 and Section 7 | Verified: The source supplies a linear obstruction at or above one half. Positive-distance regularization is explicitly supplied and credited in the manuscript. |
| C04 | Bateni et al., official PMLR paper pp.2-3 | Verified: The weak/strong model and query types are described there. |
| C05 | Bateni et al., official PDF p.5, Theorem 4 | Verified: The metric-weak-observation hypothesis and absence of strong queries are explicit; the expected approximation is O(sqrt(log n)). |
| C06 | Bateni et al., official PDF p.46, F.2.2, Theorem 32 | Verified: The stated corruption probability is 1/3 and the obstruction is logarithmic in expectation. No stronger parameter range is asserted. |
| C07 | Anand et al. v1, Theorems 1.4/5.3; current arXiv record; bounded searches | Verified: The checked record still lists only v1. Comparison is bounded to cited versions; the paper disclaims exhaustive priority. |
| C08 | C01 and Bateni et al. Theorem 32 | Verified: Logarithmic upper/lower order agrees at 1/3 only; the paper explicitly avoids extrapolating that lower bound to every p. |
| C09 | Anand et al. v1, Definition 3.1, Lemma 3.2, Definition 5.2 and Section 5 algorithm | Verified: Repair, minimum-certificate selection and first-appearance path are credited. The changed all-n expectation is proved in full. |
| C10 | Anand et al. v1, Lemma 5.6 proof, common-neighbor charging and final bad-density comparison | Verified: Their contradiction uses bad fraction 2p+2epsilon<1/2. Describing its good fraction as exceeding one half is accurate; it is a limitation of that argument, not an impossibility claim. |
| C11 | frozen proof Section 1; accepted math report Section 1; manuscript Lemma 2.1 | Verified: Constants 320 and 8, weighted order, positive hereditary rectangle density, every metric and vacuous cases match acceptance. |
| C12 | same frozen transfer proof, hereditary-density paragraph | Verified: m>=2r averaging and the 2ceil(2r/eta) star condition are transcribed faithfully. |
| C13 | same frozen transfer proof, interval definition | Verified: The 64 and 32 factors, strict inequalities, zeros and interval endpoints match. |
| C14 | same frozen transfer proof, overlap argument | Verified: Parity gives a matching; the top endpoint has no leaf neighbor anywhere, and the empty rectangle contradicts eta>0. No hidden algorithmic graph labels appear. |
| C15 | same frozen transfer proof, integration | Verified: A single integral and diameter<=M give the accepted bound; the manuscript includes the vacuous case. |
| C16 | frozen proof Section 2; accepted math report Section 2; Anand Lemma 3.2 mechanism | Verified: The explicit unconditional all-n formula is proved in the manuscript and is not misrepresented as the exact original lemma statement. |
| C17 | frozen proof observable-procedure section; accepted math report Section 3 | Verified: Rational hardcoding, lexicographic choices and finite fallback are explicit and within the exact-arithmetic scope. |
| C18 | frozen proof concentration section; accepted math report Section 2 | Verified: The constants and n^-12 union bound are unchanged; uniformity is over masks before arbitrary replacement choices. |
| C19 | frozen proof composition; accepted math report Section 3 | Verified: Qualification, comparison cost and positive density eta reproduce acceptance, with hidden graph used only for analysis. |
| C20 | same frozen composition; manuscript Section 5 | Verified: Observed Euler nonnegative weights and W<=2X are preserved. |
| C21 | same frozen composition; accepted math report Section 3 | Verified: Unconditional nonnegative X expectation is used; no false independence or conditioning is introduced. |
| C22 | same frozen expectation calculation | Verified: Universal output cost and series 2/alpha^3 match exactly, including beta=0 convention. |
| C23 | same frozen final theorem proof | Verified: Displayed C_p has the accepted finite fixed-p parameters and full adversary quantifiers. |
| C24 | Anand et al. v1, Section 7 general model; accepted math report Section 5 | Verified: The source construction has zero within-cluster distances; the manuscript transparently supplies the standard strictly positive delta version rather than attributing those formulas verbatim to the source. |
| C25 | accepted math report Section 5; manuscript displayed regularization | Verified: Substitution delta=n^-2 gives the credited Omega(n) boundary; no new lower bound is claimed. |
| C26 | frozen interval-packing-check/validation records; accepted referee-verification record | Verified: 160 instances, the four sizes and listed metric families/weights match the saved records. These are finite checks, not metric-space coverage. |
| C27 | frozen interval-packing-validation.json; audit/referee-verification.json | Verified: Both records give exactly 2,802,752 checked rectangles. |
| C28 | same frozen validation and actual referee-verification repair results | Verified: The exact mask count is 33,866 across n=2,...,6, at the four listed rational probabilities. The description does not claim all real probabilities were enumerated. |
| C29 | accepted referee math report and referee-verification code; check-math provenance | Verified: The distinct research/referee contexts and distinct verifier are documented; the manuscript calls this internal model checking, not external peer review or formal certification. |
| C30 | explicit manuscript procedure and accepted proof scope | Verified: Exhaustive search supports only finite computability; no efficient implementation or extra application is asserted. The displayed constants depend inversely on the below-half gap. |
| C31 | current arXiv abstract/version record and primary full text | Verified: All five authors, title, identifier, v1 date and arXiv-issued DOI match the BibTeX and rendered reference. |
| C32 | official PMLR landing page/BibTeX and full text | Verified: All four authors, title, editors, COLT year, volume 247 and proceedings pages 498-550 match. Internal PDF pages 1-53 do not contradict proceedings pagination. |

## Primary records and attribution limits

[Anand et al. primary record](https://arxiv.org/abs/2610.40594) and [v1 full text](https://arxiv.org/html/2610.40594v1) were checked for the five-author title, date, DOI and version. The record lists only v1, submitted 29 October 2026. Definitions 2.1-2.3 match the mask/adversary/true-cost model. Theorems 1.4/5.3 support the prior quarter upper bound; Theorem 1.5/Section 7 support the half boundary. The repair is credited to Lemma 3.2, and its all-n indicator-weighted formulation is proved here rather than misquoted. Definition 5.2, the minimum-certificate algorithm and the Lemma 5.6 bad-density calculation establish the precise known framework and limitation. The new proof does not silently attribute its interval/star argument to that source.

[Bateni et al. official metadata](https://proceedings.mlr.press/v247/bateni24a.html) and [official paper](https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf) were checked. Theorem 4 is on internal PDF page 5; Appendix F.2.2/Theorem 32 is on internal page 46. The metric-observation restriction and the lower bound at corruption 1/3 are correctly distinguished. The PMLR record supplies pages 498-550; the PDF uses internal pages 1-53. These are compatible pagination conventions. The manuscript does not generalize the logarithmic lower bound to every p.

The bounded current search found no primary equivalent extending the unrestricted upper bound through all p<1/2. The manuscript expressly limits priority comparison to checked versions and does not claim exhaustive priority. The original theorem, all-n cases, rational fixed-p parameters, adversary quantifiers and constants match the accepted proof. No unsupported strengthening was found. AI/finite-check descriptions match actual internal records without claiming external review. The accepted STOC assessment remains working_paper.

## Dependency and rendered reference review

Every publication.json source_files entry was read: main.tex; references.bib; build/main.bbl; build.sh; README.md; and the three unmodified official ACM files. The compiler recorder's project-local inputs are main.tex, acmart.cls and build/main.bbl; BibTeX identifies references.bib and ACM-Reference-Format.bst. No other authored or local imported dependency appears, and no figure or table is imported. README, the source DTX and build script are harmless extra packaged sources. System TeX packages are omitted as allowed. Evidence: evidence/release/dependency-check.json and official-template-check.json.

Exactly AGJLV26 and BDJW24 are cited, and both keys resolve exactly once in the generated bibliography. Both references and numeric cross-references were checked in extracted text and on rendered pages 2, 4, 6 and 7. There are no undefined citations, placeholders or unsupported novelty statements. Neither reference is unnecessary: the first supplies the direct framework and threshold comparison, and the second distinguishes the oracle assumption and logarithmic obstruction. No citation-access limitation remains requiring accept_with_citation_limitations.
