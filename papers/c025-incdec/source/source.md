# Frozen original: sharp deterministic incremental-decremental submodular ratio

Primary: Yann Disser, Max Klimm, Annette Lutz and Lea Strubberg,
Incremental-decremental maximization, Acta Informatica63 article31(2026),
DOI10.1007/s00236-026-00546-x; Section1 model, Table1 and Section5 pp20--21.
https://link.springer.com/article/10.1007/s00236-026-00546-x
The source asks to close the deterministic competitive-ratio gap for all
monotone submodular h,g, from2 to1+e/(e-1).

Given a finite ground set E and arbitrary normalized, nonnegative, monotone
submodular h,g on2^E, one deterministic algorithm chooses ONE permutation pi.
For EVERY k from0 to|E|, its prefix S_k is assessed by
 f(S_k)=h(S_k)+g(E\S_k), versus OPT_k=max_{|S|=k}f(S).
The exact original question is the optimal deterministic competitive constant:
find matching achievable and impossible ratios over this entire function class.
In the source's polynomial-oracle algorithm setting, an upper-bound algorithm
must use polynomially many value-oracle queries and polynomial computation.
TRIAGE must explicitly validate this computational reading against the source
infimum-over-algorithms definition; do not silently weaken a stronger source
question. The known structural lower2 and polynomial upper1+e/(e-1) are
baseline results, not new contributions. If a full2-competitive polynomial
algorithm is proved, it matches the existing lower bound and settles both
readings. A different sharp value requires matching upper and lower bounds.

A new partial upper improvement, a counterexample only to a proposed2-ratio
algorithm, a finite optimal permutation, a fixed-k static algorithm, randomized
expectations, gross-substitutes-only functions or the known equal-total case
is not full resolution. Unnormalized functions with nonnegative constant
baselines are handled explicitly by TRIAGE; no hidden negative values.
All original cardinalities, arbitrary unequal totals and source input access
remain in scope. Original_status is unresolved and candidate_kind none before
actual research. Only full resolution+substantive innovation+fresh review
permits a manuscript, under the shared STOC quality standard.
