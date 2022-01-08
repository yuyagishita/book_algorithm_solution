n = int(input())
red = [list(map(int, input().split())) for i in range(n)]
blue = [list(map(int, input().split())) for i in range(n)]

blue = sorted(blue)

used = [False for _ in range(n)]

res = 0
for i in range(n):
    maxy = -1
    maxid = -1
    for j in range(n):
        if used[j]:
            continue
        if red[j][0] >= blue[i][0]:
            continue
        if red[j][1] >= blue[i][1]:
            continue

        if maxy < red[j][1]:
            maxy = red[j][1]
            maxid = j

    if maxid == -1:
        continue

    res += 1
    used[maxid] = True

print(res)
