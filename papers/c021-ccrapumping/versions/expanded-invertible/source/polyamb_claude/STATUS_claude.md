# STATUS (polyamb, Claude) — open problem 4 of c021 manuscript_v3

Started 09:27 Beijing time, 2 Nov 2026. Deadline 13:30.

## Bottom line
Open problem 4 is SETTLED POSITIVELY, and the converse also holds.

**Theorem (thm:polyamb).** For an invertible rational series f, the following are equivalent:
1. f is polynomially ambiguous (computed by some PA weighted automaton over Q);
2. G_f° is triangularizable over Q;
3. Γ_f has a finite-index subgroup that is triangularizable over Q.

**Corollary (cor:polyamb).**
- An invertible f is CCRA-computable iff f is PA and any two unipotent elements of G_f commute. Equivalently: iff f is PA and the unipotent radical of G_f° is commutative.
- Given a rational WFA, one can decide in deterministic polynomial time whether its series is invertible and PA. This follows from Thm decision and Lemma lem:atest, because condition (2) is exactly condition (a) of sec_polytime.

By-products:
- All eigenvalues of word matrices of invertible PA series are roots of rationals, and G_f°/R_u is a Q-split torus. So a non-split torus never occurs. This answers the side question in the task.
- If P is a trim PA automaton for f, then G_f° acts on each graded piece of the SCC-induced flag through a Q-split torus. R_u(G_f°) is exactly the kernel of that action.

## Proof idea
**(2)⇒(1).** Use the cocycle of Sec. normalform. In a rational triangularizing basis each c(g,a) is upper triangular. The automaton on F × {1..d} then has at most (n+2)^d accepting runs.

**(1)⇒(2).**
- Trim the PA automaton and order its SCCs. The column-invariant flag V_j induces a G_f-stable rational flag Φ_j of Q^d ≅ W/N. Each graded piece is an invertible subquotient X_j/Y_j of an SCC diagonal block.
- In an SCC, paths are unique (Lemma lem:uniquepath).
- Component lemma (lem:component), for a block with unique paths:
  - Take the support monoid and an idempotent E = B_e in its minimum ideal. E𝔅E is a finite group of order n.
  - Let L = {z : B_z = E}; it contains every (exe)^n. Let Θ be the set of fixed points of E.
  - χ(z) = ρ(z)|_{Θ×Θ} is diagonal and multiplicative on L, and ρ(zyz') = ρ(z) ι χ(y) ι^T ρ(z').
  - Hence σ|_L factors through a Q-morphism Ψ from the closure of χ(L), which is a Q-split diagonalizable group, onto the closure K of σ(L).
  - The power-map argument of Lemma lem:dense gives H° ⊆ K. So H° is a Q-split torus.
- The proof is self-contained. It does not use PS24 or unit equations.

## Files (all in this folder)
- `section_claude.tex`: drop-in subsection "Polynomial ambiguity in the invertible sector", written with the paper's macros. It contains the theorem, the corollary, a remark comparing with PS24, and full proofs.
- `build_claude/`: a COPY of manuscript_v3 with the subsection `\input` before Section Algorithms and open problem 4 deleted. Build: `latexmk -pdf main.tex` inside `build_claude/`. It compiles with no undefined references; output is `build_claude/build/main.pdf`. The original manuscript is untouched.
- `code_claude/polyamb_check_claude.py`: exact random checks; logs in `logs_claude/check_seed*.log`.
- `code_claude/nonsplit_example_claude.py`: illustrative verdicts; log in `logs_claude/nonsplit_example.log` (ALL OK).

## Exact checks (python3 -I, fractions + python-flint)
`code_claude/polyamb_check_claude.py SEED 40`: random trim PA automata generated as block-triangular automata whose SCC letters are weighted permutations, followed by 0–3 forward/backward state splittings. The splittings make letter matrices singular and SCC blocks non-monomial while keeping the series fixed. For each automaton, the script:
- checks PA by the EDA criterion on the square automaton;
- checks trimming and minimization by exact equality on all words up to length 4–5;
- checks invertibility of the minimal representation;
- runs the paper's independent condition-(a) test (Lemma lem:atest), which Theorem thm:polyamb predicts is always TRUE;
- checks the component lemma on every SCC block: E𝔅E is a group, facts (i) and (ii), χ is multiplicative, and eq:factor holds exactly.

