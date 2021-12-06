n = int(input())
m = int(input())
a = [int(_) for _ in input().split()]

# 区間 [j, i) の平均値を前処理で求める
f = [[0.0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        sum = 0
        for k in range(j, i):
            sum += a[k]
        f[j][i] = sum/(i-j)

# DP
dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(n+1):
    for j in range(i):
        for k in range(1, m+1):
            dp[i][k] = max(dp[i][k], dp[j][k-1] + f[j][i])

res = -float('inf')

for i in range(m+1):
    res = max(res, dp[n][i])

print(res)
