from pathlib import Path
import hashlib,json,datetime
P=Path('.')
E=P/'evidence/release'
J='c037-msthalf-release-aff0d39d4223'
ms=json.loads((P/'audit/manuscript-snapshot.json').read_text())
publication=json.loads((P/'publication.json').read_text())
common={'job_id':J,'snapshot_digest':ms['snapshot_digest'],'manuscript_digest':ms['digest'],'pdf_digest':ms['pdf_digest']}
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(path,data): Path(path).write_text(json.dumps(data,indent=2)+'\n')
# Fixed pass-1 list; verification proceeds in this order, with no new claims.
claims=json.loads((E/'citation-extraction.json').read_text())
verification={
'C01':('accepted frozen original and full proof; manuscript Theorem 1.1','Same all-n, all-metric, all-post-mask-adversary scope, with explicit finite no-query procedure. No efficiency claim added.'),
'C02':('Anand et al. v1, Theorems 1.4/5.3','The arbitrary-increase/decrease upper bound has p<1/4 and expected O_p(log n) true cost.'),
'C03':('Anand et al. v1, Theorem 1.5 and Section 7','The source supplies a linear obstruction at or above one half. Positive-distance regularization is explicitly supplied and credited in the manuscript.'),
'C04':('Bateni et al., official PMLR paper pp.2-3','The weak/strong model and query types are described there.'),
'C05':('Bateni et al., official PDF p.5, Theorem 4','The metric-weak-observation hypothesis and absence of strong queries are explicit; the expected approximation is O(sqrt(log n)).'),
'C06':('Bateni et al., official PDF p.46, F.2.2, Theorem 32','The stated corruption probability is 1/3 and the obstruction is logarithmic in expectation. No stronger parameter range is asserted.'),
'C07':('Anand et al. v1, Theorems 1.4/5.3; current arXiv record; bounded searches','The checked record still lists only v1. Comparison is bounded to cited versions; the paper disclaims exhaustive priority.'),
'C08':('C01 and Bateni et al. Theorem 32','Logarithmic upper/lower order agrees at 1/3 only; the paper explicitly avoids extrapolating that lower bound to every p.'),
'C09':('Anand et al. v1, Definition 3.1, Lemma 3.2, Definition 5.2 and Section 5 algorithm','Repair, minimum-certificate selection and first-appearance path are credited. The changed all-n expectation is proved in full.'),
'C10':('Anand et al. v1, Lemma 5.6 proof, common-neighbor charging and final bad-density comparison','Their contradiction uses bad fraction 2p+2epsilon<1/2. Describing its good fraction as exceeding one half is accurate; it is a limitation of that argument, not an impossibility claim.'),
'C11':('frozen proof Section 1; accepted math report Section 1; manuscript Lemma 2.1','Constants 320 and 8, weighted order, positive hereditary rectangle density, every metric and vacuous cases match acceptance.'),
'C12':('same frozen transfer proof, hereditary-density paragraph','m>=2r averaging and the 2ceil(2r/eta) star condition are transcribed faithfully.'),
'C13':('same frozen transfer proof, interval definition','The 64 and 32 factors, strict inequalities, zeros and interval endpoints match.'),
'C14':('same frozen transfer proof, overlap argument','Parity gives a matching; the top endpoint has no leaf neighbor anywhere, and the empty rectangle contradicts eta>0. No hidden algorithmic graph labels appear.'),
'C15':('same frozen transfer proof, integration','A single integral and diameter<=M give the accepted bound; the manuscript includes the vacuous case.'),
'C16':('frozen proof Section 2; accepted math report Section 2; Anand Lemma 3.2 mechanism','The explicit unconditional all-n formula is proved in the manuscript and is not misrepresented as the exact original lemma statement.'),
'C17':('frozen proof observable-procedure section; accepted math report Section 3','Rational hardcoding, lexicographic choices and finite fallback are explicit and within the exact-arithmetic scope.'),
'C18':('frozen proof concentration section; accepted math report Section 2','The constants and n^-12 union bound are unchanged; uniformity is over masks before arbitrary replacement choices.'),
'C19':('frozen proof composition; accepted math report Section 3','Qualification, comparison cost and positive density eta reproduce acceptance, with hidden graph used only for analysis.'),
'C20':('same frozen composition; manuscript Section 5','Observed Euler nonnegative weights and W<=2X are preserved.'),
'C21':('same frozen composition; accepted math report Section 3','Unconditional nonnegative X expectation is used; no false independence or conditioning is introduced.'),
'C22':('same frozen expectation calculation','Universal output cost and series 2/alpha^3 match exactly, including beta=0 convention.'),
'C23':('same frozen final theorem proof','Displayed C_p has the accepted finite fixed-p parameters and full adversary quantifiers.'),
'C24':('Anand et al. v1, Section 7 general model; accepted math report Section 5','The source construction has zero within-cluster distances; the manuscript transparently supplies the standard strictly positive delta version rather than attributing those formulas verbatim to the source.'),
'C25':('accepted math report Section 5; manuscript displayed regularization','Substitution delta=n^-2 gives the credited Omega(n) boundary; no new lower bound is claimed.'),
'C26':('frozen interval-packing-check/validation records; accepted referee-verification record','160 instances, the four sizes and listed metric families/weights match the saved records. These are finite checks, not metric-space coverage.'),
'C27':('frozen interval-packing-validation.json; audit/referee-verification.json','Both records give exactly 2,802,752 checked rectangles.'),
'C28':('same frozen validation and actual referee-verification repair results','The exact mask count is 33,866 across n=2,...,6, at the four listed rational probabilities. The description does not claim all real probabilities were enumerated.'),
'C29':('accepted referee math report and referee-verification code; check-math provenance','The distinct research/referee contexts and distinct verifier are documented; the manuscript calls this internal model checking, not external peer review or formal certification.'),
'C30':('explicit manuscript procedure and accepted proof scope','Exhaustive search supports only finite computability; no efficient implementation or extra application is asserted. The displayed constants depend inversely on the below-half gap.'),
'C31':('current arXiv abstract/version record and primary full text','All five authors, title, identifier, v1 date and arXiv-issued DOI match the BibTeX and rendered reference.'),
'C32':('official PMLR landing page/BibTeX and full text','All four authors, title, editors, COLT year, volume 247 and proceedings pages 498-550 match. Internal PDF pages 1-53 do not contradict proceedings pagination.')}
rows=[]
for c in claims:
 loc,finding=verification[c['id']]
 rows.append({**c,'status':'Verified','confidence':'paraphrase' if c['id'] in ['C02','C03','C04','C05','C06','C09','C10','C31','C32'] else 'interpretation','evidence_location':loc,'finding':finding})
