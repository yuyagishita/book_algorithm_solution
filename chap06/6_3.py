from bisect import bisect_right, bisect_left

n = int(input())
m = int(input())
a = list(map(int, input().split()))

# 4個を2, 2に分けて、その2つを足したのがM以下になるようにする
# リストaに0を追加する。「選ばない時=0を選んだ」にする
a.append(0)

# 半分列挙をする。計算量はO(N^2)。
s = list()
for i in range(n+1):
    for j in range(n+1):
        s.append(a[i]+a[j])

s = sorted(s)

# 片方を固定して二分探索をする
# 4個を2,2に分けたのもi,jとすると、i+j<=mになるjの最大値を探す。iは固定する。
ans = 0
for i in s:
    j = bisect_right(s, m-i)-1
    ans = max(ans, i+s[j])

print(ans)
