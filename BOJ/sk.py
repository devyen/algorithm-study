def solution(width, height, diagonals):
    def dfs(i, j, used):  # s: 대각선 이용 유무
        # nonlocal answer
        if i == 0 and j == width and used:
            # answer += 1
            return 1

        if matrix[i][j] != -1:
            return matrix[i][j]

        matrix[i][j] = 0
        if [i, j] in edges and not used:
            for di, dj in ((-1, -1), (1, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni <= height and 0 <= nj <= width:
                    matrix[i][j] += dfs(ni, nj, 1)

        for di, dj in ((0, 1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni <= height and 0 <= nj <= width:
                matrix[i][j] += dfs(ni, nj, used)

        return matrix[i][j]
    # 1. dfs  2. dp로 풀어보자!
    matrix = [[-1] * (width + 1) for _ in range(height + 1)]  # dp
    edges = []
    for diagonal in diagonals:
        x, y = diagonal  # [1, 1], [2, 2]
        edges.append([height - y + 1, x])
        edges.append([height - y, x - 1])
        # matrix[height-y+1][x] = 2
        # matrix[height-y][x-1] = 2
    answer = dfs(height, 0, 0)

    return answer


print(solution(2, 2, [[1,1],[2,2]]))