# 이진 탐색1: 재귀함수로 구현 -> 이게 더 메인인 것 같음
def binary_search_recursion(target, s, e):
    if s > e:
        return None  # 탐색 실패

    mid = (s+e)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursion(target, s, mid-1)
    else:
        return binary_search_recursion(target, mid+1, e)


# 이진 탐색2: 반복문으로 구현
def binary_search_loop(target, s, e):
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid-1
        else:
            s = mid+1
    return None


n, target = 10, 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result1 = binary_search_recursion(target, 0, n-1)
print(result1)
result2 = binary_search_loop(target, 0, n-1)
print(result2)
