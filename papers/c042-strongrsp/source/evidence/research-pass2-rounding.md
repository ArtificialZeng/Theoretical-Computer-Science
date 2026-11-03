# Finite-precision static values: a finite-rank comparison

Job: c042-strongrsp-research-266844093669. Local proof record, not an
original-scope resolution or independent audit. Probabilities are supplied
finite rational laws; construction of conservative Poisson laws is still open.

## Rounded boundary oracle

Assume rho and M=1+rho and all supplied boundary prices are multiples of
h=2^-b; all are in [rho,M] and clock-monotone. In the pass-1 static solver,
round each edge candidate UP to the next multiple of h before comparing it
to a key. Initial tick candidates and overflow M already lie on the grid.
Let Z be the resulting table and Y the EXACT optimum for the same supplied
coefficient laws and boundary table, including failure on nontermination.
Let H=(2q+1)(|A|+1), a bound on the number of actions of the exact oracle's
realizing policy, established by same-layer pop rank and strictly increasing
clock layer. Then

    Y <= Z <= Y + H h.

**Lower bound.** Rounding preserves the tick-seed inequalities, so every
relaxation raw value after popping u is at least the popped value Z(u,i,j).
Upward rounding also preserves this inequality. Thus pop keys remain
nondecreasing. Selected zero-increment edges point to an earlier popped
vertex; other increments/ticks move upward in clocks. The selected policy
terminates within H actions on every outcome. For each selected action,
Z is at least the expected next Z (and at most that expectation plus h).
Backward substitution along this finite-rank policy proves its actual
expected payoff is at most Z, and hence Y<=Z. No infinite-horizon drift
assumption is used.

**Upper bound.** For every edge whose active predecessor settles earlier,
the stored key is at most the upward-rounded candidate, hence at most the
raw expectation plus h. Inactive predecessors are seeded in the same way.
For an active predecessor settling later, its final value and every higher
clock value are at least the current vertex's final value. Consequently the
raw expectation itself is already at least that current value. Self-loops
have the same property. Ticks satisfy the exact inequality. Therefore

    Z(state) <= E[Z(next state)] + h

for every action, with no residual at terminal states. Apply this inequality
along the EXACT optimum's finite-rank realizing policy, of horizon <=H.
Telescoping conditional expectations gives Z<=Y+Hh. Existence of this
finite-horizon optimum is supplied by the exact oracle; it is not an
assumption that every policy terminates rapidly. In particular zero cycles
and arbitrarily small positive tick probabilities cause no extra factor.

This avoids the intake proposal's stronger uniform expected-absorption
bound, which is unnecessary for this local value comparison. It neither
proves nor refutes that separate proposal. Finite rank is special to this
clock/tick/label-setting system; this is not a generic affine-MDP theorem.

## Propagation through offline recursion

Use H0=(2q+1)(n+1), choose alpha=1+zeta, and h<=zeta*rho/H0.
Since Y>=rho, the displayed local bound implies Y<=Z<=alpha Y.
All endpoint and boundary tables remain on the same dyadic grid under
pointwise clipping. First solve the two endpoints by the rounded oracle,
obtaining Z_0,Z_T. Set U_T=Z_T and U_0=max(Z_0,Z_T) coordinatewise.
Because X_T<=X_0, these endpoints have X<=U<=alpha X and U_0>=U_T.
Clock monotonicity is preserved by max. This avoids assuming the two
independently rounded endpoint solves are already time-monotone.

If depth-h endpoints have error factor beta_h=alpha^(2h+1), inactive prices
obey X_mid<=B<=alpha*beta_h X_mid. The exact boundary oracle has this same
factor by first hit; rounding adds at most another alpha. Clipping, with
the already-proved envelopes, therefore gives midpoint error at most
alpha^2*beta_h=beta_(h+1). Every estimate has error at most alpha^(2D+1).
Taking zeta=1/[16(2D+1)] gives alpha^(2D+1)<=16/15 by the same elementary
geometric-series bound. The nested-activity and potential proof is unchanged.
This controls value distortion only; RSP acceptance thresholds and resource
error still need complete constants and a conservative probability model.

## Charged implementation and intermediate encodings

Choose b by doubling a positive integer until 2^-b<=zeta*rho/H0; this uses
O(log(nqD/rho)) charged arithmetic/control steps, never a logarithm/floor of
an arbitrary edge weight. A bounded value in [rho,M] can be rounded up by
b+O(1) binary comparisons with dyadic midpoints, retaining the integer grid
index. This makes rounding a finite operation in the frozen comparison RAM.
The index has O(b) bits. With fixed dyadic rho, b=O(log(n+2)+log(q+2)+log(D+2)).

If joint edge probabilities are multiples of 2^-B, a candidate sum of at
most q^2+1 terms times b-bit labels has temporary numerator/denominator
length O(B+b+log(q+2)); all are rounded before becoming later DP labels.
Two separate B-bit clock laws give joint precision 2B, with the same bound
up to a constant. Persistent values use these b-bit grid labels throughout,
so repeated recursion no longer increases their denominator length.
This is conditional on finite supplied dyadic laws with polynomially bounded
B; it does not construct those laws from arbitrary real inputs. The
rounding overhead O(b) per candidate is permitted by the local polylog terms.

## Exact validation scope

`check_rounded_oracle.py` and `rounded-oracle-results.json` compare 25 q=2
fixtures at b=5,8,12 for all eight active-vertex subsets: 600 cases and
3,600 value/policy comparisons, including 603 strict rounding inflations.
All 6,864 Bellman-residual checks pass. Every selected policy's exactly
recomputed expectation is between the reference optimum and its rounded
label; its measured rank satisfies H. The reference evaluates 17,820
stationary policies, 240 with closed nontermination. The extra fixture
includes a 2^-40 probability and parallel alternatives. These finite rational
coefficient tests cover the value theorem; the encoding bound above is
specifically conditional on supplied dyadic coefficient laws.

`check_offline_composition.py` also runs four rounded offline sequences at
b=17 or 18. Its 1,230 midpoint-state comparisons check the exponent 2h+1,
the final 16/15 bound, grid membership, time/tick envelopes, and the unchanged
activity potential. There are 144 strictly inflated output entries. The
separate inherited-endpoint tests force both clipping directions; the four
rounded full sequences themselves do not force either clipping direction.
Finite tests support this proof record; they are not a probability
construction, independent referee, novelty judgment, or original resolution.
