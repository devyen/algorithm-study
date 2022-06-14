def solution(n, paths, gates, summits):
    def go(i, course, intensity, summit):  # i 방문할 노드, course 지나온 경로, checked 산봉우리 방문여부
        nonlocal min_intensity, ans_summit, adj_list, gates, summits, start
        if len(course) > n+1:
            return
        if intensity > min_intensity:  # 가지치기
            return
        if i == start:
            if summit:
                if min_intensity > intensity:
                    min_intensity = intensity
                    ans_summit = [summit]
                elif min_intensity == intensity:
                    ans_summit.append(summit)
            return
        if i in gates:  # 다른 출입구는 방문x
            return
        if i in summits:
            if summit:  # 산봉우리는 한번만 방문
                return
            else:
                summit = i
        for ni, w in adj_list[i]:
            if ni == i and i not in summits:
                continue
            go(ni, course+[i], max(intensity, w), summit)

    adj_list = [[] for _ in range(n + 1)]  # 인접리스트  # 0번 인덱스는 빈칸
    for path in paths:
        v1, v2, w = path
        adj_list[v1].append((v2, w))  # (노드번호, 가중치)
        adj_list[v2].append((v1, w))  # (노드번호, 가중치)

    min_intensity = float('inf')
    ans_summit = []
    for start in gates:
        for ni, w in adj_list[start]:
            go(ni, [start], w, 0)

    answer = [min(ans_summit), min_intensity]

    return answer


# result = solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])
# result = solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
# result = solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
result = solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
print(result)