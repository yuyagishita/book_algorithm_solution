s = input()
t = input()
len_s = len(s)
len_t = len(t)

dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]

for i in range(len_s+1):
    for j in range(len_t+1):
        # S の i 文字目と、T の j 文字目が等しいとき
        if i > 0 and j > 0:
            if (s[i-1] == t[j-1]):
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])

        #  S に 1 文字追加
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

        # T に 1 文字追加
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

print(dp[len_s][len_t])

# 復元
i = len_s
j = len_t
lenght = dp[i][j]
ans = ''
while lenght > 0:
    if s[i-1] == t[j-1]:
        ans += s[i-1]
        i -= 1
        j -= 1
        lenght -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1
print(ans[::-1])
