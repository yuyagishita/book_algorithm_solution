n = int(input())

memo = [-1 for _ in range(50)]


def tori(N):
    if N == 2:
        return 1
    if N == 1:
        return 0
    if N == 0:
        return 0

    if memo[N] != -1:
        return memo[N]

    memo[N] = tori(N-1) + tori(N-2) + tori(N-3)

    return memo[N]


print(tori(n))
