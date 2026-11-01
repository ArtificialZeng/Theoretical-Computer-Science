# Precise reading and triage scope

Provenance: `curvature-noise-triage-903fc47916c5`, triage, 2026-10-31
(Asia/Shanghai). The immutable original is `source.md`, SHA-256
`55e12bf5b8e7b5489014d1286ec0463b9bec718f4d5369b338c8e1403a6259cd`.
The original is a research question, not a conjecture already verified to be open.

## Original model

Let integers $n\ge k\ge2$ be given and $V=[n]$. A function
$f:2^V\to\mathbb R_{\ge0}$ satisfies:

* $f(\varnothing)=0$, $f(\{i\})>0$ for every $i\in V$;
* $f(A)\le f(B)$ whenever $A\subseteq B$;
* $f(A)+f(B)\ge f(A\cup B)+f(A\cap B)$ for all $A,B\subseteq V$.

Write $f(i\mid A)=f(A\cup\{i\})-f(A)$ for $i\notin A$. Its total
curvature is exactly

\[
 \kappa(f)=1-\min_{i\in V}
 \frac{f(i\mid V\setminus\{i\})}{f(\{i\})}\in[0,1].
\]

For a supplied $\epsilon\in[0,1)$, a valid oracle is a single fixed map
$g:2^V\to\mathbb R$ with

\[
 (1-\epsilon)f(T)\le g(T)\le(1+\epsilon)f(T)
 \quad\text{for every }T\subseteq V.
\]

Thus $g(\varnothing)=0$. The oracle need not be monotone or submodular.
It may have arbitrarily correlated errors across sets. It is fixed before the
algorithm's private random choices, and repeated queries give identical answers.
Queries may have any cardinality, including cardinality greater than $k$.
There is no marginal oracle and no independent resampling assumption.

The output $A\subseteq V$ must satisfy $|A|\le k$. Set
$\operatorname{OPT}(f,k)=\max_{|T|\le k}f(T)>0$. Approximation always means
$f(A)/\operatorname{OPT}(f,k)$, not $g(A)/\max_{|T|\le k}g(T)$.
The literal curvature promise is exact; algorithms for a curvature upper bound
are also admissible, and the proposed lower-bound family must have exact curvature.

## Algorithm and quantifier conventions

An algorithm knows $n,k,\kappa,\epsilon$, has access only to $g$, and may
choose queries adaptively. Deterministic guarantees quantify over every valid
pair $(f,g)$. A randomized expected guarantee $R$ means

\[
 \forall (f,g)\text{ valid},\qquad
 \mathbb E_{\omega}[f(A^{g}_{\omega})]
 \ge R(n,k,\kappa,\epsilon)\operatorname{OPT}(f,k).
\]

A randomized lower bound must instead say that for each algorithm there is a
fixed valid pair $(f,g)$, independent of its seed, with expected ratio at most
the stated bound. Expected bounds alone do not establish a high-probability
success threshold. Any such conclusion needs a separately stated probability
and ratio. A distribution over hidden instances is a proof device, not permission
to change the oracle during a run.

For this query-model triage, “polynomially many” means at most $C n^d$
queries for some constants $C,d$ fixed for each algorithm family. Arithmetic
cost and bit precision of oracle reals are not bounded. This convention must be
retained explicitly in later statements: the source does not prescribe a
bit-complexity model or a uniform dependence on $1/\epsilon$. The proposed
regime has $1/\epsilon=o(k)\le n$, so a polynomial query bound in both $n$
and $1/\epsilon$ is also polynomial in $n$ there. Never take a pointwise
supremum over arbitrary polynomial degrees at a fixed $n$.

## Full task versus proposed subsidiary target

The full task asks for the sharp joint approximation/query dependence on
$(k,\kappa,\epsilon)$, or a substantive sharp regime/separation. No complete
joint characterization is claimed. Endpoints $\epsilon=0$, $\kappa=1$,
$k=n$, small fixed $k$, and the transition $\epsilon k=O(1)$ are in the
original scope. In particular $k=n$ admits ratio 1 by outputting $V$.

The unaccepted seed proposes this narrower target: fix
$0<\alpha<1/2$, $\kappa\in[0,1)$, put $k_n=\lfloor n^\alpha\rfloor$,
and let $0<\epsilon_n<1$ with $\epsilon_n k_n\to\infty$. With
$\rho_n=(1-\epsilon_n)/(1+\epsilon_n)$, prove that every algorithm family
using at most $C n^d$ adaptive queries has a sequence of valid fixed instances
of exact curvature $\kappa$ with

\[
 \frac{\mathbb E f_n(A_n)}{\operatorname{OPT}(f_n,k_n)}
 \le \rho_n(1-\kappa)+o(1).
\]

Compare with the standard singleton method's deterministic guarantee
$\rho_n(1-\kappa+\kappa/k_n)$. This would be an additive asymptotic matching
statement, not a multiplicative relative-error characterization when
$\rho_n\to0$. It would leave the full original question unresolved.
The optional exact-curvature-1 dummy construction is outside the admitted first
test and must not be assumed valid without a separate proof.

## Nearest prior result, proposed delta, verifier

Horel--Singer, NIPS 2016, “Maximization of Approximately Submodular Functions,”
Section 3.2, Proposition 8 (printed p.8), gives
$(1-\kappa)\rho^2$ for the **noisy objective**. The later arXiv deposit is
2411.10949v1 (2024), whose Appendix D explicitly selects the largest noisy
singletons. Directly evaluating that known method against true $f$ gives
$(1-\kappa)\rho$; this elementary normalization is not a new contribution.
Their Section 2.1, equation (3), already contains the hidden capped-rank family
and the baseline-transcript indistinguishability method used by the seed.

Proposed delta: a sharp exact-curvature calibration and finite expected query
lower bound, extending to every sequence $\epsilon_n k_n\to\infty$ in the
specified sparse-cardinality regime. Verification route: prove global oracle
validity and curvature analytically; derive the hypergeometric leakage bound;
couple the adaptive randomized transcript; then verify the asymptotics and
screen for equivalent existing theorems. Finite checks are only falsification
evidence. Literature status is `status-uncertain`, with no novelty or recognized
open-problem claim. See `evidence/triage-literature.md`.

This lead is separate from the coverage paper and other selection entries.
No claim has been accepted, and no manuscript or PDF is authorized by triage.

## Research pass 1 handoff

Job `curvature-noise-research-5a09759394ef` supplies an analytic proof of the
specified finite inequality and sparse-cardinality asymptotic target in
`evidence/research-proof.md`. It also supplies exact finite checks, a primary
literature comparison, and explicit attack/scope records. This is a proposed
result-note contribution requiring the real fresh-referee gate; it does not
change the original reading above or establish mathematical acceptance.
The full original status stays unresolved. The singleton algorithm and its
normalization remain credited known ingredients. The proposed delta is the
matching calibrated query lower bound and its stated parameter regime.
