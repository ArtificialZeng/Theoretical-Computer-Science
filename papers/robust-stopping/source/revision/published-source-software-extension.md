# Narrow published-source and software extension

Research pass 3, job `robust-stopping-research-024409e96ffb`.
This is a proposed extension requiring a new freeze and fresh referee.
It does not alter the mathematical core previously accepted at snapshot
`16612a3cefda20c6efcd422319de1c7c33a069858cbf520c875c4612c7ef6b36`.
The original general-frontier task remains unresolved.

## Version and source binding

The [official PMLR page](https://proceedings.mlr.press/v306/kim26l.html)
identifies Jihwan Kim and Chenglin Fan's *Robust and Consistent Ski Rental
with Distributional Advice*, ICML 2026, PMLR 306:57411--57444. The page's
Software link leads to
<https://github.com/JihwanKim4689/distributional-ski-rental>.
Both links were read in this pass; the commit-specific GitHub tree URL
was unavailable to the web fetcher, so local Git object verification is
recorded separately rather than claiming that that URL was retrieved.
The PDF itself also links this repository in its printed-page-8 footnote.

The complete local published PDF is
`literature/kf26-published-complete.pdf`, 560,062 bytes, 34 pages, SHA-256
`5c5842ff3d0d2df8b802bc9968d520410ade6a059f83b3ca9fb1ac6a8f53ec4c`.
The incomplete similarly named PDF is excluded. A fresh `pdftotext -layout`
extraction in `kf26-published-pass3-extract.txt` matches the earlier primary
extraction byte for byte. The native official BibTeX record and download
provenance are included as source evidence, not mathematical acceptance.

Printed page 7, Sections 5.1--5.2, specifies the same discrete cost
`C_t(x)=x` for `t>x`, otherwise `b+t-1`, the constraint at every integer
actual horizon, and the linear forecast expected-cost objective. Appendix
D.1, printed page 29, gives the same deterministic-threshold cost `g`.
Appendix D.2 starts the expected-cost program at equation (26) on page 29;
on page 30 it identifies its optimum with the smallest level allowing a
robust probability law supported on `{t:g(t)<=h}`. The already-used short
excerpt “the optimal objective value equals the minimum feasible h” locates
the precise inference. No equality of the entire arXiv and published papers
is asserted. The counterexample below concerns this particular inference,
including an ideal support-feasibility checker, independently of code.

## Exact counterexample under the published model

Set `b=3`, `R=3/2`, and `p_1=2/5,p_2=3/5`. Then

    g(1)=3, g(2)=14/5, g(t)=8/5 for t>=3,
    E(T-1)<=3/2.

For every positive integer `t`,

    g(t)+(7/10)(t-1)>=3.

The reduced costs at `t=1,2,3` are `0,1/2,0`; for `t>=3` they
increase by `7/10` per day. Consequently every robust law has
`J>=3-(7/10)(3/2)=39/20`. The law `f_1=1/4,f_3=3/4` attains the
bound. Its direct costs at horizons `1,2,3` are `3/2,9/4,9/2`;
for every `x>=3` the cost remains `9/2`. Thus it satisfies the
unbounded robustness quantifier. The strict reduced costs and positive
moment price also force this optimum to be unique.

If `h<14/5`, every allowed buy-day is at least 3 (or the allowed set
is empty), so any normalized allowed law has moment at least 2 and
cannot be robust. At `h=14/5`, only days `2,3,...` are allowed. The
early horizon-2 inequality is `2 f_2<=1`, while the moment is at
least `2-f_2`. The cap `3/2` therefore forces `f_2=1/2`; equality
forces all remaining mass to day 3. This law is robust and has cost
`11/5`. Hence the minimum feasible raw support level is `14/5`, its
unique feasible law has expected cost `11/5`, and neither quantity is
the expected-cost optimum `39/20`. This proves that the identified
published D.2 inference fails in its own model.

## Actual finite software observations

The local checkout is pinned at commit
`0a86125f31e9e1b1abbba5bd4fde32a332860124`.
The two source hashes are:

| Source file | SHA-256 |
| --- | --- |
| `Figure1_Performance_Comparison_Under_Prediction_Error.py` | `a63482866e819cb695298aae494b792d1babb0679b31c851dd68c0f6e23018a3` |
| `Table2_Consistency_Comparison_under_Fixed_Robustness.py` | `f906417295005ffc8aeda7e3868350e9498acaf61d1876b7a23d27a2d9733b81` |

I inspected both class definitions and ran the existing owned wrapper
`reproduce_author_code.py` afresh, saving
`kf26-author-code-pass3-wrapper.json`. I then wrote a separate class
loader and checker, `verify_published_extension.py`, without importing
the wrapper. Both loaders compile and execute only each unchanged
`SkiRentalOptimizer` AST class node, supplying `math` and `bisect`.
No top-level experiments, plots or third-party imports are executed.

For each file and each tolerance `1e-5,1e-9,1e-12`, the literal arguments
are `(3,1.5,[1,2],[.4,.6])`. `solve` followed by
`construct_policy_pmf` returns exactly binary-representable masses
`f_1=1/4,f_2=f_3=3/8`. The returned water levels are, respectively,
`3.000001907348633`, `3.0000000004656613`, and
`2.9999999999995453` for both files. At these tolerances this is a
finite floating-point observation; no limit or all-tolerance theorem is
claimed. The last level being slightly below 3 reflects the literal
numerical predicates and is not an exact support-level certificate.
Both loaded classes return `False` for `is_feasible(14/5)` and `True`
for `is_feasible(3)` in these actual calls.

The independent checker converts returned floats with `Fraction(value)`
directly, without rounding or denominator fitting. It evaluates their
law exactly under the intended rational forecast `(2/5,3/5)` and the
original cost. The moment is `9/8`, the forecast cost is `12/5`, and
the raw support-cost maximum is 3. Direct horizon costs are `3/2,3,33/8`
at `x=1,2,3`; for every `x>=3`, the cost is `33/8<=9/2`. This verifies
true robustness without relying on the software's internal `mu`.

| Law's meaning | `(f_1,f_2,f_3)` | `J` | `E(T-1)` | Raw support maximum |
| --- | --- | --- | --- | --- |
| Global expected-cost optimum | `(1/4,0,3/4)` | `39/20` | `3/2` | `3` |
| Minimum raw-support-level law | `(0,1/2,1/2)` | `11/5` | `3/2` | `14/5` |
| Observed pinned software output | `(1/4,3/8,3/8)` | `12/5` | `9/8` | `3` |

The expected-cost/support-level distinction is an exact result. The last
row is a finite observation about the stated files and calls. In
particular, `11/5` is not the observed software output.

## Literal execution trace and a correction to the informal handoff

`published-extension-checks.json` records actual Python line/return events
for both files' `is_feasible` at `14/5` and 3, and
`construct_policy_pmf` at 3. Each line-event state is the state *before*
the reported line; each return-event state is final locals. The trace
does not change either class or replace floating arithmetic by rationals.
Displayed fractions exactly encode the observed binary values.

At `h=14/5`, `is_feasible` skips day 1, adds `1/2` at day 2 with
internal `mu=1`, then adds `1/4` at day 3. It reaches only `F=3/4`
and `mu=7/4`; the scan of forecast support points strictly above `b`
has no candidates, and it returns `False`. The ideal feasible
`(0,1/2,1/2)` law is therefore not recognized in this call.

At `h=3`, `is_feasible` reaches day-1 mass `1/4`, adds `3/8` at
day 2 and `3/8` at day 3, and returns `True`. Its internal final
`mu=15/8` is not the true moment of the returned policy.

The construction method takes a distinct path. After day 2 it resets
internal `mu` to `3/8`; at day 3 it initially adds `9/16`, reaching
`F=19/16`. Its existing normalization correction then subtracts `3/16`
from the day-3 mass, yielding the observed final `3/8`. Its final local
`F` remains `19/16`, and `mu=33/16`; neither is used as the law's
original-model certificate. The informal earlier handoff's summary
that day 3 simply adds `3/8` describes the final mass but omits this
construction overshoot and correction. The new literal trace supersedes
that intermediate-state shorthand, without changing the final output.

## Reproduction, limits, and handoff

Run from the project root:

    python3 -B revision/reproduce_author_code.py literature/kf26-official-code
    python3 -B revision/verify_published_extension.py

The second script expects the complete PDF and its saved extraction in
their research-input locations. It prints checks without overwriting any
evidence by default. Optional `--output` writes only the chosen result.
These are proposer computations, not a fresh referee pass.

No new uniform-frontier, complexity, priority or general implementation
claims are introduced. All prior core frozen evidence remains unchanged.
The original task remains unresolved, and a new combined snapshot and
fresh referee are required before writing. Packaging must omit the
unlicensed third-party Python and fulltext inputs; deliver the owned
wrapper/checks, source links and hashes, with optional checkout
instructions. The later default offline reproduction must use owned
algorithms and exact saved witnesses, without requiring this checkout.

Known proof gaps in this narrow proposed extension: none identified.
External fresh review is still pending. The code observations have only
the explicitly stated finite scope, and exact evaluation of those laws
does not upgrade floating software behavior to a universal theorem.
