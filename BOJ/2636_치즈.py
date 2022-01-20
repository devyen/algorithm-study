import sys
from collections import deque
input = sys.stdin.readline


def is_hole(i, j):  # dfs
    stack = [(i, j)]
    while stack:
        r, c = stack.pop()
        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + d[0], c + d[1]


def melt_cheese(r, c, t):
    edge = 0
    for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + d[0], c + d[1]
        if matrix[nr][nc] == 0 or 1 < matrix[nr][nc] <= t:
            edge = 1
            # 구멍 판별: 4방향 끝까지 가보기 - 하나라도 끝까지 가면 구멍x
            hole = 1
            for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nnr, nnc = nr, nc
                flag2 = 1
                while 1 <= nnr < n-1 and 1 <= nnc < m-1:
                    nnr, nnc = nnr + d[0], nnc + d[1]
                    if matrix[nnr][nnc] == 1 or matrix[nnr][nnc] > t:
                        flag2 = 0
                        break
                if flag2:
                    hole = 0
                    break

    if edge and not hole:
        matrix[r][c] = t+1
    else:
        cheeses.append((r, c))


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

t = 1
cheeses = deque()
for r in range(n):
    for c in range(m):
        if matrix[r][c]:
            melt_cheese(r, c, t)

while cheeses:
    t += 1
    l = len(cheeses)
    now = cheeses
    cheeses = deque()
    for r, c in now:
        melt_cheese(r, c, t)


print(t)
print(l)





