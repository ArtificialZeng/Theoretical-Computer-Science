# Fixed single-pump certificates are effectively checkable

Status: proved reduction to classical Presburger decidability; routine auxiliary
progress, not a solution of the frozen Wheeler-membership question. No novelty
or fresh mathematical acceptance is claimed. This settles only the verification
half of the internal first-test hypothesis; necessity and a computable template
bound remain unproved.

## Proposition

Given a finite deterministic subsequential transducer T, a target state q, nine
explicit input words x_i,y_i,z_i, and choices of peak/valley and increasing/
decreasing interval direction, it is decidable whether all four conditions in
c017-wheeler/evidence/first-test.md hold for EVERY integer n>=0, for
U_i(n)=x_i y_i^n z_i. Arbitrary empty output words are allowed. No Wheeler input
order assumption is needed just to verify a supplied certificate.

The decision procedure is a finite construction of sentences of ordinary
Presburger arithmetic followed by its classical decision procedure. A general
Presburger solver has not been run here; the reduction, not a solver result,
justifies this mathematical decidability assertion.

## 1. Finite-state output on a pumped input

For one triple (x,y,z), read x from the initial state. An undefined transition
immediately makes the proposed universal certificate invalid. Otherwise let
p_0 be the resulting state and let A_0 be the accumulated output. Iterating
the partial function F(p)=delta(p,y) either hits undefined, or enters a cycle.
An undefined iterate at index n gives a concrete invalid U(n).

In the cycle case compute its transient mu and period lambda>=1, the output A
while reading x y^mu, the output B from one whole lambda-step cycle, and, for
each 0<=r<lambda, the output C_r from y^r z starting at p_mu. Also check that
the state after this suffix is the proposed q. Failure at residue r gives
the concrete invalid index mu+r. Check the finitely many n<mu separately.

For every t>=0, deterministic output concatenation gives EXACTLY

    output(U(mu+lambda*t+r)) = A B^t C_r.

The middle word B can be empty. This identity follows by repeatedly traversing
the same state cycle, followed by the fixed residue path and z.

For three triples let mu=max(mu_i) and L=lcm(lambda_1,lambda_2,lambda_3).
For each residue 0<=r<L write

    mu+r = mu_i + lambda_i*h_i + r_i,  0<=r_i<lambda_i.

All h_i are nonnegative. On the common index n=mu+r+L*t, the ith output is

    (A_i B_i^h_i) (B_i^(L/lambda_i))^t C_(i,r_i).

Thus each output is a fixed prefix, one fixed powered word, and a fixed suffix
with the SAME parameter t. The inputs themselves have this form by using
prefix x_i y_i^(mu+r), repeated block y_i^L, and suffix z_i. For U_i(n+1),
increase the fixed input prefix exponent by1. This also handles an empty y_i.
The finitely many n<mu can be evaluated directly, including interval comparisons
with n+1. Every construction is finite and effective; L can be large, but no
polynomial-time claim is made.

## 2. Comparison of two powered words is Presburger-definable

For a parameterized word W(t)=P R^t Q define

    len_W(t) = |P| + |R|*t + |Q|.

For each output symbol c, the predicate Char_W(t,j,c) says that its zero-based
position j contains c. It is the disjunction of the following finite tests:

* j=a for a position a of P labeled c;
* |P|<=j<|P|+|R|*t and j-|P| congruent to a modulo |R|, for a position a of R
  labeled c; omit this entire branch when R is empty;
* j=|P|+|R|*t+a for a position a of Q labeled c.

Add 0<=j<len_W(t). Every coefficient and modulus is a fixed integer. Products
of two variables never occur, and no variable divisibility predicate is used.
Empty prefixes, periods and suffixes cause no difficulty.

Let PrefixEq(W,V,t,j) universally quantify a position h and require equal
characters for every 0<=h<j. Then W(t)<lex V(t) is the disjunction of:

1. len_W(t)<len_V(t) and PrefixEq(W,V,t,len_W(t));
2. there exists 0<=j<min(len_W(t),len_V(t)) such that PrefixEq(W,V,t,j) and
   Char_W(t,j,c), Char_V(t,j,d) hold for some fixed ordered symbols c<d.

This is a formula of ordinary Presburger arithmetic. Colexicographic comparison
is obtained by reversing the three fixed words:

    rev(P R^t Q) = rev(Q) rev(R)^t rev(P).

Reversal does not reverse the alphabet order. Strict inequalities use the above
formula; a reversed inequality swaps the two operands.

## 3. The complete fixed-certificate procedure

After the state/residue tests and finite transient checks in step1, construct,
for every residue r, the finite conjunction of Presburger formulas for the
two increasing input inequalities, the fixed two output peak/valley inequalities,
and the selected strict separation of the current and next input intervals.
Universally quantify t with the guard t>=0. Decide the resulting finitely many
closed sentences by Presburger quantifier elimination. Accept the supplied
certificate if and only if all sentences are true. Every step terminates and
each translation has been justified above, proving the proposition.

Classical dependency: D. C. Cooper, Theorem Proving in Arithmetic without
Multiplication, Machine Intelligence7 (1972), pp91-100, especially pp92-95 on
constant multiplication/divisibility and eliminating one quantified variable.
Primary text inspected 2026-11-01:
https://www21.in.tum.de/teaching/logik/SS16/Exercises/Cooper.pdf
Arbitrary nested quantifiers are handled from the inside using Boolean duality;
no efficient block-commutation optimization is required. Modern primary
quantifier-elimination reference: Haase etal, ICALP2024, DOI
10.4230/LIPIcs.ICALP.2024.142. No bound from its existential-only refinement
is applied to the mixed-quantifier formulas here.

## Remaining original gap

This does not prove that every non-piecewise-monotone reaching function has a
single-pump disjoint-turn certificate. It supplies no computable length bound
for a certificate and no termination argument for enumerating possible
certificates until one appears. Therefore the full source membership problem
is still unresolved, and this auxiliary routine consequence does not authorize
a manuscript under the user's policy.
