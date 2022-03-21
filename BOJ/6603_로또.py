import sys

input = sys.stdin.readline


def comb(idx, check, cnt):
    # base case
    if cnt == 6:
        c = []
        for i in range(k):
            if check[i]:
                c.append(s[i])
        result.append(c)
        return

    if idx == k:
        return

    # idx번째 원소 미포함
    comb(idx + 1, check, cnt)

    # idx번째 원소 포함
    check[idx] = 1
    comb(idx + 1, check, cnt + 1)
    check[idx] = 0


while True:
    s = list(map(int, input().split()))
    k = s.pop(0)  # s의 길이
    if k == 0:
        break

    # k개 중에서 6개를 고르는 조합
    tmp = [0] * k
    result = []
    comb(0, tmp, 0)

    result.sort()
    for a in result:
        print(' '.join(map(str, a)))
    print()