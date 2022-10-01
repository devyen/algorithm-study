import sys
sys.stdin = open('input.txt')


def comb(n, r):
    if r == 0:  # r개를 다 뽑으면 조합 완성
        combinations.append(tuple(tmp))
    elif n < r:
        return
    else:
        tmp[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    result = 987654321

    # 조합 구하기
    combinations = []  # [(3, 4), (2, 4), (1, 4), (2, 3), (1, 3), (1, 2)]
    arr = [i for i in range(1, n+1)]
    tmp = [0] * (n//2)
    comb(n, n//2)

    # 모든 경우를 돌며 맛 차이 최소값 구하기
    for case in combinations:  # case = (3, 4)
        A = case
        # 나머지는 B로
        B = []
        for i in range(1, n+1):
            if i not in case:
                B.append(i)
        # A의 맛 합 구하기
        sum_a = 0
        for r in A:
            for c in A:
                sum_a += matrix[r][c]
        # B의 맛 합 구하기
        sum_b = 0
        for r in B:
            for c in B:
                sum_b += matrix[r][c]

        result = min(result, abs(sum_a - sum_b))

    print(f'#{tc} {result}')