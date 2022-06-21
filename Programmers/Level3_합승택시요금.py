from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    def dijkstra(start):  # x에서부터 다른 모든 노드들까지의 최소 비용을 구한다.
        distance = [float('inf')] * (n + 1)  # 최단거리와 경로를 저장할 배열
        priority_q = [(0, start)]  # (비용, 노드)
        distance[start] = 0

        while priority_q:
            d, now = heappop(priority_q)
            if d > distance[now]:
                continue
            for next in adj_list[now]:
                cost = distance[now] + next[1]
                if distance[next[0]] > cost:  # 거리 갱신
                    distance[next[0]] = cost
                    heappush(priority_q, (cost, next[0]))

        return distance

    adj_list = [[] for _ in range(n+1)]  # 0번 인덱스는 빈칸
    for fare in fares:
        node1, node2, f = fare
        adj_list[node1].append((node2, f))  # [노드, 비용]
        adj_list[node2].append((node1, f))

    s_distance = dijkstra(s)
    a_distance = dijkstra(a)
    b_distance = dijkstra(b)

    answer = float('inf')
    for x in range(1, n+1):
        answer = min(answer, s_distance[x] + a_distance[x] + b_distance[x])

    return answer


result = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(result)