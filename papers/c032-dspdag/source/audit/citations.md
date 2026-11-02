Job: `c032-dspdag-release-5fe4e38b60c7`. Reviewed 2026-11-02T12:51:51.063385+00:00. Research snapshot: `df4def35c3d991745cbd37b3e8238b49c3edeedc07c6350a8a195b3092c3ad02`. Manuscript snapshot: `c2916fd05375010d302349b16227c74c3b9034412b631d619036c3087052fe3f`. PDF: `04e5cdc5235be2a9327b7f80616afcc3d5854ecbab67d4f9fe5c12c23aca20f2`. This is a local internal artifact audit, not external peer review or a venue decision.

# Verification report

Mode: Search plus primary-text and frozen-proof review. Advisory `$citation-check-skill` explicitly used. The user's bounded autonomous release instruction overrides its interactive extraction-confirmation pause. Extraction was saved before verification in evidence/release/citation-claims.md; no claim was added during verification. No Excel or other user-authoritative bibliography was designated; literature/user_bibliography_check.md was inspected. No irrelevant citation was inserted.

24 extracted claim groups covered; 9 cited records; 0 missing keys, 0 uncited records, 0 contradicted attributions, 0 unsupported strengthenings found. One edition-access limitation is disclosed below. New algorithmic propositions are checked for fidelity to the frozen accepted proof; this release review does not fabricate a new mathematical acceptance.

## Sequential fixed-claim verification

| Claim | Result and exact supporting scope |
|---|---|
| C01 | Faithful to claim.json and frozen proof Theorems/model; Theorem 1.1 preserves every fixed k>=3, original positive-weight DAG model and elementary new-operand arithmetic. |
| C02 | Frozen proof opening and Section 1 state the same O_k(m+n) original-weight operations and B-bit qualification. No arbitrary precision is free. |
| C03 | AVW full v2 Section 7, printed p.41, Open Problem 3 asks exactly this existential fixed-k improvement. k=3 and delta=7/10 are the accepted positive consequence. |
| C04 | AVW v2 printed p.2 gives O(m n^(k-1)); its Theorem 2 is two-pair detection. No three-pair result is attributed there. |
| C05 | Frozen proof Sections 2-4 defines N^k states and charges explicit transitions. This is an internal algorithm fact, not a new external attribution. |
| C06 | Eppstein original TR 95-52, abstract and Sections 2-4, Lemma 2/Theorem 2, supports the tuple representation, terminal handling and O(m n^(d-1)+K) enumeration scope. This is enumeration by combined path length, not individually shortest prescribed paths. |
| C07 | Original FGLZ author PDF printed p.3, Section 2.1 equations (1)-(2), explicitly gives distinct tuples and moving the minimum coordinate, credited to Perl-Shiloach. Its other optimization results are not attributed to arbitrary prescribed pairs. |
| C08 | BK original Proposition 10, printed 13:9, filters label-specific shortest-path edges and constructs a tuple graph. The manuscript does not call the batching bound prior work. |
| C09 | Valiant original January 1974 report introduction and closure construction reduce recognition/chronological closure to Boolean matrix multiplication. Official publisher search metadata verifies the 1975 JCSS record. Exact typeset 1975 text was inaccessible; the inspected report supports the limited attribution. |
| C10 | LGU v2 Section 2.2 defines field-polynomial degenerations and border-rank exponent; Table 3, aspect 2, gives exactly 3.251640. WXXZ v2 Table 1, aspect 2, gives 3.250385. The manuscript only calls the latter stronger, and claims no current multiplication record. |
| C11 | CKS full v2 Theorem 1.1, printed p.1, gives O(mn log n) detection for two pairs, with no negative/zero cycles. The manuscript says more general digraphs and does not claim all unrestricted weighted digraphs. |
| C12 | Frozen proof Section 1 contains the tight-edge equivalence and all three terminal conventions. The manuscript retains original shortestness and O_k(1) new vertices; no restriction was introduced. |
| C13 | Frozen proof Sections 2-3 establishes the abandoned-vertex invariant, incoming recurrence and chronological induction. Manuscript Lemma 3.1 and recurrence match them. |
| C14 | Frozen proof Section 3 supplies the k classes and beyond-current-interval targets; Section 4 supplies exact labelled-context contraction. Manuscript retains masking and final-source dependencies. |
| C15 | Frozen proof Section 4 matches Theorem 4.1's dyadic sum, repeated packing charge, and primitive-workspace addition. No stronger workspace bound is asserted. |
| C16 | Strassen original printed pp.354-355, seven displayed products and Facts 1-2, supports exponent log_2 7. The paper's own bounded-intermediate derivation matches frozen proof Section 5; positivity is used, not parity. |
| C17 | LGU dependency as in C10; the exact rational interpolation/permutation lemma is proved in the manuscript and frozen proof Section 6. Explicit first/third variable reindexing repairs the frozen prose's permutation description without changing rank or theorem. |
| C18 | Frozen proof Section 6 gives fixed rational constants, deterministic prime specialization, recurrence, bounded residues and exact thresholding. The manuscript retains all qualifications and does not claim implemented coefficients. |
| C19 | Frozen proof Section 6 supplies column blocking and the same logarithmic absorption to exponent k+0.3. |
| C20 | Frozen proof opening and Sections 6-7 cover label-specific common-order graphs, ordinary prescribed DAG paths and detection only. The manuscript makes the same limitations. |
| C21 | Frozen validation.json records full_state_set_equalities=145, including k=2,3,4,5. It explicitly says the fast tensor routine was not implemented. |
| C22 | Actual referee verification.json records 4,718=3,072+1,536+110 reached-set comparisons. This is finite evidence, not an asymptotic proof or fresh release rerun. |
| C23 | Same referee file gives 120 cases per convention and 360 comparisons; independent_verify.py includes 181-bit weights and endpoint fixtures. Counts and all-pass descriptions match. |
| C24 | All nine records checked against the primary records/texts below. WXXZ is explicitly the November 2023 v2 arXiv record despite internal key WXXZ24; no erroneous 2024 publication year is rendered. Val75 has only the edition-access qualification below. |

