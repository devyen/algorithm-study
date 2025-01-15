def dfs(i, j):
    check[i][j] = 1
    for di, dj in DIRECTION:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 0 and not check[ni][nj]:
            dfs(ni, nj)


DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))
n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

check = [[0]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not check[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
