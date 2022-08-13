import sys
from copy import deepcopy
input = sys.stdin.readline

DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))
DIAGONAL = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def grow(i, j, new_matrix):
    cnt = 0
    for di, dj in DELTA:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] > 0:
            cnt += 1
    new_matrix[i][j] += cnt
    return


def spread(i, j, new_matrix):
    blank = []
    for di, dj in DELTA:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 0 and killer_matrix[ni][nj] == 0:
            blank.append((ni, nj))

    for bi, bj in blank:
        new_matrix[bi][bj] += new_matrix[i][j]//len(blank)


def turn():
    global matrix, answer
    # 제초제 자연 감소
    for i in range(n):
        for j in range(n):
            if killer_matrix[i][j]:
                killer_matrix[i][j] -= 1

    # 성장 & 번식
    new_matrix = deepcopy(matrix)  # 동시 번식을 위해서
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                grow(i, j, new_matrix)
                spread(i, j, new_matrix)
    matrix = new_matrix

    # 제초제를 뿌릴 위치 탐색
    max_cnt = 0
    ti, tj = 0, 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                # 대각선 방향 탐색
                cnt = matrix[i][j]
                for di, dj in DIAGONAL:
                    for t in range(1, k + 1):
                        ni, nj = i + di * t, j + dj * t
                        if 0 <= ni < n and 0 <= nj < n:
                            if matrix[ni][nj] <= 0:
                                break
                            cnt += matrix[ni][nj]
                            # killer[ni][nj] = c
                if cnt > max_cnt:
                    max_cnt = cnt
                    ti, tj = i, j

    # 제초제 살포(?)
    answer += max_cnt
    matrix[ti][tj] = 0
    killer_matrix[ti][tj] = c+1
    for di, dj in DIAGONAL:
        for t in range(1, k + 1):
            ni, nj = ti + di * t, tj + dj * t
            if 0 <= ni < n and 0 <= nj < n:
                if matrix[ni][nj] < 0:  # 벽(-1)
                    break
                if matrix[ni][nj] == 0:  # 나무가 없으면
                    killer_matrix[ni][nj] = c+1
                    break
                matrix[ni][nj] = 0
                killer_matrix[ni][nj] = c+1


n, m, k, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]  # 나무 숫자, 빈칸 0, 벽 -1
killer_matrix = [[0]*n for _ in range(n)]

answer = 0
for _ in range(m):
    turn()

print(answer)
