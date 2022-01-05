import sys
input = sys.stdin.readline


# def go(r, c):
#     global cnt
#     cnt += 1
#     matrix[r][c] = 1
#     for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 델타탐색
#         nr, nc = r + d[0], c + d[1]
#         if 0 <= nr < m and 0 <= nc < n and not matrix[nr][nc]:
#             go(nr, nc)


# Recursion Error가 나서 stack으로 바꿈
def dfs(i, j):
    global cnt
    stack = [(i, j)]
    while stack:
        r, c = stack.pop()
        if not matrix[r][c]:
            cnt += 1
            matrix[r][c] = 1

            for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 델타탐색
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and not matrix[nr][nc]:
                    stack.append((nr, nc))


m, n, k = map(int, input().split())
squares = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())  # 왼쪽아래 좌표, 오른쪽위 좌표
    squares.append((x1, y1, x2-1, y2-1))  # 꼭짓점 좌표를 칸 인덱스로 치환하기위해 오른쪽위 좌표를 -1


matrix = [[0]*n for _ in range(m)]

# 사각형영역 색칠
for r in range(m):
    for c in range(n):
        for square in squares:
            if square[1] <= r <= square[3] and square[0] <= c <= square[2]:
                matrix[r][c] = 1

# 탐색
rst = []
for r in range(m):
    for c in range(n):
        if not matrix[r][c]:
            cnt = 0
            # go(r, c)
            dfs(r, c)
            rst.append(cnt)

rst.sort()
print(len(rst))
print(*rst)