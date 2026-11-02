"""Tests of the group-theoretic CCRA criterion on minimal representations.

Criterion (Theorem A of manuscript_v2_claude): for invertible minimal letter matrices,
f is CCRA-realizable iff the Zariski closure G of the generated group has
(i) identity component trigonalizable over Q and (ii) pairwise commuting unipotent elements.
Finite proxies used here:
 (T1) every sampled group element g has some power g^k (k<=24) with Q-split char. polynomial;
 (T2) unipotent Jordan parts of sampled group elements commute pairwise.
A failure of (T2) is an exact certificate of non-realizability (Prop. in Sec. 6);
a failure of (T1) for all k up to the true bound is a certificate as well.
"""
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import random
from fractions import Fraction as Fr
from wa import *

def letters_invertible(Ms):
    return all(len(M) == 0 or rank(M) == len(M) for M in Ms.values())

def random_group_element(Ms, Minv, rng, maxlen=6):
    letters = list(Ms)
    d = len(next(iter(Ms.values())))
    g = eye(d)
    word = []
    for _ in range(rng.randint(1, maxlen)):
        a = rng.choice(letters)
        if rng.random() < 0.35:
            g = mm(g, Minv[a]); word.append(a + "^-1")
        else:
            g = mm(g, Ms[a]); word.append(a)
    return word, g

def criterion(Ms, samples=25, seed=1, kmax=24, words_only=False):
    """Return (ok, info). ok=False with a certificate if (T1) or (T2) fails."""
    rng = random.Random(seed)
    if not Ms or len(next(iter(Ms.values()))) == 0:
        return True, "zero-dimensional"
    Minv = {a: inv(M) for a, M in Ms.items()}
    els = [([a], Ms[a]) for a in Ms]
    for _ in range(samples):
        w, g = random_group_element(Ms, Minv, rng)
        if words_only and any("^-1" in x for x in w):
            continue
        els.append((w, g))
    parts = []
    for w, g in els:
        k = power_splits(g, kmax)
        if k is None:
            return False, ("T1 fails", w)
        S, U = jordan_parts(g)
        parts.append((w, U))
    for i in range(len(parts)):
        for j in range(i + 1, len(parts)):
            if not is_zero(comm(parts[i][1], parts[j][1])):
                return False, ("T2 fails", parts[i][0], parts[j][0])
    return True, "consistent on %d elements" % len(els)
