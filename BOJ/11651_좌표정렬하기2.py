import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort(key=lambda point: point[0])
points.sort(key=lambda point: point[1])

for point in points:
    x, y = point
    print(x, y)