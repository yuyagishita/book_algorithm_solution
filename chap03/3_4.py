n = int(input())
a = list(map(int, input().split()))

min_v = float('inf')
max_v = 0

for i in range(n):
    if a[i] < min_v:
        min_v = a[i]
    if a[i] > max_v:
        max_v = a[i]

print(max_v-min_v)
