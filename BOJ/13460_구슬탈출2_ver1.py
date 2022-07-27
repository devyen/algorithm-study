import sys
input = sys.stdin.readline

# board를 직접 수정하고 복구하는 버전

def move(di, dj, red, blue, level):
    global answer
    if level >= answer:
        return

    ri, rj = red
    bi, bj = blue
    nri, nrj = ri, rj
    nbi, nbj = bi, bj

    # 파란구슬
    cnt = 0
    while True:
        nbi += di
        nbj += dj
        if board[nbi][nbj] == 'O':  # 실패
            return
        if board[nbi][nbj] == 'R':
            cnt += 1
        if board[nbi][nbj] == '#':
            for _ in range(cnt+1):
                nbi -= di
                nbj -= dj
            break

    # 빨간구슬
    cnt = 0
    while True:
        nri += di
        nrj += dj
        if board[nri][nrj] == 'O':  # 성공
            answer = min(answer, level)  # 최소값 갱신
            return
        if board[nri][nrj] == 'B':
            cnt += 1
        if board[nri][nrj] == '#':
            for _ in range(cnt + 1):
                nri -= di
                nrj -= dj
            break

    if (bi, bj) == (nbi, nbj) and (ri, rj) == (nri, nrj):
        return

    # 새로운 자리에 구슬 채우기
    board[bi][bj] = '.'
    board[ri][rj] = '.'

    board[nbi][nbj] = 'B'
    board[nri][nrj] = 'R'

    # board[nbi][nbj], board[bi][bj] = board[bi][bj], board[nbi][nbj]
    # board[nri][nrj], board[ri][rj] = board[ri][rj], board[nri][nrj]

    dfs((nri, nrj), (nbi, nbj), level)

    # 복구
    board[nbi][nbj] = '.'
    board[nri][nrj] = '.'

    board[bi][bj] = 'B'
    board[ri][rj] = 'R'

    # board[nbi][nbj], board[bi][bj] = board[bi][bj], board[nbi][nbj]
    # board[nri][nrj], board[ri][rj] = board[ri][rj], board[nri][nrj]
    return


def dfs(red, blue, level):
    if level >= 10:
        return
    move(0, -1, red, blue, level+1)  # 왼쪽
    move(0, 1, red, blue, level+1)  # 오른쪽
    move(-1, 0, red, blue, level+1)  # 위쪽
    move(1, 0, red, blue, level+1)  # 아래쪽


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
        if board[i][j] == 'B':
            blue = (i, j)

answer = float('inf')
dfs(red, blue, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)