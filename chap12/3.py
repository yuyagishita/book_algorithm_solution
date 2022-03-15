n, k = map(int, input().split())
a = list(map(int, input().split()))


for i in range(n):
    if i < k - 1:
        continue
    tmp = sorted(a[: i + 1])
    print(tmp)
    print(tmp[k - 1])
