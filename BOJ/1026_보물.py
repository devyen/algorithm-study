import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(enumerate(map(int, input().split())))  # (인덱스, 값)

sorted_B = sorted(B, key=lambda b: b[1])  # 값으로 정렬
sorted_A = sorted(A, reverse=True)
tmp = []
for i in range(n):
    tmp.append((sorted_B[i][0], sorted_A[i]))  # (인덱스, 값)
final_A = sorted(tmp, key=lambda t: t[0])  # 인덱스로 정렬

result = 0
for i in range(n):
    result += final_A[i][1] * B[i][1]
print(result)