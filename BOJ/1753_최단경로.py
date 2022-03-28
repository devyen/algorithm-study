import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())  # v 노드 개수, e 간선 개수
k = int(input())  # k 시작 노드
adj_list = [[] for _ in range(v+1)]  # 인접리스트  # 0번 인덱스는 빈칸
for _ in range(e):
    v1, v2, w = map(int, input().split())
    adj_list[v1].append((v2, w))  # (노드번호, 가중치)

priority_q = []  # 우선순위 큐  # (거리, 노드번호)
distances = [float('inf')]*(v+1)  # 최단거리를 저장할 배열

# 시작점 k 방문
distances[k] = 0
heapq.heappush(priority_q, (0, k))

# 남은 v-1개의 노드를 모두 방문
while priority_q:
    d, now = heapq.heappop(priority_q)
    if d > distances[now]:  # 큐에 저장돼있는 거리가 이미 갱신된 거리보다 클 경우 무시
        continue
    for next in adj_list[now]:  # next: 연결된 노드
        cost = distances[now] + next[1]
        if cost < distances[next[0]]:
            distances[next[0]] = cost
            heapq.heappush(priority_q, (cost, next[0]))  # 거리가 갱신될 경우에만 큐에 넣는다.

for i in range(1, v+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])