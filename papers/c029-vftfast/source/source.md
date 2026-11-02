# Frozen precise efficiency target from the source's open challenge

Parter, Popova and Tzalik, New Fault-Tolerant (alpha,beta)-Spanners,
arXiv2610.33934v1 (24October2026), Theorem1.4 and Introduction printedpp4--5,
explicitly leaves improving the running time of its sublinear-multiplicative
stretch construction open. Primary https://arxiv.org/abs/2610.33934v1 .
The exact source passage is retained in the immutable primary PDF.

The frozen research question is the full POLYNOMIAL-TIME realization of
Theorem1.4's tradeoff: for every fixed delta in (0,1), construct, uniformly
over all unweighted graphs and all f,k, an f-VFT (O_delta(sqrt(k)),O_delta(k))
spanner with tilde-O_delta((f+1)^(1+delta)*n^(1+1/k)) edges in polynomial
time. This is an explicit precise target selected from the source's efficiency
challenge, not a claim that its prose states a separate polynomial-time
conjecture verbatim. Preserve this question unchanged during research.

The source's matching-size construction currently takes about f*n^sqrt(k)
time; its polynomial-f-overhead Baswana-Sen result is not the same nearly
linear dependence f^(1+delta). Classical polynomial-time PURELY multiplicative
VFT spanners are known and are not this target. Question1.2 of the source
is answered in that same paper and is not the new question.
