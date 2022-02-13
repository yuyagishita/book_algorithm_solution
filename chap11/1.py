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
# ab = [map(int, input().split()) for _ in range(m)]
# a, b = [list(i) for i in zip(*ab)]

a = list()
b = list()
for _ in range(m):
    i, j = map(int, input().split())
    a.append(i - 1)
    b.append(j - 1)


ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if j == i:
            continue
        uf.unite(a[j], b[j])

    num = 0
    for k in range(n):
        if uf.find(k) == k:
            num += 1

    if num > 1:
        ans += 1

print(ans)
