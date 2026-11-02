# Held-out diagnostic execution record

First execution of root_control_heldout.py stopped before completing its first
case: BlockWA exposed integer alphabet labels to the shared invariant_basis
helper, which retains string words. Python raised TypeError at w+a. This was
an interface error, not a failed mathematical equality or counterexample.
The block labels were changed to strings, with integer conversion only when
indexing the matrix list. The subsequent actual execution outcome is recorded
in root_control_heldout.json if it completes; file existence is not a fresh
mathematical review. No frozen evidence, scheduling counter or acceptance was
changed in response.
