import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]  # 우,하,좌,상
    dy = [1, 0, -1, 0]

    total = 0
    for i in range(len(arr)):  # i <- 0 ~ 4
        for j in range(len(arr[0])):  # j <- 0 ~ 4
            abs_sum = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:  # 이거 맞았다!ㅠㅠ
                    abs_sum += abs(arr[nx][ny] - arr[i][j])  # 한 요소의 절댓값 총합
            total += abs_sum

    print(f'#{tc} {total}')
