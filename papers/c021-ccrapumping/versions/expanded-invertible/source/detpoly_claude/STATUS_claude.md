# STATUS (detpoly_claude) -- polynomial bound on B_f, deterministic polynomial time

## Bottom line (12:40 Beijing time, 2 Nov 2026)
**Claimed: the conjecture of the paper is true, and Open Problem 2 ("Complexity") is solved
positively.** For every invertible series satisfying (a), Lie(U) (U = R_u(G_f)) is spanned by matrices
of polynomial bit size in the adapted basis. Hence ht(u_j) is polynomial for every j, so B_f is
polynomial. By Theorem polytime(2) of the paper, the *unchanged* layer algorithm of Section
ssec:layers then decides CCRA-computability of invertible series in **deterministic polynomial time**.
Only the analysis is new; no new algorithm is needed.

Status of the claim:
- Written as a drop-in subsection `section_claude.tex` (Section 9.5 of the test build).
- One fresh referee subagent checked it line by line. **Verdict: "Yes, the theorem is proved, with
  fixable gaps. I found no fatal or serious error."** It listed 10 minor/presentation items; all are
  applied (see below). One item (#1) was a real but local size gap; it is fixed.
- Exact experiments (python-flint) on 4 families of examples agree with the independent exponential
  ground truth in every test run (details below).

This is a proof I believe is correct. It has been read by one AI referee, but **not yet by a human**.
Treat it accordingly.

## Files
- `section_claude.tex`: the subsection (macros of main.tex only). Place it at the end of
  sec_polytime.tex, after Remark rem:polytime.
- `build_claude/main_detpoly_claude.tex` / `.pdf`: a copy of manuscript_v3_claude/main.tex that
  `\input`s the original sec_*.tex files plus `section_claude.tex`. 46 pp.; Section 9.5 is pp. 26–31.
  Compiles with no undefined references. The manuscript folder itself was not touched.
- `code_claude/detpoly_check_claude.py`: an exact implementation of the construction in the proof:
  - torus from short words;
  - regular element and torus conjugator v0, both the Jordan-based and the Jordan-free iterations of Lemma iter;
  - the slice element xhat_a and m_a;
  - Schreier generators for U'' modulo the finite group Psi;
  - the closure of Proposition ugen.

  It compares against `gt_general` of polytime_claude (Schreier generators of the full finite quotient,
  exponential).
- `code_claude/test_detpoly_claude.py`: test driver. Run as `python3 -I test_detpoly_claude.py FAMILY SEED N L`,
  with `ITER=1` for the Jordan-free variant.
- `logs_claude/*.log`: test outputs.
- `logs_claude/section_before_referee_fixes.tex`: the version the referee read.

## Proof structure (section_claude.tex)
Notation: S = H°, a Q-split torus in L_P. The weight basis refines the adapted basis; z is the zero
weight part of u_P and Z = C_{U_P}(S) = I + z. An element Y of Lie(S) is regular if
ad(Y) is invertible on u_P^{≠0}, which gives C_{U_P}(Y) = Z.

1. **Lemma iter (tame iterations).** Three iterations of m−1 steps, each with polynomial-size output (by
   the tame calculus of Lemma sizes):
   - (1) g_s = u h u^{-1} with u ∈ U_P, for g ∈ hU_P;
   - (2) X_s = Ad(u)Y for X ∈ Y + u_P with Y regular;
   - (3) the slice U_P = exp(u_P^{≠0}) × Z is an isomorphism of varieties, with polynomial-size components.

   No Jordan decomposition is ever computed directly.
2. **Lemma torus.** Lie(H°) is the sum of Lie(closure<b(M_w)>°) over words of length ≤ 2d²+2d. Proof:
   - use a valuation cocycle c(g)_{χ,p} = v_p(det g_χ) on the permutation module of S-weights;
   - Lie(S) = col(N^{-1} span c(K_π));
   - an equivariant projection and the cycle space of the Schreier graph of the weight permutation
     action show that fundamental cycles (words of length ≤ 2d−1), together with conjugates by words of
     length ≤ d², already span.

   This is the step that deals with the possibly exponential finite group H/H°.
3. **Lemma v0.**
   - Lifts of the Lie(S_w) to Lie(Θ_w) ⊂ Lie(G°) via Lemma iter(1) give a regular Y and an X ∈ Lie(G°) of
     polynomial size with b(X) = Y.
   - Lemma iter(2) gives v0 with X_s = Ad(v0)Y.
   - Hence v0 S v0^{-1} is a maximal torus of G°. This step uses the conjugacy of maximal tori and an
     iteration inside Ad(v^{-1})u.
4. **Lemma xhat.** After conjugation by v0, S lies in G.
   - U = exp(u^{≠0}) · C_U(S), by a dimension and irreducibility argument.
   - xhat_a is the unique element of exp(u_P^{≠0}) with xhat_a S xhat_a^{-1} = M_a S M_a^{-1}. It lies in U
     and has polynomial size (linear system plus Lemma iter(3)).
   - m_a = xhat_a^{-1} M_a normalizes S.
5. **Lemma Upp.** Let U'' = R_u(closure<S, m_a>).
   - b(Γ) acts on C(S) = ⊕ End(V_χ) through a finite group Ψ, since S acts trivially. Lemma finite(2)
     gives |Ψ| ≤ (2d²+1)^{d⁴} and polynomial-size elements.
   - The Schreier generators of the kernel of Γ'' → Ψ, after removing the block-diagonal part, are
     products of Ψ-conjugates of zero-weight nilpotents. As in Lemma apriori they have polynomial size.
   - φ(g) = b(g)^{-1} g = g_u is a homomorphism on that kernel.
6. **Proposition ugen.** u is the Lie algebra generated by the smallest subspace that contains log xhat_a
   and Lie(U'') and is stable under Ad(m_a)^{±1} and ad(Lie S). Then (F1)–(F3) give polynomial height.

The QU sector (S = 1) is the special case v0 = I, xhat_a = I, which is Lemma apriori.

## Referee (one fresh subagent, given only the paper and the section)
Verdict: **proved, with fixable gaps; no fatal or serious error.** The items and how each was handled:
1. Lemma v0: the sum over exponentially many spanning vectors made the size of X unjustified.
   **Fixed:** a basis of Lie(S) is now chosen among them, so at most d words are used.
2. (F2) and (F3): the bit bounds ignored common denominators. **Fixed:** they now read O(N³(β+log N))
   and O(md²(β+log d)).
3. Lemma iter, "Sizes": the referee confirmed the appeal is legitimate but under-argued. **Expanded:**
   δ, the fixed maps, the incremental updates, and the tameness constants are now explicit.
4. Notation clashes. **Fixed:** renamed to Ξ, \mathcal Q, \mathsf W, K_π, ϱ.
5. Polynomial size of the weight idempotents. **Added** a sentence.
6. β0 bounds the block determinants, not σ. **Fixed.**
7. Rationality and size of the reduced echelon solution in Lemma xhat. **Added.**
8. u_j = π_j(u), and these are exactly the objects of Definition heights and step 3. **Added.**
9. The inclusion U'' ⊆ C_U(S) was not used. **Replaced** by U'' ⊆ U, which is used, and the fact that
   the factors lie in Z is now proved where it is used.
10. Paper consistency: see the list below.

Re-check of the revised text by the same referee: **"all ten fixes are correct, I found no new error, and the
theorem is proved."** Its one remaining notation leftover (a generic block-diagonal matrix also called Z in
Lemma v0) has been renamed B. Reminder from the referee: the paper-wide edits listed below still have to
be made in main.tex / sec_polytime.tex. I did not make them, because those files are outside my folder.

