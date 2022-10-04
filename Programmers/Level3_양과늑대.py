def solution(info, edges):
    def dfs(node, sheep, wolf):
        nonlocal nexts, answer
        if wolf and wolf >= sheep:
            return
        if node >= len(info):
            return

        answer = max(answer, sheep)

        check[node] = 1
        tmp = nexts
        nexts = nexts + adj_list[node]

        for next_node in nexts:
            if check[next_node]:
                continue
            if info[next_node]:  # 1 늑대
                dfs(next_node, sheep, wolf+1)
            else:  #  0 양
                dfs(next_node, sheep+1, wolf)

        check[node] = 0
        nexts = tmp

    adj_list = [[] for _ in range(len(info))]  # 인접리스트
    for edge in edges:
        p, c = edge
        adj_list[p].append(c)

    nexts = []
    check = [0]*len(info)
    answer = 0
    dfs(0, 1, 0)
    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))