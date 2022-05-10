import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(a)
    cnt = 0
    # 부분집합 만들기
    for i in range(2**n):
        sub = []
        for j in range(n):
            if i & (1<<j):
                sub.append(a[j])

        if len(sub) == N:
            total = 0
            for sub_i in sub:
                total += sub_i
            if total == K:
                cnt += 1

    print(f'#{tc} {cnt}')
