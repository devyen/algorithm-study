import sys

sys.stdin = open('input.txt')


def selection_sort_recursive(a, now, n):  # now: 정렬할 인덱스, n: 길이
    if now == n-1:
        return
    # 정렬
    min_idx = now  # 정렬할 인덱스를 최소값으로 잡고 시작
    for j in range(now+1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    a[now], a[min_idx] = a[min_idx], a[now]

    return selection_sort_recursive(a, now+1, n)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    selection_sort_recursive(a, 0, n)

    print(f'#{tc} ', end='')
    for i in a:
