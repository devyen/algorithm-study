import sys
sys.stdin = open('input.txt')


def is_sudoku(arr):
    # 1. 가로 검사
    for r in range(9):
        check = [0] * 10  # 인덱스 1 ~ 9 에 해당 숫자가 있는지를 체크
        for c in range(9):
            now = arr[r][c]
            if check[now]:  # 이미 숫자가 있다면
                return 0  # 스도쿠 아님
            else:
                check[now] = 1

    # 2. 세로 검사
    for c in range(9):
        check = [0] * 10  # 인덱스 1 ~ 9 에 해당 숫자가 있는지를 체크
        for r in range(9):
            now = arr[r][c]
            if check[now]:  # 이미 숫자가 있다면
                return 0  # 스도쿠 아님
            else:
                check[now] = 1

    # 3. 3*3 검사
    for r in range(3):
        for c in range(3):
            ######### 여기까지 품 #########


T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    result = is_sudoku(puzzle)
    print(f'#{tc} {result}')