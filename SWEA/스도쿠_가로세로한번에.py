import sys
sys.stdin = open('input_sudoku.txt')


# 가로, 세로를 한번에 처리
def is_sudoku(arr):

    for r in range(9):
        row_check = [0] * 10
        col_check = [0] * 10

        for c in range(9):

            # 1. 가로 검사
            row_now = arr[r][c]
            if row_check[row_now]:  # 이미 체크되어 있으면
                return 0  # 스도쿠가 아니므로 리턴
            else:  # 없으면
                row_check[row_now] = 1  # 체크

            # 2. 세로 검사
            col_now = arr[c][r]
            if col_check[col_now]:  # 이미 체크되어 있으면
                return 0
            else:  # 없으면
                col_check[col_now] = 1  # 체크

    # 3. 3*3 검사
    # 먼저 시작점 arr[i*3][j*3]을 결정
    for i in range(3):
        for j in range(3):

            # 3*3 배열을 돌면서 검사
            check = [0] * 10
            for r in range(3):
                for c in range(3):
                    now = arr[i*3+r][j*3+c]
                    if check[now]:
                        return 0
                    else:
                        check[now] = 1

    return 1


T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    result = is_sudoku(puzzle)
    print(f'#{tc} {result}')