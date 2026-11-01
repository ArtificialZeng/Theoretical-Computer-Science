# Known obstruction verified in the precise advice model

Job provenance: advice-matching-triage-5cc2f73291d9. This is a verification of
existing mathematics, not a candidate contribution or fresh referee report.

Take U={a,b}, V={x,y}, arrival order x,y, and the same advice
A={(a,x),(b,y)} in both inputs. Input G_good has edges ax,bx,by. Input G_bad
has edges ax,bx,ay. Both graphs are three-edge paths, have maximum degree two
on both sides, and have OPT=2. The advice is optimum in G_good; it remains a
valid injective advice table in G_bad, although by is absent there.
At x the entire revealed history and the entire advice table coincide.

Write p_a,p_b,p_0 for the probabilities of matching x to a, to b, or abstaining.
They are nonnegative and sum to one. Even with the best continuation at y,

    E ALG_good <= 2 p_a + p_b + p_0 = 1 + p_a,
    E ALG_bad  <= p_a + 2 p_b + p_0 = 1 + p_b.

Therefore E ALG_good + E ALG_bad <= 3. Applying consistency to the good
input and robustness to the bad input gives 2c+2r <= 3. Also, robustness on
both inputs implies 2r <= min(1+p_a,1+p_b) <= 3/2, hence r <= 3/4.
These are necessary conditions; no global achievability assertion follows.
Abstention and arbitrary correlated future random choices are covered by the
continuation upper bounds. The adversary selects a fixed input, not one that
reacts to an actual coin outcome. Taking disjoint copies gives the source's
even-n family, but n=2 already suffices for uniform guarantees.

For completeness, the routine advice-first greedy algorithm achieves (1,1/2):
at each arrival take its advised edge if present and free; otherwise match any
free neighbor if one exists. Its output is maximal, hence has size at least
OPT/2, for every advice table. When A is an optimum matching in G, every
offline endpoint used by A is matched by the algorithm at termination: an
endpoint free at termination would have been free when its advised owner
arrived, and that owner would have taken it. Thus the algorithm matches at
least |A|=OPT endpoints and is optimal. This argument covers partial optimum
advice and arbitrary arrival order. It does not need the degree restriction.
The sharp (1,1/2) endpoint is therefore routine, rather than a new result.

Primary equivalences: Choo et al., arXiv:2405.09784v3, Section 3 and Appendix A;
Jin--Ma, arXiv:2206.11397, Section 3.1, Proposition 3.1. The independent algebra
above avoids reliance on an apparent sign typo in the deterministic paragraph
of Choo et al.'s Appendix A. See literature/triage-sources.md for URLs.
