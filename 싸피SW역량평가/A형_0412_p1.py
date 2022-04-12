'''
point
그렇게 어렵진 않고 백트래킹을 잘하면 되는 문제였음
1. input 크기가 커지면 코드실행이 안 끝남 -> 원인: 가지 치기 할 때 = 을 안 써서 제대로 가지 치기가 안됨. = 의 중요성을 직접 느꼈다!!!
2. 가지 치기를 2번 함
'''


def find_goal():  # 도착점 찾기
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 3:
                goal = (r, c)
                return goal


def dfs(i, j, h):
    global min_h
    if h >= min_h:  # 가지 치기
        return
    if (i, j) == (n-1, 0):
        min_h = min(min_h, h)
        return

    visited[i][j] = 1  # 방문체크

    # 상하이동
    for di in range(1, n-1):  # 작은 높이부터 순차적으로 탐색
        if di >= min_h:  # 가지 치기
            break
        for ni in (i+di, i-di):  # 아래쪽부터 탐색 (출발점이 좌하단이므로)
            if 0 <= ni < n and matrix[ni][j] and not visited[ni][j]:
                dfs(ni, j, max(h, di))

    # 좌우이동
    for dj in (-1, 1):  # 왼쪽부터 탐색 (출발점이 좌하단이므로)
        nj = j+dj
        if 0 <= nj < m and matrix[i][nj] and not visited[i][nj]:
            dfs(i, nj, h)

    visited[i][j] = 0  # 방문해제


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    goal_r, goal_c = find_goal()

    min_h = float('inf')
    dfs(goal_r, goal_c, 0)  # 도착점에서 시작
    print(f'#{t} {min_h}')