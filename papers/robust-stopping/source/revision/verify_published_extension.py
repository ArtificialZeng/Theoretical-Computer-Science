#!/usr/bin/env python3
"""Finite, independent KF26 reproduction and direct original-model checks.

Only the unmodified class AST is executed. No benchmarks, imports from the
third-party modules, network calls, or source modifications are performed.
The supplied checkout is a research input, not a redistributable dependency.
"""
import argparse
import ast
import bisect
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

JOB = "robust-stopping-research-024409e96ffb"
COMMIT = "0a86125f31e9e1b1abbba5bd4fde32a332860124"
PDF_HASH = "5c5842ff3d0d2df8b802bc9968d520410ade6a059f83b3ca9fb1ac6a8f53ec4c"
SOURCES = {
    "Figure1_Performance_Comparison_Under_Prediction_Error.py":
        "a63482866e819cb695298aae494b792d1babb0679b31c851dd68c0f6e23018a3",
    "Table2_Consistency_Comparison_under_Fixed_Robustness.py":
        "f906417295005ffc8aeda7e3868350e9498acaf61d1876b7a23d27a2d9733b81",
}
FORECAST = {1: Q(2, 5), 2: Q(3, 5)}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    """Encode actual binary values exactly, never via rational fitting."""
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float, Q)):
        return str(Q(value))
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


def model_cost(t, x):
    return x if t > x else 3 + t - 1


def g(t):
    return sum(p * model_cost(t, x) for x, p in FORECAST.items())


def verify_law(law):
    assert all(isinstance(t, int) and t >= 1 and q >= 0
               for t, q in law.items())
    assert sum(law.values()) == 1
    moment = sum(q * (t - 1) for t, q in law.items())
    cost = sum(p * sum(q * model_cost(t, x) for t, q in law.items())
               for x, p in FORECAST.items())
    # Direct horizon checks through the largest support day, then an exact
    # constant-tail proof for every later integer horizon.
    tail_start = max(3, max(law))
    horizon_costs = {
        x: sum(q * model_cost(t, x) for t, q in law.items())
        for x in range(1, tail_start + 1)
    }
    assert all(c <= Q(3, 2) * min(x, 3)
               for x, c in horizon_costs.items())
    assert 3 + moment <= Q(9, 2)
    assert horizon_costs[tail_start] == 3 + moment
    prefix = {
        x: sum((3 + t - 1 - x) * q for t, q in law.items() if t <= x)
        for x in (1, 2)
    }
    assert all(prefix[x] <= Q(x, 2) for x in prefix)
    return {
        "law": encode(law), "normalization": "1", "cost": str(cost),
        "moment": str(moment), "prefix_rows": encode(prefix),
        "direct_horizon_costs": encode(horizon_costs),
        "constant_cost_for_all_x_ge": tail_start,
        "constant_tail_cost": str(3 + moment),
        "raw_support_maximum": str(max(g(t) for t, q in law.items() if q)),
    }


def call_with_trace(method, h):
    code = method.__func__.__code__
    events = []
    previous = None
    fields = ("s", "e_i", "F", "mu", "mass", "pmf", "remaining_prob",
              "remaining", "start_idx", "max_allowed_d", "total")

    def tracer(frame, event, arg):
        nonlocal previous
        if frame.f_code is not code:
            return None
        if event in ("line", "return"):
            state = {k: encode(frame.f_locals[k]) for k in fields
                     if k in frame.f_locals}
            if state != previous or event == "return":
                item = {"event": event, "source_line": frame.f_lineno,
                        "state_before_line_or_at_return": state}
                if event == "return":
                    item["returned"] = encode(arg)
                events.append(item)
                previous = state
        return tracer

    assert sys.gettrace() is None
    sys.settrace(tracer)
    try:
        result = method(h)
    finally:
        sys.settrace(None)
    return result, events


