# Verification report

**Mode:** Search, with separate fixed extraction and verification passes.
**Document:** the complete frozen manuscript, all publication source dependencies, and the seven-page canonical PDF.
**Method:** explicitly invoked $citation-check-skill, advisory; primary-source/manual checks supplement its claim extraction. The user's bounded autonomous-job instruction overrides the skill's extraction-confirmation pause.

Job: `c002-coverage-release-c84ac066553a`. Reviewed: 2026-10-31T22:05:01.069857+00:00.

Research snapshot: `26d2a64f317984b35b49212bdc46529ccb7f19bc1be1b5e471d28d308d18456e`.
Manuscript snapshot: `cbd9e040f4147d3e60fc3daafd59dcd1d2dfe965798be52063afe7345dcd085f`.
PDF: `b2dac13ca628fb6c3b7495516ee0acbdd390a90b0942127ada2935401ba873db`.

**Verdict: accept_with_citation_limitations.** All 31 fixed extracted assertions have the support stated below; no contradicted attribution, unsupported strengthening, undefined key, empirical numerical mismatch or unqualified worldwide-priority claim was found. The original DS03 full text was not obtained. Its bibliographic record and abstract are verified at Cambridge, and GRW11 explicitly supplies and credits the exact theorem used. This is a disclosed original-text-access limit, not an unsupported theorem dependency. The manuscript already says that its exact rational formulation is taken from GRW11 and supplies a complete proof. No prose or bibliography edit is needed.

| Metric | Count |
|---|---:|
| Fixed assertions checked in sequential order | 31 |
| Supported within the evidence basis below | 31 |
| Numerical errors / contradicted attributions / unsupported claims | 0 |
| Citation keys and bibliography entries | 5 |
| Original cited full texts not directly inspected | 1 |

Extraction is frozen in `audit/citation-extraction.md`. The extraction uses informal theorem/lemma numbering; the locations below give actual rendered numbering. New mathematical assertions are checked for fidelity to the accepted packet and the manuscript's complete proof; this release review does not manufacture a second mathematical acceptance or treat an external-source search as proof of those assertions.

## Sequential claim-to-evidence check

| ID | Check and precise support | Assessment |
|---|---|---|
| C01 | Theorem 1.1 and Section 5 retain every original quantifier, tagged multiplicity and the exact 4kt(kt-1)^2 bound in claim.json and research/proof.md. | Supported; exact |
| C02 | Section 6 retains the accepted explicit-input, binary-parameter algorithm and its bit-length argument. | Supported; exact scope |
| C03 | ARW26 Theorem 3, p.139:4, gives the stated randomized constructive bound; the square-root covers t^3 k and the logarithm is outside it. | Verified; exact formula |
| C04 | ARW26 Section 1.3, p.139:5, discusses the logarithmic loss and avoiding union bounds. | Verified; paraphrase |
| C05 | Expanding 4kt(kt-1)^2 gives O(t^3 k^3); the paper expressly makes no all-parameter pointwise improvement claim. | Supported; mathematical comparison |
| C06 | ARW26 Section 1.1 and Definition 4 support the stated convention and the separately disclosed union-notation ambiguity. | Verified; explicit qualification |
| C07 | ARW26 Section 5 and Lemma 23, pp.139:12–13, already use independent classes and restricted linear expectations. | Verified; paraphrase |
| C08 | GRW11 Theorem 2, p.58, expressly credits Doerr–Srivastav; DS03 publisher metadata/abstract agree on the multicolour topic. Original DS03 theorem text was not read. | Verified attribution via GRW11; direct-origin text limitation |
| C09 | Both cited arXiv abstracts and local full texts concern non-additive discrepancy. | Verified; paraphrase |
| C10 | HMMS25 Definition 13 and Question 14, p.10, count relevant functions and ask about general 1-Lipschitz functions. | Verified; scope comparison |
| C11 | GRW11 Theorem 2 exactly gives rational equal-group error 2 times the maximum absolute column sum and polynomial time; manuscript Lemma 2.1 proves its real-data extension. | Verified theorem; self-contained extension |
| C12 | Lemma 2.1 proof: fractional groups contain at least two fractional coordinates; heavy-row mass counting leaves fewer than V/2 rows. | Supported; accepted proof fidelity |
| C13 | Lemma 2.1 charges each row only at its single deletion; later coordinates lie in [0,1]. | Supported; accepted proof fidelity |
| C14 | Lemma 3.1 proves Hall's inequality for arbitrary subsets of demand copies, counting tagged occurrences. | Supported; accepted proof fidelity |
| C15 | Section 3's cyclic states keep each full witness rainbow in every state. | Supported; exact categorical statement |
| C16 | Lemma 3.2 counts at most q(q-2) neighbors and handles q=2 explicitly. | Supported; exact arithmetic |
| C17 | Equation (6) follows from global cyclic color symmetry of the uniform product law. | Supported; accepted proof fidelity |
| C18 | Equation (7) is an exact hit/miss decomposition using independence between blocks only. | Supported; accepted proof fidelity |
| C19 | Equations (8)–(9), Lemma 4.1, count item incidences in a block; no color/function factor is omitted relative to the accepted proof. | Supported; exact column bound |
| C20 | Equation (10) and Section 5 telescope consecutive values of the same Phi while recomputing matrices. | Supported; exact constants |
| C21 | Section 6's singleton-color case gives at most t; the bound is increasing in the degree bound. | Supported; exact boundary case |
| C22 | Section 6 caps demand copies/classes by n and reduces numerical parameters to explicit-input bounds. | Supported; accepted algorithm scope |
| C23 | Section 6's outside factors give denominator dividing k^n; targets have denominator dividing k^(n+1). | Supported; polynomial bit lengths |
| C24 | The LP-face implementation uses original row targets and fixed 0/1 coordinates, preserving polynomial constraint encoding. | Supported; accepted argument retained |
| C25 | ARW26 Section 1.3, p.139:5, supplies the same single-item lower-bound example; literal evaluation gives t. | Verified; exact |
| C26 | The theorem's hypotheses and explicit exclusions preserve the accepted boundary; priority language is bounded to inspected literature. | Supported; no strengthening |
| C27 | ARW26 publisher record and inline official BibTeX match all used fields and DOI. | Verified metadata |
| C28 | DF25 arXiv record and local v1 title page agree on authors/title/year/version. | Verified metadata |
| C29 | DS03 Cambridge record matches authors/title/CPC 12(4)/365–399/2003/DOI. | Verified metadata; full-text limit above |
| C30 | GRW11 publisher record, inline official BibTeX and primary PDF agree with the bibliography. | Verified metadata |
| C31 | HMMS25 live arXiv history identifies the cited v2 (29 September 2025); authors/title/year agree. | Verified metadata |

