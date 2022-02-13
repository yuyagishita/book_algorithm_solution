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


n, k, l = map(int, input().split())
p, q = [], []
r, s = [], []
for _ in range(k):
    i, j = map(int, input().split())
    p.append(i - 1)
    q.append(j - 1)
for _ in range(l):
    i, j = map(int, input().split())
    r.append(i - 1)
    s.append(j - 1)

road_uf = UnionFind(n)
rail_uf = UnionFind(n)
for i in range(k):
    road_uf.unite(p[i], q[i])
for i in range(l):
    rail_uf.unite(r[i], s[i])

num = dict()
for i in range(n):
    road_root = road_uf.find(i)
    rail_root = rail_uf.find(i)
    if (road_root, rail_root) in num:
        num[(road_root, rail_root)] += 1
    else:
        num[(road_root, rail_root)] = 1

for i in range(n):
    print(num[(road_uf.find(i), rail_uf.find(i))])
