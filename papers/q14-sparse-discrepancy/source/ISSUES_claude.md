# ISSUES_claude.md: proof and data issues found while writing the manuscript

Prepared while turning `q14_claude/notes_claude/partial_results_claude.tex` (and `STATUS_claude.md`)
into `main.tex`. Each step was re-derived during writing. **No gap was found that invalidates a
claimed theorem.** The items below are small inaccuracies, places where the notes were too terse, or
caveats. Each is resolved or flagged in the manuscript.

## A. Small inaccuracies in the notes (fixed in the manuscript)

1. **Theorem C, t = 2 bound.** The notes say "for t=2 the discrepancy is at most Δ·2^{Δ−1}".
   This holds only for Δ ≥ 2. For Δ = 1 the formula t·Δ·max(1, 2^{Δ−2}) gives 2, not 1.
   The manuscript states the t = 2 consequence for Δ ≥ 2 only (Theorem 1.6).

2. **SAT evidence description.** "Three functions with up to 8 items" (notes, Section 7) refers to
   `run_two.py 3 3 ...`, which builds three functions that all share **every** item. Such instances
   are t = 3, not t = 2. They are consistent with K_3 = 2 but are not evidence for the t = 2
   conjecture. The manuscript (Table 2) labels them as t = 3. Likewise, "two functions with up to 15
   items" is K_2 territory, which is already proved.

3. **SAT instance list.** STATUS lists cycle (n, b) = (3, 3), which does not appear in the q14 logs.
   I re-ran it from the ancillary copy (no cover, 0.0 s). `batch1_D3.log` also contains (5, 4)
   (m = 20, no cover, 1240 s), which STATUS omits. `batch1.sh` also lists `cycle 7 3` and
   `complete 4 3`, but no result line exists for them (presumably time-outs or unfinished runs).
   They are **not** reported. `K7_D3.log` has no result line and is not reported either.

4. **Theorem A tightness.** The notes say the bound is "attained (one bundle shared by t
   functions)". Two points needed care. (i) K_t is a supremum and need not be attained. (ii) In
   the HMMS setting sparsity is measured by *relevance*, so a worst family for K_t might not have
   every item relevant to every function. The manuscript adds Lemma 2.6 (a perturbation that makes
   every coordinate relevant at cost ε) and states tightness as "for every ε > 0 ... exceeds K_t − ε".

5. **Corollary B, t = 2 statement.** The notes say "F contains a whole parallel class of every
   cycle". The correct and intended condition is that F is a union of bundles whose removal leaves
   a forest. A partially removed bundle still forms an edge. Fixed in Corollary 1.5.

6. **Theorem D constant.** STATUS says max(2, Δ2^{Δ−1}). For Δ ≥ 2 this equals Δ2^{Δ−1}, which is
   what the manuscript states.

## B. Places where the notes were too terse (expanded to full proofs; no gap found)

7. **Theorem A with non-integer K_t (t ≥ 4).** The loop and separation notions use step length
   ≤ s for real s. All arguments (Lemmas 2.10–2.12) were re-checked for real s.

8. **Theorem C: merging private items.** Merging B_{v} into a bundle e ∈ N(v) enlarges the
   *declared* supports of the other members of S_e. To make this legitimate, the manuscript works
   with instances with declared supports and with general "bundle structures" (Definition 5.1,
   Theorem 5.2). The general form is also needed by Theorem D, where auxiliary functions with
   d = 1 are added.

9. **Theorem C: Euler class.** The notes claim that "the t_e-degree of e(V) equals k_e". Only
   "every monomial of the expansion has t_e-exponent ≤ k_e" is needed, together with e(V) ≠ 0
   (a product of nonzero linear forms in an integral domain) and the monomial-ideal membership
   criterion. The manuscript proves exactly this (Section 5.5, Fact 5.9).

