# Exact obstruction to the local extension route

This refutes only the assertion that every reachable 2-good set has a 2-good
one-item extension. It does not refute complete-chain existence or the original.

Let E={a,b,c}, h=0. On four coverage atoms x,y,z,w with weights 5,3,4,1,
let a cover {x,y,z}, b cover {y,w}, and c cover {x}. This defines a normalized
nonnegative monotone submodular g. In subset bit order a=1,b=2,c=4, its exact
value table is [0,12,4,13,5,12,9,13]. For f(S)=g(E minus S),

| S | f(S) |
|---|---:|
| empty | 13 |
| a | 9 |
| b | 12 |
| a,b | 5 |
| c | 13 |
| a,c | 4 |
| b,c | 12 |
| a,b,c | 0 |

Thus OPT by cardinality is [13,13,12,0]. The prefix {a} is reachable and
2-good since 2*9>=13. Its only two extensions have values 5 and 4, and
2*5<12 and 2*4<12. Yet the order c,b,a has values 13,12,0, hence is a
complete 2-good chain. No such local dead end exists for n<=2, because every
proper reachable nonterminal set then extends directly to an endpoint or,
from empty, some optimal singleton. This three-item witness is size-minimal.

Independent exact check: code/verify_chain_evidence.py;
evidence/research-pass-1/independent-verification.json. The larger experiment
contains 122 dead-end sets in 10 inputs, including a scaled source family.
This diagnostic terminates the every-good-set-extension route. The surviving
full-scope direction is the actual-gain bidirectional construction described
in route-status.md; its 2-ratio assertion is still unproved.
