import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while queue:
        num, t = queue.popleft()
        if num == k:
            return t

        for next_num in [num-1, num+1, num*2]:
            if next_num == k:
                return t+1
            if 0 <= next_num <= 100000 and not check[next_num]:
                queue.append((next_num, t+1))
                check[next_num] = 1  # 방문체크


n, k = map(int, input().split())

check = [0] * 100001
queue = deque([(n, 0)])  # (현재 숫자, 걸린 시간)
print(bfs())