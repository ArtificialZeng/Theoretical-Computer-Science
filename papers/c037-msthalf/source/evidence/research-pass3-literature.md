# Current primary-source comparison for the full-resolution proposal

Job c037-msthalf-research-d39900f29f79; checked 2026-11-02 UTC during pass 3.
This is the proposer's bounded literature screen, not a fresh novelty or STOC
assessment, and not a guarantee of priority.

## Nearest result, verified against the primary full text

Anand, Gupta, Jayaram, Lee and Vakilian, *Approximating Minimum Spanning
Trees in Metrics under Semi-Random Corruptions*, arXiv:2610.40594v1,
29 October 2026. [Primary record](https://arxiv.org/abs/2610.40594),
[primary HTML](https://arxiv.org/html/2610.40594v1). The fresh record lists
only v1 and identifies the paper as SODA 2027. Local input is
`intake/primary/2610.40594v1.html` and its extracted text.

- Definitions 2.1-2.3 match the unchanged source model: independent unordered
  pair marking; the adversary sees the metric and mask; arbitrary symmetric
  replacements; expected true tree cost; observations need not be metric.
- Theorem 1.4 (formal Theorem 5.3) gives O_p(log n) in the unrestricted
  replacement model for p<1/4. Theorem 1.5 gives an n/4 expected-cost lower
  bound for p>=1/2 against arbitrary randomized no-query algorithms.
- Lemma 3.2 supplies an all-unmarked comparison tree of expected constant
  cost on a high-probability repair event for fixed p<1, with the proof's
  high-probability bound stated for sufficiently large n. Our Section 2
  reconstructs the known repair idea and Section 4 uses its explicit failure
  formula, so small n does not rely on that asymptotic convention.
- Lemma 5.6 uses a common-good-neighbor charging argument. Many simultaneous
  charges imply bad-pair density tending to one half; comparing this to
  2p+2epsilon requires p<1/4. This is the specific limitation replaced here.
  It is not an information-theoretic barrier established by that proof.

The source's decrease-only theorem for all p<1 and its efficient results
do not directly apply to arbitrary post-mask increases and decreases.
The proposed algorithm remains computationally inefficient, as permitted by
the original information-theoretic question. It does not improve the source's
running-time guarantees.

## Earlier primary work and scope distinction

Bateni, Dharangutte, Jayaram and Wang, *Metric Clustering and MST with Strong
and Weak Distance Oracles*, COLT 2024, PMLR 247:498-550.
[Official proceedings](https://proceedings.mlr.press/v247/bateni24a.html),
[official paper](https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf),
[arXiv record](https://arxiv.org/abs/2310.15863).
The official record and the displayed metric-MST section were inspected.
The no-strong-query O(sqrt(log n)) algorithm there is for metric-preserving
weak observations. That assumption is absent from source.md. It cannot be
substituted for a full upper bound in the arbitrary replacement model.
The Anand et al. primary text also identifies the earlier logarithmic lower
bound for unrestricted corruptions. Our resolution does not require that
lower bound; no new claim about its exact p-range is submitted for review.

## Bounded searches actually performed

The exact current title plus threshold/half; exact identifier plus
improvement/corruption; minimum spanning tree semi-random corruption with
half/rectangle/interval packing; semi-random corruptions spanning 1/2;
corrupted MST rectangle approximation metric; and the four-author COLT
2024 oracle query were searched. Primary records returned the two papers
above. No primary equivalent establishing the entire p<1/2 upper bound
was identified. Secondary aggregators were not used to establish theorem
scope or novelty. This is a short current screen, not exhaustive coverage of
all recent preprints, conference versions, alternative terminology or
unpublished work.

## Specific proposed substantive difference

The main new assertion is a deterministic theorem for EVERY metric and
EVERY nonnegative weighted order: rectangle density eta at side size r,
together with domination on graph H, forces true path length at most
(320r/eta)(W+MST). A metric star among smaller overlapping intervals lets
one pick a forbidden endpoint from EACH larger interval; the resulting empty
rectangle contradicts density. Integrating a single overlap bound avoids
an extra logarithm from separate scales. It uses positive hereditary density
without requiring a same-vertex common neighbor for each original edge.

The observable rectangle certificate is uniformly feasible by concentration
of the random mask and the known repair benchmark. Its combination with the
packing theorem extends the SAME expected O_p(log n) objective through the
whole p<1/2 interval. This closes the threshold gap relative to the verified
p>=1/2 lower bound. This is more than the earlier two-level/ultrametric
diagnostics or a routine parameter substitution in Lemma 5.6: its decisive
geometric implication is absent from that proof and is proved separately
in the submitted packet. The author must still receive an actual fresh
correctness, novelty, significance and venue-level assessment. No numerical
acceptance chance, submission_ready label, or acceptance is claimed here.
