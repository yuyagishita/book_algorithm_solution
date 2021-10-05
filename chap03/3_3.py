n = int(input())
a = list(map(int, input().split()))

min_value = float('inf')
secound_min_value = float('inf')

for i in range(n):
    if a[i] < min_value:
        secound_min_value = min_value
        min_value = a[i]
    elif a[i] < secound_min_value:
        secound_min_value = a[i]

print(secound_min_value)
