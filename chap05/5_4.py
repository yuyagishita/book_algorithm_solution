n = int(input())
w = int(input())
k = int(input())

a = []
for i in range(n):
    a.append(int(input()))

dp = [[float('inf') for _ in range(w + 1)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(w+1):
        if dp[i+1][j] > dp[i][j]:
            dp[i+1][j] = dp[i][j]

        if j >= a[i]:
            if dp[i+1][j] > dp[i][j-a[i]] + 1:
                dp[i+1][j] = dp[i][j-a[i]] + 1

if dp[n][w] <= k:
    print('Yes')
else:
    print('No')
