import sys
from collections import deque
import copy
import math
import time
input = sys.stdin.readline


start = time.time()


def bfs():
    tomatos = 0
    q = deque()
    for l in range(h):
        for r in range(n):
            for c in range(m):
                if matrix[l][r][c] == 1:
                    q.append((l, r, c))  # 익은 토마토 큐에 담기
                elif matrix[l][r][c] == 0:
                    tomatos += 1  # 안 익은 토마토 카운팅

    if tomatos == 0:  # 안 익은 토마토가 없으면 0 리턴
        return 0

    day = 0
    cnt = 0
    while q:
        nq = copy.deepcopy(q)  # day를 세야하므로 하루치 큐를 만든다.
        q = deque()
        while nq:
            l, i, j = nq.popleft()
            for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 델타 + 상하 탐색
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < n and 0 <= nj < m and matrix[l][ni][nj] == 0:
                        cnt += 1
                        matrix[l][ni][nj] = 1
                        q.append((l, ni, nj))

            for d in [-1, 1]:  # 하 상
                nl = l + d
                if 0 <= nl < h and matrix[nl][i][j] == 0:
                    cnt += 1
                    matrix[nl][i][j] = 1
                    q.append((nl, i, j))

        day += 1
        
        if cnt == tomatos:
            return day

    if cnt < tomatos:
        return -1


m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

print(bfs())

end = time.time()
print(f'{end-start: .5f} sec')  # 예제2에서 `0.83292 sec`, `4.08474 sec` 로 차이난다.