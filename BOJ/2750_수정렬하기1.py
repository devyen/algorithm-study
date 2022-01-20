# 병합정렬을 이용했다.

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    # 1. 분할
    left = merge_sort(arr[:n // 2])
    right = merge_sort(arr[n // 2:])
    # 2. 병합
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged += left[i:]
    elif j < len(right):
        merged += right[j:]
    return merged


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

for i in merge_sort(arr):
    print(i)
