import sys
sys.stdin = open('input.txt')

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))  #우하좌상


def hit(i, row, col):
    global tmp
    ## 구슬치기 1번할 때 루틴
    # 1. 폭발
    # stack = []
    bomb(row, col)  # 스타트 벽돌 치기
    while stack:  # 영향 받은 벽돌 다 터트리기
        tr, tc = stack.pop()
        bomb(tr, tc)
    # 2. 남은 벽돌 재위치
    replace_bricks()

    if i == n:
        # 남은 벽돌 개수 구하기
        cnt = 0
        for r in range(h):
            for c in range(w):
                if matrix[r][c]:
                    cnt += 1
        tmp = min(tmp, cnt)

    else:
        for col in range(w):
            for row in range(h):  # 위에서부터 탐색하면서
                hit(i+1, row, col)


def bomb(r, c):
    power = matrix[r][c]  # 폭발력 == 폭발 범위
    for d in DIRECTION:  # 오른쪽부터
        for _ in range(power):  # power 범위만큼 작업
            nr, nc = r + d[0], c + d[1]  # 한칸 이동
            if 0 <= nr < h and 0 <= nc < w:
                if matrix[nr][nc] > 1:  # 1은 폭파범위가 없으므로 2부터 담기
                    stack.append([nr, nc])
                matrix[nr][nc] = 0  # 전부 0으로 만들어준다


def replace_bricks():
    for c in range(w):
        blank = 0
        for r in range(h-1, -1, -1):
            now = matrix[r][c]
            if now:  # 빈값이 아니면
                matrix[blank][c] = now  # 블럭 옮기기
                matrix[r][c] = 0
                blank -= 1
                continue
            if not blank:  # blank가 아직 0이면 == 처음 나온 빈값
                blank = r


T = int(input())
for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]

    # 완전 탐색
    result = float('inf')
    for col in range(w):
        for row in range(h):  # 위에서부터 탐색하면서
            if matrix[row][col]:  # 0이 아닌 벽돌을 만나면
                stack = []
                tmp = float('inf')
                hit(1, row, col)
                result = min(result, tmp)

    print(f'#{tc} {result}')