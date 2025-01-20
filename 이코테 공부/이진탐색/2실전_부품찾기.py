import sys
input = sys.stdin.readline


def binary_search(value, low, high):
    if low > high:
        return False
    mid = (low + high)//2
    if arr[mid] > value:
        return binary_search(value, low, mid-1)
    elif arr[mid] < value:
        return binary_search(value, mid+1, high)
    else:
        return True


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()  # 정렬

for target in targets:
    if binary_search(target, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
