# A finite obstruction to a shared parity interface

This dossier rules out one precise way of combining three-colorings of TP-graph search-tree rotation graphs. It leaves the original three-colorability conjecture unresolved: the tested graphs themselves admit three-colorings.

The attempted composition uses a **single shared table with 72 entries**. An entry depends on the two factor colors (3 choices each), the two prefix-length parities (2 choices each), and inversion parity (2 choices). The factors may choose their proper colorings jointly. The CNF requires that the resulting colors form proper colorings on eleven two-factor graphs with at most six vertices. The CNF is unsatisfiable, even with this freedom in the factor colorings. This excludes that shared interface, rather than arbitrary recursive coloring rules.

`encoding_audit.py` independently enumerates search trees from all vertex orders, reconstructs tube-adjacency edges and the interface semantics, and compares the complete clause multiset with `training.cnf`. It checks 2,852 global states, 490 factor states of eight types, 10,242 variables, and 114,459 clauses. Literal duplication in 189 clauses is normalized because it does not change clause semantics. The input packets are included.

The exact CNF has SHA-256 `3e9821fb2df6fa10066e594af77530d6dfc28d5f0fad3fc15669961e6f9a3d33`. Both DRAT and LRAT refutations are supplied. The bundled checkers are executable C implementations from [drat-trim](https://github.com/marijnheule/drat-trim); their source receipt and original license are preserved. This is a computational certificate with an independently reconstructed encoding, not a claim that the checker implementation is formally verified.

## Reproduce

From the repository root, use Python 3.10+ and a C compiler:

```sh
python3 notes/tp-parity-interface/encoding_audit.py
make -C notes/vendor/drat-trim drat-trim lrat-check
notes/vendor/drat-trim/drat-trim notes/tp-parity-interface/training.cnf notes/tp-parity-interface/training.drat
notes/vendor/drat-trim/lrat-check notes/tp-parity-interface/training.cnf notes/tp-parity-interface/training.lrat
```

The Python audit writes `encoding-audit.json` beside the inputs. The certificate checks do not require rerunning the original SAT search. No manuscript is associated with this method-obstruction result.
