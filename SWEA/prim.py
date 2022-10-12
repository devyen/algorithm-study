import sys
sys.stdin = open('input.txt')


def prim():
    # 일단 0번 정점을 시작으로 고른다.
    now = 0
    mst = [0]
    total = 0
    while len(mst) < v+1:
        min_edge = 11  # 가중치의 최대값이 10이기 때문
        for tmp in adj_list[now]:
            if tmp[0] in mst:  # 해당 정점이 이미 mst에 있으면 continue
                continue
            if tmp[1] < min_edge:  # 0번 정점과 연결되어있고, 가중치가 min_edge보다 크면
                min_edge = tmp[1]
                select = tmp[0]
        # 최소비용 간선이 존재하는 정점 선택
        p[find_set(select)] = find_set(now)
        mst.append(select)
        total += min_edge
        now = select

    return total


def find_set(x):  # path compression 최적화
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())  # v: 마지막 노드번호, e: 간선 개수
    # edges = [list(map(int, input().split())) for _ in range(e)]
    adj_list = [[] for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append([n2, w])

    p = list(range(v + 1))  # 각 정점의 대표를 나타내는 배열. make_set

    print(f'#{tc} {prim()}')