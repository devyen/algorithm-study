def solution(v):
    xdic = {}
    ydic = {}

    for i in range(3):
        if xdic.get(v[i][0]) == None:
            xdic[v[i][0]] = 0
        if ydic.get(v[i][1]) == None:
            ydic[v[i][1]] = 0
        xdic[v[i][0]] += 1
        ydic[v[i][1]] += 1

    answer = []
    for key, val in xdic.items():
        if val == 1:
            answer.append(key)
    for key, val in ydic.items():
        if val == 1:
            answer.append(key)

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
