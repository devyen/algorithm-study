import sys
input = sys.stdin.readline

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

for num2 in nums2:
    cnt = 0
    for num1 in nums1:
        if num1 == num2:
            cnt += 1
    print(cnt, end=' ')