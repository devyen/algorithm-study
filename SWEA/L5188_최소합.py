import sys
sys.stdin = open('input.txt')


def go(row, col, total):
    global min_total
    # 현재 위치의 숫자 합계에 더하기
    total += matrix[row][col]
    # 최소값을 넘어가면 리턴(=>백트래킹)
    if total > min_total:
        return
    # 오른쪽 이동
    if col < n-1:
        go(row, col+1, total)
    # 아래로 이동
    if row < n-1:
        go(row+1, col, total)
    # 리턴 지점
    if row == n-1 and col == n-1:  # 오른쪽 아래에 도달하면
        min_total = total


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    min_total = float("inf")  # 무한대값으로 최소값 설정
    go(0, 0, 0)  # DFS

    print(f'#{tc} {min_total}')