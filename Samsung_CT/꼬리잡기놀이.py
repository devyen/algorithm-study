import sys
from copy import deepcopy
input = sys.stdin.readline

DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))


def move_tail(i, j):
    while matrix[i][j] != 3:
        for di, dj in DELTA:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and 2 <= matrix[ni][nj] < 4:
                if matrix[ni][nj] == 3:
                    matrix[ni][nj] = 4
                    matrix[i][j] = 3
                    break
                i, j = ni, nj


n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
heads = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            heads.append([i, j])

answer = 0
for time in range(1, k+1):
    # 1. 한칸씩 이동
    for h in range(m):
        hi, hj = heads[h]
        for di, dj in DELTA:
            ni, nj = hi+di, hj+dj
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 4:
                matrix[ni][nj] = matrix[hi][hj]
                matrix[hi][hj] = 2
                move_tail(hi, hj)
    # 2. 공 던짐
    q, r = divmod(time, n)
    if q%2:  # 홀수
        for j in range(n):
            if 0 < matrix[q-1][j] < 4:
                break

