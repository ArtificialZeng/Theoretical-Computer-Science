# Citation-check-skill pass 1: fixed extraction

Extraction only; verification is a separate pass. The user authorized this autonomous release audit, so no confirmation pause is added.

[C01] | A nontrivial binary upcycle exists with n=12,d=3,L=512; it answers Question 9.2 affirmatively. | Existence | Abstract; Theorem 1; sections 1,4
[C02] | The 512 windows partition all 4096 binary 12-words into sets of eight completions. | Statistic + Existence | Abstract; proof
[C03] | 128 octal digits specify the complete cycle. | Statistic | Abstract; section 2
[C04] | The window length 12 does not divide cycle length 512. | Existence | Abstract; section 4
[C05] | Chen, Kitaev, Mütze and Sun introduced universal partial words and cyclic versions. | Attribution | Section 1 paragraph 1; CKMS17
[C06] | Fillmore et al. Theorem 3.1 gives binary n=8,d=1 examples. | Attribution | Section 1; FGKMM26
[C07] | Fillmore et al. Question 9.2 asks whether upcycles with d>1 exist. | Attribution | Abstract; sections 1,4; FGKMM26
[C08] | Theorem 5.1 and Corollary 5.2 multiply alphabet size while preserving n,d. | Attribution | Section 1; FGKMM26
[C09] | Corollary 8.14 requires d=n/4 for nontrivial period-four frames. | Attribution | Section 1; FGKMM26
[C10] | Carey et al. Definition 8.2 permits several cyclic words in a universal partial quasi-family. | Attribution | Section 1; CKKP25
[C11] | The four displayed rows have 128 octal digits and decode to the accepted word. | Statistic + Existence | Section 2 displayed object
[C12] | Digits 0,1,7 decode to wildcard000, wildcard001, wildcard111. | Existence | Section 2
[C13] | Completion sets are disjoint iff ordinary unequal symbols occur at a common offset. | Existence | Lemma 2 and proof
[C14] | The cycle has 512 positions with wildcards precisely at indices zero modulo four, also cyclically. | Statistic + Existence | Proof of Theorem 1
[C15] | Every window has three wildcards and nine ordinary symbols, with no repeated physical position. | Statistic + Existence | Proof of Theorem 1
[C16] | Each completion set has exactly eight members. | Statistic | Proof of Theorem 1
[C17] | All 130816 pairs have an ordinary conflict; every test succeeds. | Statistic + Existence | Equation 1; proof; listing
[C18] | Pairwise disjoint completion sets have union cardinality 512*8=4096=2^12. | Statistic | Proof of Theorem 1
[C19] | The direct loop checks all 4096 total words at all 512 starts without sampling. | Statistic | End of section 2; section 3; listing
[C20] | Eleven starts 501 through 511 wrap around and are included. | Statistic | Section 3
[C21] | The program performs 2097152 compatibility tests and prints the stated counts. | Statistic | Section 3
[C22] | The direct check counts starting indices, with shared characters read from one decoded word and exact integer counts. | Existence | Section 3
[C23] | FGKMM26 raises n not dividing cycle length immediately after Question 9.2. | Attribution | Section 4
[C24] | FGKMM26 has authors Fillmore, Goeckner, Kirsch, Martin, McGinnis; DCC 94 article152 (2026), DOI10.1007/s10623-026-01841-x. | Attribution + Temporal | Bibliography
[C25] | CKKP25 has authors Carey, Kearney, Kirsch, Popescu; DCC93 pp2803-2822 (2025), DOI10.1007/s10623-025-01609-9. | Attribution + Temporal | Bibliography
[C26] | CKMS17 has authors Chen, Kitaev, Mütze, Sun; DMTCS19(1) paper16 (2017), DOI10.23638/DMTCS-19-1-16. | Attribution + Temporal | Bibliography
