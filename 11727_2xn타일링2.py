import sys
input = sys.stdin.readline

n = int(input())

a, b = 1, 3
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for _ in range(3, n+1):
        tmp = 2*a + b
        a = b
        b = tmp

    print(b % 10007)
