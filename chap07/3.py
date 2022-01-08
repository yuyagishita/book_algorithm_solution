n = int(input())
w = [list(map(int, input().split())) for i in range(n)]

w = sorted(w, key=lambda x: x[1])

ans = 0
now = 0
for i in range(n):
    now += w[i][0]
    if now <= w[i][1]:
        ans += 1


if ans == n:
    print('Yes')
else:
    print('No')


