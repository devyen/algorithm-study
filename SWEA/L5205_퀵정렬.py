import sys
sys.stdin = open('input.txt')

# 런타임 에러 남
# l, r을 쓰지 않는 방법
def quick_sort(a):
    if len(a) > 1:
        s = partition(a)
        # 양쪽을 따로 재귀 돌린다
        # ★ l, r을 쓰지 않고 배열 a를 슬라이싱할 경우, 재귀 돌린 각 부분을 하나로 합쳐 result를 따로 만든 다음 그걸 리턴해야함
        result = quick_sort(a[:s]) + [a[s]] + quick_sort(a[s+1:])
        return result
    # 길이가 1이하이면 그대로 a를 리턴
    return a


def partition(a):
    # partition 파트
    pivot = a[0]  # 가장 왼쪽 값을 피봇으로
    i, j = 0, len(a) - 1

    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        # i랑 j랑 교환
        if i < j:
            a[i], a[j] = a[j], a[i]

    # j < i 가 되면 피봇과 j를 교환
    a[0], a[j] = a[j], a[0]

    return j


def quick_sort(a, l, r):
    if l < r:  # 정렬할 구간이 남아있으면
        s = partition(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)
    return a


# partition 부분을 quick_sort 안에 넣는 것도 가능함!
def partition(a, l, r):
    pivot = a[l]
    i, j = l, r

    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] >= pivot:
            j -= 1
        # i랑 j랑 교환
        if i < j:
            a[i], a[j] = a[j], a[i]

    # j < i 가 되면 피봇과 j를 교환
    a[l], a[j] = a[j], a[l]

    return j


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    A = quick_sort(a, 0, n-1)

    # A[n//2]번 원소를 출력
    print(f'#{tc} {A[n//2]}')