n = int(input())
a = list(map(int, input().split()))

# 累積和をとる
s = [0 for _ in range(n+1)]
for i in range(n):
    s[i+1] = s[i] + a[i]

# DP
dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

# 初期条件
for i in range(n):
    dp[i][i+1] = 0

# 更新
for bet in range(2, n+1):
    for i in range(n+1-bet):
        j = i + bet

        # dp[i][j]を更新する
        for k in range(i+1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + s[j]-s[i])


print(dp[0][n])
