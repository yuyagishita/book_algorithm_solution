from collections import defaultdict


class WeightUnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.diff_weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            return self.parents[x]

    def unite(self, x, y, w):
        w += self.weight(x) - self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y, w = y, x, -w
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.diff_weight[y] = w
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

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n, m = map(int, input().split())
uf = WeightUnionFind(n)
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1

    if uf.same(l, r):
        diff = uf.diff(l, r)
        if diff != d:
            print("No")
            exit()
    else:
        uf.unite(l, r, d)

print("Yes")
