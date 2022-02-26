from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
mv_list = [tuple(map(int, input().split())) for _ in range(n)]
bag_weights = [int(input()) for _ in range(k)]

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

# 풀이2
mv_list.sort()
bag_weights.sort()

for i in range(k):
    max_heap = []
    weight = bag_weights[i]
    for j in range(n):
        if mv_list[j][0] <= weight:
            heappush(max_heap, (-mv_list[j][1]))


print(result)






