from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    heappush(jewels, tuple(map(int, input().split())))  # min heap - 가벼운순
bags = [int(input()) for _ in range(k)]
bags.sort()  # 가벼운순

# 풀이2
result = 0
candidate = []
for b in bags:
    while jewels and b >= jewels[0][0]:
        w, v = heappop(jewels)
        heappush(candidate, -v)  # max heap - value가 높은 순으로

    if candidate:
        result += -heappop(candidate)

print(result)

# 풀이1
# mv_list.sort(key=lambda mv: mv[1], reverse=True)
# bag_weights.sort()
#
# cnt = 0
# result = 0
# i = 0
# check = [0] * k
# while cnt < k and i < n:
#     m, v = mv_list[i]
#     for j in range(k):
#         if m <= bag_weights[j] and not check[j]:
#             check[j] = 1
#             cnt += 1
#             result += v
#             break
#     i += 1