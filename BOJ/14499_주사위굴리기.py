import sys
input = sys.stdin.readline


def move(x, y, top, east, south, order):
    if order == 1:  # 동쪽
        nx, ny = x, y+1
        ntop = 7-east
        neast = top
        nsouth = south
    elif order == 2:  # 서쪽
        nx, ny = x, y-1
        ntop = east
        neast = 7-top
        nsouth = south
    elif order == 3:  # 북쪽
        nx, ny = x-1, y
        ntop = south
        neast = east
        nsouth = 7-top
    else:  # 남쪽
        nx, ny = x+1, y
        ntop = 7-south
        neast = east
        nsouth = top

    if 0 <= nx < n and 0 <= ny < m:
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = dice[7-ntop]
        else:
            dice[7-ntop] = matrix[nx][ny]
            matrix[nx][ny] = 0
        print(dice[ntop])
        return nx, ny, ntop, neast, nsouth
    else:
        return x, y, top, east, south


n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dice = [0]*7
top, east, south = 1, 3, 5  # 인덱스
for o in orders:
    x, y, top, east, south = move(x, y, top, east, south, o)
