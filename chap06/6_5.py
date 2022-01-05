from bisect import bisect_right

n = int(input())
k = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()


def check(x: int) -> bool:
    cnt = 0
    for i in range(n):
        cnt += bisect_right(b, x // a[i])
    return cnt >= k


left = 0
right = 10**18
while (right - left) > 1:
    mid = (right + left) // 2
    
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