10. **Theorem D ("proof sketch with all steps" in the notes).** Fully written out (Section 7),
    including: (a) contracting light components gives a forest *without parallel edges*, since a
    2-cycle or longer cycle in the block graph lifts to a cycle of H through a heavy vertex;
    (b) heavy feasible sets are c-separating and contain c-loops (Lemma 2.12 with q = 1, K_2 = 2 ≤ c);
    (c) light components: Theorem 5.2 applied to the auxiliary instance gives |φ_j| ≤ k_{B_j} ≤ c
    and |ψ| ≤ k_P ≤ c, with k_internal ≤ 2^{Δ−1}, k_pendant ≤ 2^{Δ−2}+1 ≤ c ≤ 2^{Δ−1}, and Δ ≥ 2 used
    throughout; (d) both root cases. No gap found.

## C. Caveats stated in the manuscript

11. **K_3 is computer-assisted.** The script `k3_rigorous_exact.py` was re-run from a copy
    (`ancillary/`) with `python3 -I`. Output: `choices 7365 boxes 20613 fails 0` (about 10 s). An
    independent dependency-free re-implementation `ancillary/k3_certificate.py` gives
    `choices 7365 boxes 20613 max_depth 6 fails 0`. The reduction from K_3 ≤ 2 to the finite check
    (Lemmas 3.3, 3.4) was re-derived by hand, including the symmetry of the mixed-pair condition
    under y ↔ ȳ, which justifies the script's use of `P[0]`.

12. **Product structure remark.** The notes say "without the product structure the linear system
    is feasible". I re-ran the LP part of `k3_exact.py`: 72 of the 7365 configurations are feasible
    for arbitrary weights in [0,1], with margin 0.2, hence also for strictly positive weights. These
    are only *necessary* conditions, so this shows that the certificate needs the product structure.
    It does **not** produce a counterexample for non-product weights. The manuscript's phrasing
    (Remark 3.6) reflects this.

13. **K_4 remark** rests on a floating-point LP (`corner_check.py`, eps = 1e-6). It is hedged as
    "indicates" / "appear to be" in Remark 3.6.

14. **SAT evidence.** UNSAT answers from kissat 4.0.4 were not independently certified (no DRAT
    proofs). All instances have m ≤ 21, so the full CNF (all 2^{m−1} cover clauses) is solved in one
    call. Positive controls (D = 2 covers for two functions sharing two items and for C_4 with
    bundles of size 2) and a negative control (one function, D = 2) behave as expected. Random
    instance counts were taken from `q14_claude/random_D3_*.log`, which another agent was still
    extending while I wrote. The manuscript reports the counts at the time of the final check.

15. **Topology references.** No theorem numbers are cited for Fadell–Husseini, Matoušek,
    Blagojević–Ziegler or Milnor–Stasheff. The facts used (monotonicity; the index of a product of
    spheres; the Euler class of a sum of characters via Whitney sum and Gysin; monomial ideals)
    are given with short justifications in Section 5.4. The products-of-spheres computation is
    cited with "cf." to Mani-Levitska–Vrećica–Živaljević and Blagojević–Ziegler, because I could
    not check the exact statements in those texts.

16. **Bibliography.** Entries for HMMS (incl. ITCS 2026 data), Dupré la Tour–Fujii, ARW (ESA 2026),
    Beck–Fiala, Beck, Spencer, Banaszczyk, Bansal, Lovett–Meka, Bansal–Jiang (FOCS'25, STOC'26),
    Simmons–Su, Alon, Filos-Ratsikas–Goldberg, FHSZ (SODA'21, SICOMP'23), GHIMS (WINE 2020) and
    Manurangsi–Suksompong come from the reference lists of the source texts. Entries for Hobby–Rice,
    Pinkus, Fadell–Husseini, Matoušek (two books), Blagojević–Ziegler, Milnor–Stasheff, Hatcher,
    Ramos, Mani-Levitska–Vrećica–Živaljević and Berge are standard data from memory. They should be
    spot-checked before the camera-ready version (in particular the Blagojević–Ziegler page range
    273–341 and the Pinkus page range 82–84).

## D. Late update of the source notes (incorporated)

