def solution(places):
    def go(i, j, s):
        nonlocal flag
        if flag:
            return

        if s > 2 or matrix[i][j] == 'X':
            return

        if (i, j) != (r, c) and matrix[i][j] == 'P':
            flag = 1

        visited[i][j] = 1
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                go(ni, nj, s+1)
        visited[i][j] = 0
        return

    answer = []
    for place in places:
        matrix = [list(p) for p in place]
        visited = [[0]*5 for _ in range(5)]
        flag = 0
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == 'P':
                    # 주변 체크
                    go(r, c, 0)

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer


tc = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = solution(tc)
print(result)