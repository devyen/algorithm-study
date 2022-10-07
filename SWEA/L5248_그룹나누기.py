import sys
sys.stdin = open('input.txt')


def make_set(x):
    p[x] = x


def find_set(x):  # path compression
    if x != p[x]:
        p[x] = find_set(p[x])  # 호출된 함수가 리턴하면서 경로에 존재하는 노드가 루트를 부모로 가리키도록 갱신!
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    pairs = list(map(int, input().split()))

    # 먼저 각각을 서로소 집합으로 만들기
    p = [0] * (n + 1)
    for i in range(1, n+1):
        make_set(i)
    # p = [i for i in range(n+1)]
    # p = list(range(n+1))

    for j in range(m):
        union(pairs[j*2], pairs[j*2+1])

    # 그룹 수 세기
    groups = []
    for k in range(1, n+1):  # 1번부터 n번까지니까
        groups.append(find_set(k))
    # 방법2
    # ans = 0
    # for k in range(1, n+1):
    #     if k == p[k]:
    #         ans += 1

    print(f'#{tc} {len(set(groups))}')