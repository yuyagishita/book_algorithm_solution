def count753Number(K: int, n: int, use: int, result: list) -> None:
    if n > K:
        return

    if use == 0b111:
        result.append(n)

    count753Number(K, n*10 + 3, use | 0b001, result)
    count753Number(K, n*10 + 5, use | 0b010, result)
    count753Number(K, n*10 + 7, use | 0b100, result)


K = int(input())

if K < 357:
    raise ValueError('Invalid input')

result = []
count753Number(K, 0, 0b000, result)
print('result: {}'.format(result))
print('count : {}'.format(len(result)))
