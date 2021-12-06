n = int(input())
w = int(input())

a = []
for i in range(n):
    a.append(int(input()))

dp = [[False for _ in range(w + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(w+1):
        if dp[i][j]:
            dp[i+1][j] = True

        if j >= a[i] and dp[i][j-a[i]]:
            dp[i+1][j] = True

if dp[n][w]:
    print('Yes')
else:
    print('No')
