import sys
input = sys.stdin.readline

n = int(input())

# memo = [0] * (n+1)
# memo[1], memo[2] = 1, 2
#
# for i in range(3, n+1):  # 상향식
#     memo[i] = memo[i-1] + memo[i-2]
#
# print(memo[n]%10007)

if n < 3:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n+1):
        tmp = a + b
        a = b
        b = tmp

    print(b % 10007)

