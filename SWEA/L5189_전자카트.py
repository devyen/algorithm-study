import sys
sys.stdin = open('input.txt')


def perm(n, k):  # 2부터 n까지 순열 생성
    if k == n:  # 순열 완성
        routes.append([1] + sections + [1])
    else:
        for i in range(k, n):
            sections[k], sections[i] = sections[i], sections[k]
            perm(n, k+1)
            sections[k], sections[i] = sections[i], sections[k]


def get_min_total(routes):
    min_total = float("inf")  # 무한대값으로 최소값 설정
    for route in routes:
        total = 0
        for i in range(n):
            total += energy[route[i]][route[i+1]]
            if total > min_total:  # 최소값을 넘어버리면 break
                break
            if i == n-1:  # 끝까지 구했다면
                min_total = total

    return min_total


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # energy: 배터리 사용량 정보. 0번 인덱스는 비워둠
    energy = [[0*(n+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

    # 1. 순열로 경로 생성
    # [1, 2, 3, 1], [1, 3, 2, 1] -> 2개 경로
    sections = [i for i in range(n + 1)[2:]]  # 1번(사무실)은 출발점이자 도착점이 될 것이므로 일단 제외
    routes = []
    perm(n-1, 0)  # 1번 제외하므로 n-1을 넣어준다

    # 2. 배터리 소비량 계산
    print(f'#{tc} {get_min_total(routes)}')