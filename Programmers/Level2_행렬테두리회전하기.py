from collections import deque


def solution(rows, columns, queries):
    def switch(x, y):
        nonlocal min_num
        q.append(matrix[x][y])
        min_num = min(min_num, matrix[x][y])
        matrix[x][y] = q.popleft()

    s, e = 1, columns + 1
    matrix = []
    for r in range(rows):
        matrix.append(list(range(s, e)))
        s, e = e, e + columns

    answer = []
    for query in queries:
        x1, y1, x2, y2 = [x-1 for x in query]
        q = deque([matrix[x1][y1]])
        min_num = matrix[x1][y1]
        for j in range(y1 + 1, y2):
            switch(x1, j)
        for i in range(x1, x2):
            switch(i, y2)
        for j in range(y2, y1, -1):
            switch(x2, j)
        for i in range(x2, x1 - 1, -1):
            switch(i, y1)
        answer.append(min_num)
    return answer


result = solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
print(result)