17. **Theorem D upgraded (notes updated at 04:49).** The research notes replaced the original
    Theorem D ("for t = 2, no heavy vertex on a cycle ⇒ disc ≤ Δ2^{Δ−1}", proved by a block-tree
    decomposition into light components) with a stronger *bounded block-degree* theorem: for general t,
    if every heavy function (d_v > Δ) has at most Δ ports in each of its lobes, then
    disc ≤ tΔ·max(1, 2^{Δ−2}). For t = 2 this means: if every block has maximum degree ≤ Δ, then
    disc ≤ Δ2^{Δ−1}; cacti have disc ≤ 4. The proof is an induction on the number of heavy functions
    that uses a "closing-vertex" lemma. The manuscript now uses this version (Theorem 1.8 =
    Theorem 7.6, Lemma 7.7, Corollary 7.8). The old Theorem D appears as Corollary 7.8.
    I re-derived the new proof in full and found **no gap**. Points the notes left implicit, now
    proved in the manuscript:
    - Lemma 7.2: each hyperedge at v is a port of exactly one lobe; lobe item sets are disjoint;
      functions outside v's lobes form an independent instance. The notes' proof ignores components
      of H − v not attached to v; the manuscript handles them by induction, since that instance
      also has fewer heavy functions.
    - Lemma 7.4(c): hypothesis (★) is inherited by the closing instance. The notes' sentence ("a
      heavy v' ∈ L keeps its lobes except that the lobe containing c_L has ports contained in the
      ports of the lobe of v' containing v") is replaced by a cleaner injection argument: every
      lobe of u in the closing instance maps into a lobe of u in the original, injectively on ports.
    - Lemma 7.7: for t = 2, lobes correspond to blocks, and ports to the edges of the block at v. This
      uses the standard fact that two edges are in the same block iff they lie on a common cycle.
    - The notes' wording "lies in more than Δ bundles" for heavy is read as "more than Δ hyperedges
      of H" (private bundles do not count), consistent with Theorem C's convention.
    **The orchestrator checked the old Theorem D, not this version. Please re-check Section 7.**
    The notes' informal remark (capacity / mod-2 cancellation / embedding simple graphs) was not
    included, apart from the one-line explanation of why the closing reduction stalls on a block
    with a high-degree vertex (Remark 7.9).

## E. Final data snapshot (05:0x Beijing)

18. Random-instance counts in the manuscript (intro and Table 2): **148 instances, 146 with no
    cover, 2 time-outs (1200 s), 0 covers**, read from `q14_claude/random_D3_*.log` at the final check.
    Copies of all `*_D3*.log` files are in `ancillary/sat_logs/`. New named instances found in the
    logs were added: K_{2,4} and K_{2,5} with bundles of size 2 (no cover; I re-ran K_{2,4}).
    Still-running instances (K_{2,3}×3, K_5×2, W_4(2,3), W_5(2,2), W_7(1,2), K_7) have no result
    line and are not reported.

## D. Version with Theorem F (degeneracy bound), 2026-11-02 ~07:00 Beijing

Source: `q14b_claude/notes_claude/q14b_degeneracy_claude.tex`.
- **Independent checks of the source note:**
  - the q14b agent's own referee subagent found no error;
  - the orchestrator re-derived every step: the component tree via crossing parity on simply
    connected |K|; Borsuk–Ulam to the tree; the separator lemma; the ε-bookkeeping in the hub
    lemma; Corollary G; Theorem F; and the hybrid, thin-spoke and example corollaries.
- **New Section 8.** Integrated with the paper's own lemmas:
  - crossing, certificate and necklace (k = 2), and the multilinear extension.
  - Constraint systems and c-good graphs are phrased via "c-coarse" sets.
- **Changes relative to the note:**
  1. The rounding step now states that x_S is piecewise linear on each octahedron face. The path
     is subdivided so that every coordinate keeps its weak sign, which yields a finite antipodal
     1-path of nearest-sign roundings. The note only sketched this step.
  2. The 1-sum lemma is proved with explicit item sets E_j, I_j, R, including the case E_j = ∅.
  3. Corollary 8.x (pairwise hubs, general t) is stated as a corollary with a proof sketch.
  4. The t ≥ 3 obstruction (Remark "limits of the method") was re-checked: e_j is even and
     2-Lipschitz, ψ is odd and 2-Lipschitz (needs M ≤ m), the χ-path is a 1-path, and the four
     pair-constant sets contain 2-loops.
  5. The note's "discrete-cube analogue false (Q(7) search)" and "parallel hub transfer false"
     claims are NOT included: they were not independently verified.
  6. The note's "exact version (2 fractional items per bundle)" is NOT included: sketch only.
