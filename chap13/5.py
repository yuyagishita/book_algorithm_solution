from collections import deque


n, m = map(int, input().split())
g = [[] for _ in range(n)]
deg = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[b].append(a)
    deg[a] += 1

que = deque()
for i in range(n):
    if deg[i] == 0:
        que.append(i)


order = []
while que:
    v = que.popleft()
    order.append(v)

    for next_v in g[v]:
        deg[next_v] -= 1

        if deg[next_v] == 0:
            que.append(next_v)

reverse_order = reversed(order)
for v in order:
    print(v)
