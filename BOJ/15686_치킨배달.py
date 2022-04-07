import sys
from collections import deque
input = sys.stdin.readline

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(row, col, d):
    global cnt
    global flag

    check[row][col] = 1

    if matrix[row][col] > 1:
        # 치킨집
        matrix[row][col] += 1
        cnt += d
        flag = 1
        return

    for dir in DIRECTION:  # 4방향 탐색
        new_row = row+dir[0]
        new_col = col+dir[1]
        if 0 <= new_row < n and 0 <= new_col < n:
            queue.append((new_row, new_col, d+1))

    while queue:
        if flag:
            return
        now = queue.popleft()
        bfs(now[0], now[1], now[2])
        check[now[0]][now[1]] = 0


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


chicken_cnt = 0
# 가장 가까운 치킨집 찾기
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            check = [[0]*n for _ in range(n)]
            flag = 0
            queue = deque()
            bfs(r, c, 0)
        elif matrix[r][c] > 1:
            chicken_cnt += 1

# 치킨집 폐업
if m < chicken_cnt:
    chicken_house = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] > 1:
                chicken_house.append((matrix[r][c], r, c))
    chicken_house.sort(reverse=True)
    for _ in range(chicken_cnt-m):
        closed = chicken_house.pop()
        matrix[closed[1]][closed[2]] = 0

# 최소거리 찾기
cnt = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            check = [[0]*n for _ in range(n)]
            flag = 0
            queue = deque()
            bfs(r, c, 0)

print(cnt)
print(chicken_cnt-m)
print(matrix)

