# polytime_claude: status (Nov 2, 2026)

## Bottom line

**Proved, with complete proofs in `section_claude.tex`:**

1. **Quasi-unipotent sector: deterministic polynomial time.**
   Given a rational weighted automaton, one can decide in deterministic polynomial time (Turing model, binary rationals) whether its series is invertible and quasi-unipotent. If it is, one can also decide whether it is CCRA-computable, equivalently whether Γ_f is virtually abelian. This is Theorem `thm:polytime`(1).
   - The proof is self-contained: it uses exact linear algebra over Q and Hermite normal forms (Kannan–Bachem) only.
   - It needs no factoring, no Friedl–Rónyai, and no Babai–Beals–Rockmore, because the finiteness test is reproved in Lemma `lem:finite`.
   - **This answers the paper's open problem 2 for quasi-unipotent series.**
2. **General invertible sector, deterministic.** There is a decision procedure for condition (3), i.e. for CCRA-computability. It runs in time polynomial in the input length and in a height parameter B_f, the bit size of the Lie algebras of the unipotent radicals of the truncations it visits. Unconditionally it runs in time 2^{O(m log(dk))}·poly(input), where m ≤ d is the nilpotency index of rad(span Γ). So it is polynomial for bounded m. This is Theorem `thm:polytime`(2).
3. **General invertible sector, randomized: Monte Carlo (two-sided error) polynomial time.** This is Theorem `thm:polytime`(3). It follows from (2) by running the layered linear algebra modulo a random prime with O(m log(dk) + log σ) bits.

Parts 2 and 3 call the Friedl–Rónyai deterministic polynomial-time algorithm for the simple components (central primitive idempotents) of a semisimple Q-algebra. It is used only to test condition (a).

**Conjectured, not proved:** B_f is always polynomially bounded. With part 2, this would give **deterministic** polynomial time for the whole invertible sector. Experiments are consistent with it (heights of the computed Lie algebras grow slowly), but the proof of the a priori height bound works only when b(Γ) is finite (Lemma `lem:apriori`).

**Not claimed:**
- No deterministic polynomial-time algorithm for general invertible series with a non-trivial torus and many layers. Part 2 is exponential in m·log d in the worst case.
- Nothing about singular minimal representations.

**Independent review.** A separate referee agent read the section against `main.tex`.
- It found no fatal error, and judged correctness of the decision procedure fully proved.
- It found one real bug: the bit-size bookkeeping in Lemma `sizes` was false as written, because the definition of "tame" did not support the claimed constants. The bug is now repaired with the referee's suggested definition, and the conclusions are unchanged.
- Several minor points were also fixed: the update formula v = I − Σ y_t, the two-pass definition of δ, wording of step 2, the modular-reduction details, and remarks (i)–(iii).
- On a second pass, the referee judged the repaired Lemma `sizes` and the proofs of parts (2) and (3) correct.
  It raised three wording points: a missing one-sided b_a-multiplication bullet, F' taken as a maximum over levels, and σ' for bit sizes in the adapted basis. All three are fixed.
  Its conclusion: "all three parts of the Theorem are proved as stated."

## The idea in one paragraph

Put Γ in the block-triangular form given by the radical series J^i Q^d of A = span Γ. The block-diagonal part b(Γ) is completely reducible, and R_u(G) = G ∩ U_P (Lemma `lem:radical`).

Condition (a) holds iff H° = closure(b(Γ))° is a Q-split torus. This is tested with Beals' centralizer construction plus a splitting test. The ingredients are the finite-image isotypic part B of Ad(b(Γ)) on M_d(Q) and C = centralizer(B) = Q[H°] (Lemma `lem:atest`). Finiteness itself is tested by trace duality, lattice closure and a Reynolds-projected positive form (Lemma `lem:finite`).

U = R_u(G) is then computed layer by layer along the block-distance filtration, stopping at the first non-commutative layer. Each layer is an extension by an abelian group L ⋉ M. There, Lie(D ∩ M) is the minimal "working" submodule: the one modulo which the generator cocycle becomes a coboundary. It equals ∩_{φ∈Φ} ker φ, where Φ = {φ in the commutant : φ∘c is a coboundary on generators} is a left ideal (Lemma `lem:abext`). This is pure linear algebra on generators.

