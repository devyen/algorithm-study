def solution(user_id, banned_id):
    def compare(id, pattern):
        if len(id) != len(pattern):
            return False
        for i in range(len(id)):
            if pattern[i] != '*' and id[i] != pattern[i]:
                return False
        return True

    def dfs(level, comb):
        # base case
        if level == len(banned_id)-1:
            cases.add(tuple(sorted(comb)))
            return
        for nj in range(len(graph[level+1])):
            if graph[level+1][nj] not in comb:
                dfs(level+1, comb+[graph[level+1][nj]])

    graph = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if compare(user, ban):
                tmp.append(user)
        graph.append(tmp)

    cases = set()
    for j in range(len(graph[0])):
        dfs(0, [graph[0][j]])

    return len(cases)


result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(result)