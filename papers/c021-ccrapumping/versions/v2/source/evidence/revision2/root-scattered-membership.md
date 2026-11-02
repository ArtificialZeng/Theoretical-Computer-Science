# Working algorithmic consequence: copyless recognition of scattered-word sums

UNACCEPTED extension of the same CCRA discovery. It depends on the unaccepted finite-control theorem in root-unipotent-generalization.md. It is not part of the current frozen claim, not a new open-problem admission, and not a separate paper. Obtain fresh mathematical/innovation review before inclusion in any manuscript.

The baseline one-state obstruction has since passed the actual local referee
d846876ce849. This does not accept the finite-control generalization or the
algorithm below. The original accepted packet remains unchanged.

## Proposed complete statement

Input: finitely many explicit words p over a finite alphabet Sigma and rational coefficients c_p. Let [w:p] be the number of scattered/subsequence embeddings of p into w, including [w:epsilon]=1. Define f(w)=sum_p c_p [w:p].

Proposed result: one can decide in polynomial time whether f has ANY finite-state copyless polynomial CRA over Q, with arbitrarily many registers. The answer is YES exactly when f is invariant under permutations of its input letters. On YES, one can construct a one-state Q-CCRA of polynomial size and with at most sum_p |p| registers. On NO, finite words with the same Parikh vector and different f-values are a checkable certificate. These claims need fresh audit; known commutativity testing is not itself a claimed innovation.

## 1. A promised-unipotent weighted representation

For one pattern p=p1...pl, use states0,...,l. For each a, put

    M_a=I+sum_{i:pi=a} E_(i-1,i).

Initial row e0 and final column el count embeddings: an accepting path ignores a position by a loop or advances once on the next required letter. A single transition never advances twice, including when adjacent pattern letters coincide. Block-direct-sum these representations, placing c_p on each block's initial row. Every letter and word matrix is upper unitriangular. After minimization, unipotence survives invariant subquotients. The zero function is handled separately.

Conditional on the finite-control unipotent theorem, f is CCRA-recognizable iff the minimal letter matrices commute, iff f is a commutative function. Thus the promise required in that theorem is automatic for this explicit natural input class, not an undecidable oracle assumption.

## 2. Exact polynomial-time decision and witness

It is unnecessary to construct a particular minimal basis. In the supplied D-dimensional weighted representation, compute a basis R of rows lambda M_u and a basis C of columns M_v gamma by standard invariant-span closure, retaining the actual words u,v generating chosen basis vectors. Both dimensions are at mostD. Test

    r (M_a M_b-M_b M_a) c=0

for every r inR,c inC,a,b inSigma. Exact rational linear algebra takes polynomially many operations with polynomial bit length: basis words can be chosen of length at mostD-1, and their matrices/entries have polynomially bounded bit length for the explicit input. This is the usual recognizable-series commutativity test and is credited as standard.

If a test fails, the retained words give

    f(uabv) != f(ubav).

These two words have equal Parikh vectors and length at most2D. If all tests vanish, the identity holds for every context by bilinearity. Adjacent swaps generate all permutations, hence f is commutative. The test covers zero/cancellation cases; a zero reachable or observable space yields YES.

Bit complexity: let B be the total binary encoding length of the rational
coefficients and D=sum_p(|p|+1). Each retained word has length at most D-1.
Within a pattern block, matrix entries count embeddings in such a word and
are at most 2^(D-1); reachable coordinates multiply these integers by one
input coefficient. A common denominator for the coefficients has at most B
bits. Thus the original candidate vectors have polynomial bit length.
Exact rank tests can use fraction-free elimination; Hadamard's determinant
bound makes the relevant minors have O(D(B+D+log D)) bits. The number of
candidate vectors and tests is polynomial in D and the alphabet size. This
establishes polynomial bit time, rather than merely a polynomial number of
unit-cost arithmetic operations. Factorials in the output construction
have O(D log D) bits; its disjoint counters and expression have polynomial
encoding size. This argument still needs the fresh extension audit.

