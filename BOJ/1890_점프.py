import sys
input = sys.stdin.readline


def go(i, j):
    global result

    if i >= n or j >= n:
        return

    v = matrix[i][j]
    if v == 0:  # 종착지
        result += 1
        return

    go(i, j+v)  # 오른쪽 이동
    go(i+v, j)  # 아래 이동


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = 0
go(0, 0)

print(result)

