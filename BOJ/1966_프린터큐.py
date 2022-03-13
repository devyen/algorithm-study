import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))

    queue = deque()
    for t in enumerate(tmp):
        queue.append(t)

    cnt = 0
    while queue:
        flag = 0
        front = queue[0]
        for q in queue:
            if q[1] > front[1]:
                queue.append(queue.popleft())  # queue 가장 뒤에 재배치
                flag = 1
                break
        if not flag:
            out = queue.popleft()
            cnt += 1
            if out[0] == m:
                print(cnt)