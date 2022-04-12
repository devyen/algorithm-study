'''
point
1. 육각형 이동 처리
2. dfs로 푸는게 아니었어 ㅠㅠㅠ 연결된 영역의 최대값을 구하는건 어떤 알고리즘으로 풀어야하지?
'''


def dfs(i, j, cnt, s):
    global max_benefit

    # if h >= min_h:  # 가지 치기
    #     return
    if cnt == 4:
        visited[i][j] = 1  # 방문체크
        max_benefit = max(max_benefit, s)
        visited[i][j] = 0  # 방문해제
        return

    visited[i][j] = 1  # 방문체크

    # 육각형 이동
    k = 1 if j%2 else -1  # 홀짝 구분
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (k, -1), (k, 1)):  # 상,하,좌,우,k1,k2
        ni, nj = i+di, j+dj
        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
            dfs(ni, nj, cnt+1, s + matrix[ni][nj])

    visited[i][j] = 0  # 방문해제


for t in range(1, int(input())+1):
    w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    max_benefit = -1
    for r in range(h):
        for c in range(w):
            dfs(r, c, 1, matrix[r][c])
    print(f'#{t} {max_benefit}')