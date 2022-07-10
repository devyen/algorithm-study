# 보텀업
n = int(input())
d = [0] * (n+1)


def fill(x):
    for next in (x*5, x*3, x*2, x+1):
        if next <= n:
            if d[next]:
                d[next] = min(d[next], d[x]+1)
            else:
                d[next] = d[x] + 1


for i in range(1, n+1):
    fill(i)

print(d[n])
