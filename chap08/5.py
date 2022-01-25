n = int(input())
m = int(input())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(m):
    if b[i] in a:
        ans += 1

print(ans)
