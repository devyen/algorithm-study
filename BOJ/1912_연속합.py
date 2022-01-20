import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = arr[0]
s = 0
for i in range(n):
    s = max(s+arr[i], arr[i])
    if s > result:
        result = s

print(result)