## Actual new finite diagnostics, 2026-11-01 UTC

`root_scattered_check.py` was actually executed with seed20261102. It builds
the block weighted representation, computes exact reachable/observable
bases retaining actual words, tests adjacent commutators, extracts NO
certificates, and constructs/evaluates the YES copyless counter machine.
The companion JSON reports474 input instances, including rational negative
coefficients, cancellations, empty patterns, the zero function, and sums
of all distinct permutations of pattern multisets over binary/ternary
alphabets. Dimensions reach180. There are150 YES and324 NO cases;
33,980 direct pattern-count/weighted-value comparisons,11,712 YES-machine
comparisons and324 explicit equal-Parikh/different-value NO certificates
all pass. Every output register has exactly one operand occurrence, and
every update consumes each old register once. These diagnostics check the
algorithm/construction. They do NOT prove the universal finite-control
CCRA exclusion theorem on which the characterization depends, and are not
a fresh audit or manuscript authorization.

The new primary-source search additionally checked the University of Warsaw
seminar announcement “Pumping Sequence Families: An Inexpressibility Result
for Copyless Cost Register Automata,” Antoni Puch,17December2025. Its date
precedes the STACS2026 body and its abstract describes that joint pumping
work; it is not evidence of a later resolution of Example26. Searches for
copyless together with unipotent, scattered/subword, binomial and Parikh
did not locate an equivalent characterization in the bounded screen.
This is not an exhaustive priority certificate. Source:
https://mimuw.edu.pl/en/seminars/talk/pumping-sequence-families-an-inexpressibility-result-for-copyless-cost-register-automata/

## 3. Polynomial-size copyless synthesis on YES

Fix a total order onSigma. Let sort(w)=a1^n1...as^ns. By commutativity, f(w)=f(sort(w)). A pattern p can embed in sort(w) only if p is weakly increasing in this letter order. For such p the number of embeddings is

    product_a binom(n_a,m_(p,a)),

where m_(p,a) is the multiplicity ofa in p. Consequently, on YES,

    f(w)=sum_(p weakly increasing) c_p product_a binom(|w|_a,m_(p,a)).

For each retained pattern p, lettera, and j=0,...,m_(p,a)-1 allocate a distinct register x_(p,a,j), initially -j. Increment all copies for a when readinga; other copies retain their values. Output

    sum_(p weakly increasing) [c_p / product_a(m_(p,a)!)]
                              product_(a,j) x_(p,a,j).

The updates use each old register once; each final register occurs in exactly one monomial. The output and all updates are therefore copyless. Negative starts and rational coefficients are permitted over Q. Empty patterns contribute constants, including the constant/zero edge cases. The number of registers is at most the explicit total pattern length. Factorial-denominator bit lengths are polynomial in that length; no expanded monomial enumeration is needed. Thus synthesis is polynomial-size, not merely an existence argument.

## 4. Relation to the source witness

For binary words,

    sum_(positions i with wi=1) i = [w:1]+[w:01]+[w:11].

This is not commutative (01 and10 give2 and1). The general criterion therefore recovers the frozen sourceExample26 without pretending the known pumping formula is new. In contrast [w:01]+[w:10]=|w|_0 |w|_1 and [w:aa]=binom(|w|_a,2) are YES controls synthesized above. The general criterion rules out cancellation-assisted finite-control representations for every noncommutative rational linear combination in this class, not only this one witness.

## Required gate

First audit the finite-control transfer and original one-state obstruction. Then independently check the decision/witness dimension and bit bounds, sorted-word formula under rational cancellations, and the exact copyless synthesis. Assess significance against existing scattered-subword counting, recognizable-series commutativity, and copyless normal-form literature. Do not call the standard linear algebra or sorted-word evaluation independently new. This extension belongs in one coherent revision of the same CCRA paper if accepted, with all previous snapshots/attempts preserved.