- Thin-hub Theorem E / Corollary F of q14_claude are superseded for t = 2 and are not included.
- Bib entries added: Spa66 (edge-path group), Kos84 and Tho84 (degeneracy of K_r-minor-free graphs).

## E. Additions from q14_claude's final report (2026-11-02 ~08:10)
- **Lemma pair** (loss-1 transfer for spokes with |S| ≤ a+1): re-derived by the orchestrator. Added: the case
  analysis showing that B and N partition the cube.
- **Theorem mult** (disc ≤ q + max Σ w_q; dgn + μ): re-derived. The extension step uses jumps z → −z of length ≤ q.
- **Theorem sqrtn / Theorem dense:** the agent's Theorem G, re-proved in a simpler "ownership" form.
  - Each fractional item gets an owner; non-owners average it out.
  - For t = 2, Hakimi's orientation theorem improves the constant to 1 + 2⌈√(sn/2)⌉ (agent: 1 + 2s√(2n)).
  - For general t, the agent's degeneracy argument is kept: 1 + 2s√(t(t−1)n).
- **Proposition t3** (3-sparse additive family with disc 3 > K_3): brute-force checked (scratchpad t3cover.py,
  t3check2.py: all 16 colourings are covered exactly once). This answers the paper's former open problem
  "disc ≤ K_t for all t-sparse?" negatively.
- **Remark K4:** K_4 ≥ 3 by an elementary example. The open problem "Is K_4 = 2?" is replaced by "Is K_4 = 3?".
- **NOT yet included:**
  - Theorem H (all t = 2 families with ≤ 5 functions have disc ≤ 2);
  - K_4 ≤ 3.

  Both are computer-assisted. An independent re-implementation is running; include them only if it confirms.

