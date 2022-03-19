from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()

    reverse = 0
    flag = 0
    for o in p:
        if o == 'R':
            reverse ^= 1
        elif o == 'D':
            if len(arr) == 0:
                print('error')
                flag = 1
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if flag:
        continue

    if reverse:
        arr.reverse()

    print('[' + ','.join(arr) + ']')