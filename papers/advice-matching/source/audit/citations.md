# Fresh release citation and claim-support audit

Job: `advice-matching-release-01731cae3c13`. Search and inspection: 2026-10-30 UTC.
Verdict: **accept**. Advisory method: explicitly invoked `$citation-check-skill`,
two-pass extraction followed by fixed-claim verification, with direct primary
passage inspection. The autonomous bounded-job instruction supersedes the
skill's intermediate confirmation pause. Extraction is frozen separately in
`audit/citation-extraction.md`; verification below follows those IDs.

34 extracted claims checked: 13 external attribution/metadata checks and 21
checks of manuscript scope, proof transcription and finite evidence against
the accepted mathematical dossier. No contradicted attribution, unsupported
strengthening, undefined citation, numerical transcription error, or remaining
reference-access limitation was found. Internal mathematical checks below mean
consistency with the accepted proof and exact certificates; this release audit
is not a replacement mathematical acceptance or a priority certificate.

## Primary sources and nearby support

- **FM18**, [publisher metadata](https://link.springer.com/chapter/10.1007/978-3-319-98355-4_17): Josep Fàbrega and Xavier Muñoz, 2018, LNCS 11011, pp. 297–310, DOI 10.1007/978-3-319-98355-4_17. Inspected the original chapter in `literature/regular-randomized-adversary-book.pdf` and its text, printed pp. 300–302, Propositions 1–2. The displayed eight-cycle edge sets equal the manuscript pair after relabelling; the contraction/orientation argument computes a quarter of failed joins and a 7/8 matching. The chapter uses the reciprocal 8/7 competitive ratio. The manuscript expressly credits the baseline, gadget and method. Publisher subscription notice does not limit the available primary chapter text.
- **FLWZ25**, [versioned primary text](https://arxiv.org/html/2510.00965v1): full authors Yilong Feng, Haolong Li, Xiaowei Wu, Shengwei Zhou; title and 1 October 2025 version agree. Algorithm 2, lines 276–295 in the HTML rendering, weights available neighbors by revealed degree; the following paragraph identifies two-way semi-OCS at degree two and its limiting priority choice. The definition at lines 59–60 gives an offline minimum degree and online maximum degree. The manuscript credits only the relevant rule/cycle overlap, without transferring that minimum-degree theorem to paths.
- **CGLB24**, [arXiv v3](https://arxiv.org/html/2405.09784v3): Davin Choo, Themis Gouleakis, Chun Kai Ling, Arnab Bhattacharyya, 23 May 2024. Section 3, Theorem 3.1, displayed edge sets and the following extension (lines 158–175) support the Z obstruction and linear bound. Their broader advice domain is not silently equated to a matching table; the manuscript proves its table specialization directly. The arXiv author spelling Themis is used; the ICML publisher also lists the full name Themistoklis.
- **JM24**, [arXiv v3](https://arxiv.org/html/2206.11397v3): Billy Jin and Will Ma; version date 4 November 2024 supports the explicitly cited 2024 v3, despite the identifier's 2022 first deposit. Section 2, Definition 2.1 (lines 181–215) defines two batches and the advice-following/optimal-completion benchmark. Section 3.1 (lines 222–250), including Proposition 3.1, gives both endpoints, interpolation and the Z upper bound. The manuscript preserves the information/benchmark distinction.
- **BCH25**, [official record and BibTeX](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2025.13), [primary full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.13/LIPIcs.ISAAC.2025.13.html): Amey Bhangale, Arghya Chakraborty, Prahladh Harsha, ISAAC 2025, LIPIcs 359, 13:1–13:19, DOI 10.4230/LIPIcs.ISAAC.2025.13. Theorems 1–2 explicitly restrict online degree only and separate randomized integral from fractional matching; the fractional theorem is 0.75. No claim of a conflicting both-sides theorem is made.
- **LMP26**, [primary v1 text](https://arxiv.org/html/2609.15837): Alexander Lindermayr, Nicole Megow, Lauren Paul, 14 September 2026; title and identifier agree. Theorems 1–3 and Section 5 were inspected. Theorem 2 (lines 85–88) explicitly gives vertex-weighted online fractional matching with integral predictions; the singleton arrival setting retains fractional actions. This is the exact distinction stated in the manuscript, rather than a claim based merely on stage count.

Search templates were run for every record: first author/year/title words;
full title restricted to arXiv/Semantic Scholar; author/year/venue or arXiv;
each supplied DOI; and each supplied arXiv identifier. The official publisher
and original arXiv texts, rather than search snippets or secondary indexes,
support the decisions above. Additional bounded searches combined online
matching, advice/predictions, degree two, cycles, consistency/robustness and
7/4. No equivalent frontier was located in those inspected results. This is
not an exhaustive literature census; the manuscript makes no priority guarantee.

## Fixed extraction verification, in order

| ID | Status and evidence |
|---|---|
| C01 | Verified: Theorem 1 and abstract exactly match claim.json and accepted audit/math.md, including oblivious integral/full-table scope. |
| C02 | Verified: accepted endpoints and manuscript Lemmas 2 and 5. |
| C03 | Verified: manuscript decreasing-arrival argument matches the accepted perfect-advice proof, including partial maximum tables. |
| C04 | Verified: deterministic occupied-port counting, accepted arbitrary-advice cycle endpoint. |
| C05 | Verified, paraphrase: FM18 Propositions 1–2, printed pp. 300–302; ratio convention explicitly disclosed. |
| C06 | Verified, paraphrase: FLWZ25 Algorithm 2 and its following paragraph; only degree-two rule overlap claimed. |
| C07 | Verified, paraphrase: CGLB24 Theorem 3.1 and extension immediately after it. |
| C08 | Verified, paraphrase: JM24 Section 3.1 endpoints, interpolation and Proposition 3.1. |
| C09 | Verified, paraphrase: JM24 Section 2, Definition 2.1 and definition of ADVICE. |
| C10 | Verified, paraphrase: BCH25 Theorems 1–2 and their explicit online-degree hypotheses. |
| C11 | Verified, paraphrase: LMP26 Theorems 1–3, especially Theorem 2; actions remain fractional. |
| C12 | Verified: accepted exhausted-neighbor implementability argument and degree promise. |
| C13 | Verified: Lemma 2 matches the accepted augmenting-path proof; no extra oracle capability. |
| C14 | Verified: accepted root and initial-leaf invariant, reproduced in Section 3. |
| C15 | Verified: accepted deterministic transport/consumption invariant, with sources fixed by graph/order. |
| C16 | Verified: distinct source coin probabilities 1/4 and 1/2; manuscript does not condition on history. |
| C17 | Verified: all four count identities agree with accepted reconstruction. |
| C18 | Verified: path formula and rootless optimum match accepted report and fresh finite reproduction. |
| C19 | Verified: cycle formula and counts match accepted report and fresh finite reproduction. |
| C20 | Verified: both explicit referee arithmetic corrections appear correctly in Corollary 4. |
| C21 | Verified: accepted path/cycle inequalities and additivity under interleaving. |
| C22 | Verified: accepted maximality and occupied-port deterministic bounds. |
| C23 | Verified: all table entries and mixing algebra match accepted endpoints and theorem. |
| C24 | Verified: accepted Z coupling argument; fresh checker verifies all three early choices, including abstention. |
| C25 | Verified: accepted cycle pair; fresh checker verifies all nine prefixes and optimal continuations. |
| C26 | Verified: common table agrees literally; only (y1,3) is absent in G0, implementing the third referee correction. |
| C27 | Verified: fresh run audit/release-reproduce.json has ok=true, 265 graphs, 1590 orders, 2652 maximum-advice and 54060 arbitrary-advice cases, 3490 component orders through six vertices, 3552 orientations and all 12 gadget prefixes. These are finite checks. |
| C28 | Verified: both stated arguments use the last-appearance degree promise; extensions are posed as questions. |
| C29 | Verified: FM18 publisher metadata and chapter first page. |
| C30 | Verified: FLWZ25 versioned arXiv heading and authors. |
| C31 | Verified: CGLB24 versioned arXiv heading and authors. |
| C32 | Verified: JM24 versioned arXiv heading and authors; 2024 is v3's date. |
| C33 | Verified: BCH25 official embedded BibTeX and citation data. |
| C34 | Verified: LMP26 v1 heading and authors. |

## Bibliography and complete dependency scope

Read `literature/user_bibliography_check.md`: no user Excel workbook or
authoritative BibTeX list was supplied. Accordingly no workbook metadata basis
is invented and no irrelevant reference is inserted to satisfy a count.
All six included papers are genuinely relevant and accessible for these claims.

Reviewed every sorted `publication.json` source_files entry: the main/body TeX,
references.bib, generated main.bbl, official class and its upstream sources,
alpha.bst, build/reproduction scripts, provenance and handoff/readme files.
The recorder's local TeX inputs are acmart.cls, main.tex, body.tex and main.bbl;
regenerated auxiliary files and installed TeX packages are not authored inputs.
BibTeX's actual log names references.bib and alpha.bst, both declared. There
are no external authored imports, figures, dynamic source generators or hidden
project dependencies. Extra declared upstream/readme/reproduction files are
also bound. The portable source ZIP matches every current declared input and
contains no literature fulltexts; see audit/release-validation.json.

All six cited keys equal the six generated bibitems. The final TeX/BibTeX logs
have no undefined keys or cross-references. Extracted and rendered references
are resolved, use alpha hyperlinks and full author lists. No unnecessary
citation was found. The accepted scope is preserved throughout; old baselines,
gadgets, the priority rule and mixing receive explicit credit.
