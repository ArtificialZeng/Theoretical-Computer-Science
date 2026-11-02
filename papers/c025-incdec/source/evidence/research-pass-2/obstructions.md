# Exact obstructions to intermediate charging lemmas

These witnesses refute only the named stronger proof templates. They do not
refute the actual-gain algorithm, the ratio-2 chain assertion, or the immutable
original question. Full rational tables and tie-admissible maximal-gain traces
are in template-screen.json and comparator-screen.json. The separate checker
code/verify_pass2.py uses no numerical solver and verifies every pairwise
submodularity inequality, monotonicity, normalization, each maximal choice,
the positive gaps, and every output prefix's factor-2 inequality.

## Bounds on h alone are too strong

Take E={a,b_1,...,b_5}. There are five coverage features of weight 2/15;
a covers all five and b_i covers just feature i. Let g be modular with
c_a=1/3 and c_b=0. Hence H=2/3 and G=1/3.
A valid trace deletes a on the right (gain 1/3, tied with adding a), then
adds the five b's on the left (gain 2/15 each). At L={b_1}, O={a}, k=1,
the current maximum remaining gain is d=2/15 and f(L)=7/15. Thus

    h(O)+G-2f(L)=1/15 > 0;
    h(O)-f(L)-k d=1/15 > 0.

Both proposed h-only charging bounds are false. The actual comparator
objective is f(O)=2/3, so the desired factor-2 bound still holds.
The output's worst ratio is 10/7.

This scales to every m>=5: a covers m disjoint features of weight 2, each
b_i covers one, and c_a=m. The same R-then-L trace has prefix-one ratio
2m/(m+2), tending to 2, and both h-only templates have positive gap m-4.
This is a method-specific asymptotic family, not an impossibility family
for all algorithms: other orders can do better.

## Comparator loss is not bounded by G

Take E={a,b,c,d,e}. Give h the following weighted coverage features, written
as (covering items; weight): ({a,b};1/7), ({a,c};2/7), ({b,d};1/7),
({b,e};1/7), ({c};1/7). Give g one feature ({a,b};1/7).
The exact maximal-gain trace is L(a), R(b), L(c), L(d), L(e), with gains
3/7,1/7,1/7,1/7,1/7. At L={a,c}, T={a,c,d,e}, comparator O={b,c},
the tracked comparator O_i=(O union L) intersect T is {a,c}=L. Then

    f(O)=1, f(O_i)=5/7, G=1/7,
    f(O)-f(O_i)-G=1/7 > 0.

The cardinality excess |O_i|-|O| is zero. Thus neither ignoring that excess
nor merely bounding total comparator loss by the smaller endpoint budget
provides the desired telescoping proof. This output's worst ratio is 7/5,
so the original factor-2 goal is again unrefuted.

## Surviving coupled template and exact finite certificate

The weaker coupled kernel is f(O)<=f(L)+G+|O|d when |O|=|L|.
It was screened by 4148 numerical LPs at n=3..7 and a separately chosen
239-LP n=8 attack. No positive witness was found. Both screens are bounded;
the n=7 and n=8 trace regions are incomplete and numerical nonfindings do
not prove even finite nonexistence. The final trace-word entry may be partial.
All constraints include future maximal-gain comparisons, as permitted by the
assigned test; these screens do not establish a prefix-only certificate.

residual-dual.json is a 12-term, coefficientwise rationally verified proof
of this kernel for ONE six-item trace RLLRRL, L={1,2}, O={0,5}, and
current d=f({1,2,4,5})-f({1,2,3,4,5}). It uses future choices and does not
supply a uniform telescoping formula. The independently checked modular-side
analytic proof is in modular-side-lemma.md; arbitrary nonmodular g remains
outside that proof.
