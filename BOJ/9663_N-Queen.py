import sys
input = sys.stdin.readline


def do_check(r, c):
    for i in range(n):
        # 행 체크
        check[r][i] += 1
        # 열 체크
        check[i][c] += 1

    gap = c - r
    s = c + r
    for i in range(n):
        try:
            # 좌상우하 대각선 체크x`
            if i + gap >= 0:
                check[i][i + gap] += 1
            # 우상좌하 대각선 체크
            if s-i >= 0:
                check[i][s - i] += 1
        except:
            pass


def de_check(r, c):
    for i in range(n):
        check[r][i] -= 1
        check[i][c] -= 1
    for i in range(n):
        try:
            if i + c - r >= 0:
                check[i][i + (c - r)] -= 1
            if c + r - i >= 0:
                check[i][(c + r) - i] -= 1
        except:
            pass
        # finally:
        #     continue


def dfs(r):
    global cnt
    # 베이스 케이스
    if r == n:
        cnt += 1
        return

    for c in range(n):
        if not check[r][c]:
            # r, c 가 정해짐
            do_check(r, c)
            now[r][c] = 1
            dfs(r+1)
            de_check(r, c)
            now[r][c] = 0


n = int(input())
check = [[0]*n for _ in range(n)]
now = [[0]*n for _ in range(n)]

cnt = 0
dfs(0)

print(cnt)
