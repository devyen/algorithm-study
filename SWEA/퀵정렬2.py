# append 하는 방법 - 더 직관적
def quick_sort(arr):
    # 베이스 케이스
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽을 피봇으로

    left = []
    right = []
    for i in range(1, len(arr)):  # 피봇 다음부터 순회하면서
        if arr[i] < pivot:  # 피봇보다 작으면 왼쪽에
            left.append(arr[i])
        else:  # 같거나 크면 오른쪽에
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

print(quick_sort(a))
print(quick_sort(b))
print(quick_sort(c))