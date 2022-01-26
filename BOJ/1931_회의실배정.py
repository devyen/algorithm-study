import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
i = n-1
while i > -1:
    if coins[i] <= k:
        cnt += k//coins[i]
        k = k%coins[i]

    i -= 1

print(cnt)