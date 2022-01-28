# 1920과 동일. 이진탐색.
# 출력에 join을 써봄.
def binary_search(A, value, low, high):
    if low > high:  # 탐색실패
        return False
    mid = (low+high)//2
    if A[mid] > value:
        return binary_search(A, value, low, mid-1)
    elif A[mid] < value:
        return binary_search(A, value, mid+1, high)
    else:
        return True


N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))

result = []
for a in arr2:
    # print(1 if binary_search(arr1, a, 0, len(arr1)-1) else 0, end=" ")
    if binary_search(arr1, a, 0, len(arr1)-1):  # high에 len(arr1)이라고 넣는 실수 주의
        result.append(1)
    else:
        result.append(0)
print(" ".join(map(str, result)))