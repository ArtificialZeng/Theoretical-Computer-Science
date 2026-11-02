"""Referee utilities (independent code).  Corners of {+-1}^n are ints 0..2^n-1
(bit i set <=> coordinate i is -1, say).  dist = popcount(x^y), -z = z ^ (2^n-1).
Subsets of the cube are Python ints used as bitmasks over the 2^n corners."""
import itertools


class Cube:
    def __init__(self, n):
        self.n = n
        self.N = 1 << n
        self.mask = self.N - 1
        N = self.N
        self.ball1 = [0] * N   # closed ball radius 1 (bitmask over corners)
        self.ball2 = [0] * N   # closed ball radius 2
        self.nb1 = [[] for _ in range(N)]
        self.nb2 = [[] for _ in range(N)]   # 1 <= dist <= 2
        for z in range(N):
            for w in range(N):
                d = (z ^ w).bit_count()
                if d <= 1:
                    self.ball1[z] |= 1 << w
                if d <= 2:
                    self.ball2[z] |= 1 << w
                if d == 1:
                    self.nb1[z].append(w)
                if 1 <= d <= 2:
                    self.nb2[z].append(w)
        self.full = (1 << N) - 1

    def neg(self, z):
        return z ^ self.mask

    def negset(self, A):
        # {-z : z in A}
        r = 0
        a = A
        while a:
            low = a & -a
            z = low.bit_length() - 1
            r |= 1 << (z ^ self.mask)
            a ^= low
        return r

    def dilate(self, A, ball):
        r = 0
        a = A
        while a:
            low = a & -a
            z = low.bit_length() - 1
            r |= ball[z]
            a ^= low
        return r

    def components(self, A, ball=None):
        """components of the graph on A with adjacency given by ball (default dist<=2)."""
        if ball is None:
            ball = self.ball2
        comps = []
        rest = A
        while rest:
            low = rest & -rest
            comp = low
            frontier = low
            while frontier:
                new = self.dilate(frontier, ball) & A & ~comp
                comp |= new
                frontier = new
            comps.append(comp)
            rest &= ~comp
        return comps

    def comp_near_antipodal(self, C):
        """C contains z,w with dist(w,-z)<=1."""
        return (self.dilate(self.negset(C), self.ball1) & C) != 0

    def has_nearloop(self, A):
        if self.n == 0:
            return A != 0
        for C in self.components(A, self.ball2):
            if self.comp_near_antipodal(C):
                return True
        return False

    def has_loop(self, A, step):
        """A contains an antipodal step-path (step-loop): some component (adjacency
        dist<=step) contains a pair z,-z."""
        if self.n == 0:
            return A != 0
        ball = [0] * self.N
        for z in range(self.N):
            for w in range(self.N):
                if (z ^ w).bit_count() <= step:
                    ball[z] |= 1 << w
        for C in self.components(A, ball):
            if self.negset(C) & C:
                return True
        return False

    def has_generalized_loop(self, A, step, defect):
        """A contains a step-path z0..zk with dist(zk,-z0)<=defect."""
        ball = [0] * self.N
        balld = [0] * self.N
        for z in range(self.N):
            for w in range(self.N):
                d = (z ^ w).bit_count()
                if d <= step:
                    ball[z] |= 1 << w
                if d <= defect:
                    balld[z] |= 1 << w
        for C in self.components(A, ball):
            if self.dilate(self.negset(C), balld) & C:
                return True
        return False

    def bits(self, A):
        a = A
        out = []
        while a:
            low = a & -a
            out.append(low.bit_length() - 1)
            a ^= low
        return out


def code_max(n, d=3):
    """A(n,d): max size of a binary code with min distance d (brute force for small n)."""
    N = 1 << n
    best = 0
    # greedy-exact by DFS
    pts = list(range(N))

    def dfs(start, chosen):
        nonlocal best
        if len(chosen) > best:
            best = len(chosen)
        for i in range(start, N):
            if all((i ^ c).bit_count() >= d for c in chosen):
                if len(chosen) + (N - i) <= best:
                    return
                dfs(i + 1, chosen + [i])
    dfs(0, [])
    return best
