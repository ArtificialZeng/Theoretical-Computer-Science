# Frozen original: all-or-nothing flow, Conjecture5.1

Primary: Bansal, Jambulapati and Saranurak, Expander Decomposition with Almost
Optimal Overhead, arXiv:2602.15015v2 (28April2026), Section5, printedp13;
ICALP2026 article22. https://arxiv.org/abs/2602.15015v2

Original assertion: there is a polynomial-time log^(1+o(1))k approximation
algorithm for the all-or-nothing flow problem.

The source defines the problem here on an undirected unit-edge-capacity graph
and k terminal pairs: select as many pairs as possible and route one unit for
EACH selected pair, allowing splitting, with total load at most1 on every edge.
The target is one uniform polynomial-time algorithm for the whole input class.
No congestion augmentation or fractional admission credit is allowed. The
question is algorithmic and does not require that a particular LP or method work.
