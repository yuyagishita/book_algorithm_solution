from math import sin, pi

a, b, c = map(int, input().split())

# 関数f
def f(t: float) -> float:
    return a*t + b*sin(c*t*pi) 


alpha = 0
beta = 200
for i in range(100):
    gamma = (alpha + beta) / 2
    if f(gamma) <= 100:
        alpha = gamma
    else:
        beta = gamma

print(alpha)
print(beta)
