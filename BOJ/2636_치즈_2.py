import sys
from collections import deque
input = sys.stdin.readline


# def melt_cheese(r, c):
#     for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#         nr, nc = r + d[0], c + d[1]
#         if matrix[nr][nc] == 0:
#             # 구멍 판별: 4방향 끝까지 가보기 - 하나라도 끝까지 가면 구멍x
#             hole = 1
#             for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#                 nnr, nnc = nr, nc
#                 flag2 = 1
#                 while 0 <= nnr < n and 0 <= nnc < m:
#                     nnr, nnc = nr + d[0], nc + d[1]
#                     if matrix[nnr][nnc] == 1:
#                         flag2 = 0
#                         break
#                 if flag2:
#                     hole = 0
#                     break
#             break
#
#     if not hole:
#         matrix[r][c] = 0
#     else:
#         cheeses.append((r, c))


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(matrix)





