import sys
input = sys.stdin.readline

DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))


def evaluate():
    # 그룹 짓기
    group_matrix = [[0]*n for _ in range(n)]
    visited1 = [[0]*n for _ in range(n)]
    group = []
    index = 0
    for i in range(n):
        for j in range(n):
            if not visited1[i][j]:
                num = matrix[i][j]
                cnt = 0
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if visited1[r][c]:
                        continue
                    cnt += 1
                    visited1[r][c] = 1
                    group_matrix[r][c] = index  # 그룹 번호 할당
                    for d in DELTA:
                        nr, nc = r+d[0], c+d[1]
                        if 0 <= nr < n and 0 <= nc < n and not visited1[nr][nc] and matrix[nr][nc] == num:
                            stack.append((nr, nc))
                group.append([num, cnt, (i, j)])
                index += 1
    # 점수 계산
    score = 0
    visited2 = [[0] * n for _ in range(n)]
    for idx, g in enumerate(group):
        neighbours = {}
        num, cnt, (si, sj) = g
        stack = [(si, sj)]
        while stack:
            r, c = stack.pop()
            if visited2[r][c]:
                continue
            visited2[r][c] = 1
            for d in DELTA:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < n and 0 <= nc < n and not visited2[nr][nc]:
                    if group_matrix[nr][nc] == idx:
                        stack.append((nr, nc))
                    elif group_matrix[nr][nc] > idx:  # 앞에서 확인한 조합은 안 보기 위해
                        neighbours[group_matrix[nr][nc]] = neighbours.get(group_matrix[nr][nc], 0) + 1

        # 점수 계산
        for key, val in neighbours.items():
            tmp = (cnt+group[key][1])*num*group[key][0]*val
            score += tmp
    return score


def turn():
    k = n//2
    # 십자모양
    col = [matrix[i][k] for i in range(n)]
    row = matrix[k][::-1]
    matrix[k] = col
    for i in range(n):
        matrix[i][k] = row[i]
    # 정사각형
    sq1 = [[matrix[i][j] for i in range(k-1, -1, -1)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            matrix[i][j] = sq1[i][j]

    sq2 = [[matrix[i][j] for i in range(k-1, -1, -1)] for j in range(k+1, n)]
    for i in range(k):
        for j in range(k):
            matrix[i][j+k+1] = sq2[i][j]

    sq3 = [[matrix[i][j] for i in range(n-1, k, -1)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            matrix[i+k+1][j] = sq3[i][j]

    sq4 = [[matrix[i][j] for i in range(n-1, k, -1)] for j in range(k+1, n)]
    for i in range(k):
        for j in range(k):
            matrix[i+k+1][j+k+1] = sq4[i][j]

    return


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = evaluate()
for _ in range(3):
    turn()
    answer += evaluate()

print(answer)
