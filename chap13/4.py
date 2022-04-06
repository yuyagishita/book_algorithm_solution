from collections import deque


def bfs(sy, sx):
    que = deque([(sy, sx)])
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if field[y][x] == "#":
                continue

            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                que.append((ny, nx))


h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
dist = [[-1 for _ in range(w)] for _ in range(h)]
sy, sx, gy, gx = -1, -1, -1, -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(h):
    for j in range(w):
        if field[i][j] == "S":
            sx, sy = j, i
        if field[i][j] == "G":
            gx, gy = j, i

dist[sy][sx] = 0
bfs(sy, sx)
print(dist[gy][gx])
