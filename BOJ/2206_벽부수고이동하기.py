import sys
from collections import deque
input = sys.stdin.readline


# (0, 0) 에서 (n-1, m-1)까지의 최소 거리
def bfs():
    q = deque()
    q.append((0, 0, 0, 1, 0, 0))  # 행 인덱스, 열 인덱스, 벽 부신 횟수, 현재까지의 거리, 직전r, 직전c
    while q:
        r, c, w, s, pr, pc = q.popleft()
        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 델타탐색
            nr, nc = r + d[0], c + d[1]

            if nr == n - 1 and nc == m - 1:
                return s + 1

            if 0 <= nr < n and 0 <= nc < m and not(nr == pr and nc == pc):
                if matrix[nr][nc] == 0:
                    q.append((nr, nc, w, s + 1, r, c))
                elif matrix[nr][nc] == 1 and w == 0:  # 벽이 있고, 아직 한 번도 벽을 부수지 않은 경우
                    q.append((nr, nc, w + 1, s + 1, r, c))

    return -1


n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())