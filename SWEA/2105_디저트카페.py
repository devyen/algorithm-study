import sys

sys.stdin = open('input.txt')

''' case 7
10
18 8 21 24 8 4 20 15 14 23
17 22 3 14 3 19 19 7 6 13
2 26 10 10 10 7 18 14 15 17
13 25 7 20 18 21 8 2 4 24
4 3 1 5 15 3 15 12 22 23
19 22 9 17 6 9 22 26 2 5
12 13 19 13 6 2 12 19 24 8
21 21 24 15 4 1 20 13 14 5
6 10 17 13 7 4 22 16 9 7
17 8 12 11 20 13 5 24 11 3
'''

DIRECTION = ((1, 1), (1, -1), (-1, -1), (-1, 1))  # 각각 0번, 1번, 2번, 3번 방향


def go(r, c, s):  # s: 현재까지의 합
    global result
    # 완성 조건: 1. 네 방향을 다 돌고 2. 원점으로 돌아오면
    if len(set(dir_check)) == 4 and (r, c) == (row, col):
        # s를 처리
        if s > result:
            result = s
            return

    if matrix[r][c] in visited:
        return

    visited.append(matrix[r][c])
    for d in range(4):
        if d in dir_check[:-1]:  # 바로 직전 방향을 제외하고 진행해온 방향들은 앞으로 선택에서 제외 -> 그래야 사각형을 만들 수 있음
            continue
        nr, nc = r + DIRECTION[d][0], c + DIRECTION[d][1]
        if 0 <= nr < n and 0 <= nc < n:
            # if d not in dir_check:  # 중복되면 안되니까
            dir_check.append(d)  # 사각형을 그려야하므로 진행한 방향을 저장
            go(nr, nc, s + 1)
            dir_check.pop()

    visited.pop()

# def go(r, c, s):  # s: 현재까지의 합
#     global result
#     # 완성 조건: 1. 네 방향을 다 돌고 2. 원점으로 돌아오면
#     if len(set(dir_check)) == 4 and (r, c) == (row, col):
#         # s를 처리
#         if s > result:
#             result = s
#             print(r, c)
#             print(s)
#             return
#
#     if matrix[r][c] == 'V':
#         return
#
#     if matrix[r][c] in visited:
#     # return
#
#     visited.append(matrix[r][c])
#     tmp = matrix[r][c]
#     matrix[r][c] = 'V'
#     for d in range(4):
#         if d in dir_check[:-1]:  # 바로 직전 방향을 제외하고 진행해온 방향들은 앞으로 선택에서 제외 -> 그래야 사각형을 만들 수 있음
#             continue
#         nr, nc = r + DIRECTION[d][0], c + DIRECTION[d][1]
#         if 0 <= nr < n and 0 <= nc < n:
#             # if d not in dir_check:  # 중복되면 안되니까
#             dir_check.append(d)  # 사각형을 그려야하므로 진행한 방향을 저장
#             go(nr, nc, s + 1)
#             dir_check.pop()
#
#     visited.pop()
#     matrix[r][c] = tmp

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = -1
    for row in range(n):
        for col in range(n):
            if not ((row == 0 or row == n-1) and (col == 0 or col == n-1)):  # 꼭지점은 출발점에서 제외
                visited = []
                dir_check = []
                go(row, col, 0)  # row, col => 시작점

    # 출력: 디저트를 가장 많이 먹을 때의 디저트 수(최대값), 먹을 수 없는 경우 -1
    print(f'#{tc} {result}')

# # 7번 케이스 테스트용
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# result = -1
#
# for row in range(n):
#     for col in range(n):
#         print(f'**{row}, {col}')
#         if not ((row == 0 or row == n-1) and (col == 0 or col == n-1)):  # 꼭지점은 출발점에서 제외
#             visited = []
#             dir_check = []
#             go(n - 1, 2, 0)
#             go(row, col, 0)  # row, col => 시작점
#
# # 출력: 디저트를 가장 많이 먹을 때의 디저트 수(최대값), 먹을 수 없는 경우 -1
# print(f'#7 {result}')