"""Optional refinement of lem:schedule (suggested in the report): the proof's hypotheses hold
whenever l_v >= p_v + max(1, a_v) for all v and l_v >= p_v + 2 for every v incident with an
absorbed edge.  (All edges paid -> Theorem thm:Finst; all absorbed -> Theorem thm:maxtwod.)
Simulates the proof (cheap deletion of v_1 with J = absorbed neighbours) on random inputs.
The inheritance step needs care because v's earlier edges shrink; we just check all cheap-deletion
hypotheses along the whole run.  Run: python3 -I schedule_refined_ref.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schedule_orient_ref import rand_graph, ap_counts
HERE = os.path.dirname(os.path.abspath(__file__))


def run_hyp(n, order, edges, mark, level):
    lev = dict(level); alive = set(range(n))
    E = {frozenset(e): m for e, m in zip(edges, mark)}
    for h in order:
        nbrs = [u for u in alive if u != h and frozenset((h, u)) in E]
        J = [u for u in nbrs if E[frozenset((h, u))] == "A"]
        if any(lev[u] < 2 for u in nbrs) or len(J) > lev[h] or (J and lev[h] < 2) or lev[h] < 1:
            return False
        for u in nbrs:
            if u not in J:
                lev[u] -= 1
        alive.remove(h)
    return True


rng = random.Random(5)
bad = 0; T = 30000; strictly_weaker = 0
for _ in range(T):
    n = rng.randint(1, 12)
    edges = rand_graph(n, rng.uniform(0.1, 0.9), rng)
    order = list(range(n)); rng.shuffle(order)
    mark = [rng.choice("AAP" if rng.random() < 0.5 else "APP") for _ in edges]
    a, pp = ap_counts(n, order, edges, mark)
    incA = {v: any(m == "A" and v in e for e, m in zip(edges, mark)) for v in range(n)}
    level = {v: max(pp[v] + max(1, a[v]), pp[v] + 2 if incA[v] else 0) for v in range(n)}
    if any(level[v] < pp[v] + max(2, a[v]) for v in range(n)):
        strictly_weaker += 1
    if not run_hyp(n, order, edges, mark, level):
        bad += 1
msg = (f"refined schedule condition: {T} random inputs, hypothesis failures {bad} (must be 0); "
       f"inputs where the refined levels are below the lemma's p_v+max(2,a_v) somewhere: {strictly_weaker}")
print(msg)
open(os.path.join(HERE, "log_schedule_refined.txt"), "w").write(msg + "\n")
