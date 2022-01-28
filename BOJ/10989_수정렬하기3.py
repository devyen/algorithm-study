import sys
input = sys.stdin.readline

count_list = [0] * 10001  # 1 ~ 10000

N = int(input())
for _ in range(N):
    a = int(input())
    count_list[a] += 1

for i in range(10001):
    if count_list[i]:
        for _ in range(count_list[i]):
            print(i)