dump(E/'citation-verification.json',{**common,'mode':'Search plus frozen-record transcription checks','two_pass':True,'total_claims':len(rows),'verified':len(rows),'unverified':0,'numerical_errors':0,'misleading':0,'hallucinations':0,'claims':rows})
queries=[
'Anand 2026 Approximating Minimum Spanning',
'"Approximating Minimum Spanning Trees in Metrics under Semi-Random Corruptions" site:semanticscholar.org OR site:arxiv.org',
'Anand 2026 SODA minimum spanning corruptions',
'doi:10.48550/arXiv.2610.40594',
'arxiv:2610.40594',
'Bateni 2024 Metric Clustering and',
'"Metric Clustering and MST with Strong and Weak Distance Oracles" site:semanticscholar.org OR site:arxiv.org',
'Bateni 2024 Conference on Learning Theory',
'"minimum spanning" "semi-random" "one half"',
'"2610.40594" "1/2" improvement',
'"minimum spanning trees" "rectangle" "corruption"',
'arxiv:2310.15863']
dump(E/'citation-search-log.json',{**common,'date_utc':'2026-11-02','queries_executed':queries,'primary_records':['https://arxiv.org/abs/2610.40594','https://arxiv.org/html/2610.40594v1','https://proceedings.mlr.press/v247/bateni24a.html','https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf','https://arxiv.org/abs/2310.15863'],'result':'Both cited records and theorem passages verified through primary web text. Bounded searches found no primary equivalent for the full below-half upper bound; this is not exhaustive priority verification. Irrelevant search hits were not used as evidence.','operational_limit':'Direct urllib downloads failed local DNS lookup; web primary text access succeeded. This is not mathematical evidence or an unverified citation. No workbook was designated.'})
header=f'Job: `{J}`. Date: 2026-11-02 UTC.\n\nMathematical snapshot: `{ms["snapshot_digest"]}`. Manuscript: `{ms["digest"]}`. PDF: `{ms["pdf_digest"]}`.\n\n'
cite_report='''# Verification Report

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

'''+header+'''$citation-check-skill was explicitly invoked as an advisory aid. Pass 1 is saved in evidence/release/citation-extraction.md and .json; pass 2 uses that unchanged list in order below. The user's bounded autonomous JSON-only release instruction supersedes the advisory skill's interactive confirmation step. The two passes were kept separate.

No Excel workbook or authoritative user BibTeX record was designated; literature/user_bibliography_check.md was read. Both genuinely relevant primary papers already appear in the bibliography. No unrelated reference was inserted. All applicable academic search templates were run; exact queries and primary URLs are in evidence/release/citation-search-log.json. Search hits were used for discovery only, and no secondary hit establishes a theorem. Both cited sources and original theorem passages were accessible through the web tool. Optional direct local downloads failed DNS resolution; this operational limitation has no mathematical or bibliographic implication.

## Claim-to-source check, in fixed extraction order

| Claim | Source and location | Finding |
|---|---|---|
'''
for r in rows:
 cite_report+=f'| {r["id"]} | {r["evidence_location"]} | Verified: {r["finding"]} |\n'
