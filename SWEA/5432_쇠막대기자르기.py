import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stick = input().replace('()','|')
    n = len(stick)

    current = 0
    cnt = 0
    for i in range(n):
        if stick[i] == '|':
            cnt += current
        elif stick[i] == '(':
            current += 1
            cnt += 1
        elif stick[i] == ')':
            current -= 1

    print(f'#{tc} {cnt}')