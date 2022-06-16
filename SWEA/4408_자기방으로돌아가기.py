import sys

sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n = int(input())  # 돌아갈 사람 수

    students = [list(map(int, input().split())) for _ in range(n)]

    # 경로가 겹치는지 아닌지 보기 위해 복도 배열을 만든다
    hallway = [0] * 200
    i = 0
    while i < n:

        s, g = students[i]  # [1, 4]
        if s > g:  # s가 g보다 큰 경우 자리를 바꿔줌
            s, g = g, s

        for h in range((s-1)//2, (g-1)//2+1):  # 사용한 복도 체크
            hallway[h] += 1

        i += 1

    print(f'#{tc} {max(hallway)}')