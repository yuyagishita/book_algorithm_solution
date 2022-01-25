n = int(input())
m = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_dict = dict()
b_dict = dict()

for i in range(n):
    if a_list[i] in a_dict:
        a_dict[a_list[i]].append(i)
    else:
        a_dict[a_list[i]] = [i]

for i in range(m):
    if b_list[i] in b_dict:
        b_dict[b_list[i]].append(i)
    else:
        b_dict[b_list[i]] = [i]

print(a_dict)
print(b_dict)

ans = 0

for i in range(m):
    if b_list[i] in a_dict:
        ans += len(a_dict[b_list[i]])

print(ans)
