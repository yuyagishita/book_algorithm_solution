from collections import deque


def dfs(g, v):
    seens[v] = True

    for next_v in g[v]:
        if seens[next_v]:
            continue
        dfs(g, next_v)


def bfs(g, s):
    que = deque()
    dist[s] = 0
    que.append(s)
    print(g)

    while que:
        print(dist)
        print(que)
        v = que.popleft()

        for next_v in g[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            que.append(next_v)


n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

result = 0
seens = [False for _ in range(n)]
for v in range(n):
    if seens[v]:
        continue
    dfs(g, v)

    result += 1

print(result)

result2 = 0
dist = [-1 for _ in range(n)]
for v in range(n):
    if dist[v] != -1:
        continue
    bfs(g, v)
    result2 += 1

print(result2)
