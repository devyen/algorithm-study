from collections import deque


def solution(n, clockwise):
    if clockwise:
        # 시계
        # 우 하 좌 상
        DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, 0, 1), (0, n - 1, 1, 1), (n - 1, n - 1, 2, 1), (n - 1, 0, 3, 1)])
    else:
        # 반시계
        # 하 우 상 좌
        DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(0, 0, 0, 1), (n - 1, 0, 1, 1), (n - 1, n - 1, 2, 1), (0, n - 1, 3, 1)])
    
    graph = [[0] * n for _ in range(n)]

    while queue:
        y, x, d, num = queue.popleft()
        if graph[y][x]:
            continue
        graph[y][x] = num

        dy, dx = DELTA[d]
        ny, nx = y + dy, x + dx

        if graph[ny][nx]:
            d = (d + 1) % 4
            dy, dx = DELTA[d]
            ny, nx = y + dy, x + dx
            if graph[ny][nx]:
                continue

        queue.append((ny, nx, d, num + 1))

    print(graph)


n = int(input())
solution(n, True)