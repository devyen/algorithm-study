from heapq import heappop, heappush


def solution(n, m, x, y, z):
    def dijkstra(start):
        distance = [[float('inf'), [i]] for i in range(n+1)]
        priority_q = [(0, start)]
        distance[start][0] = 0

        while priority_q:
            d, now = heappop(priority_q)
            if d > distance[now][0]:
                continue
            for next_node in adj_list[now]:
                cost = distance[now][0] + next_node[1]
                if distance[next_node[0]][0] > cost:
                    distance[next_node[0]][0] = cost
                    distance[next_node[0]][1] = distance[now][1] + [next_node[0]]
        routes = []
        for i in range(1, n+1):
            if i == start:
                continue
            routes.append(distance[i][1])
        return routes


    adj_list = [[] for _ in range(n+1)]
    for i in range(m):
        node1, node2, fare = x[i], y[i], z[i]
        adj_list[node1].append((node2, fare))
        adj_list[node2].append((node1, fare))

    routes = []
    for i in range(1, n+1):
        routes += dijkstra(i)

    cnts = {}
    for i in range(1, n+1):
        cnts[i] = 0
    for route in routes:
        for node in route:
            cnts[node] += 1
    sorted_dict = sorted(cnts.items(), key=lambda item: item[1], reverse=True)

    answer = [x[0] for x in sorted_dict]


    return answer


result = solution(3, 3, [1,1,2],[3,2,3],[1,5,2])
print(result)