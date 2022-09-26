import sys
sys.stdin = open('input.txt')


# 이진탐색 - 재귀
def binary_search(arr, l, r, key):
    global flag
    global prev
    if l == r and arr[l] != key:  # 길이가 1이지만 key값을 찾지 못했을 때 => 탐색 실패
        return

    m = (l+r)//2
    if arr[m] == key:
        flag = 1
        return

    elif arr[m] > key:  # 가운데값이 key보다 크면
        now = 'left'
        if prev == now:
            return
        prev = now
        binary_search(arr, l, m-1, key)  # 왼쪽 탐색
    else:  # 가운데값이 key보다 작으면
        now = 'right'
        if prev == now:
            return
        prev = now
        binary_search(arr, m+1, r, key)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # 정렬된 리스트. 정렬 필요? => 필요함.. 안하면 test case 중 오류남
    B = list(map(int, input().split()))

    cnt = 0
    for num in B:
        prev = None
        flag = 0
        binary_search(A, 0, n-1, num)

        if flag:
            cnt += 1

    print(f'#{tc} {cnt}')