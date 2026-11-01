"""Small solver-free check of the explicit octal-encoded upcycle."""
from itertools import product

panes = (
    '00177617563754173657321716771457'
    '12371016661655164636441633162656'
    '22161556133611160676045602151214'
    '46141314063206120412261006540236'
)
u = ''.join('*' + format(int(c), '03b') for c in panes)
assert len(panes) == 128 and len(u) == 512
assert all((c == '*') == (i % 4 == 0) for i, c in enumerate(u))
windows = [u[i:] + u[:i] for i in range(512)]
windows = [w[:12] for w in windows]
assert all(w.count('*') == 3 for w in windows)
for bits in product('01', repeat=12):
    assert sum(all(c == '*' or c == b for c, b in zip(w, bits))
               for w in windows) == 1
assert 512 == 2 ** (12 - 3) and 512 > 12
print('Verified: a=2, n=12, d=3, L=512; all 4096 words covered exactly once.')
