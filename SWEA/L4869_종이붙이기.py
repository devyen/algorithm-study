import sys
sys.stdin = open('input.txt')


def dp(n):
    if n < 2:
        return 1
    return dp(n-1) + dp(n-2) * 2


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = dp(n/10)
    print(f'#{tc} {result}')