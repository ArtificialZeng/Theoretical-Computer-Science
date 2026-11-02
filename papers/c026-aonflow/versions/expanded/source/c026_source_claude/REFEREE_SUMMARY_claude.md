# c026 (AN-MCF) - referee and verification summary (2026-11-02)

## Fresh referee subagent (on v1, given only the manuscript and the three primary PDFs)
- Correctness: "correct with fixable gaps"; every proof checked line by line; no error affecting the main theorem.
- STOC recommendation: WEAK REJECT. Reason: depth/novelty. The reduction is "routine once BJS Theorem 3.1
  exists" (BJS themselves say such a decomposition "would immediately imply" the conjecture). The self-contained
  rounding proof is a real service but follows CKS13 Sec. 3.4 step by step.
- Suggested venues: SOSA, short ICALP/ESA paper, journal note.
- Required fixes (all applied in v2): attribution of AN-MCF to Chekuri-Mydlarz-Shepherd; credit for CKS05
  Lemmas 1.1/2.2 and HHR03; BJS usage caveats (phi vs phi/2, small |A|, unknown constant -> doubling search,
  determinism of BJS not verified); Theorem 3.1 for arbitrary matchings + empty-set fallback; Anand remark made
  conditional; s_i = t_i case; basic path solution in the integer-capacity remark.

## Claude's own check of v2 (after the agent finished)
- Sec. 4 (decomposition): discretization, doubling search (j <= ceil(log c0), phi >= eps/(16 Gamma)), cut charge,
  degree-one property, Lemma 2.4 application and the final constant 3F/(128 Gamma(4k)) re-derived.
- Sec. 3 (rounding): Lemmas 3.3 (degree reduction), 3.4-3.5 (common distribution, assembly), 3.7 (criterion),
  3.8 (clusters), 3.9 (bad-bridge chain, tag edge), 3.10 (tagging), 3.11 (tree pairing), Claims 1-8 and the
  counting 23040 < 2^15 re-derived; Corollary 3.2 (pendant copies, lambda-rescaling, 9/2^22 >= 1/2^19) re-derived.
- BJS Theorem 3.1 statement, the A-respecting demand definition and Fact 2.1 (phi/2) checked verbatim against
  intake/primary/2602.15015-expanders.pdf; Conjecture 5.1 and the "would immediately imply" sentence confirmed.
- Not independently re-checked: correctness of BJS itself (used as a black box), CKS13 citations' page-level details.

## Computational checks (code/)
- verify_rounding.py: full Sec. 3 algorithm, LP-verified routability, 270 random instances, all pass.
- verify_tagging.py: Lemmas 3.8/3.11/3.12 on 20,000 random graphs, all pass.
- Case (gamma) / branch Y'_a never triggered in the full runs (stated in the paper).
