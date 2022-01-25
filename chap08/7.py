n = int(input())
k = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_dict = dict()
b_dict = dict()

# 下準備で連想配列を作る
for i in range(n):
    a_dict[a_list[i]] = False


# それぞれを判定するための

for i in range(n):
    a = k - b_list[i]
    if a in a_dict:
        a_dict[a] = True


print(a_dict)
