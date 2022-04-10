import sys
input = sys.stdin.readline

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(r, c):
    global cnt
    cnt += 1
    check[r][c] = 1
    for dr, dc in DIRECTION:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == '1' and not check[nr][nc]:
            dfs(nr, nc)


n = int(input())
matrix = [input() for _ in range(n)]
check = [[0]*n for _ in range(n)]

towns = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == '1' and not check[r][c]:
            # 단지탐색
            cnt = 0  # 현재 단지 집의 수
            dfs(r, c)
            towns.append(cnt)

print(len(towns))
for town in sorted(towns):  # 오름차순 정렬
    print(town)