from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n, m = map(int, input().split())
a, b = [], []
for _ in range(m):
    i, j = map(int, input().split())
    a.append(i - 1)
    b.append(j - 1)

uf = UnionFind(n)
cur = n * (n - 1) // 2
res = []
for i in range(m):
    res.append(cur)

    aa, bb = a[m - 1 - i], b[m - 1 - i]
    if uf.same(aa, bb):
        continue

    sa, sb = uf.size(aa), uf.size(bb)
    cur -= sa * sb
    uf.unite(aa, bb)

res.reverse()

for i in range(len(res)):
    print(res[i])
