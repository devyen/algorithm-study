import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []  # 합을 저장할 리스트

    # 왼쪽 위에서 내려오는 대각선을 대각선1, 오른쪽 위에서 내려오는 대각선을 대각선2라고 하자.
    # 행, 열로 두 번 순회하면서 대각선1은 행과 함께 대각선2는 열과 함께 구한다.

    # 1. 행, 대각선1
    cross_1_sum = 0  # 대각선1
    for i in range(len(matrix)):
        row_sum = 0  # 행
        for j in range(len(matrix[0])):
            row_sum += matrix[i][j]

            if i == j:
                cross_1_sum += matrix[i][j]

        sum_list.append(row_sum)
    sum_list.append(cross_1_sum)

    # 2. 열, 대각선2
    cross_2_sum = 0  # 대각선2
    for j in range(len(matrix[0])):
        col_sum = 0  # 열
        for i in range(len(matrix)):
            col_sum += matrix[i][j]

            if i + j == 99:
                cross_2_sum += matrix[i][j]

        sum_list.append(col_sum)
    sum_list.append(cross_2_sum)

    # 최댓값 구하기
    max = sum_list[0]
    for sum in sum_list:
        if sum > max:
            max = sum

    print(f'#{tc} {max}')
