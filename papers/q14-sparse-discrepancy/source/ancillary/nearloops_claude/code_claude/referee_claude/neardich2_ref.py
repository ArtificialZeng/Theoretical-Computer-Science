"""Near-dichotomy with dist(P,N) >= 2 (insert v4), independent checks.
 Part 1: exhaustive for n = 2..5: every near-loop-free W, every split of the complement into
         P, N with dist(P,N) >= 2 (= unions of 1-step components of the complement):
         P or N near-thick (and not both, by the cover lemma).
 Part 2: random for n = 6, 7, 8: random maximal near-loop-free W (WLOG maximal: moving a corner
         of P or N into W keeps a counterexample a counterexample), all or random splits.
 Part 3: step-by-step check of the v4 proof on the coned complex K for random instances
         (n = 3..6): barycentre labelling well defined and admissible; the 'Components' claim;
         Gamma a tree; for every M-node D the hypothesis of lem:nearpairs (no near pair of corners,
         no c_q, c_{-q} both in D) and its conclusion (-D in one component Z of K-D; R = V(K)-Z has
         no corners r, r' with dist(r,-r') <= 1).
Run: python3 -I neardich2_ref.py
"""
import sys, os, random, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_neardich2.txt"), "w") if __name__ == "__main__" else None


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def check_splits(c, W, rng=None, maxsplits=4096):
    comp = c.components(c.full ^ W, c.ball1)
    k = len(comp)
    viol = both = 0
    if k <= 12:
        it = range(1 << k)
    else:
        it = [rng.getrandbits(k) for _ in range(maxsplits)]
    cnt = 0
    for bits in it:
        P = 0
        for i in range(k):
            if bits >> i & 1:
                P |= comp[i]
        N = (c.full ^ W) ^ P
        cnt += 1
        pt = not c.has_nearloop(c.full ^ P)
        nt = not c.has_nearloop(c.full ^ N)
        if not (pt or nt):
            viol += 1
        if pt and nt:
            both += 1
    return cnt, viol, both, k


def part1():
    for n in range(2, 6):
        c = Cube(n)
        st = dict(W=0, disc=0, splits=0, viol=0, both=0)
        t0 = time.time()

        def dfs(W, start):
            st['W'] += 1
            cnt, v, b, k = check_splits(c, W)
            if k >= 2:
                st['disc'] += 1
            st['splits'] += cnt
            st['viol'] += v
            st['both'] += b
            for x in range(start, c.N):
                W2 = W | (1 << x)
                if not c.has_nearloop(W2):
                    dfs(W2, x + 1)
        dfs(0, 0)
        log(f"Part 1 n={n}: near-loop-free W {st['W']}, with 1-step-disconnected complement {st['disc']}, "
            f"splits {st['splits']}, violations {st['viol']}, both near-thick {st['both']} ({time.time()-t0:.0f}s)")


def random_maximal_nlf(c, rng, start=0):
    order = list(range(c.N))
    rng.shuffle(order)
    W = start
    for v in order:
        if not (W >> v) & 1 and not c.has_nearloop(W | (1 << v)):
            W |= 1 << v
    return W


def part2(rng):
    for n, T in [(6, 3000), (7, 600), (8, 100)]:
        c = Cube(n)
        st = [0, 0, 0, 0, 0]
        maxk = 0
        t0 = time.time()
        for _ in range(T):
            W = random_maximal_nlf(c, rng)
            cnt, v, b, k = check_splits(c, W, rng, 512)
            maxk = max(maxk, k)
            st[0] += 1
            st[1] += (k >= 2)
            st[2] += cnt
            st[3] += v
            st[4] += b
        log(f"Part 2 n={n}: random maximal near-loop-free W {st[0]}, disconnected complement {st[1]}, "
            f"max #1-components {maxk}, splits {st[2]}, violations {st[3]}, both near-thick {st[4]} ({time.time()-t0:.0f}s)")


class ConedK:
    def __init__(self, n):
        self.c = Cube(n)
        c = self.c
        self.n = n
        self.squares = []   # list of corner tuples (a, b, a', b') with a,a' opposite? store set
        for i, j in itertools.combinations(range(n), 2):
            rest = [k for k in range(n) if k not in (i, j)]
            for vals in range(1 << (n - 2)):
                base = 0
                for t, k in enumerate(rest):
                    if vals >> t & 1:
                        base |= 1 << k
                corners = [base, base | (1 << i), base | (1 << j), base | (1 << i) | (1 << j)]
                self.squares.append(corners)
        self.sqindex = {frozenset(q): idx for idx, q in enumerate(self.squares)}
        N = c.N
        self.V = N + len(self.squares)
        adj = [set() for _ in range(self.V)]
        for z in range(N):
            for w in c.nb1[z]:
                adj[z].add(w)
        for idx, q in enumerate(self.squares):
            b = N + idx
            for z in q:
                adj[b].add(z)
                adj[z].add(b)
        self.adj = adj
        m = c.mask
        self.bar = list(range(N)) + [N + self.sqindex[frozenset(z ^ m for z in q)] for q in self.squares]
        for z in range(N):
            self.bar[z] = z ^ m

    def components(self, verts):
        verts = set(verts)
        seen = set()
        comps = []
        for v in verts:
            if v in seen:
                continue
            comp = {v}
            stack = [v]
            seen.add(v)
            while stack:
                u = stack.pop()
                for w in self.adj[u]:
                    if w in verts and w not in seen:
                        seen.add(w)
                        comp.add(w)
                        stack.append(w)
            comps.append(comp)
        return comps


