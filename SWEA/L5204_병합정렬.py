import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    global cnt
    n = len(arr)

    # 베이스 케이스
    if n == 1:  # 한개만 남았을 때 리턴
        return arr
    # 분할 -> 재귀
    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    # 병합
    i = j = 0
    merged = []
    while i <= len(left) and j <= len(right):
        # 둘 중 한쪽이 끝나면 다른쪽의 남은 부분을 다 병합
        if i == len(left):
            merged += right[j:]
            break
        elif j == len(right):
            merged += left[i:]
            cnt += 1
            break

        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    return merged


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    result = merge_sort(arr)

    print(f'#{tc} {result[n//2]} {cnt}')