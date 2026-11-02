# c021 simulated STOC-PC review (2026-11-02, ~16:10) and fixes applied (~16:45)

Verdict: weak reject (borderline; "solid accept at ICALP-B or LICS"). No false statement found.
Checked line by line by the reviewer: Prop. compression + Cor. onestate, Lemma abext, (1)=>(3), (3)=>(2),
Thm polyamb, Lemma finite, Prop. layer, Lemma torus-type cycle argument, Prop/Thm affinecontext, Cor reversal,
Prop. interact.

Gaps found and fixed (both builds):
- Thm onereset (sufficiency): on a residue class, exponential polynomials whose bases differ by a root of unity
  coincide, so the identification with K[Gamma] needs torsion-free base groups. Fixed: p' is now a multiple of the
  torsion order of Gamma (eigenvalues of M_a + characteristic roots of q), and everything is read as exponential
  polynomials in m (n = s + p'm) with bases in the torsion-free groups Gamma_0 and Gamma^{p'}.
- Lemma atest: the semisimplicity test always succeeds (H reductive, M_d = Q^d (x) Q^d* semisimple in char 0);
  now stated explicitly, condition kept because the central idempotents are needed.

Presentation/attribution fixes (both builds):
- Title: "Exact Characterization for Invertible Series, ..." (was "Exact Characterization, ...").
- Abstract: the two resolved MPS conjectures stated up front; polynomial-ambiguity result attributed as an
  intrinsic form of Puch–Smertnig; "A characterization for arbitrary singular series remains open."
- New Corollary cor:reversible: invertible CCRA series = series of reversible CCRA (permutation control +
  bijective updates). Proof: a copyless polynomial bijection is an affine coordinate permutation (disjoint
  supports + no constant coordinate), so the linearization is invertible and so is its minimal subquotient;
  converse by Thm main (2). (Claude's proof, checked.)
- "Why this matters" (acmart) / new paragraph after "Scope and significance" (article): concrete stakes
  (reversal vs. polynomial ambiguity, subclass-membership line of work, MPS's pessimism vs. Remark localcond).
- Techniques: one sentence on why compression has no pumping counterpart.
- Related work: BS23 (LICS'23), JMP24 (LICS'24), WS91 (TCS'91), KMOWW13 (LMCS'13), HOPW18 (LICS'18),
  CMMR21 (LMCS'21; reviewer had the authors wrong), DRT16 (LICS'16) — all verified on Crossref.
  Not added (unverifiable on Crossref): Babai–Beals–Cai–Ivanyos–Luks SODA'96, Mazowiecki–Riveros CSL'15.
- Cor. local moved from the open-problems section to the start of the singular section (used there).
- Sec. polytime: roadmap of the deterministic polynomial-time proof added.
- Sanity-check paragraphs shortened (acmart main; singular "Exact checks" in both).
Not done: notation clean-up (e, N, L reuse); verbatim quote of MPS's uniform pumping definition (MPS PDF not
available locally); demoting Thm polyamb to a corollary.

## Second full re-review (v3.4 integrated, both builds; 2026-11-02 ~19:30) and fixes (v3.5)
Verdict: WEAK ACCEPT (6/10). No mathematical error in cor:reversible, the onereset coset argument, or the
atest remark. Fixes applied to both builds:
- cor:reversible lead-in no longer overclaims ("the invertible CCRA series are exactly the series of reversible
  CCRA"); proof says it uses Section 2 notation; "alpha != 0 since nonconstant"; notes it proves the last
  sentence of Thm main. acmart motivation sentence reworded likewise.
- onereset: "characteristic roots" defined (nonzero coefficients for large n); "for all large n"; Gamma now
  includes the characteristic roots of b/a.
- atest remark expanded into the three explicit steps (Q -> Qbar complete reducibility; R_u(H) = 1 via the
  Lemma radical argument; reductive + averaging over H/H° => V (x) V* completely reducible).
- Roadmap no longer cites Lemma apriori; singular-section overview and Organization mention cor:local; article
  Organization no longer says the open-problems appendix contains the local condition.
- Transposition claim now attributed to non-closure under reversal (Remark localcond).
- Abstracts no longer state non-closure twice; article abstract "Such a series is CCRA-computable"; article
  l.105 "If f is CCRA-computable and a word e satisfies ...".
- Dependency sentence: Thm main uses only Secs 2–6 (acmart) / Secs 2–5 + App. sectors (article); decidability,
  quasi-unipotent polytime and Monte Carlo do not need ssec:detpoly.
- Ported to acmart from the article: pumping-condition credit to MPS (Example 26), explicit witness
  UV−VU = −2E_13 for Example positive (iii) (re-verified by hand), "routine modifications" for other fields of
  characteristic zero; removed the STATUS_claude comment from references.bib.
Left for the human authors: the author list (acmart: 1 author; article: 5 authors) and the AI statements
(acmart: "substantial AI-generated content"; article: "the authors verified the correctness and originality of
all content") must be made identical and true.