def part3(rng):
    for n, T in [(3, 2000), (4, 2000), (5, 800), (6, 200)]:
        K = ConedK(n)
        c = K.c
        N = c.N
        fails = dict(welldef=0, admiss=0, comps=0, tree=0, hyp=0, concl=0, final=0)
        inst = 0
        nodes_max = 0
        for _ in range(T):
            W = random_maximal_nlf(c, rng)
            # random sub-W sometimes
            if rng.random() < 0.3:
                W &= rng.getrandbits(N) | rng.getrandbits(N)
            comp1 = c.components(c.full ^ W, c.ball1)
            bits = rng.getrandbits(max(1, len(comp1)))
            P = 0
            for i, C in enumerate(comp1):
                if bits >> i & 1:
                    P |= C
            Nn = (c.full ^ W) ^ P
            inst += 1
            lab = {}
            for z in range(N):
                lab[z] = 'P' if P >> z & 1 else ('N' if Nn >> z & 1 else 'M')
            for idx, q in enumerate(K.squares):
                a, b, b2, a2 = q   # a=base, a2 opposite; b, b2 opposite
                Wq = [z for z in q if W >> z & 1]
                opp = ((W >> a & 1) and (W >> a2 & 1)) or ((W >> b & 1) and (W >> b2 & 1))
                meetP = any(P >> z & 1 for z in q)
                meetN = any(Nn >> z & 1 for z in q)
                if opp:
                    L = 'M'
                elif meetP:
                    L = 'P'
                elif meetN:
                    L = 'N'
                else:
                    L = None
                if L is None or (meetP and meetN and L != 'M'):
                    fails['welldef'] += 1
                lab[N + idx] = L
            # admissible
            if any(lab[u] == 'P' and lab[w] == 'N' for u in range(K.V) for w in K.adj[u]):
                fails['admiss'] += 1
            # components claim
            for Lset, A in ((('M', 'N'), W | Nn), (('M', 'P'), W | P), (('M',), W)):
                kc = K.components([v for v in range(K.V) if lab[v] in Lset])
                qc = c.components(A, c.ball2)
                kcorners = sorted(sum(1 << v for v in C if v < N) for C in kc)
                if 0 in kcorners or kcorners != sorted(qc):
                    fails['comps'] += 1
            # Gamma tree
            nodes = []
            nodeof = {}
            for L in ('P', 'M', 'N'):
                for C in K.components([v for v in range(K.V) if lab[v] == L]):
                    for v in C:
                        nodeof[v] = len(nodes)
                    nodes.append((L, C))
            nodes_max = max(nodes_max, len(nodes))
            edges = set()
            for u in range(K.V):
                for w in K.adj[u]:
                    if nodeof[u] != nodeof[w]:
                        edges.add((min(nodeof[u], nodeof[w]), max(nodeof[u], nodeof[w])))
            if len(edges) != len(nodes) - 1:
                fails['tree'] += 1
            # nearpairs hypothesis/conclusion for each M-node
            for L, D in nodes:
                if L != 'M':
                    continue
                Dc = [v for v in D if v < N]
                near = any((d ^ (e ^ c.mask)).bit_count() <= 1 for d in Dc for e in Dc)
                barpair = any(v >= N and K.bar[v] in D for v in D)
                if near or barpair:
                    fails['hyp'] += 1
                    continue
                negD = {K.bar[v] for v in D}
                rest = [v for v in range(K.V) if v not in D]
                comps = K.components(rest)
                Zs = [C for C in comps if C & negD]
                if len(Zs) != 1 or not negD <= Zs[0]:
                    fails['concl'] += 1
                    continue
                Rc = [v for v in range(N) if v not in Zs[0]]
                Rset = set(Rc)
                if any(((r ^ c.mask) ^ (1 << i)) in Rset for r in Rc for i in range(n)) or \
                   any((r ^ c.mask) in Rset for r in Rc):
                    fails['concl'] += 1
            # final conclusion
            if c.has_nearloop(W | Nn) and c.has_nearloop(W | P):
                fails['final'] += 1
        log(f"Part 3 n={n}: instances {inst}, max #nodes of Gamma {nodes_max}, failures {fails} (all must be 0)")


if __name__ == "__main__":
    rng = random.Random(77)
    t0 = time.time()
    part3(rng)
    part1()
    part2(rng)
    log(f"total time {time.time()-t0:.0f}s")
    out.close()
