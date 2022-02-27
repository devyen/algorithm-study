import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = sorted(prices[:-1])[0]

result = 0
i = 0
while i < n:
    if prices[i] == min_price:  # 기름값이 가장 낮은 도시이면
        result += prices[i] * sum(distances[i:])  # 남은 거리만큼 다 주유하고 종료
        break

    e = i+1
    while prices[i] < prices[e]:
        e += 1
    result += prices[i] * sum(distances[i:e])
    i = e

print(result)