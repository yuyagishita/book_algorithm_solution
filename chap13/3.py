from collections import deque


def bfs(g, s):
    que = deque()
    colors[s] = 0
    que.append(s)

    while que:
        v = que.popleft()

        for next_v in g[v]:
            if colors[next_v] != -1:
                if colors[next_v] == colors[v]:
                    return False
                continue
            colors[next_v] = 1 - colors[v]
            que.append(next_v)

    return True


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

colors = [-1 for _ in range(n)]
is_bipartite = True

for v in range(n):
    if colors[v] != -1:
        continue
    if not bfs(g, v):
        is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")
