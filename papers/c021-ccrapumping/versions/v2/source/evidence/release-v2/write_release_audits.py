from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parents[2]
job='c021-ccrapumping-release-e862e3a691c8'
load=lambda p:json.loads((P/p).read_text())
sha=lambda p:hashlib.sha256((P/p).read_bytes()).hexdigest()
m=load('audit/manuscript-snapshot.json')
base={'job_id':job,'snapshot_digest':m['snapshot_digest'],'manuscript_digest':m['digest'],'pdf_digest':m['pdf_digest']}
header=f'Job: `{job}`. Reviewed 2026-11-01 UTC / 2026-11-02 Asia/Shanghai.\n\nEvidence snapshot: `{m["snapshot_digest"]}`.\nManuscript snapshot: `{m["digest"]}`.\nCurrent PDF: `{m["pdf_digest"]}`.\n\n'
citations='''# Verification Report

**Mode:** Search, with original-text inspection and accepted-scope comparison.
**Document:** manuscript/main.tex and all publication.json sources; final 11-page PDF.
**Method:** $citation-check-skill explicitly invoked as advisory. Fixed extraction in evidence/release-v2/claims-extracted.md/json preceded verification. The user's bounded autonomous release instruction overrides the skill's confirmation pause; no extra user approval was required. No designated Excel or authoritative external bibliography exists; literature/user_bibliography_check.md was read. No citation quota was imposed.

## Summary

Fifteen fixed claim groups were extracted. Nine attribution groups C05–C13 are supported by inspected primary text; five internal theorem/mechanism groups C01–C04 and C14 match the accepted frozen claim and the manuscript's proofs. C15 covers seven real bibliographic records: their identifying metadata and relevant texts were located, with one remaining optional publisher-label limitation for C25. No numerical discrepancy, hallucinated source, contradicted mathematical attribution, undefined key, unsupported strengthening or unsupported global priority assertion was found. **Verdict: accept_with_citation_limitations**, solely for the disclosed C25 metadata refresh limit.

## Sequential claim verification

| ID | Finding and precise support |
|---|---|
| C01 | Scope match: Theorem 1 is the accepted nonzero rational all-word-unipotent four-way characterization. Sections 3–6 retain arbitrary finite control, any finite register count, signed constants and singular/nonlinear updates. Zero is explicitly handled. |
| C02 | Scope match: Theorem 2 and Section 7.1 give intrinsic minimal-sector recognition and sector membership in polynomial bit time, not general CCRA membership. The universal trace criterion is proved, not inferred from finite enumeration. |
| C03 | Scope match: Theorem 3 and Sections 7.2–7.3 retain D=sum(|p|+1), NO length 2D, register count at most sum |p|, explicit patterns, binary rational coefficients, cancellation and empty cases. These are proved in the article and accepted packet. |
| C04 | Scope match: Theorem 4 and Section 8 use the exact source witness, one R=Z[1/2], one m=1, every triple and every n>=0, every degree sum, and full finite-state rational polynomial nonrecognizability. Disproved concerns the sufficiency implication. |
| C05 | Verified, paraphrase: MPS26 Definition 11, Theorem 15 and Section 3.2/Example 26, printed pp. 67:8 and 67:13, state the necessary condition, insufficiency conjecture and position-sum witness. Original official page images were inspected, including overbars on the algebraic closure. The source does not prove the nonrecognizability asserted here. |
| C06 | Verified, paraphrase: MPS26 Example 26 and MPSfull Appendix B.4 (printed p. 23:28) supply the polynomial pumping calculation. The manuscript credits it and uses the valid larger subsemiring Z[1/2], with its own explicit n+1 formula. |
| C07 | Verified, paraphrase: MPSfull Lemma 50, Appendix B.1 (printed p. 23:26), linearizes CCRA by maintaining squarefree monomials. The manuscript includes the short argument and does not claim this step as new. |
| C08 | Verified, paraphrase: MR19 Proposition 3 on p. 9 and Lemma 5 on p. 10 both expressly assume a non-zero semiring and non-zero automaton. Their no-cancellation hypotheses cannot be imported into arbitrary signed rational computations. The article's comparison is limited to these results. |
| C09 | Verified, paraphrase: PS24 Theorem 3.4/Corollary 3.5 (Section 3) concern invertible semigroup representations and block-triangular epimonomial/monomial covers under the stated spectral/power-splitting assumptions. Proposition 9.4 (Section 9) supplies corresponding ambiguity consequences for invertible weighted representations. No global polynomial copyless conclusion is attributed. |
| C10 | Verified, paraphrase: C25 Introduction explicitly gives polynomial-time rational-series commutativity via minimal matrices; Theorem 1 gives decidability for effective prevarieties. The full v2 primary text was inspected. This is correctly credited prior algorithmic work, distinct from the article's realizability theorem. |
| C11 | Verified, paraphrase: C26 Theorem 1, Corollary 2 and Theorem 3, printed pp. 29:4–29:5, classify bilinear associative commutative products and decide equivalence for finite-variable polynomial P-automata over finite alphabets. Section 1.2 also addresses commutativity. The manuscript's summary respects that scope. |
| C12 | Verified, paraphrase: BLR24 official abstract/Introduction, p. 23:1, explicitly concern linear register updates and extension to affine updates. The manuscript makes this limited comparison. |
| C13 | Verified, paraphrase: MPS26 Definition 11 and Theorem 15 match the EPS families and degree sums stated in Section 2. Partial sums exclude base 1, which is supplied by n; the manuscript distinguishes eventual EPS representation from the witness's all-n identity. |
| C14 | Scope match: Sections 3–6 preserve one common observable subquotient using the polynomial projection, only infer physical invertibility after restriction to the minimum image, and retain both minimality spans in the return-block transfer. No rectangular bridge or finite-search proof appears. |
| C15 | All seven records exist. Author/title/date/version/venue/page/identifier checks are documented below. Only C25's optional publisher label retains a metadata limitation; no nearby mathematical statement relies on that label. |

## Primary sources and record checks

- **MPS26:** Filip Mazowiecki, Antoni Puch and Daniel Smertnig; STACS 2026, LIPIcs 364, 67:1–67:21, DOI 10.4230/LIPIcs.STACS.2026.67. Official metadata matches. Original local PDF and pp. 8/13 images were read. [Official record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.67).
- **MPSfull:** same authors/title; arXiv:2502.07356v2, revised 12 January 2026, confirmed by the current primary version record. The bibliography's 2026 refers explicitly to this revised full version, not a claim that v1 first appeared in 2026. [Version record](https://arxiv.org/abs/2502.07356v2). Local Appendix B.1/B.4 text inspected.
- **MR19:** Filip Mazowiecki and Cristian Riveros; JCSS 100 (2019), 1–29, DOI 10.1016/j.jcss.2018.07.002. Publisher metadata and the actual author-hosted 29-page journal PDF match. [Original journal PDF](https://criveros.ing.uc.cl/papers/jcss19.pdf), [publisher record](https://www.sciencedirect.com/science/article/pii/S0022000018307815).
- **PS24:** Antoni Puch and Daniel Smertnig; arXiv:2410.03444v2, revised 29 October 2024. Current version record and original frozen PDF match the cited statements. [Version record](https://arxiv.org/abs/2410.03444v2). No subsequent published version was inferred from search snippets.
- **C25:** Lorenzo Clemente; LICS 2025, 804–817; full version arXiv:2503.21697v2, revised 16 May 2025. [Original full text](https://arxiv.org/html/2503.21697v2), [version record](https://arxiv.org/abs/2503.21697v2), [official conference archive](https://lics.siglog.org/archive/2025/Clemente-Thecommutativitypro.html). The author's official LICS 2026 paper, reference 13 on p. 29:22, prints IEEE and DOI 10.1109/LICS65433.2025.00066, matching the manuscript. The conference archive's export instead labels the publisher ACM. Direct DOI and Crossref refresh were inaccessible in this bounded audit. Preserve the primary author-supplied IEEE record and disclose this optional publisher-label ambiguity; source existence, author/title/year/pages and claim support are verified. No user-bibliography authority override is claimed.
- **C26:** Lorenzo Clemente; LICS 2026, LIPIcs 380, 29:1–29:23, DOI 10.4230/LIPIcs.LICS.2026.29. [Official record and original PDF](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.29). Bibliographic fields and Theorems 1–3 inspected directly.
- **BLR24:** Yahia Idriss Benalioua, Nathan Lhote and Pierre-Alain Reynier; MFCS 2024, LIPIcs 306, 23:1–23:15, DOI 10.4230/LIPIcs.MFCS.2024.23. [Official primary record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2024.23). Author/title/venue/year/pages match and abstract directly supports the comparison.

## Dependency, novelty and final-reference scope

Every source_files entry in publication.json was checked. Recorder inputs plus BibTeX log/configuration show authored dependencies main.tex, references.bib, local acmart.cls and ACM-Reference-Format.bst; BUILD.md, latexmkrc and official distribution README/dtx/ins are also frozen. Generated aux/out/bbl and system TeX packages are not omitted authored sources. There are no figures or imported custom mathematical files. All five local official distribution files are byte-identical to the designated official inputs; evidence/release-v2/official-inputs.json records the comparison.

All seven used keys equal all seven database keys and all seven resolved aux bibliography keys. The extracted and rendered final page 11 gives complete, readable references without question marks. The theorem and section cross-references resolve. Nothing in the article claims a first-ever commutativity algorithm or a general CCRA decision. A bounded current search on copyless/unipotent realizability, the exact source title/question, position-sum nonrecognizability and scattered-pattern/permutation terms found no equivalent full-scope resolution in the inspected primary sources. This is a bounded comparison, not a priority certificate; the substantive novelty verdict remains the actual accepted math/innovation review. The source's pumping calculation and known tools remain credited.

No citation was added or removed. No manuscript prose or accepted mathematical evidence was changed. Metadata access limits do not suppress the clean PDF or local release. The guessed CFP /cfp.html URL failed; the actual official [STOC 2027 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html) was then checked for named authors, 11pt single column, letter paper, one-inch margins and substantial AI disclosure. Numerical citation labels are a permissible difference from its preference for alphanumeric references. No submission or contact was performed.
'''
build='''# Fresh clean-build audit

**Verdict: accept.** After the PDF skill artifact marker succeeded once, this release context ran latexmk -C and latexmk -pdf main.tex from manuscript/. The build completed with exit code zero. Clean and command transcripts are in evidence/release-v2/clean.log and build-command.log. The binding compiler log is manuscript/build/main.log; the bibliography log manuscript/build/main.blg was also inspected.

Final TeX/BibTeX logs contain no compilation error, fatal diagnostic, undefined citation/reference, unresolved rerun, overfull box or underfull box. All seven bibliography entries were regenerated. Two harmless optional metadata warnings remain: acmart has no affiliation city, and C25 lacks a publisher address. The supplied institution/country and bibliographic data are retained rather than inventing information. These are not mathematical or layout failures. Intermediate first-pass unresolved references were resolved in the completed build.

The output has a valid PDF header, 11 pages, letter-size 612x792 point pages, selectable nonempty text and no encryption. It respects the user's 12-total-page cap. All 17 listed font instances are embedded with Unicode mappings. The PDF title matches the article. Its rendered author/contact and XMP creator are checked separately against authors.json; no external publication identifier or venue-acceptance statement is supplied. The PDFInfo Author field is not populated; this is not required by the current submission format, and the complete sole-author identification is plainly printed on page 1.

The manuscript sources, all frozen mathematical inputs and source.md remain byte-identical. The rebuild changes the PDF binary digest, as expected for a fresh compilation; freeze-manuscript was rerun successfully. The old/current extracted text and all eleven corresponding rendered-page PNG hashes are identical (evidence/release-v2/rebuild-comparison.json). Current final pages were then individually inspected. No proof, statement, bibliography or pagination was altered by the rebuild.

Complete dependency accounting is in evidence/release-v2/dependencies.json. The compiled local class and bibliography style and the remaining official input files all match the user-designated official distribution byte for byte. No source from another project was used. A preservation snippet initially used project-relative paths from manuscript/ and failed before copying; the clean build itself still ran, and preservation was corrected from the project root. evidence/release-v2/operations.md records that operational error honestly. It has no mathematical significance and no counter was reset.
'''
visual='''# Fresh rendered-page audit

**Verdict: accept.** The current manuscript/build/main.pdf was freshly rendered by pdftoppm at 110 dpi into evidence/release-v2/final-pages/page-01.png through page-11.png. Each final page was actually opened with the image viewer and inspected individually in this release context. This is not a pdftotext-only or file-existence check. The previous and current page images also match pixel for pixel after the clean rebuild.

| Page reviewed | Actual observations |
|---|---|
| 1 | Two-line title, one named author, UCSI University, Malaysia and correct email in the contact footer. Abstract text, Z[1/2], m=1 and footer are clear. Deliberate title-page whitespace; no clipping. |
| 2 | Four-way theorem enumeration and all-word hypotheses readable. Pattern dimension D, register/length bounds, witness sum and numbered equation fit within margins. |
| 3 | Full-model separation, prior-work paragraphs, citation numbers and definitions legible. No overlap between text and section heading. |
| 4 | EPS partial sums, W/N definitions, squarefree space and image/rank lemma render correctly, with subscripts and proof square visible. |
| 5 | Minimum-image restriction, affine-permutation equation, retraction, polynomial projection and barred E identity are distinct and readable. No lost overbar or clipped equation number. |
| 6 | Common quotient equation, lemma assumptions, Jordan factors and shifted variables fit. Dense proof remains legible with consistent spacing. |
| 7 | Finite root formula and Theorem 8 readable. Return blocks, B/A algebra, inverse and root equations clear; bottom equation remains inside margins. |
| 8 | Both minimality spans, theorem completion and universal trace criterion readable. The continuation onto page 9 is normal and no line is clipped. |
| 9 | Pattern matrix, adjacent-swap certificate, bit bounds and falling-factorial synthesis formula legible. Equation 9 and its denominator fit. |
| 10 | Position-sum matrices, order convention, uniform quadratic, subsemiring generators and complete nonrecognizability proof readable. No physical-invertibility assumption appears through lost notation. |
| 11 | Scope limitations, substantial AI disclosure and all seven references clear. DOI wrapping has no overlap or clipping. Running header and page number are consistent. |

No figures, statistical charts or tables occur in the manuscript. All mathematical glyphs examined are visible; there are no black boxes, unreadable raster elements, overlapping equation numbers or margin escapes. Single-column 11pt letter layout uses the official acmart inputs with one-inch margins. Fonts are embedded. The current official STOC 2027 CFP specifies named-author submissions and substantive AI disclosure, both present; its proceedings sigconf rule is separate from the current submission layout. The user cap is met at 11 total pages including title and references. This is a local artifact audit, not a venue quality or acceptance decision.
'''
for name,report in [('citations',citations),('build',build),('visual',visual)]:
 (P/f'audit/{name}.md').write_text(header+report)
 data=dict(base,verdict='accept',report=f'audit/{name}.md')
 if name=='citations':
  data.update(verdict='accept_with_citation_limitations',sources_checked=sorted(load('publication.json')['source_files']),dependency_scope_complete=True,undefined_citations=False,citation_audit_method='citation-check-skill-advisory-plus-primary-source-manual',scope='Complete publication dependency list, all seven references, original cited statements/hypotheses, accepted-scope manuscript comparison, bounded current primary novelty search, and extracted/rendered references checked. No user-designated Excel bibliography exists. C25 existence and mathematical support verified; optional publisher-label metadata refresh remains unavailable/conflicting, as disclosed in report.',unverified_citations=[{'key':'C25','limitation':'Optional publisher-label metadata: official author LICS 2026 reference says IEEE and gives the retained DOI; conference archive export says ACM. Direct DOI and Crossref refresh unavailable. Existence, identifying record and cited mathematical support verified from primary full text.'}])
 elif name=='build':
  data.update(build_log='manuscript/build/main.log',build_log_digest=sha('manuscript/build/main.log'),clean_build=True)
 else:
  data.update(pages_reviewed=list(range(1,12)))
 (P/f'audit/{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
