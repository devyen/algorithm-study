def solution(n, m, a, b, c, d):
    # 부모 테이블
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    # find
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    # union
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edges = []
    total_cost = 0
    t = 1
    for i in range(m):
        cost = c[i] * t + d[i]
        edges.append((cost, a[i], b[i]))
    edges.sort()

    mst = []
    for i in range(m):
        cost, a, b = edges[i]
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            total_cost += cost
            mst.append(i)

    p = parent[1]
    for i in range(2, n + 1):
        if parent[i] != p:
            return 'NONE'

    answer = ''
    c_sum = 0
    t = float('inf')
    for i in mst:
        c_sum += c[i]

    if c_sum >= 1:
        answer = '1'
    if c_sum == 0:
        answer = '-INF'
    elif c_sum < 0:
        answer = 'INF'

    return answer


print(solution(2, 2, [1, 1], [2, 2], [0, 1], [1, 0]))