## F. Full-paper referee (2026-11-02 ~08:40): no mathematical error in the new content; fixes applied
- **E1–E4** (fractional items in no support; δ ≤ √(t(t−1)n); s ≥ 1; Theorem mult and Corollary thin applied
  directly to the instance's own bundles): fixed.
- **C1–C13:**
  - The abstract is rewritten to lead with the t = 2 degeneracy theorem; the results list is reordered.
  - Fixed: the Table 1 caption and rows (merged and deduplicated; K_{s,n} renamed to K_{p,n}), related work,
    organization, stale loss-1 statements, the K_4 remark, "Moreover" in Theorem F, non-private bundles, and the
    outdated K_6 and wheel comparisons.

## G. K_4 = 3 and Theorem H (2026-11-02 ~09:15)
- An independent re-implementation from scratch (scratchpad indepH, copied to ancillary/small_n_check/) confirms
  both. Exact arithmetic; 13 boxes for K_4, j = 4; 299 patterns and 1213 boxes for t = 2, n ≤ 5.
  - The results agree with q14_claude's kn_bnb_exact.py and sparse_bnb_dfs.py.
  - Sanity checks fail exactly where they must.
  - The run was repeated from the ancillary copy with identical output.
- Caveat noted by the checker: kn_bnb_exact.py treats only antipodal single points as mixed sets. That is complete
  for j ≤ floor(c)+1, which covers K_4 (j ≤ 4, c = 3); the main checker cover_bnb.py has no such restriction.
- Added: Section 3.4 (Lemma necessaryc, Theorem H with reduction), Theorem Kn now includes K_4 = 3, the abstract,
  Table 1 row, open problem "Is K_5 = 3?", and the appendix.

## H. Loss-1 hub transfer: Theorem F improved from 2d+1 to d+1 (2 Nov 2026, ~10:55)

Source: loss1_claude/ (agent proof + independent referee subagent, "correct with minor fixes").
I re-verified every step myself before integrating: the reduction (facts (i)-(iii)), the
component-tree lemma on the coned 2-skeleton K_S (simple connectivity via Hatcher Prop. 1.26),
the Borsuk-Ulam nearly-antipodal lemma via the necklace map S^2 -> |K_S|, the free-involution
separation lemma, Lemma corners (components in K vs the cube), the dichotomy, the edge-cover lemma
and the separation lemma, and the substitution into the deletion proof (levels C - m_k(v), l >= 2,
hub level >= 1).

Changes in main.tex:
- Sec. 8: replaced "Labelled triangulations of S^2" + old loss-2 hub lemma by
  "The coned 2-skeleton of the cube" (lem:tree, lem:nearlyantipodal, lem:invsep, lem:corners) and
  a new hub-transfer subsection (thick sets, lem:dichotomy, lem:thicksep, lem:edgecover, lem:hub
  with threshold a+1 and the T = empty case with threshold 2, cor:hub with l >= 2 -> l-1).
- thm:Finst: 2d+1 -> d+1, with tightness for d <= 1 (K_1 = 1, K_2 = 2).
- Removed (now subsumed): cor:thin, lem:pair, cor:pair, thm:mult, Theorem F(d).
- cor:hybrid and cor:pairwise: max(2d_1+1, beta+2q) -> max(d_1+1, beta+q).
- cor:examples: wheels 4, K_{p,n} p+1 (K_{2,n} 3), planar 6, treewidth k+1, outerplanar /
  series-parallel / cycles / cacti 3, Delta+1.
- rem:hublimits(1): now states the loss of one level is optimal.
- Abstract, informal results list, Theorem F, the paragraph after thm:dense, the technical
  overview, Table 1, the computational-evidence paragraph, Sec. 9 summary, open problems
  (old problem 2 "loss in hub transfer" resolved; replaced by "degeneracy versus discrepancy").
Build: 40 pp, no undefined refs, 13/13 checks.

## I. Second referee on the integrated paper (2 Nov 2026, ~11:35)
No mathematical errors found. Applied: six-function consequence (disc <= 3; K_n <= n-3) as cor:examples (vii) /
Theorem F(d); SAT-evidence wording (instances with <= 5 functions are implied by Theorem H); Table 1 fixes;
softened "limit of this approach"; rigour additions in lem:tree and before cor:onesum; minor fixes.
Full list: q14referee2_claude/REPORT_claude.md. Build: 41 pp, 13/13 checks.

## J. Leveled deletions: disc <= 2 for cycles, cacti, triangle-free outerplanar (2 Nov 2026, ~13:30)
Source: dense_claude/ (three referee subagents, no mathematical error; exhaustive checks of all leveled
instances on graphs of the class with <= 11 vertices). Claude re-verified Lemma K12 (asymmetric K_2), the
leaf/deletion/1-sum rules with levels, Theorem leveled (a)-(d) and Corollary leveled before integrating.
New subsection sec:leveled after cor:pairwise. Updated: abstract, informal list, Theorem F(b), paragraph
after thm:dense, technical overview, computational-evidence paragraph, Table 1 (cycle, cactus, new row,
wheel/K_{p,n}), remark after cor:B, proof of thm:F, paragraph after thm:F, Sec. 9 summary, open
problems 2 and 7. cor:examples (i)-(iii) kept as degeneracy consequences, with a pointer to the
improvement. Build: 44 pp, 13/13 checks.

## K. Simulated STOC-PC review (2026-11-02, ~15:50) and fixes
Verdict: weak reject (borderline), no false theorem found; every Sec. 8 proof checked line by line.
Fixed:
- Open frontier misstated ("remaining open case is dense patterns with large bundles"): now "open on every class of
  unbounded degeneracy, already for K_n with single-item bundles" (abstract, Sec. 1.1).
- Abstract restructured: t=2 degeneracy theorem + hub transfer first; K_n values demoted to one sentence.
- "Our main result is Theorem F" sentence at the start of Sec. 1.1; summary table cut to 11 rows, t=2 first.
- New "why t=2 is hard" paragraph (Cor B cost, n fractional items, one cut per bundle fails, |x1+x2|<=1 & |x1-x2|<=1).
- Tightness: "tight for d<=1 (forests); for d>=2 the only lower bound we know is 2"; "a transfer of this kind must
  lose one level" (was "a loss of one level is unavoidable"; the leaf rule loses none).
- New intro Theorem thm:thick-intro (antipodal blocking sets = Lemmas dichotomy + separation, (b) restated via
  "P ∪ N thick", equivalent to "M has no 1-loop").
- Credit: Thm C uses de Longueville–Živaljević product-of-necklace-spheres setup; parity decomposition = character
  decomposition familiar from GHR problem (Ramos, BFHZ18). Related work adds dLZ08, BFHZ18, AW86, FS13, HMMS ITCS 2026.
  All five verified (Crossref / arXiv / Dagstuhl page).
- Theorem F now flags the parts that use computer-assisted Theorem H (triangles in (b), W_3, part (d)).
- Restated Theorem "first part" (K_4 = 3 proved in Sec. 3.4).
- SAT overclaim "the truth is 2 in all these cases" -> "no discrepancy-3 instance for the bundle sizes tested".
- Notation clash: the constants are now \mathcal{K}_n; K_n is reserved for complete graphs (80 lines; every remaining
  bare K_n/K_4/K_5 checked to be a graph).
Not done: DRAT certificates for SAT runs; physical reordering of Sec. 1.1 theorems.

## L. Near-loop transfer (dense2_claude, integrated 2026-11-02 ~17:50)
New subsection sec:nearloops (Sec. 8.7) from dense2_claude/notes_claude/paper_insert_claude.tex (v4):
lem:nearpairs, lem:neardichotomy (dist(P,N) >= 2), lem:nearcover (Borsuk–Ulam), lem:neartransfer /
cor:neartransfer (NO level loss), lem:cheap, thm:maxtwod (max(2,d)), lem:schedule, thm:orient (in-degree k
=> k+1; pseudoarboricity + 1; planar <= 4), cor:maxtwod (2-degenerate and wheels <= 2 tight; floor(n/2)).
Verification: agent proof; one referee subagent, 4 passes (final: CORRECT); exhaustive near-dichotomy |S|<=5,
SAT for the transfer up to |S|=7, cover-lemma SAT |S|<=7; Claude re-derived every lemma line by line
(near pairs, labelling admissibility, component claim, cover-lemma weight argument, cheap-deletion path,
schedule bookkeeping a_v+p_v = in-degree, wheel schedule, K_{2L}/K_{2L+1} reductions).
Consistency edits: abstract, Sec. 1.1 (main-result sentence, item (1), small families), Theorem F rewritten
(max(2,d), p+1, planar 4, 2-degenerate/wheels 2, floor(n/2)), discussion after Thm dense, near version of
thm:thick-intro, evidence paragraph, summary table, overview, Sec. 8 title/intro, cor:examples removed
(replaced by one sentence), new proof of Thm F after sec:nearloops, sec:leveled retitled and its fan / C_4
remarks corrected, cor:leveled(iii) (wheels <= 3) removed, rem:hublimits(1), SAT section, open problems 1-2.
Fallback (v3, dist >= 3 only) kept at dense2_claude/notes_claude/paper_insert_v3_refereed_claude.tex.

## M. Planar <= 3 (Claude, 2026-11-02 ~18:30)
New Theorem thm:degforest (in sec:nearloops): a union of a 2-degenerate graph and a-2 forests is a-good
(mark 2-degenerate edges absorbed, charge forest edges to the child; Lemma schedule at level a).
Planar: canonical ordering (de Fraysseix–Pach–Pollack 1990) splits a triangulation into D (u_1u_2 and the
two contour-endpoint edges of each u_k; 2-degenerate in reverse order) and F (edges to inner contour
vertices; each vertex covered once, so a forest) => planar <= 3 (was 4).
Computer check (planar3_claude/canon_check2_claude.py): 402 random triangulations up to n=120 + octahedron +
icosahedron satisfy the schedule hypotheses at level 3 with this marking.
Negative: C_12^2 minus {0,1},{6,7} (arboricity 2) has no level-2 cheap-deletion schedule
(planar3_claude/tight_search_claude.py), so "arboricity a => a" is not provable by these rules.
Updated: abstract, intro item (1), Thm F(a), table, cor:maxtwod(ii) and proof, thm:orient (planar claim
dropped as superseded), subsection title/intro, overview.
Referee (fresh subagent, 2026-11-02 ~18:45): thm:degforest CORRECT WITH MINOR FIXES (no math repair; own
checks: 3000 random D+forests instances with simulated cheap deletions, 330 triangulations via networkx's
canonical ordering, octahedron and K_4 by hand). Fixes applied: canonical-ordering statement made precise
(embedding, C_2, path in C_{k-1}-u_1u_2, one-line "never return" argument); parameter renamed a -> c and
d_v -> delta_v; arboricity remark no longer overclaims (only rules out two forests at level 2; arboricity 3 at
level 3 open, all random tests positive); counts "400 random triangulations with 5..120 vertices + 2";
abstract/intro "Hence ... wheels, planar, floor(n/2)" reworded as "refinements of the method"; cor:maxtwod proof
labels; ancillary files copied into q14paper_claude/ancillary/ (planar3_claude, nearloops_claude).

## N. Full-paper re-review of the integrated version (2026-11-02 ~19:00)
Verdict: WEAK ACCEPT (up from weak reject). No mathematical error in Sec. 8.7 (every proof re-checked).
Fixed: counting limit (new Remark nearlimits(3): any cheap-deletion schedule needs level >= max |E(H')|/|V(H')|,
so Thm orient is within one of the method's limit and Cor maxtwod(iv) is optimal for all n; replaces the
n <= 30 computer claim); block max degree Delta now gives ceil(Delta/2)+1 (was max(2,Delta); redundant min
removed); Cor maxtwod proof labels (K_4 = W_3, fans outerplanar); remark after degforest restricted to
cheap-deletion schedules; open problem 2 cites the counting limit; paid count renamed pi_v, K_{p,n} -> K_{q,n};
"near-cover lemma"; ceil(n/2) stated with floor(n/2) flagged as computer-assisted (abstract, item (1), table);
exceptions depending on n (Sec. 1.1, related work); 43 random six-function instances: "at most 3, and 2 when
2-degenerate or blocks <= 5 vertices"; cor:leveled no longer cites Thm H for triangles; Sec. 8.8 opening;
Thms C/D marked superseded for t=2; headings; "first bounds" softened.
Not done: writing out Steps 1-2 inside Lemma neardichotomy; cutting superseded leveled material.
- Near-dichotomy (lem:neardichotomy): Steps 1-2 now written out in full (no deferral to Lemma dichotomy); labelling parenthetical fixed for both X. (~19:05)
- Restructure (~19:25): SAT-evidence section moved to Appendix (sec:sat), references updated; Organization now points readers of the main result to Secs 2 and 8; roadmap paragraph at the start of Sec. 8.

## O. Real thresholds, six functions, K_5/K_6, sqrt(n) (dense3_claude, integrated 2026-11-02 ~23:50)
Source: dense3_claude/ (agent report frozen 23:43; one fresh referee: CORRECT WITH MINOR FIXES, 12 fixes applied).
Integrated (main.tex; backup scratchpad q14paper_main_before_dense3.tex):
- New Sec. 3.5 (sec:realc): Lemma lem:integrality (corner method at c < D proves D-1, from lem:cover);
  Thm thm:six: (a) every 2-sparse instance with <= 6 functions has disc <= 2; (b) K_5 = 3, K_6 = 4, K_8 >= 5
  (additive lower bounds: antipodal radius-1 covering of {+-1}^6 by 6 pairs; Hamming [7,4] code).
- Sec. 8.7: Thm thm:leveledsmall: leveled conjecture for <= 5 vertices and 6 vertices with <= 2 level-1
  vertices; => 8 functions <= 3; 3-core on <= 6 vertices => 2; 7-vertex patterns => 2 except K_7 minus a
  subgraph of C_4, 3K_2, K_3; star barrier for |I| = 3.
- Sec. 8.8 (now "Dense patterns", label sec:dense): Thm thm:sqrtnew: t-sparse => sqrt(2 ln(2t) n) (McDiarmid,
  weighted union bound; new bib entry McD89); pair barrier for the residual method (bundle >= 25).
- Consistency: abstract, intro items (1)-(2), small-families paragraph, after thm:dense, computational
  evidence (every SAT row is now a theorem), Table 1 (three rows), open problems 1/2/5, App. A (ancillary
  dense3_claude/ + new verification paragraph), App. B (table caption, final paragraph).
Lead's independent verification (dense3_claude/leadcheck_claude/, copied to ancillary):
- lower bounds K_6 >= 4, K_8 >= 5 and the pair barrier at k = 25: exhaustive exact check (scratchpad lb_check.py);
- thm:six(a): own pattern enumeration (Burnside 2,7,23,76,245,782), ORIGINAL ancillary cover_bnb.py at
  c = 299/100: all 1135 cleared (391 boxes j<=5, 1232 j=6; the C lists give 1256, representative-dependent);
  sanity: c = 199/100 fails on two functions sharing two items;
- thm:six(b): cover_bnb.py, K_5 at 3.99: 1,1,1,3,29 boxes; K_6 at 4.99: 1,1,1,1,3,15; K_4 at 2.99 fails (j=3);
- leveled: cover_bnb.py patched textually to per-function thresholds (and symmetry only for equal thresholds),
  own enumeration up to S_I x S_rest with Burnside: n <= 5, all |I|: 3966 patterns cleared;
- seven vertices: own schedule search (lead_seven_claude.py): exactly the same 8 exceptional graphs;
- n = 7 pattern lists of the agent: complete and duplicate-free (Burnside 2,7,23,78,264,915,3111).
Not adopted: thm:seven (<= 7 functions, no two sharing >= 7 items): paper-checker confirmation of the j = 7
patterns not complete at integration time; pattern "two functions sharing 7 items" unresolved; K_7; n = 8.
Lead re-runs finished (00:02): leveled n=6, |I|=1 and |I|=2 with cover_bnb.py: all patterns cleared except one
each that hit the 900 s limit without coordinate sorting (a level-1 and a level-2 function sharing all six
fractional items; the same problem for both); rerun with sort_coords (valid: all items have the same readers):
see leadcheck_claude/lead_leveled_pair6_sorted.log. The C program clears all (logs_claude/final/lev_n6_*).
K_6 at 3.99 (sanity): cover_bnb.py aborts at the time limit (j=6), the C program reports an uncleared box
(consistent with K_6 >= 4, proved by the construction). |I|=3 sanity: C run uncleared near uniform p.
Fresh referee of the integrated additions (00:05): CORRECT WITH MINOR FIXES; all applied:
7-vertex statement (literal reading included K_7) now "other than the eight graphs K_7-E(F)"; pair barrier
needs >= 25 functions (j <= n); range "n=12 and all n>=14" (n=13 false) and "Thm sqrtn(a) better for large n";
open problem 1 wording; counting-limit remark and open problem 2 qualified (bounded bases give an additive
gain, K_8 at 3 < p(K_8)=4); App. A counts per (n,|I|); |I|=0 and |I|=n cases named; computer-assisted labels in
intro (1),(2), Table 1 (three rows), evidence paragraph, App. B; tab:sat caption lists all six-function rows;
K_{2,5} citation harmonized (Thm F(b)); "per-function version of Lemma cover"; star barrier thresholds
l_v+0.99; exceptions list in Sec. 1.1; intro (2) now K_4=K_5=3, K_6=4; floor(sqrt(2 ln(2t) n)) via
lem:integrality; stray ancillary/small_n_check/__pycache__ removed; K7_D3.log annotated as unfinished.
Build: 54 pp, 0 overfull, readiness 13/13.
01:15: the sorted cover_bnb.py rerun of the hardest leveled pattern (level-1 and level-2 function sharing all six
fractional items) PROVED with 316 boxes (4205 s), the same box count as the C program
(leadcheck_claude/lead_leveled_pair6_sorted.log, lead_C_pair6_lev12.log). So both programs clear all leveled
patterns; App. A says so, and notes the sorting for this pattern.