The possibly exponential finite group G/G° (e.g. of order 2^d·d!) never has to be enumerated. Short words provably do not suffice (affine Weyl example, Remark (ii)). Levi conjugators are updated by corrections in a single graded piece (Proposition `prop:layer`). Their bit size is controlled by a weighted "tameness" induction (Lemma `lem:sizes`).

In the quasi-unipotent sector, Schreier generators of exponential word length but polynomial bit size give an a priori polynomial bound on all heights (Lemma `lem:apriori`).

## Dependencies on cited results

| Ingredient | Exact statement used | Where verified | Confidence |
|---|---|---|---|
| Friedl–Rónyai, STOC 1985 [FR85] | For a subalgebra A ⊆ M_n(F), F a number field, given by generators: Rad(A) and the minimal ideals of A/Rad(A) (equivalently the primitive central idempotents) can be computed in deterministic polynomial time. | Quoted verbatim as Theorem 2.6 [FR] in Beals, JCSS 58 (1999), which I read in full (PDF from math.ucla.edu/~pak/papers/Beals.pdf). Rónyai's group summary (ERCIM) says the same for number fields. I did not read FR85 itself. | High. Classical, widely cited. Used **only** in part (2)/(3), for testing (a). |
| Rónyai, J. Symb. Comput. 9 (1990) 355–373 [Ron90] | Cited only as "see also". | Bibliographic data from dblp. The referee recalls it is mainly about finite fields. | Not relied on. |
| Babai–Beals–Rockmore, ISSAC'93 pp. 117–126 [BBR93] | Deterministic polynomial-time finiteness test for f.g. subgroups of GL_n(Q). | As quoted in Beals 1999, Theorem 2.1. | Cited for priority only. Lemma `lem:finite` reproves what is needed. |
| Beals, JCSS 58 (1999) 260–279 [Bea99] | Lemma 3.1 / Section 5: the centralizer construction for testing virtual solvability of completely reducible groups. | Read in full. | Our Lemma `lem:atest` gives a self-contained proof of the variant we need, adding the Q-splitting test. Beals' Corollary 1.6 (abelian-by-finite decidable in polynomial time) is mentioned in Remark (iv) but **not relied on**; its proof there is only sketched. |
| Kannan–Bachem, SIAM J. Comput. 8 (1979) 499–507 [KB79] | Hermite normal form of an integer matrix in polynomial time. | Standard. Not fetched. | High. |
| Borel, Linear Algebraic Groups, 4.7 [Bor91] | In a commutative algebraic group, the semisimple and the unipotent elements form closed subgroups. | Already cited by main.tex for the same fact. | High. |
| Standard facts | (A1)–(A6) of main.tex; Kolchin's fixed-point theorem; a bijective morphism of algebraic groups in characteristic 0 is an isomorphism; closed subgroups of vector groups in characteristic 0 are subspaces; Schreier's lemma; Cramer's rule and Hadamard's bound; left ideals of semisimple algebras are generated by idempotents. | Textbook. | High. |

No result about Zariski-closure computation (DJK05, NPSSW22) is used.

## Files

- `section_claude.tex`: the drop-in section, using main.tex macros.
  - Theorem `thm:polytime`.
  - Lemmas `radical`, `acrit`, `finite`, `atest`, `qutest`, `abext`.
  - Proposition `layer`.
  - The algorithm.
  - Lemmas `apriori`, `sizes`.
  - The proof of the theorem.
  - Remarks: the finite part is never enumerated; the affine Weyl example; the finiteness lower bound; relation to Beals.
- `refs_claude.bib`: five new bib entries (FR85, Ron90, BBR93, Bea99, KB79).
- `build_claude/main_polytime_claude.tex` and `.pdf`: a copy of main.tex with `\input{section_claude}` inserted before "Limits and open problems". It compiles cleanly (25 pages, no undefined references, no overfull boxes). **The original manuscript was not edited.**
- `code_claude/`:
  - `linalg_claude.py`: exact linear algebra on top of python-flint.
  - `polyccra_claude.py`: the algorithm.
    - `Setup` does step 1.
    - `is_finite_cr` is Lemma `finite`.
    - `a_test` is Lemma `atest`.
    - `u_layers` is step 3.
    - `decide` and `decide_qu` are the full procedures.
  - `groundtruth_claude.py`: an independent exponential-time ground truth.
    - In the quasi-unipotent case it uses Schreier generators of K = ker b.
    - Under (a) it uses Schreier generators of the kernel of the finite action on B, with Lie(U) generated by the logs of unipotent parts and of commutators.
  - Tests: `test_paper_examples_claude.py`, `test_random_claude.py`, `test_deep_claude.py`, `test_big_claude.py`, `test_affine_weyl_claude.py`, `test_ccra_claude.py`.
    - The last one uses a copy of the random CCRA generator and Hankel minimisation from `indep_verify_claude/necessity_check.py`, which was not edited.
  - `run_all_claude.sh` reruns everything.
