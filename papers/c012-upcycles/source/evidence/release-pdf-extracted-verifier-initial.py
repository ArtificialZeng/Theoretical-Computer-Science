"""Exhaustive check of the printed binary upcycle; run without -O."""
 from itertools import product

 P = (
     '00177617563754173657321716771457'
     '12371016661655164636441633162656'
     '22161556133611160676045602151214'
     '46141314063206120412261006540236'
 )
 u = ''.join('*' + format(int(b), '03b') for b in P)
 L, n, d = len(u), 12, 3
 assert len(P) == 128 and L == 512 == 2 ** (n - d)
 assert L > n and set(u) == {'*', '0', '1'}
 assert all((c == '*') == (i % 4 == 0)
             for i, c in enumerate(u))
 W = [''.join(u[(i + k) % L] for k in range(n))
       for i in range(L)]
 assert all(w.count('*') == d for w in W)

 pairs = 0
 for i in range(L):
     for j in range(i + 1, L):
         assert any(a != '*' and b != '*' and a != b
                    for a, b in zip(W[i], W[j]))
         pairs += 1
 assert pairs == 130816

 counts = []
 for x in product('01', repeat=n):
     count = sum(all(c == '*' or c == b
                     for c, b in zip(w, x)) for w in W)
     counts.append(count)
 assert len(counts) == 4096 and min(counts) == max(counts) == 1
 print('Verified: 512 windows, 130816 pairs, 4096 words.')
