k = int(input())
n = int(input())

ans = 0

for x in range(k+1):
    for y in range(k+1):
        z = n-x-y
        if z <= k and z >= 0:
            ans += 1

print(ans)
