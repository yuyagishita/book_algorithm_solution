n = int(input())

abc = [[int(_) for _ in input().split()] for i in range(n)]

dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue

            # if dp[i+1][k] < (dp[i][j] + abc[i][k]):
                # dp[i+1][k] = dp[i][j] + abc[i][k]
            if dp[i+1][j] < (dp[i][k] + abc[i][j]):
                dp[i+1][j] = dp[i][k] + abc[i][j]

print(max(dp[n][0], dp[n][1], dp[n][2]))
