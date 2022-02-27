import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())  # n: 책의 개수, m: 학생 수
    scopes = [tuple(map(int, input().split())) for _ in range(m)]
    scopes.sort(key=lambda a: a[1])  # 끝범위가 작은 순으로 정렬

    check = [0] * (n+1)
    cnt = 0
    for scope in scopes:
        a, b = scope
        for i in range(a, b+1):
            if not check[i]:
                check[i] = 1
                cnt += 1
                break
    print(cnt)