## Primary sources and current literature scope

Search date: 2026-10-31 UTC / 2026-11-01 Asia/Shanghai. All four applicable academic search templates per bibliography item were actually issued: author/year/title prefix, full-title arXiv/Semantic Scholar query, author/year/venue, and DOI or arXiv identifier. Only primary material supports the findings. Exact queries and primary hits are recorded in `evidence/release-searches.json`.

- [ARW26 official record and inline BibTeX](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.139), local `literature/publisher-source.pdf`/`.txt`: Theorem 3, Definition 4, Sections 1.1/1.3, Section 5 and Lemma 23. [Current arXiv history](https://arxiv.org/abs/2602.09948) remains v3, 1 July 2026. The manuscript correctly credits the prior class-rounding architecture and distinguishes its parameter tradeoff.
- [GRW11 official record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2011.55) and [original primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol013-fsttcs2011/LIPIcs.FSTTCS.2011.55/LIPIcs.FSTTCS.2011.55.pdf): Section 3, Theorem 2, p.58 and reference 5, p.65. The exact rational grouped theorem was read in this job.
- [DS03 Cambridge publisher page](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/multicolour-discrepancies/B3B9E2D4477711A2B29A197DCA886EDE): metadata and abstract read; full text unavailable in this bounded review. No exact DS03 theorem/page is invented. GRW11 is the direct formulation source.
- [HMMS25 current arXiv record](https://arxiv.org/abs/2509.09252), cited local v2 full text, Definition 13/Question 14/Theorem 15, p.10: supports the broader-context comparison, not the present coverage theorem. A later ITCS 2026 abstract publication exists; the explicitly versioned arXiv citation remains accurate.
- [DF25 current arXiv record](https://arxiv.org/abs/2509.16802) and local v1 full text, abstract/introduction: supports only the broad contextual attribution made here. No all-color occurrence-degree bound is attributed to it.

Four additional current equivalence queries (in the search record) found no equivalent coverage resolution in the material returned. This refresh and the accepted referee's comparison cannot certify worldwide priority. There is no unsupported novelty strengthening in the manuscript: known Hall matching, greedy graph coloring and grouped rounding are credited, while the claimed change is precisely the accepted compatible categorical reduction and all-size conclusion.

Separate Dagstuhl BibTeX endpoints returned cache misses; the official pages themselves expose complete inline BibTeX, which was checked successfully. This creates no metadata uncertainty. No Excel or authoritative user BibTeX table was designated; `literature/user_bibliography_check.md` was read. No workbook, bibliography-authority label or irrelevant reference was invented.

## Complete dependencies and resolved references

`evidence/release-verification.json` records a fresh comparison of TeX citation keys, BibTeX keys, generated bibitems, the recorder's project inputs and the source list. All five keys occur in all three places; none is undefined or unused. PDF page 7 and extracted text show all five resolved labels, authors, titles, years and identifiers. No citation is removable as irrelevant: three establish the closest coverage/rounding dependence and two accurately distinguish the broader setting.

The complete sorted dependency scope is:

- `manuscript/README.md`
- `manuscript/build.py`
- `manuscript/main.bbl`
- `manuscript/main.tex`
- `manuscript/references.bib`
- `manuscript/vendor/acmart.cls`
- `manuscript/vendor/alpha.bst`
- `manuscript/vendor/download-provenance.json`

The recorder loads only main.tex, main.bbl and the local unmodified acmart class, apart from generated aux/out and system TeX inputs. Source review also checks the bibliography, standard local alpha.bst, build script, README and provenance record. There are no figures, other TeX imports, external authored files or hidden project dependencies. The local class is byte-identical to the official user-supplied distribution. The source-list inclusion of build/support records is conservative and complete. No manuscript or PDF edit occurred; all frozen digests remain unchanged.
