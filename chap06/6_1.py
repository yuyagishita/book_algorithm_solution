a = list(map(int, input().split()))
b = sorted(set(a))
d = {v: i for i, v in enumerate(b)}

print(list(map(lambda v: d[v], a)))
