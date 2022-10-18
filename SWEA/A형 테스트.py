import sys
sys.stdin = open('input.txt')

# 어려웠다....ㅠㅠㅠ 역시 A형은 어렵다. 엄청 오래 걸려서 알고리즘 만들고

def make_roads(road1, road2):
    # n1, n2 -> 첫 번째 직통노선의 두 역
    # n3, n4 -> 두 번째 직통노선의 두 역
    n1, n2 = min(road1[0], road1[1]), max(road1[0], road1[1])  # n1 < n2 가 되도록 해야함(안하면 테스트케이스 중에 답이 틀린 것이 나옴)
    n3, n4 = min(road2[0], road2[1]), max(road2[0], road2[1])

    # 조건4) 역이 겹치면 안됨
    if n3 in road1[:2] or n4 in road1[:2]:
        return

    # 조건3) 인접한 두 역에서 출발하거나 도착할순 없음
    flag = 0
    for i in (n1, n2):  # 모든 조합을 해봐야함
        for j in (n3, n4):
            if abs(i - j) == 1 or abs(i - j) == n - 1:  # 0이나 n-1인 경우 앞뒤의 차이가 n-1이 된다.
                flag = 1
                break
    if flag:
        return

    # 조건1) 직통노선은 서로 교차할 수 없음
    if n1 < n3 < n2 and (n4 < n1 or n4 > n2):
        return
    if n1 < n4 < n2 and (n3 < n1 or n3 > n2):
        return

    # 모든 가지치기를 통과했으면 타당도를 리턴
    return road1[2] + road2[2]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    stations = list(map(int, input().split()))

    # 직통노선 후보들을 구한다.
    check = [[0] * n for _ in range(n)]
    roads = []
    for n1 in range(n):
        for n2 in range(n):
            if n2 == n1 or abs(n1 - n2) == 1 or abs(n1 - n2) == n - 1 and check[n1][n2]:
                continue
            # n1, n2로 직통노선을 하나 만든다.
            check[n1][n2] = check[n2][n1] = 1  # 중복 방지를 위해 체크
            w = (stations[n1] + stations[n2])**2
            roads.append([n1, n2, w])

    # 조건을 맞추며 2개의 직통노선을 선택한다.
    max_w = -1
    for road1 in roads:  # road1 == [0, 2, 21025]
        for road2 in roads:  # road2 == [0, 3, 18225]
            if road2 == road1:  # 같은건 패스
                continue
            result = make_roads(road1, road2)  # 둘의 조합이 가능하면, 타당도의 합을 리턴
            if result:
                max_w = max(max_w, result)

    print(f'#{tc} {max_w}')