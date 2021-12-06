n = int(input())
w = int(input())
a = [int(_) for _ in input().split()]

dp = [[False for _ in range(w + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(w+1):
        if dp[i][j]:
            dp[i+1][j] = True

        if j >= a[i] and dp[i+1][j-a[i]]:
            dp[i+1][j] = True

if dp[n][w]:
    print('Yes')
else:
    print('No')
