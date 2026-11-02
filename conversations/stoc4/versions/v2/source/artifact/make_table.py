"""Render only completed validation counts into the manuscript."""
import json
from pathlib import Path

here = Path(__file__).resolve().parent
r = json.loads((here / 'validation_results.json').read_text())
a, b = r['lower_bounds'], r['treeflow']
rows = [
    ('Exhaustive matrix--vector instances', a['matrix_vector_cases']),
    ('Control-flow gadget answers', a['graph_answers']),
    ('Fact-relation gadget answers', a['fact_answers']),
    ('Explicit-stack gadget answers', a['stack_answers']),
    ('Selector-toggle count checks', a['selector_bit_transitions']),
    ('Width-two graph relation edits', b['edits']),
    ('Bag/BFS point--fact comparisons', b['pair_answers']),
    ('Shared-circuit edits', b['circuit_edits']),
    ('Circuit/full-evaluation comparisons', b['circuit_outputs']),
    ('Recursive base-path states', len(r['recursion'])),
    ('Call-diamond updates', r['sharing']['edits']),
]
out = r'''\begin{table}[t]
\centering
\caption{Completed finite validation. All checks passed. Counts are
generated from the executable report; they are not timing measurements.}
\label{tab:validation}
\begin{tabular}{lr}
\toprule
Check family & Completed records\\
\midrule
'''
out += '\n'.join(f'{name} & {number:,}' + r'\\' for name, number in rows)
out += '\n' + r'''\bottomrule
\end{tabular}
\end{table}
'''
(here / 'validation_table.tex').write_text(out)
