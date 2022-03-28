import sys
import heapq
input = sys.stdin.readline


def Dijkstra():
    priority_q = []  # 우선순위 큐  # (거리, i, j)
    distances = [[float('inf')]*n for _ in range(n)]  # 최단거리를 저장할 배열

    # 시작점 [0][0] 방문
    distances[0][0] = matrix[0][0]
    heapq.heappush(priority_q, (matrix[0][0], 0, 0))

    while priority_q:
        dis, i, j = heapq.heappop(priority_q)
        if dis > distances[i][j]:  # 큐에 저장돼있는 거리가 이미 갱신된 거리보다 클 경우 무시
            continue
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                cost = distances[i][j] + matrix[ni][nj]
                if cost < distances[ni][nj]:
                    distances[ni][nj] = cost
                    heapq.heappush(priority_q, (cost, ni, nj))  # 거리가 갱신될 경우에만 큐에 넣는다.
    return distances[-1][-1]


t = 0
while True:
    t += 1
    n = int(input())
    if not n:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(f'Problem {t}: {Dijkstra()}')
