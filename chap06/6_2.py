import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ans = 0

# bを固定して考える
for j in range(n):
    i = bisect.bisect_left(a, b[j])
    k = n - bisect.bisect_right(c, b[j])
    ans += i*k

print(ans)
