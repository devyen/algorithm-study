# 이진 탐색으로 풀었다.
def binary_search(arr, value, low, high):
    if low > high:
        return False  # 탐색 실패
    mid = (low + high) // 2
    if arr[mid] > value:
        return binary_search(arr, value, low, mid-1)
    elif arr[mid] < value:
        return binary_search(arr, value, mid+1, high)
    else:
        return arr[mid]


N = int(input())
nums1 = sorted(list(map(int, input().split())))
M = int(input())
nums2 = list(map(int, input().split()))

for i in range(M):
    print(1 if binary_search(nums1, nums2[i], 0, N-1) else 0)