## Primary records and versions

- AVW24: [official ICALP record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.9), authors Shyan Akmal, Virginia Vassilevska Williams, Nicole Wein; ICALP 2024, LIPIcs 297, 9:1-9:17. Original question checked in local full arXiv:2404.15916v2, not assumed to occur on a proceedings page.
- BK17: [official ESA record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2017.13), Kristof Berczi and Yusuke Kobayashi; 2017, volume 87, 13:1-13:13. Original full text inspected locally.
- Epp95: [author report](https://www.ics.uci.edu/~eppstein/pubs/Epp-TR-95-52.pdf), David Eppstein, University of California Irvine, TR 95-52, 15 December 1995. Original text inspected, copied to evidence/release/primary.
- FGLZ07: [official Springer chapter](https://link.springer.com/chapter/10.1007/978-3-540-72870-2_13), Rudolf Fleischer, Qi Ge, Jian Li, Hong Zhu; AAIM 2007, LNCS 4508, 134-143. Author-hosted original text copied from the supplied primary cache and inspected; web re-open failed but official metadata succeeded.
- Val75: [official publisher record](https://www.sciencedirect.com/science/article/pii/S0022000075800468), Leslie G. Valiant, JCSS 10(2), 308-315, April 1975, DOI 10.1016/S0022-0000(75)80046-8. Official indexed metadata was accessible through search, direct page returned 403. The original 1974 CMU report is the inspected proof text. Exact 1975 typeset edition not refreshed.
- LGU18: [author-deposited v2](https://arxiv.org/abs/1708.05622v2), Francois Le Gall and Florent Urrutia, revised 6 November 2017; journal-reference metadata confirms SODA 2018, 1029-1046, DOI 10.1137/1.9781611975031.67. SIAM timed out; original v2 text was available locally and inspected.
- WXXZ24: [v2 record](https://arxiv.org/abs/2307.07970v2), Virginia Vassilevska Williams, Yinzhan Xu, Zixuan Xu, Renfei Zhou; 4 November 2023. Bibliography deliberately cites this 2023 version. Table 1 inspected locally.
- CKS26: [official ITCS record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.39), Keerti Choudhary, Amit Kumar, Lakshay Saggi; LIPIcs 362, 39:1-39:23, 23 January 2026. Theorem checked in original full v2.
- Str69: [official Springer metadata](https://link.springer.com/article/10.1007/BF02165411) confirms Volker Strassen, Numerische Mathematik 13, 354-356, August 1969. [Original scan](https://courses.grainger.illinois.edu/cs357/su2013/Honors/Strassen.pdf) was opened and seven-product identities inspected.

All applicable academic citation query templates were run, with search date 2026-11-02 UTC; queries/results are in web-search.json, primary retrievals in web-primary.txt and primary-details.txt. Bounded novelty refresh is in novelty-refresh.txt. No equivalent full theorem was found in these inspected sources; this is not a priority certificate. Existing fresh innovation/STOC judgments are preserved, including working_paper.

## Complete source scope and limitations

All seven sorted publication.json source_files were inspected: main.tex, references.bib, generated main.bbl, official acmart.cls, official ACM BST, build.py and README.md. The four copied TeX inputs and generated bibliography account for every authored build dependency; there are no figures, imported local subfiles or external data dependencies. Standard installed TeX packages are system dependencies. Official class/BST bytes match the designated distribution. All nine keys resolve, and the extracted and rendered bibliography agrees with the source. No citations are recommended for removal.

Verdict: accept_with_citation_limitations. The sole unresolved issue is refreshing the exact 1975 typeset Valiant edition; primary report text supports the actual claim, and metadata is supported by the official publisher record. There is no contradicted or unsupported attribution. Endpoint failures are access events, not evidence that a reference does not exist. No access limitation suppressed the PDF or local release.
