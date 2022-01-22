def quick_sort(A):

    if len(A) < 2:
        return A

    criteria = A[-1]
    p1 = []
    p2 = []
    middle = [criteria]
    for a in A[:-1]:
        if a < criteria:
            p1.append(a)
        elif a > criteria:
            p2.append(a)
        else:
            middle.append(a)
    return quick_sort(p1) + middle + quick_sort(p2)


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

sorted_arr = quick_sort(arr)
for num in sorted_arr:
    print(num)