import sys
input = sys.stdin.readline

n = int(input())
quests = [int(input()) for _ in range(n)]

stack = []
cals = []
j = 0
for i in range(1, n+1):
    stack.append(i)
    cals.append('+')
    while stack and stack[-1] == quests[j]:
        stack.pop()
        cals.append('-')
        j += 1

if stack:
    # 불가능
    print('NO')
else:
    for cal in cals:
        print(cal)