## Exact experiments (all agree with the ground truth)
| family | tests | Lie(S) from short words = GT | Lie U from construction = GT | xhat_a ∈ U | |Ψ| |
|---|---|---|---|---|---|
| deep_yes, L=3 | 25 | 25 | 25 | 25 | 1–2 |
| deep_no, L=3 | 25 | 25 | 25 | 25 | 1–2 |
| deep_yes, L=3, Jordan-free iterations | 40 | 40 | 40 | 40 | 1–2 |
| deep_yes / deep_no, L=2, Jordan-free | 15 + 15 | all | all | all | 1–2 |
| deep_no, L=3, Jordan-free | 40 | 40 | 40 | 40 | 1–2 |
| weyl2, L=4, Jordan-free | 10 | 10 | 10 | 10 | 6, 24 |
| weyl2 (mult. affine Weyl Ã_n ⋉ unipotent, 2 blocks), L=4 | 12 | 12 | 12 | 12 | 6, 24 |
| weyl3 (3 blocks, d up to 9), L=4 | 3 + 6 (Jordan-free) | all | all | all | 6, 24 |

Weyl families with L=3 and n=3: Lie(S) from words of length ≤ 3 is 0, while the true Lie(S) is
3-dimensional. This is expected: words of length ≤ n lie in finite parabolic subgroups. Length 4 = n+1
suffices. The lemma's bound is 2d²+2d.

