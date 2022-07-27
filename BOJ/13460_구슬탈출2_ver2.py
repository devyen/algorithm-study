import sys
input = sys.stdin.readline

# board를 수정하지 않고 R, B 구슬의 위치 정보만 들고다니는 버전

def move(level, bi, bj, ri, rj, di, dj):
    global answer

    # 파란구슬 이동
    Nbi, Nbj = bi, bj
    cnt = 0
    while board[Nbi][Nbj] != '#':
        Nbi += di
        Nbj += dj
        if board[Nbi][Nbj] == 'O':  # 파란구슬이 구멍을 만나면 실패
            return
        if (Nbi, Nbj) == (ri, rj):  # 빨간구슬
            cnt += 1
    for _ in range(cnt+1):
        Nbi -= di
        Nbj -= dj

    # 빨간구슬 이동
    Nri, Nrj = ri, rj
    cnt = 0
    while board[Nri][Nrj] != '#':
        Nri += di
        Nrj += dj
        if board[Nri][Nrj] == 'O':  # 성공
            answer = min(answer, level)
            return
        if (Nri, Nrj) == (bi, bj):  # 다른 구슬
            cnt += 1
    for _ in range(cnt+1):
        Nri -= di
        Nrj -= dj

    if (bi, bj) == (Nbi, Nbj) and (ri, rj) == (Nri, Nrj):  # 이동이 없으면 가지치기
        return

    dfs(level+1, Nbi, Nbj, Nri, Nrj)


def dfs(level, bi, bj, ri, rj):
    if level >= 11:
        return
    if level >= answer:  # 가지치기
        return
    move(level, bi, bj, ri, rj, 0, -1)  # 왼쪽
    move(level, bi, bj, ri, rj, 0, 1)  # 오른쪽
    move(level, bi, bj, ri, rj, -1, 0)  # 위쪽
    move(level, bi, bj, ri, rj, 1, 0)  # 아래쪽


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 빨간구슬, 파란구슬의 좌표를 구하고, .으로 만들기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
            board[i][j] = '.'
        if board[i][j] == 'B':
            bi, bj = i, j
            board[i][j] = '.'

answer = float('inf')
dfs(1, bi, bj, ri, rj)

if answer == float('inf'):
    print(-1)
else:
    print(answer)