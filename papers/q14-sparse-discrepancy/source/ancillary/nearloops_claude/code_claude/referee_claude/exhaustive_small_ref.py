"""Exhaustive checks for |S| = n <= 4 of
  (A) cover lemma (lem:nearcover): for all U, U or complement(U) contains a near-loop
      (monotonicity of 'contains a near-loop' reduces U cup V = cube to V = complement U);
  (B) near-dichotomy (lem:neardichotomy): for all W with no near-loop and all splits
      of the complement into P, N with dist(P,N) >= 3 (= unions of G_S-components of the
      complement), P or N is near-thick; also exactly one (by (A));
  (C) sharpness probes: dichotomy with dist(P,N)>=2; cover lemma with 1-steps; cover lemma
      with deficiency 0 (2-loops).
Run: python3 -I exhaustive_small_ref.py
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube


def run(n, log):
    c = Cube(n)
    N = c.N
    full = c.full
    t0 = time.time()
    nl = bytearray(1 << N)
    for A in range(1 << N):
        nl[A] = 1 if c.has_nearloop(A) else 0
    # (A) cover lemma
    bad_cover = [A for A in range(1 << N) if not nl[A] and not nl[full ^ A]]
    log(f"n={n}: subsets={1<<N}, with near-loop={sum(nl)}, without={(1<<N)-sum(nl)}; "
        f"cover-lemma violations: {len(bad_cover)}")
    # also with 1-steps and defect 1 (should fail for some n), and 2-steps defect 0
    if n >= 1:
        v1 = 0
        v0 = 0
        ex1 = ex0 = None
        for A in range(1 << N):
            B = full ^ A
            if A > B:
                continue
            if not c.has_generalized_loop(A, 1, 1) and not c.has_generalized_loop(B, 1, 1):
                v1 += 1
                if ex1 is None:
                    ex1 = (A, B)
            if not c.has_generalized_loop(A, 2, 0) and not c.has_generalized_loop(B, 2, 0):
                v0 += 1
                if ex0 is None:
                    ex0 = (A, B)
        log(f"   probe: partitions (up to swap) with neither side containing a (1-step,defect<=1) path: {v1}"
            f" e.g. {None if ex1 is None else [c.bits(ex1[0]), c.bits(ex1[1])]}")
        log(f"   probe: partitions with neither side containing a 2-loop (2-step, defect 0): {v0}"
            f" e.g. {None if ex0 is None else [c.bits(ex0[0]), c.bits(ex0[1])]}")
    # (B) near-dichotomy
    nW = 0
    nsplit = 0
    bad = 0
    boththick = 0
    bad2 = 0
    nsplit2 = 0
    for W in range(1 << N):
        if nl[W]:
            continue
        nW += 1
        comp = c.components(full ^ W, c.ball2)
        k = len(comp)
        for bits in range(1 << k):
            P = 0
            for i in range(k):
                if bits >> i & 1:
                    P |= comp[i]
            Nn = (full ^ W) ^ P
            nsplit += 1
            pthick = not nl[full ^ P]
            nthick = not nl[full ^ Nn]
            if not (pthick or nthick):
                bad += 1
            if pthick and nthick:
                boththick += 1
        # probe: dist(P,N) >= 2 (components w.r.t. dist<=1 adjacency)
        comp1 = c.components(full ^ W, c.ball1)
        k1 = len(comp1)
        if k1 <= 16:
            for bits in range(1 << k1):
                P = 0
                for i in range(k1):
                    if bits >> i & 1:
                        P |= comp1[i]
                Nn = (full ^ W) ^ P
                nsplit2 += 1
                if nl[full ^ P] and nl[full ^ Nn]:
                    bad2 += 1
    log(f"   near-dichotomy: W without near-loop: {nW}, splits checked: {nsplit}, "
        f"violations: {bad}, both near-thick: {boththick}")
    log(f"   probe dist(P,N)>=2 instead of 3: splits {nsplit2}, failures {bad2}")
    log(f"   time {time.time()-t0:.1f}s")
    return nl


if __name__ == "__main__":
    out = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_exhaustive_small.txt"), "w")

    def log(s):
        print(s)
        out.write(s + "\n")
        out.flush()
    for n in range(1, 5):
        run(n, log)
    out.close()
