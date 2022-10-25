import sys
sys.stdin = open('파리퇴치.txt')


def get_sum(r, c, m):  # (r, c)부터 m*m 합 구하기
    sum = 0
    for i in range(m):
        for j in range(m):
            sum += matrix[r+i][c+j]  # matrix[시작좌표+변하는인덱스]
    return sum


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())  # 5 2
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            result = get_sum(r, c, m)
            # result vs max 비교
            if result > max:
                max = result

    print(f'#{tc} {max}')
