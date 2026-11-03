# Pass 2 adversarial reconstruction

Job c040-mstdecfull-research-e695ca56645f. Same proposer context, not a referee.
The full argument is research/quadratic-resolution-proof.md. No manuscript or
authored PDF was created. Old frozen proof and actual reviews remain intact.

## Decisive changed mathematical argument

The strengthened extraction charges retain the exact number of outliers:
immediate edges cost at most 2 beta H; late edges cost at most 12 beta Omega.
For a late edge, promotion starts at its least common cluster level j, and
the later promotion is k>j. Its selected endpoint is absent from the core
at level k-1, even if cores are nonnested. A point has at most two incidences
in the final path. Each level-cluster pair therefore gets at most twice
its actual outlier count, with no global r substitution. Repeated clusters
are distinct nodes by level. Empty-core clusters cause no intersection gap:
the common promoted cluster at level k has nonempty core by the endpoint
attaining k; its intersection with the other promoted core follows from
the size/budget argument, or from the full root core. Bottom singletons
are empty; the root is full.

At each intermediate scale, the carving loop emits only seed-generated
nonsingletons and leftover singleton clusters. Every old nonsingleton must
be selected or absorbed before the loop can stop. Hence the two category
bounds K_i<=1+W/t_i and N_i<=(R-1)(1+4W/t_i) cover every cluster, including
unchanged carried ones. Counting fewer than r outliers for each generated
cluster and one for each leftover gives O_i<=2R+5RW/t_i. Including the
bottom n and root zero, Omega<=14R(L+1)W. Together with the already proved
H bound this gives 50176 R(L+1)W in the normalized metric, instead of
50176 rR(L+1)W. The constant 10^15 q^-5 covers the full quadratic theorem.

## Real attempted falsification and scope

research/check_outlier_charges_pass2.py was written without importing the
old checkers. It generated 84 selected coalescent partition hierarchies on
n in {6,7,8,9,10,12,16}, heights 2..15, with repeated sets, independent
changing cores and empty cores. It varied b in {1,2,3,5} and B in
{b,b+3}; there were 2016 core assignments and six compatible DFS orders
per assignment. Exact integer shortest paths give the maximal metric
satisfying each core-diameter constraint. Every feasible true metric is
entrywise bounded by that constraint metric, by its triangle inequality.
The test checked intersection, promotion, immediate- and late-charge
multiplicities, the separate cost sums, and the retained bound itself.
All 12096 ordered cases and 105408 edges passed, including 51745 late
edges. There were 4357 changing repeated-core occurrences. Output is
evidence/outlier-charges-pass2.json. This changed finite domain is neither
exhaustive nor an all-n proof, and does not run the seed-carving algorithm.

No counterexample to the named retained-charge or category assertions was
found; their proof is the all-n argument, not the negative finite search.
The old rH estimate remains valid but loses a logarithm; it is not a failed
algorithm or a disproof of the immutable problem. No obstruction to all
algorithms is claimed.

## Whole original coverage reconstructed

The self-contained proof retains the mask rectangle concentration and
adaptive-adversary uniformity, seed-core bootstrap, exact quantile ranks,
all future tests, first absorption by old or fresh seeds, and at most one
representative change per level. It retains separate packing, observable
normalization, metric flooring and its factor two, the scale failure event
p^(n-1), unconditional bad-mask expectation, every-input spanning output,
aspect-independent every-execution quasipolynomial arithmetic/control-bit
bound, and zero private bits. Literal n=2, R>n, U=0 and p=0 cases remain.
The original source and precise problem have not changed.

## Remaining review obligations

No mathematical gap is currently identified in the proposed strongest
proof. A new actual freeze and fresh referee must check the whole theorem,
not inherit the old cubic acceptance. It must check present novelty and
substantive significance against the precise primary results. Adjacent
SODA full-text access remains limited. The short new estimate is an
accounting refinement of the same DFS method and must not be inflated into
an independent innovation. The actual previous working_paper assessment
is preserved; no new acceptance, invented referee, venue upgrade, counter
reset, manuscript or external contact is supplied by this research pass.
