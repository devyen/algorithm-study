import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split()))+[0]*97 for _ in range(3)] + [[0]*100 for _ in range(97)]

n = m = 3  # n 행 길이, m 열 길이
answer = 0
while matrix[r-1][c-1] != k:
    if answer >= 100:
        answer = -1
        break
    new_matrix = [[0] * 100 for _ in range(100)]
    if n >= m:
        nm = 0
        for i in range(n):
            # 행 정렬
            cnt_dic = {}
            for j in range(n):
                if matrix[i][j]:
                    cnt_dic[matrix[i][j]] = cnt_dic.get(matrix[i][j], 0) + 1
            new_row = []
            for num, cnt in sorted(cnt_dic.items(), key=lambda x: (x[1], x[0])):
                new_row += [num, cnt]
            new_row = new_row[:100]
            nm = max(nm, len(new_row))
            for j in range(len(new_row)):
                new_matrix[i][j] = new_row[j]
        m = nm
    else:
        nn = 0
        for j in range(m):
            # 열 정렬
            cnt_dic2 = {}
            for i in range(n):
                if matrix[i][j]:
                    cnt_dic2[matrix[i][j]] = cnt_dic2.get(matrix[i][j], 0) + 1
            new_col = []
            for num, cnt in sorted(cnt_dic2.items(), key=lambda x: (x[1], x[0])):
                new_col += [num, cnt]
            new_col = new_col[:100]
            nn = max(nn, len(new_col))
            for i in range(len(new_col)):
                new_matrix[i][j] = new_col[i]
        n = nn
    matrix = new_matrix
    answer += 1

print(answer)