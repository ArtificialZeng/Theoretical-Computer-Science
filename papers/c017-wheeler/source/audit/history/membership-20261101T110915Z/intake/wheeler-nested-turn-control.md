# Infinite turns can still require only two monotone pieces

This is an exact countermodel to a proposed shortcut, not to the original
membership question. It passes even the usual input-consistency/initial-state
graph conventions, in addition to the frozen source's reaching-language order.

Take states s,p,r, initial state s, sole final state p, input alphabet 0<1,
and these defined input/output transitions:

    s --0/epsilon--> p
    s --1/epsilon--> r
    r --0/epsilon--> p
    p --0/0-------> p.

All other input transitions are undefined; the terminal output at p is empty.
Every state is accessible and coaccessible. The reaching languages are

    I_s={epsilon},
    I_p=Z union O,  Z={0^m:m>=1},  O={10^m:m>=1},
    I_r={1}.

They are totally ordered I_s<I_p<I_r; moreover every word of Z precedes every
word of O. The input graph has order s<p<r, input-consistent labels, and no
incoming initial edge. Thus no ambiguity between graph definitions is involved.

Accumulated output at p is

    f(0^m)=0^(m-1),   f(10^m)=0^(m-1).

On Z the colex input order increases with m, and f is nondecreasing. On O the
input order decreases with m, and f is nonincreasing. Z,O are disjoint convex
pieces in I_p. The other states have singleton reaching languages. Therefore
this transducer satisfies the FULL current-v3 Wheeler-transducer membership
property. Exactly two pieces are needed at p: 0<00<10 is a strict output peak.

Nevertheless, for every n>=0 the three words

    U1(n)=0^(n+1), U2(n)=0^(n+2), U3(n)=10^(n+1)

all reach p and satisfy U1<U2<U3, with outputs 0^n,0^(n+1),0^n: a strict peak.
They are obtained from the same fixed peak by appending the same p-loop 0^n.

Their endpoint intervals are strictly NESTED, not disjoint: the left endpoint
increases and the right endpoint decreases as n grows. Each peak interval
crosses the unique cut between Z and O. In fact every strict-turn interval
at p crosses this cut, so any two such intervals overlap. The largest disjoint
packing is exactly one even though infinitely many strict turns exist.

Consequently both shortcuts are false:

1. a strict turn at a cyclic state implies failure of piecewise monotonicity;
2. infinitely many strict-turn triples imply unbounded disjoint-turn packing.

Fixed-certificate condition4 (strict interval separation) cannot be omitted.
Discarding an arbitrary common post-merge suffix preserves the output signs
but can lose the essential interval-position information. This is directly
relevant to the remaining bounded-pair-path approach. Original membership
remains unresolved; no novelty or publication candidate is asserted.
