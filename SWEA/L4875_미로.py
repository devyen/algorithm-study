import sys
sys.stdin = open('input.txt')


def go(i, j):
    visited[i][j] = True

    if maze[i][j] == '3':  # 도착지에 도착했으면
        return 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if maze[ni][nj] == 0 and not visited[ni][nj]:
            go(ni, nj)

    for new_v in graph[v]:
        if not visited[new_v]:
            go(new_v)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [input() for _ in range(n)]  # ['13101', '10101', '10101', '10101', '10021']

    for i in maze:
        for j in i:
            if j == '2':  # 출발지
                S = (i, j)
            elif j == '3':  # 도착지
                G = (i, j)

    visited = [[0] * n for _ in range(n)]

    go(S[0], S[1])





