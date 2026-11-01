# Frozen first research test

Job: c015-imagebound-triage-104fc05d5d7d. This is an untested construction
and proposed proof route, not a theorem, a candidate, or an audit.

## Sequential queue plus reset clock

Parameters: k>=2, m>=2, ell_i>=2. States are a queue P={p_0,...,p_(m-1)}
and k disjoint clocks C_i={c_(i,0),...,c_(i,ell_i-1)}. Let
S={c_(i,0):1<=i<=k}, L=lcm(ell_1,...,ell_k), n=m+sum ell_i.
Alphabet {a,b}:

* a rotates P and each C_i by one.
* p_0.b=S; p_1.b={p_(m-1)}; p_j.b={p_(j-1)} for 2<=j<m.
* c_(i,ell_i-1).b=empty; every other clock state has b-image {p_0}.

This replaces the long deterministic excursion in the binary partial-DFA
example in Ryzhikov, arXiv:2405.19622v4, Section 5, by a simultaneous clock.
It is a proposed extension of known work; substantive novelty is unverified.

## Claims to prove or falsify first

1. Every singleton image under every word is empty, a singleton, or S.a^t.
   This is the proposed invariant for global k-image-boundedness; verify it
   on both letters, independently of per-letter outdegree.
2. Immediately after the first b, Q has image P union S. At subsequent
   b-boundaries every image has form T union S or T, with T subset P.
   Test potential |T|+1_(clock present). The proposed lemma is that a strict
   decrease can occur only when an existing S.a^t is killed by b, which
   requires t=-1 mod every ell_i. Thus each such decrease costs at least L
   letters since the preceding b. If valid this suggests a lower bound
   1+(m+1)L. Do not assume the potential lemma or mortality.
3. Establish mortality constructively, first under gcd(m,L)=1, rather than
   assuming bounded singleton images imply a global mortal word. Only if
   both directions hold should comparable pairwise coprime parameters be
   used to ask about an all-k Omega_k(n^(k+1)) family.

## Bounded exact test and stop rule

First independently reproduce evidence/check_clock_baseline.py controls
(3,5),(2,3,5),(3,4,5). Then test exactly the frozen queue family for
m in {2,3,4} and clock vectors (3,5),(2,3,5),(3,4,5): nine models,
at most 16 states each. Explore full singleton-image closure and the complete
reachable subset graph from Q, storing distances, transitions and witnesses;
at most 2^16 subsets per model. Check the proposed potential on every
reachable b-boundary transition, including the intervening a-run. A shortest
path witnesses any finite violation; an empty-unreachable claim requires
complete closure. No parameter growth if the invariant, potential, or
mortality fails: save the precise obstruction and reassess the route.

Finite survival of these tests is no all-parameter proof. An eventual exact
family still needs current-literature comparison against known clock/product
constructions and a substantive innovation assessment before any candidate.
