import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

'''
idea
dfs랑 dp를 동시에 이용
그래프를 도착점부터 탐색한다.
'''


def dfs(i, j):
    if i == m-1 and j == n-1:
        return 1

    if dp[i][j] != -1:  # 이미 방문했으면
        return dp[i][j]

    dp[i][j] = 0
    for di, dj in DIRECTION:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]


DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))