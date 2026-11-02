# Independent necessity verification for c021 (written separately from the c021 agent)

Script: necessity_check.py (seeded). Random deterministic CCRAs over Q with 1–3 control states, 1–3 registers,
copyless updates mixing affine coordinate permutations, sums, products, merges, dropped registers (resets) and
constants; outputs copyless. Minimal representation by Hankel blocks (prefixes/suffixes ≤ length 4), validated
on all words ≤ length 7. For representations with invertible letter matrices (dim ≥ 2) we test necessary
consequences of the claimed criterion on random words u,v (length ≤ 3), with N = 12:
 (1) M_u^N has rational spectrum; (2) commutators of the M_u^N are unipotent; (3) unipotent Jordan parts of
 the M_u^N commute pairwise.
Controls: random invertible integer matrices.

Results (seeds 11–13, 60 trials each, ~2026-11-02 02:50 CST): 41 invertible CCRA instances, 41 pass, 0 failures.
Controls: 26 of 29 fail (irrational spectrum), confirming the tests discriminate.
Seed 12 earlier run (25 trials, older generator): 6 invertible CCRA, all pass; controls 8/9 fail.
Seed 14 (60 trials): 6 invertible CCRA instances, all pass; controls 5 of 5 fail (4 irrational spectrum,
1 non-unipotent commutator). Running total over seeds 11–14: 47/47 CCRA pass, 31/34 controls fail.
