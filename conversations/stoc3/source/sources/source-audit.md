# Reference and source audit

Checked 2026-10-31 without loading any skill. Primary publisher records, author-hosted PDFs, and official compiler documentation were used. Crossref metadata fetched from the publisher DOI records are archived as `*-metadata.json` and consolidated in `../qa/reference-metadata.json`.

| Key | Verified record and scope |
|---|---|
| AC93 | Amadio and Cardelli, TOPLAS 15(4), 575–631 (1993), DOI 10.1145/155183.155231. Historical exponential decision procedure; not mislabeled a quadratic algorithm. |
| KPS93 / KPS95 | POPL 1993, 419–428, DOI 10.1145/158511.158700; journal MSCS 5(1), 113–125 (1995), DOI 10.1017/S0960129500000657. Author-hosted `kps.pdf` checked for the polarity product and graph-representation size bound. The publisher's 2009 online date is not the paper's publication year. |
| PZ01 | Palsberg and Zhao, Information and Computation 171(2), 364–387 (2001), DOI 10.1006/inco.2001.3090. Equality/matching modulo associative/commutative products; not the same subtype problem. |
| GLP02 | Gapeyev, Levin, Pierce, JFP 12(6), 511–548 (2002), DOI 10.1017/S0956796802004318. Distinguish this journal paper from ICFP 2000. |
| HK71 | Cornell TR 71-114, Hopcroft and Karp (1971), official Cornell repository. Deterministic automata equivalence by equivalence closure; the paper supplies its regular-tree adaptation proof. |
| PT87 | Paige and Tarjan, SICOMP 16(6), 973–989 (1987), DOI 10.1137/0216062. Partition refinement; our executable uses simpler Moore refinement and does not claim this runtime. |
| OW18 | Oliveira Oliveira and Wehar, DLT 2018, LNCS 11088, 282–290, DOI 10.1007/978-3-319-98654-8_23. Publisher Crossref metadata verified. Used as context, not as an unexamined two-DFA OV theorem. |
| OW20 | Same authors, DLT 2020, LNCS 12086, 69–82, DOI 10.1007/978-3-030-48516-0_6. PDF mirrored at https://perso.ens-lyon.fr/denis.kuperberg/CR18/fine.pdf archived and first-page metadata checked. Crossref API returned HTTP 429 for this item; direct primary PDF supplies the record. Its stronger simulation/circuit implications are not misattributed to OVH. |
| Williams05 | TCS 348(2–3), 357–365 (2005), DOI 10.1016/j.tcs.2005.09.023. Context for vector/SAT connection; exact OVH definition is given independently in the paper. |
| IP01 | Impagliazzo and Paturi, JCSS 62(2), 367–375 (2001), DOI 10.1006/jcss.2000.1727. ETH source. |
| FCB08 | Frisch, Castagna, Benzaken, JACM 55(4), Article 19 (2008), DOI 10.1145/1391289.1391293. Final publisher metadata give title “Semantic subtyping” and 64 pages. The author manuscript has an extended title and 67 pages; bibliography uses the final metadata, not mixed versions. |
| QuickSub25 | Zhou and Oliveira, PACMPL 9(POPL), Article 33, 954–985 (2025), DOI 10.1145/3704869. Binder-sensitive bound concerns iso-recursive Amber subtyping, not equi-recursive shared graphs. |
| TS46 | Official TypeScript 4.6 release notes: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-6.html . Documentation of structural-recursion heuristics. No headline compiler speedup imported into our experimental results. |
| TS57915 | Primary issue https://github.com/microsoft/TypeScript/issues/57915 (CJ Quines, 2024). Its conditional/generic tuple language is outside our extractor; used only as motivation. |
| DT | Primary repository pinned to 72e15dbdd8088284d3f0387a05539e7c2e6c743b. Reproducibility command and file/content digest archived; no attribution of artificial adjacent-root queries to tsc. |

A bounded search for prior fine-grained subtype lower bounds found the automata context above and recent recursive-subtyping work. This is not an exhaustive novelty certification. The manuscript explicitly attributes its equality and minimization ingredients to classical methods.

## Revision 2: 2025 automata antecedent

DDFMW25: Karolina Drabik, Anita Dürr, Fabian Frei, Filip Mazowiecki, Karol Węgrzycki, arXiv:2501.14725v3 (21 July 2025), DOI 10.48550/arXiv.2501.14725. Primary PDF archived as Drabik2025v3.pdf. Checked Lemma 6.4, Claims 6.1–6.2, and their Appendix B encodings. Vector selection and coordinate checks proceed through finite layers; bit gadgets have finite depth. The availability of acyclic partial automata is an inference from these constructions, explicitly acknowledged in the revised text. The January v1 uses different numbering (Theorem C.9); the citation is pinned to v3 to match Lemma 6.4. This antecedent narrows the paper's claim to a type-semantic transfer.

Official STOC 2027 CFP was rechecked on 2026-10-31. The revised artifact follows the review submission format rather than the camera-ready sigconf specification.
