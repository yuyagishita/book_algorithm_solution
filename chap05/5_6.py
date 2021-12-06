n = int(input())
w = int(input())
a = [int(_) for _ in input().split()]
m = [int(_) for _ in input().split()]

dp = [[float('inf') for _ in range(w + 1)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(w+1):
        if dp[i][j] < float('inf'):
            if dp[i+1][j] > 0:
                dp[i+1][j] = 0

        if j >= a[i] and dp[i+1][j-a[i]] < m[i]:
            if dp[i+1][j] > dp[i+1][j-a[i]]+1:
                dp[i+1][j] = dp[i+1][j-a[i]]+1


if dp[n][w] < float('inf'):
    print('Yes')
else:
    print('No')
