#!/usr/bin/env python3
"""Run the pinned KF26 class without running its top-level experiments.

The third-party files are not redistributed. Supply an independently obtained
checkout of the publisher-linked repository at the pinned commit. Only the
unchanged class node is executed; all numerical outputs remain observations.
"""
import argparse
import ast
import bisect
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

COMMIT = "0a86125f31e9e1b1abbba5bd4fde32a332860124"
SOURCES = {
    "Figure1_Performance_Comparison_Under_Prediction_Error.py":
        "a63482866e819cb695298aae494b792d1babb0679b31c851dd68c0f6e23018a3",
    "Table2_Consistency_Comparison_under_Fixed_Robustness.py":
        "f906417295005ffc8aeda7e3868350e9498acaf61d1876b7a23d27a2d9733b81",
}


def run(source_directory):
    records = []
    for name, expected in SOURCES.items():
        path = source_directory / name
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != expected:
            raise ValueError(f"Pinned source hash mismatch: {path}")
        tree = ast.parse(raw, filename=str(path))
        classes = [node for node in tree.body
                   if isinstance(node, ast.ClassDef)
                   and node.name == "SkiRentalOptimizer"]
        if len(classes) != 1:
            raise ValueError("Expected exactly one SkiRentalOptimizer class")
        module = ast.Module(body=classes, type_ignores=[])
        namespace = {"math": math, "bisect": bisect}
        exec(compile(module, str(path), "exec"), namespace)
        optimizer_class = namespace["SkiRentalOptimizer"]
        for tolerance in (1e-5, 1e-9, 1e-12):
            optimizer = optimizer_class(3, 1.5, [1, 2], [.4, .6])
            level = optimizer.solve(tolerance=tolerance)
            policy = optimizer.construct_policy_pmf(level)
            rational = {int(t): Fraction(v).limit_denominator(10**6)
                        for t, v in policy.items()}
            expected_policy = {1: Fraction(1, 4), 2: Fraction(3, 8),
                               3: Fraction(3, 8)}
            assert rational == expected_policy
            # The binary floats in this case equal these fractions exactly.
            assert all(Fraction(v) == rational[int(t)]
                       for t, v in policy.items())
            forecast = {1: Fraction(2, 5), 2: Fraction(3, 5)}
            cost = sum(p * sum(q * (x if t > x else 3+t-1)
                               for t, q in rational.items())
                       for x, p in forecast.items())
            moment = sum(q * (t-1) for t, q in rational.items())
            assert cost == Fraction(12, 5)
            assert moment == Fraction(9, 8)
            reject_low = optimizer.is_feasible(14/5)
            accept_three = optimizer.is_feasible(3)
            assert not reject_low and accept_three
            records.append({
                "file": name, "sha256": digest, "tolerance": tolerance,
                "water_level": level,
                "feasible_at_14_over_5": reject_low,
                "feasible_at_3": accept_three,
                "policy": {str(t): float(q) for t, q in rational.items()},
                "exact_policy": {str(t): str(q) for t, q in rational.items()},
                "reported_cost": optimizer.expected_cost(policy),
                "exact_model_cost": str(cost), "exact_model_moment": str(moment),
            })
    return {"repository": "https://github.com/JihwanKim4689/distributional-ski-rental",
            "commit": COMMIT, "execution": "Unmodified AST class node only",
            "scope": "Six floating-point software runs; exact evaluation of their returned laws",
            "records": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.source_directory)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
