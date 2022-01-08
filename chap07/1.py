n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
     ai = a[n-i-1]
     if ai < b[-1]:
         ans += 1
         b.pop()

print(ans)
