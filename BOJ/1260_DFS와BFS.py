import sys
from collections import deque
input = sys.stdin.readline


def dfs(now):
    check[now] = 1
    print(now, end=' ')
    for i in sorted(adj_list[now]):  # 번호가 작은 정점부터 방문해야함
        if not check[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    check[v] = 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in sorted(adj_list[now]):
            if not check[i]:
                check[i] = 1
                queue.append(i)


n, m, v = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

adj_list = [[] for _ in range(n+1)]
for edge in edges:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])  # 양방향 그래프

# 1. dfs
check = [0] * 1001
dfs(v)
print()

# 2. bfs
check = [0] * 1001
bfs(v)