The bit sizes observed (v0 up to 137 bits, Lie U heights ≤ 5) are small. The experiments test the
mathematical claims, not asymptotics.

## Exactly which statements of the paper change
(line numbers as in manuscript_v3_claude; nothing there was edited)
1. **Abstract** (main.tex l.49): "polynomial ambiguity of invertible series is decidable in
   deterministic polynomial time, and CCRA membership in randomized polynomial time, and
   deterministically in the quasi-unipotent sector" → "polynomial ambiguity and CCRA membership of
   invertible series are decidable in deterministic polynomial time".
2. **Theorem decision** (main.tex l.101), last sentence: "and CCRA-computability of invertible series
   is decidable in Monte Carlo polynomial time (Theorem polytime)" → "and CCRA-computability of
   invertible series is decidable in deterministic polynomial time (Theorems polytime and detpoly)".
   The quasi-unipotent sentence before it becomes a special case.
3. main.tex l.377: "it runs in deterministic polynomial time in the quasi-unipotent sector and in Monte
   Carlo polynomial time in general" → "it runs in deterministic polynomial time (Theorem detpoly)".
4. main.tex l.382: "the quasi-unipotent and randomized claims are Theorem polytime" → "the remaining
   claims are Theorems polytime and detpoly".
5. **Theorem polytime** (sec_polytime l.21–29):
   - (2): append "By Theorem detpoly, B_f is bounded by a polynomial in the input length, so this
     algorithm runs in deterministic polynomial time on all invertible series."
   - (3) (Randomized): superseded. Either delete it or keep it with the remark that it is no longer needed.
   - The 2^{O(m log dk)} bound becomes moot.
6. sec_polytime l.35–38, "We conjecture that B_f is always bounded …": replace with "Theorem detpoly
   (Section ssec:detpoly) shows that B_f is always bounded by a polynomial in the input length, so the
   algorithm runs in deterministic polynomial time on the whole invertible sector; in the quasi-unipotent
   sector this is Lemma apriori."
7. sec_polytime l.40–45, "The proof has three ingredients": add a fourth, the a-priori height bound of
   Section ssec:detpoly.
8. **Remark polytime(ii)**: still true for unipotent parts. Optionally add the contrast with Lemma torus:
   for the torus, words of length O(d²) suffice.
9. **Open problem 2 ("Complexity", main.tex l.422)**: resolved. Delete it, or replace it with a
   finer question, e.g. "Is CCRA-computability of invertible series in NC, or decidable in time
   Õ(d^ω·poly(σ))? Can Lie(R_u(G_f)) be computed in polynomial time without the layer-by-layer
   cohomology, e.g. from words of polynomial length?"
10. **Related work / Sectors** (main.tex l.98, l.118): "polynomial ambiguity is decidable in
    deterministic polynomial time" stays. Where CCRA membership is mentioned as randomized, change it
    to deterministic.
11. **Table:** there is no table environment in manuscript_v3_claude (grep finds none). If a summary
    table exists elsewhere (e.g. READY_claude or slides), change the entry "CCRA membership, invertible
    sector: Monte Carlo poly / deterministic in QU sector" to "deterministic polynomial time".

## Progress log
- 11:03 Start. Read sec_polytime.tex and the relevant parts of main.tex.
- 11:20–12:00 Mathematics. The first attempt needed a "torus word length" parameter. The valuation
  cocycle and fundamental-cycle argument (Lemma torus) then removed it. The Jordan-free iterations
  (Lemma iter) avoid quasi-polynomial Newton bounds and the problem of large rational points of tori.
- 12:00–12:10 Exact tests, all agreeing (logs_claude).
- 12:10–12:17 Wrote section_claude.tex and compiled the test build.
- 12:17–12:30 Referee subagent. Verdict: proved with fixable gaps.
- 12:30–12:35 Applied all referee items, recompiled, and wrote this file.
- 12:36 Referee re-check: fixes correct, no new error, theorem proved. Renamed the last notation clash and
  recompiled (46 pp., 0 undefined references).
