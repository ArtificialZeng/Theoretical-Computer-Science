# Additional working lemma: testing the all-word unipotence condition

UNACCEPTED same-project extension, not a new open-problem admission. This
elementary auxiliary lemma is not claimed as a separate innovation. The main
finite-control characterization remains subject to fresh mathematical review.

Let M_a be rational d-by-d matrices. Every M_w is unipotent if and only if
tr(M_w)=d for every word w. Necessity is immediate. For sufficiency, fix w.
For each j=1,...,d, the word w^j is also in the monoid, so
tr(M_w^j)=d. Newton's identities in characteristic zero determine all
elementary symmetric polynomials of the eigenvalues from these first d
power sums. They are therefore the coefficients of (T-1)^d. Cayley-Hamilton
gives (M_w-I)^d=0, proving unipotence. This step uses the trace condition
for ALL words, not just for the original letter matrices.

The trace condition has a polynomial-bit-time test. Form vectors
(vec(M_w),1) in Q^(d^2+1), starting with (vec(I),1). Right multiplication
by a letter is the linear operation (vec(X),c) -> (vec(X M_a),c).
Compute their invariant span by exact basis closure. The trace condition
holds exactly when the linear functional (vec(X),c) -> tr(X)-dc vanishes
on the resulting basis. A breadth-first basis can retain actual words of
length at most d^2, so every failed condition has a polynomial-length word
certificate. Entries of these bounded products have polynomial bit length
in d and the encoded input size. Fraction-free Gaussian elimination and
the determinant bound give polynomial bit complexity. This is simply a
constant-series equivalence test in a d^2+1 dimensional representation.

To make the condition intrinsic to a weighted function rather than to an
arbitrary redundant representation, first minimize the rational weighted
automaton by the standard reachable/observable quotient construction. Its
letter matrices are unique up to simultaneous similarity. The zero function
can be handled separately. The test then decides whether its minimal word
monoid is unipotent. It does not decide general CCRA recognizability outside
that sector. If the proposed finite-control theorem is freshly accepted,
the commutativity test gives CCRA membership inside this effectively
recognized sector. Polynomial-size synthesis is asserted only for the
explicit-pattern input representation in root-scattered-membership.md;
no polynomial-size synthesis claim is made for arbitrary compact weighted
representations.

`root_unipotence_check.py` and its JSON provide exact test controls; their
execution status and ranges are recorded in the JSON, not inferred here.
