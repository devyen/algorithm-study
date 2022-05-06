import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 거꾸로 사다리 타기
    # 배열 마지막 행에서 값이 '2'인 지점에서 위로 올라가 X를 찾는다.

    i = 99  # 시작점 row 인덱스

    for idx, v in enumerate(matrix[-1]):
        if v == 2:
            j = idx  # 배열 마지막 행에서 값이 '2'인 idx를 찾아 j에 저장

    while i > 0:  # 0행이 될때까지
        i -= 1  # 위로 한 칸 이동
        # 왼쪽에 통로가 있으면
        if j > 0 and matrix[i][j-1] == 1:
            while j > 0 and matrix[i][j-1] != 0:
                j -= 1
        # 오른쪽에 통로가 있으면
        elif j < 99 and matrix[i][j + 1] == 1:
            while j < 99 and matrix[i][j+1] != 0:
                j += 1
        # 통로가 없으면 위로

    X = j

    print(f'#{tc} {X}')