# Working construction, research pass 1

Job: c022-spe-memory-research-5979be48ad66. This is an unreviewed research record.
Original scope/status: source.md, unresolved pending full validation.

Proposed theorem: every pure SPE in an arbitrary no-dead-end n-player Boolean
reachability arena has a pure SPE with exactly its payoff and at most n*3^n
vertex-update memory states per player.

Let X consist of reachable pairs x=(v,W), where W is the set of targets already
visited, INCLUDING the current vertex. Fix the assumed original SPE sigma.
Let P(x) be the set of full Boolean payoff sets of sigma-continuations after
all legal histories represented by x. P(x) is nonempty and finite, and all
p in P(x) contain W.

Two properties require proof/check:
1. For x owned by i, p in P(x), and ANY successor y, some q in P(y) has
   q_i <= p_i. Use an occurrence of x realizing p and its one-shot deviation.
2. Every x in X_p={x:p in P(x)} admits an infinite path within X_p whose
   union of visited-target bits is exactly p. Follow the corresponding
   original sigma continuation. In particular, the distance d_p(x) inside
   X_p to a vertex (u,p) is a finite natural number.

Choose a selector f_p(x) that decreases d_p by one when d_p>0, and stays
within X_p when d_p=0. This is an arbitrary vertex-dependent table, not
stored memory. It realizes payoff p from every x in X_p.

Memory: (W,p,j) with W subset p subset players and j a player; n*3^n states.
At current vertex v, W was accumulated STRICTLY BEFORE v. Form x=(v,W union
T(v)). Normalize incoming (p,j) to r=p if p in P(x), otherwise choose
lexicographically first q in P(x) minimizing q_j. Both next and up recompute
this normalization from the SAME incoming memory and current vertex.
Define next_i((W,p,j),v)=f_r(x), and
up((W,p,j),v)=(W union T(v),r,owner(v)). Initialize (empty,p0,1).
Thus no edge, previous vertex or expected successor is stored.

For every legal history, normalized r is in P(x). After any prescribed
move it remains r at the next vertex, and the rank realizes that promise.
After any one-shot move of current owner i, either r remains available,
or normalization selects q minimizing q_i; property 1 bounds q_i<=r_i.
At histories where player i loses, arbitrary unilateral deviations also
preserve normalized payoff bit i=0 along every step: other players follow
f_r and preserve r, while player i can only induce a reset to another label
with bit i=0. Since labels contain visited bits, target i is never reached.
This directly proves SPE after every legal history, if all definitions hold.

Next adversarial checks: implement finite label-set/rank construction and
an all-legal-history product verifier; test merging histories, already-visited
targets, empty/full payoffs, arbitrary branch choices, and non-credible-NE
controls. Independently reread the proof for hidden edge memory, history
selection and infinite-arena progress gaps. No candidate declared yet.
