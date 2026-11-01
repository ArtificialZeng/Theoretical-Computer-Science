"""Deterministic marked-palindrome repair, with a suffix-array LCE index.

Time O(n log^2(n+2) + k^2), space O(n log(n+2) + k^2),
for a fixed nonempty alphabet. Materializing the witness takes O(n+k).
Python's comparison sort is deliberately included in the stated bound.
"""
import argparse
import json
from itertools import islice


class LCE:
    def __init__(self, text):
        self.text = text
        n = len(text)
        ranks = [ord(c) for c in text]
        suffixes = list(range(n))
        step = 1
        while step < n:
            suffixes.sort(key=lambda i: (ranks[i], ranks[i+step] if i+step < n else -1))
            nxt = [0]*n
            for z in range(1, n):
                p, q = suffixes[z-1], suffixes[z]
                first = (ranks[p], ranks[p+step] if p+step < n else -1)
                second = (ranks[q], ranks[q+step] if q+step < n else -1)
                nxt[q] = nxt[p]+int(first != second)
            ranks = nxt
            if ranks[suffixes[-1]] == n-1:
                break
            step *= 2
        self.rank = [0]*n
        for z, p in enumerate(suffixes):
            self.rank[p] = z
        lcp, common = [0]*n, 0
        for i in range(n):
            z = self.rank[i]
            if z == 0:
                common = 0
                continue
            j = suffixes[z-1]
            while i+common < n and j+common < n and text[i+common] == text[j+common]:
                common += 1
            lcp[z] = common
            common = max(0, common-1)
        self.table = [lcp]
        width = 2
        while width <= n:
            prev = self.table[-1]
            self.table.append([min(prev[i], prev[i+width//2]) for i in range(n-width+1)])
            width *= 2

    def query(self, a, b):
        if a == b:
            return len(self.text)-a
        low, high = sorted((self.rank[a], self.rank[b]))
        low += 1
        width = high-low+1
        power = width.bit_length()-1
        return min(self.table[power][low], self.table[power][high-(1 << power)+1])


def repair(s, k, alphabet='ab'):
    if k < 0 or not alphabet or '#' in alphabet or any(c not in alphabet+'#' for c in s):
        raise ValueError('Nonnegative budget and alphabet disjoint from # required')
    # Two distinct sentinels, neither present in input nor alphabet.
    reserved = list(islice((chr(z) for z in range(1, 0x110000) if chr(z) not in alphabet+'#'), 2))
    separator, blocked = reserved
    reverse = s[::-1].replace('#', blocked)
    n = len(s)
    index = LCE(s+separator+reverse)
    levels, parents = [], []
    query_count = 0
    best, terminal = k+1, None
    for budget in range(k+1):
        layer, links = {}, {}
        for delta in range(-budget, budget+1):
            candidates = []
            if budget == 0 and delta == 0:
                candidates.append((0, None, ''))
            if budget:
                previous = levels[budget-1]
                if delta in previous:
                    candidates.append((previous[delta], (budget-1, delta), ''))
                for old_delta, increment in ((delta-1, 1), (delta+1, 0)):
                    if old_delta in previous:
                        i = previous[old_delta]
                        j = i-old_delta
                        if i+j < n:
                            candidates.append((i+increment, (budget-1, old_delta), ''))
            for cost in (1, 2):
                if budget < cost or delta not in levels[budget-cost]:
                    continue
                i = levels[budget-cost][delta]
                j = i-delta
                if i+j+1 < n:
                    a = min(alphabet, key=lambda c: (s[i] != c)+(s[n-1-j] != c))
                    if (s[i] != a)+(s[n-1-j] != a) <= cost:
                        candidates.append((i+1, (budget-cost, delta), a))
            candidates = [c for c in candidates if c[0] >= 0 and c[0]-delta >= 0 and 2*c[0]-delta <= n]
            if not candidates:
                continue
            raw, parent, emitted = max(candidates, key=lambda c: c[0])
            j = raw-delta
            cap = (n-raw-j)//2
            extension = min(cap, index.query(raw, n+1+j)) if cap else 0
            query_count += int(cap > 0)
            i = raw+extension
            layer[delta] = i
            links[delta] = parent, emitted, raw, i
            remainder = n-2*i+delta
            center = 1 if remainder == 0 else int(s[i] != '#') if remainder == 1 else None
            if center is not None and budget+center < best:
                best, terminal = budget+center, (budget, delta)
        levels.append(layer)
        parents.append(links)
        if budget >= best:
            break
    if terminal is None or best > k:
        return {'distance': None, 'repair': None, 'lce_queries': query_count,
                'frontier_entries': sum(map(len, levels))}
    pieces = []
    pointer = terminal
    while pointer is not None:
        e, d = pointer
        pointer, emitted, raw, end = parents[e][d]
        pieces.append(emitted+s[raw:end])
    half = ''.join(reversed(pieces))
    return {'distance': best, 'repair': half+'#'+half[::-1],
            'lce_queries': query_count, 'frontier_entries': sum(map(len, levels))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    parser.add_argument('budget', type=int)
    parser.add_argument('--alphabet', default='ab')
    args = parser.parse_args()
    print(json.dumps(repair(args.text, args.budget, args.alphabet), indent=2))
