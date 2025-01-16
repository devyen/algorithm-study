from collections import deque

DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs():
    while q:
        i, j, t = q.popleft()
        for di, dj in DIRECTION:
            ni, nj = i+di, j+dj
            if ni == n-1 and nj == m-1:  # 목표점 (n-1, m-1)에 도달하면 return
                return t+1
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1 and not check[ni][nj]:
                q.append((ni, nj, t+1))
                check[ni][nj] = 1


n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

q = deque([(0, 0, 1)])  # 시작점 i, 시작점 j, 이동거리
check[0][0] = 1
print(bfs())
