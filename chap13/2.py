from collections import deque


def bfs(g, s):
    que = deque()
    dist[s] = 0
    que.append(s)

    while que:
        v = que.popleft()

        for next_v in g[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            que.append(next_v)


n, m, s, t = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dist = [-1 for _ in range(n)]
bfs(g, s)

if dist[t] != -1:
    print("Yes")
else:
    print("No")
