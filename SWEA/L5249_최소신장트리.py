import sys
sys.stdin = open('input.txt')


def make_set(x):
    p[x] = x


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)


def mst_kruskal(G):
    mst = []  # 최소신장트리를 구성하는 간선들의 집합

    for i in range(V+1):  # 상호배타집합 생성
        make_set(i)

    mst_cost = 0

    while len(mst) < V:
        u, v, val = G.pop(0)
        if find_set(u) != find_set(v):  # 둘이 같은 집합인지 검사
            union(u, v)
            mst.append((u, v))
            mst_cost += val

    return mst_cost


T = int(input())
for tc in range(1, T+1):
    V, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]

    edges.sort(key=lambda x: x[2])  # 가중치에 따라 오름차순으로 정렬

    p = [0] * (V + 1)  # 인덱스가 원소, 값이 부모

    print(f'#{tc} {mst_kruskal(edges)}')