Results, 2-letter alphabet (seeds 1 and 3):
- 80/80 PA automata had an invertible minimal representation of dimension 1–6, and (a) held in 80/80.
- 49 of them had singular letter matrices and 38 had non-monomial SCC blocks.
- All 143 component-lemma checks passed.
- 10 of the 80 are PA but not CCRA (R_u nonabelian).
- Control: random invertible 3x3 integer pairs fail (a) in 40/40.

Results, 3-letter alphabet (seeds 2 and 4):
- (a) held in 80/80.
- 60 had singular letters and 61 had non-monomial SCC blocks.
- All 165 component-lemma checks passed.
- 26 are PA but not CCRA.
- Control: (a) fails in 40/40.

TOTAL:
- 160/160 invertible PA examples satisfy (a), with 0 counterexample candidates.
- 308 component-lemma checks passed.
- 36 examples are PA but not CCRA.
- Control: 80/80 random invertible pairs fail (a).

`code_claude/nonsplit_example_claude.py`:
- The rotation (3+4i)/5 (non-split torus) is rejected, alone and together with diag(2,2), so it is not PA.
- diag(2,1), I+E12, I+E21 is rejected (all eigenvalues of the letters are rational, but G° = GL_2), so it is not PA.
- MPS Ex. 17 and Ex. heis are accepted, with R_u nonabelian: PA but not CCRA.
- A monomial example is accepted with R_u abelian.

## Referee
A fresh general-purpose subagent refereed `section_claude.tex` against main.tex and sec_polytime.tex.
- Verdict: **correct, with minor fixes; no fatal error, no gap**.
- It also checked the combinatorial core of the component lemma on 1606 random unambiguous supports, with exact arithmetic.
- It confirmed consistency with PS24 Thm 1.6(2) and Def. 2.4/9.1.
- Every minor point has been applied: subsemigroup closure line, normal-form constructions independent of (3), degenerate D=0, |w|≥1 and alignment in lem:uniquepath, notation (Φ_j, h_0), wording "unipotent radical of G_f°", Q-specific complexity, header labels.
- Not independently verified by the referee: that Friedl–Rónyai is deterministic polynomial time, and Lemma lem:finite. These are the manuscript's own claims.

## Suggested edits to the manuscript (not applied to manuscript_v3)
1. Insert `section_claude.tex` as a subsection at the end of Sec. consequences, or just before Sec. algorithms (as in build_claude). Forward references to thm:decision and lem:atest are fine.
2. Open problems: delete item 4 ("Polynomial ambiguity").
3. Abstract: replace "Consequences: in the invertible sector CCRA series are polynomially ambiguous and closed under reversal;" with:
   "Consequences: in the invertible sector a series is polynomially ambiguous iff the identity component is triangularizable over $\Q$, so the CCRA series are exactly the polynomially ambiguous series whose unipotent radical is commutative; CCRA series are closed under reversal;"
   Optionally add: "polynomial ambiguity of invertible series is decidable in deterministic polynomial time".
4. Intro, after Corollary cor:consequences, add:
   "Conversely, an invertible series is polynomially ambiguous iff $\cG_f^\circ$ is triangularizable over $\Q$ (Theorem~\ref{thm:polyamb}); thus in the invertible sector CCRA-computability is exactly polynomial ambiguity plus commutation of unipotent elements, and polynomial ambiguity is decidable in deterministic polynomial time (Corollary~\ref{cor:polyamb})."
5. Related work, sentence on PS24: replace "the property and the proof are different, and Corollary~\ref{cor:consequences} shows that CCRA form a proper subclass of polynomially ambiguous series in the invertible sector." with:
   "Theorem~\ref{thm:polyamb} recasts their arithmetic characterization of polynomial ambiguity structurally, as triangularizability of $\cG_f^\circ$ over $\Q$, with a direct proof and a deterministic polynomial-time test, and shows that the invertible CCRA series are exactly the polynomially ambiguous ones with commutative unipotent radical."
6. Organization paragraph: add "Section~\ref{ssec:polyamb} characterizes polynomial ambiguity in the invertible sector."

## Progress log
- 09:27 Read main.tex (Thm main, Cor consequences, open problem 4).
- 09:35 Read PS24 (arXiv:2410.03444v2). Thm 1.6(2): a minimal invertible representation is PA iff μ(X*) has finitely generated spectrum and is power-splitting.
- 09:50 Found the proof; wrote section_claude.tex; integration build compiles.
- 10:00–10:25 Referee pass: correct with minor fixes; fixes applied; recompiled.
- 10:20 Exact checks launched (4 seeds × 40 random PA automata).
- 10:50 All checks finished: 160/160 consistent, no counterexample candidate. Done.
