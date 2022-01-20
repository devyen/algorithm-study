import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs():
    tomatos = 0
    q = deque()
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                q.append((r, c))  # 익은 토마토 큐에 담기
            elif matrix[r][c] == 0:
                tomatos += 1  # 안 익은 토마토 카운팅

    if tomatos == 0:  # 안 익은 토마토가 없으면 0 리턴
        return 0

    day = 0
    cnt = 0
    while q:
        nq = copy.deepcopy(q)  # day를 세야하므로 하루치 큐를 만든다.
        q = deque()
        while nq:
            i, j = nq.popleft()
            for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 델타탐색
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 0:
                        cnt += 1
                        matrix[ni][nj] = 1
                        q.append((ni, nj))
        day += 1
        
        if cnt == tomatos:
            return day

    if cnt < tomatos:
        return -1


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(bfs())