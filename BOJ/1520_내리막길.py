import sys
input = sys.stdin.readline

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
memo = [[0]*n for _ in range(m)]
memo[0][0] = 1

result = 0
for i in range(n):
    for j in range(m):
        if memo[i][j]:
           for di, dj in DIRECTION:
               if 0 <= i + di < n and 0 <= j + dj < n:
                   


print(result)

