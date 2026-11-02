# STATUS (c026_claude) -- progress log

Folder: claude_stoc2027_claude/c026_claude/ (all work here; research/ untouched).

## Log
- 13:47 Start. Read c026 manuscript, audit (math.md, stoc-assessment.json), evidence (research-2), intake notes.
- 13:55-14:05 Read primary texts: BJS Thm 3.1 / Sec 5; CKS05 Lemma 1.1, Thm 2.1, Thm 3.1 (+ footnote 1), Thm 3.2;
  CKS13 Sec 3.3-3.4 (Lemmas 3.3, 3.4, 3.9-3.14, Thm 3.8).
- 14:05 Findings so far:
  * Main reduction verified. Simplification found: the sampling step, the small-k brute-force branch and
    randomness are unnecessary. Deterministic splitting of each commodity's flow into floor(x_i/eps) copies with
    eps = 1/(2k) (discarding x_i < eps) gives |A| = O(k^2) directly; charging uses only that a copy whose two
    endpoints are separated sends all its flow (>= eps) across the cut. No path needs to stay intact.
  * The CKS congestion-1 rounding: CKS05 Thm 3.1 is stated with a footnote saying the published clustering is
    insufficient; CKS13 Thm 3.8 is stated only for "nice" Raecke-tree instances, and its Sec 3.4 proof is
    partly sketched (node-disjointness assumed "for simplicity", weighted details omitted). Plan: write a
    complete self-contained proof for alpha-flow-linked terminal sets, using (i) a max-flow/min-cut
    "pseudocenter criterion" that replaces centers (Lemmas 3.9/3.12/3.13), (ii) a flow-preserving degree
    reduction so that clusters are vertex-disjoint, (iii) CKS-style tagging/pairing with full counting.
  * General decomposition (BJS Sec 5 question) follows: CKS05 Thm 2.1 form with log^{1+o(1)} k loss.
  * Weighted AON: obstruction identified (cut charge counts flow, not weight); not claimed.
- 14:10 Anand 2610.17237 checked via arXiv HTML: Thm 5.1 needs A: V -> R_{>=1} (every vertex weight >= 1, so |A| >= n);
  overhead O(log|A| loglog|A|). Sec 5 summary of App. C: A >= 0 allowed but overhead O(log n loglog n).
  => (c) k-dependent O(log k loglog k) NOT obtained; only conditional O(log n loglog n) corollary via App. C.
- 14:10 Further simplification: uniformize at granularity eps = F/(2k): at most 2k copy pairs, |A| <= 4k.
- 14:10 Nonuniform paired congestion-1 rounding (pi-flow-linked, pi(s)=pi(t), leaf terminals) follows from the
  uniform one by weight-copies + leaf bridges. Will be Corollary 3.2.
- 14:14 BJS Algorithm 1 inspected: LP + sweep cuts + deterministic neighborhood cover => deterministic.
- 14:14 Start writing main.tex.
- 14:20-14:27 Wrote main.tex (15 pp), compiled cleanly, checker all PASS. Snapshot -> referee_snapshot/.
- 14:27 Spawned ONE fresh referee (general-purpose subagent; only manuscript + 3 primary PDFs).
- ~14:46 Referee report received. Verdict: correctness "correct with fixable gaps", no mathematical error affecting
  the main theorem; every proof checked line by line. STOC recommendation: WEAK REJECT (expects reject on depth /
  novelty); suggests SOSA, short ICALP/ESA, or journal note. Required fixes: misattributions (AN-MCF origin
  = Chekuri-Mydlarz-Shepherd; CKS05 Lemma 1.1/2.2 credit; "max-throughput recomputation" wording), BJS usage
  caveats (phi vs phi/2, small |A|, unknown constant -> doubling search, determinism unverified), Thm 3.1 for
  arbitrary matchings, empty-set fallback, Anand remark conditional, s_i=t_i in Sec 6, basic path solution.
  Optional: simplify Thm 4.1 with integral weights A(s_i)=A(t_i)=d_i (no copy graph).
- Applying all fixes now.
- 14:47-14:55 Revision v2 applied (all referee "required changes"): new abstract/intro (attribution to
  Chekuri-Mydlarz-Shepherd, HHR03, CKS05 Lemma 1.1/2.2 credits, BJS "would immediately imply", honest
  contribution paragraph), BJS black-box conventions (unknown constant c0 -> doubling search, phi/2 factor,
  small |A|, determinism not claimed for BJS step), Lemma 2.4 generalized to weighted A, Theorem 4.1
  simplified to integral endpoint weights A(s_i)=A(t_i)=d_i (no copy graph; referee's optional suggestion),
  Thm 3.1 for arbitrary matchings + empty-set fallback, Anand remark explicitly conditional, Sec 6 fixes,
  Remark 5.2 basic path solution. Builds cleanly (16 pp), checker all PASS.
- 14:55 Weighted AN-MCF re-examined (flow scaling by w_i/W, capacitated BJS, profit classes): each attempt
  either loses the profit ratio or needs BJS for capacitated graphs with |A|-only overhead (not formally
  stated in BJS) -> not claimed. Anand Thm 5.1 (A>=1 everywhere) cannot give k-dependence (|A|>=n).
- 14:55 Starting computational check of Section 3 rounding (code/verify_rounding.py).
- 15:00 code/verify_rounding.py (full Section-3 algorithm + LP routability check) and code/verify_tagging.py
  (Lemmas 3.8/3.11/3.12 directly). Results: 200 mixed instances ALL PASS (branches Z1 153, Yb 41, I2 3,
  base 3); 40 k_simple instances ALL PASS (case beta exercised 6 times); 20000 lemma trials ALL PASS
  (criterion 7421, nesting 89, tagging 22). Logs: code/run_*.log.
- 15:03 Added Remark 5.3 (weighted AN-MCF: log^{2+o(1)} k via profit classes -- honest, extra log) and a
  "Computational sanity checks" paragraph in Sec 6.
- 15:04 k_big batch (30 instances, q up to 68) ALL PASS. Total 270 full-algorithm instances, all selected sets
  verified routable with congestion 1 by LP; case (gamma) / branch Y'_a never occurred (stated in paper).
- 15:06 FINAL: main.tex/main.pdf (16 pp) compile with latexmk, no undefined refs, no overfull boxes;
  stoc_ready_check_claude.py: all PASS. Referee verdict (on v1): correct with fixable gaps; STOC weak reject.
  All required fixes applied in v2 (v1 kept in referee_snapshot/). Honest venue: SOSA / short ICALP-ESA /
  journal note; STOC unlikely.
