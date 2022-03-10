import sys
input = sys.stdin.readline


def is_vps(ps):
    stack = []
    for a in ps:
        if a == '(':
            stack.append(a)
        else:
            if not stack:
                return 'NO'
            stack.pop()

    if stack:
        return 'NO'
    else:
        return 'YES'


T = int(input())
for _ in range(T):
    ps = input().rstrip()
    result = is_vps(ps)
    print(result)