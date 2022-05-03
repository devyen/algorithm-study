import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]  # 0으로 채워진 N * N 배열을 만든다.

    # 방향순서: 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    i, j = 0, -1  # snail[0][0] 왼쪽인 snail[0][-1]을 시작점으로 잡는다.
    k = 0  # dy, dx의 인덱스
    cnt = 1  # 채워넣을 숫자
    while cnt <= N**2:

        ni = i + dy[k]  # 새로 이동할 자리의 i
        nj = j + dx[k]  # 새로 이동할 자리의 j

        # 조건1 : ni, nj가 0보다 크고 N보다 작아야 인덱스를 벗어나지 않는다.
        # 조건2 : 새로 이동할 자리가 0이어야 한다. (0이 아니면 이미 지나간 자리라는 것)
        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
            snail[ni][nj] = cnt
            i, j = ni, nj  # i, j 갱신
            cnt += 1
        else:
            k = (k + 1) % 4

    print(f'#{tc}')
    for i in snail:
        for j in i:
            print(j, end = ' ')
        print()