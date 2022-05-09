import sys
sys.stdin = open('input.txt')

T = int(input())
n = 10

for tc in range(1, T+1):

    matrix = [[0] * n for _ in range(n)]

    N = int(input())
    cnt = 0  # 겹쳐진 부분(=보라색 칸)
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        i, j = r1, c1
        # 주어진 영역을 차례대로 돌며 color를 채운다
        while i <= r2:
            while j <= c2:
                # 다른 색이 이미 채워져 있는 부분을 만나면 색이 겹쳐지므로 cnt +1
                if matrix[i][j] != color and matrix[i][j] != 0:  # 같은 색이 아니고 0도 아니라면 == 다른색
                    cnt += 1

                matrix[i][j] = color
                j += 1
            j = c1  # 열 순회가 끝나면 j를 다시 시작점으로 리셋
            i += 1

    print(f'#{tc} {cnt}')