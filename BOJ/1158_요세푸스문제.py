from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque(range(1, n+1))

josephus = []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    josephus.append(queue.popleft())

print('<' + ', '.join(map(str, josephus)) + '>')