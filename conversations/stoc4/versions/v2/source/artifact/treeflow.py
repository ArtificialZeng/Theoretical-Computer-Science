"""Executable reference for the fixed-certificate TreeFlow theorem.

Boolean relations use Python integers as rows. This implementation uses
Warshall closure, not fast matrix multiplication. It is a semantic reference.
"""
from collections import deque


def identity(n):
    return tuple(1 << i for i in range(n))


def union(*relations):
    return tuple(map(lambda xs: __import__('functools').reduce(int.__or__, xs), zip(*relations)))


def compose(a, b):
    rows = []
    for mask in a:
        out = 0
        while mask:
            low = mask & -mask
            out |= b[low.bit_length() - 1]
            mask ^= low
        rows.append(out)
    return tuple(rows)


def closure(a):
    n = len(a)
    rows = [r | (1 << i) for i, r in enumerate(a)]
    for k in range(n):
        for i in range(n):
            if rows[i] & (1 << k):
                rows[i] |= rows[k]
    return tuple(rows)


class Circuit:
    def __init__(self):
        self.nodes = []
        self.users = []
        self.values = []

    def add(self, op=None, inputs=(), value=None):
        index = len(self.nodes)
        self.nodes.append((op, tuple(inputs)))
        self.users.append([])
        for child in inputs:
            assert child < index
            self.users[child].append(index)
        self.values.append(value if op is None else op(*(self.values[j] for j in inputs)))
        return index

    def update(self, leaf, value):
        assert self.nodes[leaf][0] is None
        self.values[leaf] = value
        seen, postorder = set(), []

        def visit(node):
            if node in seen:
                return
            seen.add(node)
            for parent in self.users[node]:
                visit(parent)
            postorder.append(node)

        visit(leaf)
        for node in reversed(postorder):
            op, ins = self.nodes[node]
            if op is not None:
                self.values[node] = op(*(self.values[j] for j in ins))
        return len(seen) - 1


class BagReference:
    """Rooted decomposition, one edge owner, all-pairs subtree summaries.

    The test supplies a fixed width-two certificate. Queries pin endpoints
    only along the selected endpoint-to-root paths.
    """
    def __init__(self, bags, children, edges, owners, facts):
        self.bags = [tuple(b) for b in bags]
        self.children = children
        self.edges = dict(edges)
        self.owners = dict(owners)
        self.d = facts
        self.parents = {child: i for i, cs in enumerate(children) for child in cs}
        self.depths = {0: 0}
        todo = [0]
        while todo:
            i = todo.pop()
            for child in children[i]:
                self.depths[child] = self.depths[i] + 1
                todo.append(child)
        self.summaries = {}
        self.last_recomputed = 0
        self.evaluate()

    def _calculate(self, i, bags, summaries):
        bag = bags[i]
        indices = {(v, a): k for k, (v, a) in
                   enumerate((v, a) for v in bag for a in range(self.d))}
        rows = [0] * len(indices)
        for (u, v), relation in self.edges.items():
            if self.owners[(u, v)] != i:
                continue
            for a, mask in enumerate(relation):
                for b in range(self.d):
                    if mask & (1 << b):
                        rows[indices[u, a]] |= 1 << indices[v, b]
        for child in self.children[i]:
            child_rel, child_ix = summaries[child]
            overlap = set(bag) & set(bags[child])
            for u in overlap:
                for v in overlap:
                    for a in range(self.d):
                        for b in range(self.d):
                            if child_rel[child_ix[u, a]] & (1 << child_ix[v, b]):
                                rows[indices[u, a]] |= 1 << indices[v, b]
        return closure(tuple(rows)), indices

    def evaluate(self, pin=()):
        if not pin:
            summaries = {}
            for i in sorted(self.depths, key=self.depths.get, reverse=True):
                summaries[i] = self._calculate(i, self.bags, summaries)
            self.summaries = summaries
            return summaries[0]
        bags = [set(b) for b in self.bags]
        marked = set()
        for vertex in pin:
            owner = next(i for i, bag in enumerate(self.bags) if vertex in bag)
            while True:
                bags[owner].add(vertex)
                marked.add(owner)
                if owner == 0:
                    break
                owner = self.parents[owner]
        bags = [tuple(sorted(b)) for b in bags]
        temporary = dict(self.summaries)
        for i in sorted(marked, key=self.depths.get, reverse=True):
            temporary[i] = self._calculate(i, bags, temporary)
        self.last_recomputed = len(marked)
        return temporary[0]

    def update(self, edge, relation):
        self.edges[edge] = relation
        owner = self.owners[edge]
        count = 0
        while True:
            self.summaries[owner] = self._calculate(owner, self.bags, self.summaries)
            count += 1
            if owner == 0:
                break
            owner = self.parents[owner]
        return count


def bfs_graph(vertices, edges, source):
    adj = {v: [] for v in vertices}
    for u, v in edges:
        adj[u].append(v)
    seen = {source}
    todo = deque([source])
    while todo:
        for v in adj[todo.popleft()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen


def matrix_product(matrix, vector, k):
    return tuple(bool(matrix[i] & vector) for i in range(k))


def stack_gadget(matrix, vector, row, k):
    """Explicit configuration exploration, independent of procedure summaries."""
    start = (('p', row, 'e'), ())
    todo, seen = deque([start]), {start}
    while todo:
        node, stack = todo.popleft()
        typ, idx, stage = node
        if node == ('p', row, 'x') and not stack:
            return True
        nxt = []
        if typ == 'p' and stage == 'e':
            nxt.append((('p', idx, 'c'), stack))
        elif typ == 'p' and stage == 'c':
            for j in range(k):
                if matrix[idx] & (1 << j):
                    nxt.append((('q', j, 'e'), stack + (('p', idx, 'r'),)))
        elif typ == 'p' and stage == 'r':
            nxt.append((('p', idx, 'x'), stack))
        elif typ == 'q' and stage == 'e' and vector & (1 << idx):
            nxt.append((('q', idx, 'x'), stack))
        elif typ == 'q' and stage == 'x' and stack:
            nxt.append((stack[-1], stack[:-1]))
        for config in nxt:
            if config not in seen:
                seen.add(config)
                todo.append(config)
    return False
