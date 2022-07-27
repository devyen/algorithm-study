import copy
import sys
input = sys.stdin.readline


def move(dir, level):
    global answer
    global board

    old = copy.deepcopy(board)

    # 왼쪽1 & 오른쪽2
    if dir <= 2:
        for i in range(n):
            row = []
            for j in range(n):
                if board[i][j]:
                    row.append(board[i][j])
            if len(row) == 0:
                continue

            if dir == 1:  # 왼쪽
                num = row[0]
                new_row = [num]
                for block in row[1:]:
                    if block == num:
                        new_row[-1] = block * 2
                        num = 0
                    else:
                        new_row.append(block)
                        num = block

                board[i] = new_row + [0] * (n - len(new_row))

            elif dir == 2:  # 오른쪽
                num = row[-1]
                new_row = [num]
                for block in row[-2::-1]:
                    if block == num:
                        new_row[-1] = block * 2
                        num = 0
                    else:
                        new_row.append(block)
                        num = block

                board[i] = [0] * (n - len(new_row)) + new_row[::-1]

    # 위쪽3 & 아래쪽4
    else:
        for j in range(n):
            col = []
            for i in range(n):
                if board[i][j]:
                    col.append(board[i][j])
            if len(col) == 0:
                continue

            if dir == 3:  # 위쪽
                num = col[0]
                new_col = [num]
                for block in col[1:]:
                    if block == num:
                        new_col[-1] = block * 2
                        num = 0
                    else:
                        new_col.append(block)
                        num = block

                new_col = new_col + [0] * (n - len(new_col))
                for i in range(n):
                    board[i][j] = new_col[i]

            elif dir == 4:  # 아래쪽
                num = col[-1]
                new_col = [num]
                for block in col[-2::-1]:
                    if block == num:
                        new_col[-1] = block * 2
                        num = 0
                    else:
                        new_col.append(block)
                        num = block

                # 채우기
                new_col = [0] * (n - len(new_col)) + new_col[::-1]
                for i in range(n):
                    board[i][j] = new_col[i]

    # dfs & 복구
    dfs(level + 1)
    board = copy.deepcopy(old)


def dfs(level):
    global answer
    if level >= 6:
        # 마지막에 borad의 가장 큰 숫자를 찾으면 됨
        for row in board:
            answer = max(answer, max(row))
        return
    move(1, level)  # 왼쪽
    move(2, level)  # 오른쪽
    move(3, level)  # 위쪽
    move(4, level)  # 아래쪽


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = -1
dfs(1)

print(answer)