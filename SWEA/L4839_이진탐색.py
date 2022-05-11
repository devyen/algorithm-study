import sys
sys.stdin = open('input.txt')

def get_binary_cnt(P, goal):
    l, r = 1, P
    cnt = 0

    while True:
        cnt += 1
        c = int((l+r)/2)
        if c == goal:
            break
        elif c > goal:  # c > goal 이면 왼쪽을 탐색한다.
            r = c
        elif c < goal:  # c < goal 이면 오른쪽을 탐색한다.
            l = c

    return cnt


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())  # 400 300 350

    if get_binary_cnt(P, Pa) > get_binary_cnt(P, Pb):
        winner = 'B'
    elif get_binary_cnt(P, Pa) < get_binary_cnt(P, Pb):
        winner = 'A'
    else:
        winner= 0

    print(f'#{tc} {winner}')