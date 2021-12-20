n = int(input())
m = int(input())
a = sorted(list(map(int, input().split())))

left = 0
right = 1000

while (right - left) > 1:
    x = (left + right) // 2
    cnt = 1
    prev = 0
    
    for i in range(n):
        if a[i] - a[prev] >= x:
            cnt += 1
            prev = i

    if cnt >= m:
        left = x
    else:
        right = x

print(left)
