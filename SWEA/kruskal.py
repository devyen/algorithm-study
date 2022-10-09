import sys
sys.stdin = open('input.txt')


def kruskal():
    # 간선 하나를 선택
    cnt = 0  # 선택한 간선의 개수
    total = 0  # 가중치의 합
    while cnt < v:
        w, n1, n2 = edges.pop(0)  # 1, 0, 1
        if find_set(n1) != find_set(n2):  # 둘이 같은 집합에 속해있지 않으면 -> union
            p[find_set(n2)] = find_set(n1)
            cnt += 1
            total += w

    return total


def find_set(x):  # path compression 최적화
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())  # v: 마지막 노드번호, e: 간선 개수
    edges = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append([w, n1, n2])  # 가중치로 정렬하기 위해 가중치를 첫 번째 요소로 넣음
    edges.sort()  # 가중치로 오름차순 정렬

    p = list(range(v + 1))  # 각 정점의 대표를 나타내는 배열. make_set

    print(f'#{tc} {kruskal()}')