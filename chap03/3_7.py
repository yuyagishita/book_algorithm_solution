s = input()
n = len(s)

# plus_list = [[''] * (n-1) for _ in range(2**(n-1))]

ans = 0
for i in range(2**(n-1)):
    tmp = s[0]
    for j in range(n-1):
        if i >> j & 1:
            # plus_list[i][j] = '+'
            tmp += '+'
        tmp += s[j+1]

    ans += sum(map(int, tmp.split('+')))


print(ans)
