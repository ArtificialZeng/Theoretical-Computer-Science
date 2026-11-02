# Independent referee of ssec:detpoly and ssec:polyamb (2 Nov 2026, ~14:00; saved by the main session)

Verdict: no error that invalidates a claim. Theorem thm:detpoly (polynomial heights, hence deterministic
polynomial time) and Theorem thm:polyamb / Corollary cor:polyamb are correct as written. The referee
re-verified Lemma sizes and checked that its tame calculus transfers to Lemma iter (fixed linear maps folded
into delta, O(m) dependency depth, graded bound), Lemma torus (cocycle, fundamental cycles, bound
2d^2+2d), Lemma v0 (torus conjugacy only inside S x U_P, transfer via regularity), Lemma xhat, Lemma Upp
(sizes via Psi, Lemma finite(2) in dimension <= d^2), Prop. ugen and the proof of the theorem (conjugations
undone before projecting), and the polynomial-ambiguity section line by line.

Fixes applied to both builds (manuscript_v3_claude and READY_claude/c021_submission_v3_claude):
B1 weight basis: C computed in Lemma atest equals Q[H°] under (a). B2 size bookkeeping in Lemma iter made
explicit. B3 group element renamed upsilon in Lemma v0. B4 size of log xhat_a; ad(Y') over a basis. B5 block
form step mentioned in Cor. polyamb. B6 PS24 attribution corrected after checking PS24 (Thm 1.3, Prop. 9.4
give a block-triangular monomial form; only their sufficiency direction uses unit equations) - remark
rewritten and "structurally" -> "intrinsically, in terms of G_f°" in related work. C1 "condition (3) of
Theorem main" / "(C3)". C2 "conjectured" removed. C3 Theorem polytime(2) now points to Theorem detpoly.
C4 Remark polytime(i) cites Lemma Upp too. C5 Theorem decision sentence clarified. C6 duplicate
"superseded" removed. D1 m -> r, pi_j -> varpi_j in sec_polyamb. D3, D4, D5 applied.