- `logs_claude/`: all outputs; the `final_*` logs are from the final code.

## Sanity checks (exact arithmetic)

- **Paper examples: all verdicts as predicted.**
  - Not CCRA: heis 2^a3^b[w:ab]; MPS Example 17; alternating position sum (quasi-unipotent); position sum (unipotent).
  - CCRA: BS(1,2) Σ2^i b_i; alternating sum; letter counts.
  - Controls: SL_2(Z) generators fail (a). [[1,1],[1,2]] and [[2,−1],[1,2]] are non-split tori, so NO. The Pythagorean rotation is an anisotropic torus, so NO. The dihedral group of order 8 gives YES. M = [[0,2],[1,0]] has M² = 2I, so H° is the split scalar torus; this gives **YES**, which corrected my initial expectation; it is CCRA with parity control.
- **Cross-checks of the full Lie algebra Lie(U), compared level by level against the exponential ground truth.**
  - Final code (`logs_claude/final_*`): 160 random and 240 deep instances, plus 18 CCRA-derived ones, give **418/418 agreements**.
  - Earlier code versions: about 600 more instances, also with 0 mismatches.

  Families:
  - random quasi-unipotent (YES-type and generic);
  - torus+finite (YES-type and generic);
  - deep towers with m up to 5 and d up to 10, using a torus Levi with monomial finite part and abelian or generic unipotent part, conjugated by random unipotent and random GL elements;
  - d = 6 towers with 2×2 monomial torus blocks.
- **Random CCRA-derived invertible minimal representations:** 108 instances over 5 seeds (d ≤ 6). **All pass**, as the necessity theorem predicts, and in 108/108 the computed Lie(U) equals the ground truth.
  - Control (random integer matrices): never "YES while a finite proxy certifies failure".
- **Large finite parts, never enumerated:**
  - Affine Weyl group Ã_n in GL_{n+2}(Q), with finite quotient of order (n+1)!: correct YES with the right n-dimensional U (equal to the ground truth for n ≤ 5); the n = 8 instance (9! = 362880) takes 1.8 s. The multiplicative (torus) version passes the (a)-test for n ≤ 5, but the naive Python span closure in End(M_d) takes 237 s at d = 6 (polynomial, but slow in this implementation).
  - Random signed-permutation blocks with d = 12 and m = 3, 4: YES instances recognised in 2–5 s.
- Bit sizes of the computed u_j and Levi conjugators stayed small (≤ 17 bits) in all runs.

## Suggested edits to main.tex (for the authors, not made here)

- **Theorem `thm:decision`:** add "and in polynomial bit time in the quasi-unipotent sector; in general in time polynomial in the input and B_f, in 2^{O(m log dk)}·poly time deterministically, and in Monte Carlo polynomial time".
- **Section 8 sentence** "We do not know whether … the Zariski-closure step is the bottleneck": replace it with a pointer to the new section. Note that the new procedure avoids Zariski closures altogether.
- **Open problem 2:** reformulate as "Is CCRA-computability of invertible series decidable in deterministic polynomial time? It is in the quasi-unipotent sector, in Monte Carlo polynomial time in general, and deterministically polynomial if the heights B_f are polynomially bounded."
- **Abstract** (optional): "…membership is decidable in randomized polynomial time, and in deterministic polynomial time in the quasi-unipotent sector".

## Confidence

- Correctness of the decision procedure (Lemmas `radical`–`abext`, Proposition `layer`): **high**. It was checked by an independent referee pass and by more than 600 exact cross-checks against an independent exponential algorithm.
- Polynomial bit complexity in the quasi-unipotent sector (Lemmas `apriori` and `sizes`): **moderately high**.
  - Lemma `sizes` is a bookkeeping argument. Its first version was wrong in detail and has been repaired.
  - Lemma `apriori` was judged correct by the referee.
- Monte Carlo claim (3): **moderately high**. It is a standard modular-simulation argument resting on the bound from (2).
