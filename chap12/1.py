n = int(input())
a = list(map(int, input().split()))

sort_a = sorted(a)

for i in range(n):
    for j in range(n):
        if a[i] == sort_a[j]:
            print(j + 1)
