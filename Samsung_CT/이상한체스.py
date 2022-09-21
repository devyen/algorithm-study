import sys

input = sys.stdin.readline
DIRECTIONS = (
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
)  # 말 순서대로 경우의 수와 방향
DELTA = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def cal_blank():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not matrix[i][j]:
                cnt += 1
    return cnt


def dfs(idx):
    global answer
    if idx == len(pieces):  # base case
        cnt = cal_blank()
        answer = min(answer, cnt)
        return

    num, i, j = pieces[idx]
    if num == 6:
        dfs(idx+1)
        return

    for dirs in DIRECTIONS[num-1]:
        # 범위 체크
        for dir in dirs:
            check(i, j, dir)
        # dfs
        dfs(idx+1)
        # matrix 복구
        for dir in dirs:
            reverse_check(i, j, dir)


def check(i, j, dir):  # 해당 방향에 대해 범위를 체크하는 함수
    while True:
        di, dj = DELTA[dir]
        i, j = i+di, j+dj
        if not (0 <= i < n and 0 <= j < m):
            break
        if matrix[i][j] == 6:
            break
        elif matrix[i][j] == 0 or matrix[i][j] > 6:
            matrix[i][j] += 9


def reverse_check(i, j, dir):
    while True:
        di, dj = DELTA[dir]
        i, j = i+di, j+dj
        if not (0 <= i < n and 0 <= j < m):
            break
        if matrix[i][j] >= 9:
            matrix[i][j] -= 9
        elif matrix[i][j] == 6:
            break


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
pieces = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            pieces.append([matrix[i][j], i, j])

answer = 8*8
dfs(0)
print(answer)