import sys
sys.stdin = open('오목.txt')

def is_five(r, c):
    # 8방향 배열이 필요함
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # 상 부터 오른쪽으로
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for t in range(8):
        nr, nc = r, c
        cnt = 0
        while cnt < 5 and 0 <= nr < n and 0 <= nc < n:
            if matrix[nr][nc] == 'o':
                cnt += 1
                nr += dr[t]
                nc += dc[t]
            else:
                break
        if cnt == 5:
            return 1  # 오목을 찾으면 1 리턴

    return 0  # 8방향 다 탐색했는데도 오목이 없으면 0 리턴



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [input() for _ in range(n)]

    flag = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'o':
                result = is_five(r, c)
                if result == 1:
                    flag = 1
                    break

    if flag == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')