cite_report+='''
## Primary records and attribution limits

[Anand et al. primary record](https://arxiv.org/abs/2610.40594) and [v1 full text](https://arxiv.org/html/2610.40594v1) were checked for the five-author title, date, DOI and version. The record lists only v1, submitted 29 October 2026. Definitions 2.1-2.3 match the mask/adversary/true-cost model. Theorems 1.4/5.3 support the prior quarter upper bound; Theorem 1.5/Section 7 support the half boundary. The repair is credited to Lemma 3.2, and its all-n indicator-weighted formulation is proved here rather than misquoted. Definition 5.2, the minimum-certificate algorithm and the Lemma 5.6 bad-density calculation establish the precise known framework and limitation. The new proof does not silently attribute its interval/star argument to that source.

[Bateni et al. official metadata](https://proceedings.mlr.press/v247/bateni24a.html) and [official paper](https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf) were checked. Theorem 4 is on internal PDF page 5; Appendix F.2.2/Theorem 32 is on internal page 46. The metric-observation restriction and the lower bound at corruption 1/3 are correctly distinguished. The PMLR record supplies pages 498-550; the PDF uses internal pages 1-53. These are compatible pagination conventions. The manuscript does not generalize the logarithmic lower bound to every p.

The bounded current search found no primary equivalent extending the unrestricted upper bound through all p<1/2. The manuscript expressly limits priority comparison to checked versions and does not claim exhaustive priority. The original theorem, all-n cases, rational fixed-p parameters, adversary quantifiers and constants match the accepted proof. No unsupported strengthening was found. AI/finite-check descriptions match actual internal records without claiming external review. The accepted STOC assessment remains working_paper.

## Dependency and rendered reference review

Every publication.json source_files entry was read: main.tex; references.bib; build/main.bbl; build.sh; README.md; and the three unmodified official ACM files. The compiler recorder's project-local inputs are main.tex, acmart.cls and build/main.bbl; BibTeX identifies references.bib and ACM-Reference-Format.bst. No other authored or local imported dependency appears, and no figure or table is imported. README, the source DTX and build script are harmless extra packaged sources. System TeX packages are omitted as allowed. Evidence: evidence/release/dependency-check.json and official-template-check.json.

Exactly AGJLV26 and BDJW24 are cited, and both keys resolve exactly once in the generated bibliography. Both references and numeric cross-references were checked in extracted text and on rendered pages 2, 4, 6 and 7. There are no undefined citations, placeholders or unsupported novelty statements. Neither reference is unnecessary: the first supplies the direct framework and threshold comparison, and the second distinguishes the oracle assumption and logarithmic obstruction. No citation-access limitation remains requiring accept_with_citation_limitations.
'''
(P/'audit/citations.md').write_text(cite_report)
scope='All eight sorted publication.json source_files, both primary bibliographic records and original theorem passages, every fixed extracted claim, accepted-proof transcription, complete recorder/BibTeX dependencies and extracted/rendered references checked on 2026-11-02 UTC. No user workbook designated. Both references verified via primary web access; direct local download DNS failures did not prevent primary text inspection. Current novelty screen is bounded and makes no exhaustive-priority certification. No citation remains unverified; working_paper retained.'
dump(P/'audit/citations.json',{**common,'verdict':'accept','report':'audit/citations.md','sources_checked':sorted(publication['source_files']),'dependency_scope_complete':True,'undefined_citations':False,'scope':scope,'citation_audit_method':'citation-check-skill-advisory plus primary-source-manual','unverified_citations':[]})
log='manuscript/build/main.log'
build_report='# Fresh build and source-package audit\n\n'+header+'''Verdict: accept. The reviewed final manuscript/PDF and all frozen mathematics were preserved byte for byte. The current final compiler log is manuscript/build/main.log; its exact digest is bound by audit/build.json. The reviewed PDF has seven Letter pages (612 by 792 points), below the user cap of twelve total pages. Text extraction is nonempty, fonts are embedded, and no encryption or JavaScript is present.

I built a new local source ZIP from publication.json and its eight source inputs, unpacked it in evidence/release/reproduction, and ran `sh manuscript/build.sh` there from clean auxiliary/build state. The included BBL is a declared generated input and was regenerated by BibTeX. The command exited zero. The fresh command log is evidence/release/reproduction-build.log, and the final replica compiler log is evidence/release/reproduction/manuscript/build/main.log. The recomputed BBL and full extracted PDF text match the reviewed originals exactly. All seven rendered replica PNG hashes match their reviewed-page PNGs exactly. PDF binary hashes differ; timestamp/document identifiers may differ, and no byte-identical PDF reproduction is asserted. The original reviewed PDF bytes, to which release checks bind, were not replaced. Evidence: source-package.zip, reproduction-result.json, dependency-check.json and content-checks.json under evidence/release/.

Both the final original and clean replica logs were inspected. There is no compilation failure, undefined reference/citation, undefined control sequence, overfull or underfull box warning, or remaining rerun warning. Exactly two optional-field diagnostics remain: acmart says no affiliation city was supplied, and BibTeX says the PMLR entry has no address. The sole authorized author/affiliation/email are correct; no city was invented. The official PMLR bibliographic record does not require a publisher address. These warnings affect neither content nor layout and do not make the build fail.

All three local ACM files are byte-identical to the designated official distribution, with matching hashes recorded separately. The current official STOC 2027 CFP was checked at https://acm-stoc.org/stoc2027/stoc2027-cfp.html: the title page names the author and affiliation; the layout is nonanonymous, single-column, 11pt, single-spaced, Letter, with one-inch body margins. The CFP's submission rules are distinct from camera-ready sigconf rules. Substantial AI use is disclosed. Format compliance does not establish venue quality; the actual working_paper assessment is preserved unchanged. No submission, upload, email or contact occurred.

Before the reproduction command, the PDF skill's artifact-operation marker ran successfully once in this release context with create/count=1/pdf. All generated replica pages are visually identical to pages actually opened and inspected. No new scientific text or frozen evidence was edited.
'''
(P/'audit/build.md').write_text(build_report)
dump(P/'audit/build.json',{**common,'verdict':'accept','report':'audit/build.md','build_log':log,'build_log_digest':h(log),'clean_build':True,'reproduction_build_log':'evidence/release/reproduction/manuscript/build/main.log','reproduction_build_log_digest':h('evidence/release/reproduction/manuscript/build/main.log'),'reproduction_result':'evidence/release/reproduction-result.json','source_package':'evidence/release/source-package.zip','source_package_digest':h(E/'source-package.zip'),'warnings':['Optional acmart affiliation city absent','Optional BibTeX publisher address absent in BDJW24']})
observations=[
'Title wraps cleanly over two lines; sole author and UCSI affiliation are legible; the full abstract is contained; contact line and folio do not overlap. Title-page whitespace follows the requested separate title page.',
'Original-scope theorem, expectation display and context/attribution paragraphs are legible; citation numbers, square-root log expression and linked theorem/section numbers resolve; margins and folio are intact.',
'Transfer lemma and equations (1)-(5), interval definitions and star inequalities fit; subscripts, summation limits, strict inequalities and right-aligned numbers are distinguishable. The proof continues cleanly on the next page.',
'Continuation of interval integration and repair lemma/proof are fully readable; equation (6), geometric sums and proof-end squares are contained. The bottom line and folio remain separated.',
'Rational parameter display (7), observable qualification (8), four algorithm steps and concentration display (9) fit without clipping; long mathematical set notation remains within margins.',
'Expectation bounds (10)-(11), infinite series, explicit C_p and strict-metric boundary explanation are readable. Superscripts, indicator notation and fraction denominators are clear; no overlap at the section transition.',
'Computation counts, limitations and substantial-AI disclosure are legible. Both references have resolved author/title/date/location and intact DOI/URL text. No placeholder glyphs, clipped links or overlap; the last folio is correct.'
]
visual_report='# Fresh every-page visual audit\n\n'+header+'''Verdict: accept. I rendered the exact frozen seven-page PDF with Poppler pdftoppm at 125 dpi and actually opened and inspected each PNG using the image-view tool. Text extraction was an additional check, not a substitute for looking at the pages. There are no figures, tables or charts requiring data comparison.

| Page | Direct visual observation |
|---|---|
'''
for i,o in enumerate(observations,1):visual_report+=f'| {i} | {o} |\n'
visual_report+='''
Every reviewed page has adequate contrast and consistent typography. No clipping, overlaps, missing glyphs or illegible equations/references were found. Headers/footers and numbered equations have no collisions. Seven total pages satisfy the user cap, and the explicit title page is deliberate. Fonts are embedded. The paper names exactly the authorized sole author and discloses substantial AI assistance.

Reviewed images: evidence/release/rendered/page-1.png through page-7.png. The clean ZIP reproduction was also rendered at the same resolution; all seven PNG SHA-256 hashes are identical to these inspected images, as recorded in evidence/release/reproduction-result.json. This verifies its identical visual appearance without pretending the generated PDF bytes are identical. The audit binds only to the original reviewed PDF digest. No source, manuscript, PDF or prior assessment was changed. The readiness classification remains working_paper.
'''
(P/'audit/visual.md').write_text(visual_report)
dump(P/'audit/visual.json',{**common,'verdict':'accept','report':'audit/visual.md','pages_reviewed':list(range(1,8)),'render_method':'Poppler pdftoppm -r 125 -png; direct image inspection of every page','page_images':[{'page':i,'path':f'evidence/release/rendered/page-{i}.png','sha256':h(E/f'rendered/page-{i}.png')} for i in range(1,8)],'page_observations':observations})
print('Three fresh reports/audits and fixed-list citation verification saved. All required digest bindings use the current frozen snapshots.')
