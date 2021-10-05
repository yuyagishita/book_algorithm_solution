n = int(input())
a = list(map(int, input().split()))

ans = float('inf')
for i in range(n):
    cnt = 0
    tmp = a[i]

    while tmp % 2 == 0:
        tmp /= 2
        cnt += 1

    if ans > cnt:
        ans = cnt

print(ans)
