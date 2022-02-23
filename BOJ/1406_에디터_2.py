# 2개의 스택

import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []

m = int(input())
for _ in range(m):
    tmp = input().split()
    command = tmp[0]
    if command == 'L' and stack1:
        stack2.append(stack1.pop())
    elif command == 'D' and stack2:
        stack1.append(stack2.pop())
    elif command == 'B' and stack1:
        stack1.pop()
    elif command == 'P':
        stack1.append(tmp[1])

print(''.join(stack1 + stack2[::-1]))
