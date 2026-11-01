# Exact source target, trace and objective distinction

Research job robust-stopping-research-cd75b220d422. Primary target:
https://arxiv.org/html/2603.29233v1#A4.SS2, Appendix D.2, following equation
(26). The only quoted prose from KF26 in this new revision dossier is:

> the optimal objective value equals the minimum feasible h

This ten-word excerpt identifies the exact inference under examination.
The section first defines the expected-cost objective, then describes a
feasibility check restricting every supported buy-day to g(t)<=h, and
identifies its minimum feasible level with that expected objective. That
inference is false even with an ideal support-feasibility checker. We make
no claim that all price-adjusted filling algorithms fail.

## Exact trace of the stated support prescription

Take b=3, r=1/2, p_1=2/5, p_2=3/5. Direct summation gives
 g(1)=3, g(2)=14/5, g(t)=8/5 for every t>=3, and K=rb=3/2.
For h<8/5 the allowed support is empty. For 8/5<=h<14/5 it is
{3,4,...}; every probability law there has moment at least 2>K.
Thus such levels are infeasible. At h=14/5 the allowed support is
{2,3,...}. The D.3-D.4 prefix saturation rule at day 2 gives
 f_2=(r*2)/(b-1)=1/2.
It consumes moment 1/2, leaving mass 1/2 and moment budget 1. The D.5
moment convention from Lemma 5.1 admits tail day 3 with exactly the needed
moment (3-1)/2=1. Completion yields f_2=f_3=1/2 and J=11/5.

Indeed this law is forced by the support prescription, not merely one
possible tie-breaking: the x=2 row imposes f_2<=1/2, while any law on
{2,3,...} has moment at least 2-f_2; the moment cap requires f_2>=1/2.
Equality forces all remaining mass onto day 3. This proves the minimum
feasible support level 14/5 and its unique feasible law, whose expectation
is 11/5. Neither number is the true global expected optimum 39/20.
The global certificate is g(t)>=3-(7/10)(t-1) at every t, attained exactly
at 1 and 3; it gives J>=3-(7/10)(3/2)=39/20, achieved by
f_1=1/4,f_3=3/4. The prefix rows for that law are (1/2,1/4)<= (1/2,1).
All statements concern the source's unbounded actual horizons.

## What a literal execution of published Algorithm 3 does and does not say

D.7 Algorithm 3 lines 9-16, on the singleton active interval s=e=2,
compute atom 1/2. Its line 12 updates mu to 1; line 15 leaves F=1/2;
line 16 resets mu to 1/2. These values are faithfully recorded by
`trace_kf_and_objectives.py`. Its line 26 scans forecast support points
 d_j>=b; here the forecast support is {1,2}, so that written candidate
set is empty, although feasible completion day 3 exists. D.5 also mixes
strict/non-strict tail ranges, while line 26 omits the +1 associated with
moment t-1; constant-cost tail segments need a zero-slope convention.
Consequently the text does not specify a unique consistent executable
implementation for this input. We do not report 11/5 as the literal output
of an unspecified implementation. It is the forced output of the minimum
raw-support prescription, and the trace of D.3-D.5 with Lemma 5.1's stated
indices. The exact literal fragment and ideal prescription are separately
labelled in `kf-and-objective-checks.json`.

## A globally certified objective-normalization separation

Take b=3,R=3/2,p_1=p_2=1/2. Expected-cost coefficients are
 g=(3,5/2,3/2,3/2,...).
The per-horizon expected-ratio coefficients are
 q=(9/4,3/2,1,1,...),
since the ratio objective weights the forecast by p_x/min(x,b). These
weights sum to 3/4; they are objective coefficients, not a new probability
forecast. The two global affine inequalities are

 g(t)+(3/4)(t-1)>=3,     equality only at t=1,3;
 q(t)+(1/2)(t-1)>=2,     equality only at t=2,3.

After t=3 both reduced costs increase strictly with t, so these are global
certificates. They respectively prove minima 15/8 and 5/4 under moment
cap 3/2. The first is attained by f_1=1/4,f_3=3/4, the second by
f_2=f_3=1/2; both obey all prefix rows. Their costs under the other
objective are respectively 21/16 (ratio) and 2 (cost). Strict reduced
costs and positive moment prices also prove that both optimizers are
unique. Thus even the optimizer, not just the scale of the objective,
changes. By contrast dividing J by the fixed positive E_p OPT only rescales
J and leaves its minimizers unchanged.

Run `python3 revision/trace_kf_and_objectives.py` for the exact saved trace,
all equalities and the unbounded-tail certificate check. This is proposer
reproduction evidence, not an independent referee report.
