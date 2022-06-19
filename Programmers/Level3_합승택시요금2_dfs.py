import heapq


def solution(n, s, a, b, fares):
    adj_list = [[] for _ in range(n+1)]  # 0번 인덱스는 빈칸
    for fare in fares:
        c, d, f = fare
        adj_list[c].append((d, f))  # [노드, 비용]
        adj_list[d].append((c, f))

    priority_q = [(0, s)]  # (비용, 노드)
    min_dis = [[float('inf'), []] for _ in range(n+1)]  # 최단거리와 경로를 저장할 배열
    min_dis[s][0] = 0
    while priority_q:
        f, node = heapq.heappop(priority_q)
        if f > min_dis[node][0]:
            continue
        for next in adj_list[node]:
            cost = min_dis[node][0] + next[1]
            if min_dis[next[0]][0] > cost:
                min_dis[next[0]][0] = cost
                min_dis[next[0]][1] = min_dis[node][1] + [node]
                heapq.heappush(priority_q, (cost, next[0]))


    answer = 0
    return answer


result = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(result)