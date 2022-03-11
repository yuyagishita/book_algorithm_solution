n, m = map(int, input().split())
ab = []

for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

sort_ab = sorted(ab)

ans = 0
for i in range(n):
    if m <= 0:
        break
    if sort_ab[i][1] < m:
        ans += sort_ab[i][0] * sort_ab[i][1]
        m -= sort_ab[i][1]
    else:
        ans += sort_ab[i][0] * m
        m = 0


print(ans)
