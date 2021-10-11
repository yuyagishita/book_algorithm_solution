n = int(input())
w = int(input())

a = [int(_) for _ in input().split()]

memo = [[-1 for _ in range(w+1)] for i in range(n+1)]


def func(i, w, a):
    if i == 0:
        if w == 0:
            return True
        else:
            return False

    if memo[i][w] != -1:
        return memo[i][w]

    if func(i-1, w, a):
        memo[i][w] = True
        return memo[i][w]

    if func(i-1, w-a[i-1], a):
        memo[i][w] = True
        return memo[i][w]

    memo[i][w] = False
    return False


if func(n, w, a):
    print('Yes')
else:
    print('No')
