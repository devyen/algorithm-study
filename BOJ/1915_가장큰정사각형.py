import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
result = -1
for j in range(m):
    for r in range(n):
        if j == 0:
            dp[r][j] = matrix[r][j]
            continue
        if matrix[r][j]:
            dp[r][j] = dp[r][j-1] + matrix[r][j]  # j열까지의 가로누적합 쭉 구하기

    # 정사각형이 되는지 체크
    i = 0
    while i < n:
        val = dp[i][j]
        if not val:  # 0이면 pass
            i += 1
            continue
        for width in range(val, 0, -1):  # 길이 1씩 줄여가면서 검사
            cnt = 0
            flag = 0
            for d in range(-width+1, width):
                ni = i + d
                if 0 <= ni < n:
                    if dp[ni][j] >= width:
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt == width:
                        flag = 1
                        break
            if flag:
                dp[i][j] = width
                result = max(result, width)
                i += width
                break
            else:
                i += 1

print(result*result)