def verify(project, checkout):
    pdf = (project / "literature/kf26-published-complete.pdf").read_bytes()
    assert len(pdf) == 560062 and digest(pdf) == PDF_HASH
    assert pdf.startswith(b"%PDF-") and pdf.rstrip().endswith(b"%%EOF")
    extracted = (project / "revision/kf26-published-pass3-extract.txt").read_bytes()
    prior_extract = (project / "revision/literature-audit/classical-kf26-published-source.txt").read_bytes()
    assert extracted == prior_extract
    pages = extracted.decode().split("\f")
    assert len([p for p in pages if p.strip()]) == 34
    # Locate the already-frozen short excerpt rather than adding a second
    # prose quotation. Equations and their interpretation are checked in the
    # accompanying argument against printed pages 7 and 29--30.
    fragment = "the optimal objective value equals the minimum feasible h"
    assert fragment in " ".join(pages[29].split())
    assert "5.1. Equivalent Conditions for Robustness" in pages[6]
    assert "5.2. Optimization of the Stopping Distribution" in pages[6]
    assert "D.2. Step 2:" in pages[28]
    records, traces = [], []
    for filename, expected_hash in SOURCES.items():
        path = checkout / filename
        raw = path.read_bytes()
        assert digest(raw) == expected_hash
        nodes = [n for n in ast.parse(raw, filename=filename).body
                 if isinstance(n, ast.ClassDef) and n.name == "SkiRentalOptimizer"]
        assert len(nodes) == 1
        namespace = {"math": math, "bisect": bisect}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), filename, "exec"), namespace)
        cls = namespace["SkiRentalOptimizer"]
        for tolerance in (1e-5, 1e-9, 1e-12):
            obj = cls(3, 1.5, [1, 2], [.4, .6])
            level = obj.solve(tolerance=tolerance)
            returned = obj.construct_policy_pmf(level)
            law = {t: Q(q) for t, q in returned.items()}
            assert law == {1: Q(1, 4), 2: Q(3, 8), 3: Q(3, 8)}
            check = verify_law(law)
            assert check["cost"] == "12/5" and check["moment"] == "9/8"
            assert obj.is_feasible(14 / 5) is False
            assert obj.is_feasible(3) is True
            records.append({"file": filename, "sha256": expected_hash,
                            "tolerance": tolerance, "water_level": level,
                            "exact_binary_water_level": str(Q(level)),
                            "is_feasible_at_14_over_5": False,
                            "is_feasible_at_3": True,
                            "exact_original_model_checks": check})
        for name, level in (("is_feasible", 14 / 5),
                            ("is_feasible", 3.0),
                            ("construct_policy_pmf", 3.0)):
            obj = cls(3, 1.5, [1, 2], [.4, .6])
            result, events = call_with_trace(getattr(obj, name), level)
            if name == "construct_policy_pmf":
                assert any(e["state_before_line_or_at_return"].get("F") == "19/16"
                           for e in events)
                assert any(e["state_before_line_or_at_return"].get("pmf", {}).get("3") == "9/16"
                           for e in events)
                assert encode(result) == {"1": "1/4", "2": "3/8", "3": "3/8"}
            traces.append({"file": filename, "method": name,
                           "h_binary_exact": str(Q(level)), "events": events})

    optimum = verify_law({1: Q(1, 4), 3: Q(3, 4)})
    threshold = verify_law({2: Q(1, 2), 3: Q(1, 2)})
    assert optimum["cost"] == "39/20" and threshold["cost"] == "11/5"
    assert [g(t) + Q(7, 10) * (t - 1) - 3 for t in (1, 2, 3)] == [0, Q(1, 2), 0]
    assert 3 - Q(7, 10) * Q(3, 2) == Q(39, 20)
    return {
        "job_id": JOB, "role": "research", "status": "checks_passed",
        "scope": "Finite software observations and exact evaluations; not referee acceptance",
        "python": platform.python_version(), "repository_commit": COMMIT,
        "published_pdf_sha256": PDF_HASH, "published_pdf_bytes": len(pdf),
        "published_pdf_pages": 34, "fresh_pdf_extraction_matches_prior": True,
        "published_model_page": 7, "published_inference_pages": [29, 30],
        "critical_inference_page": 30,
        "fresh_extraction_sha256": digest(extracted),
        "global_optimum": optimum, "minimum_support_level_law": threshold,
        "global_dual": {"alpha": "3", "lambda": "7/10", "y": {},
                        "reduced_costs_t_1_2_3": ["0", "1/2", "0"],
                        "reduced_cost_tail_increment": "7/10"},
        "software_runs": records, "literal_execution_traces": traces,
        "trace_limit": "Line events show state before the named line; return events show final locals. Internal mu is not assumed to be the true model moment.",
        "infinite_robustness_check": "Direct costs through max(3,max support); all later costs equal 3+moment <=9/2.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--checkout", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checkout = args.checkout or args.project / "literature/kf26-official-code"
    rendered = json.dumps(verify(args.project, checkout), indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
