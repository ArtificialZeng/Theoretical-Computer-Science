# Verification Report

Mode: Search verification, with accepted mathematical packet for the article's own results.
Job: c015-imagebound-release-b1a7d726335d. Checked 2026-11-01. Verdict: accept.

The advisory $citation-check-skill was explicitly invoked. Its extraction-only pass is fixed in audit/citation-extraction.md; the separate ordered verification pass is audit/citation-verification.json. The user authorized a complete bounded release audit, so no extra confirmation stage was introduced. All 21 extracted substantive claims pass at the stated scope: 21 verified, zero numerical errors, zero unverified, zero hallucinations, zero misleading claims. This is a source/scope audit and does not replace the actual fresh mathematical referee.

## Primary sources and attribution

KR2025: [publisher full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.62/LIPIcs.MFCS.2025.62.html), Sections 2, 7 and 9, with [official metadata/BibTeX](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.62). The model, bound and tightness question match. All bibliographic fields agree.

R2024: [corrected v4 text](https://arxiv.org/html/2405.19622v4), Sections 1, 3 and 4; [version record](https://arxiv.org/abs/2405.19622v4); [publisher record](https://link.springer.com/chapter/10.1007/978-3-031-72621-7_8). The deterministic queue transition agrees after the stated indexing change; the physical tail and quadratic benchmark are accurately credited. Rystsov is attributed through this inspected discussion, rather than presented as separately inspected. General NFA reset transitions do not give fixed image boundedness. Publisher metadata matches the bibliography. The publisher chapter text is subscription-only, but the expressly cited corrected author text is accessible and supplies the relevant passages.

A2017: [primary v1 PDF](https://arxiv.org/pdf/1701.07954v1) and [metadata](https://arxiv.org/abs/1701.07954v1). Section 2, Lemma 2.1 gives the appended-tail increment with its almost-permutation and divisibility conditions. The manuscript credits Vorel via the reproduced lemma and distinguishes sink synchronization from NFA mortality. No claim is made about an uninspected journal lemma number. Author, title, year, identifier and DOI agree.

## Original scope and novelty comparison

The current original-paper record remains v2, 23 July 2025. Fresh exact-terminology and mortality searches on 2026-11-01 identified no equivalent full fixed-k hierarchy resolution in the screened primary sources; this bounded result does not establish exhaustive priority. Current closest mechanisms were inspected directly above. The accepted innovation assessment in audit/innovation.json remains applicable: compressed shared clocks plus the port-separated potential supply the missing linear factor. The article makes no priority claim for CRT, the queue, known k=1 order, or upper bound. All theorem and proof environments remain byte-identical after the requested prose compression; explicit constants and every-sufficiently-large-n quantifiers agree with the accepted claim. Computational support was freshly replayed on exactly 22 finite automata and is described as finite support.

## Complete dependency and output scope

Reviewed all five publication source_files, including the local official class/style and generated bibliography, plus final extracted text and rendered references. The compiler recorder's only local source inputs are main.tex, acmart.cls and main.bbl; .aux/.out are generated state. BibTeX additionally consumes references.bib and ACM-Reference-Format.bst. All authored/local dependencies are enumerated, with no figure or external authored import. System TeX packages and fonts are installed dependencies. Citation keys A2017, KR2025 and R2024 each have exactly one bibliography item; no undefined citation or cross-reference remains. All three primary sources are relevant and none is inserted to meet a generic citation count.

literature/user_bibliography_check.md confirms that no Excel or user-designated bibliography was supplied. No workbook was invented. There is no unresolved citation-access limitation affecting the supported prose. The full query templates, primary retrievals and finite search limits are recorded in audit/release-web-records.json and audit/release-final-literature.json. The author/year/arXiv venue and original-paper arXiv-identifier queries also ran; their receipts are audit/release-template-completion.json.
