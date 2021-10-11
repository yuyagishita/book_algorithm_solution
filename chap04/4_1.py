n = int(input())


def tori(N):
    if N == 2:
        return 1
    if N == 1:
        return 0
    if N == 0:
        return 0

    return tori(N-1) + tori(N-2) + tori(N-3)


print(tori(n))
