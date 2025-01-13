n, m = map(int, input().split())
i, j, d = map(int, input().split())  # 1 1 0
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[i][j] = 1  # 현재 좌표 방문 체크

dd = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 좌하우상 순서

result = 1
while True:
    flag = 0
    for k in range(4):  # 4방향 탐색
        nd = (d+k)%4
        di, dj = dd[nd]
        ni, nj = i+di, j+dj
        if matrix[ni][nj] == 0 and not visited[ni][nj]:
            i, j = ni, nj
            visited[i][j] = 1  # 방문 체크
            result += 1
            flag = 1
            break

    if not flag:  # 4방향 모두 이동하지 않은 경우
        di, dj = dd[d]
        ni, nj = i+(di*-1), j+(dj*-1)  # 뒤로 이동
        if matrix[ni][nj] == 0:
            i, j = ni, nj
        else:
            break  # 뒤쪽이 바다인 경우 멈춘다
    else:
        d = nd

print(result)