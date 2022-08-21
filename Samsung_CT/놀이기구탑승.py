import sys
input = sys.stdin.readline

DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))


def place(person, likes):
    candidates = []
    for i in range(n):
        for j in range(n):
            if not matrix[i][j]:
                # 델타 탐색
                like_cnt = blank_cnt = 0
                for di, dj in DELTA:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if matrix[ni][nj] in likes:
                            like_cnt += 1
                        elif not matrix[ni][nj]:
                            blank_cnt += 1
                candidates.append([like_cnt, blank_cnt, i, j])
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    ti, tj = candidates[0][2:]
    matrix[ti][tj] = person
    return


n = int(input())
matrix = [[0]*n for _ in range(n)]

like_dic = {}
for _ in range(n*n):
    tmp = list(map(int, input().split()))
    like_dic[tmp[0]] = tmp[1:]  # 최종 점수 합산에 쓰기 위해 딕셔너리에 저장
    place(tmp[0], tmp[1:])

# 점수 합산
answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in DELTA:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if matrix[ni][nj] in like_dic[matrix[i][j]]:
                    cnt += 1
        if cnt != 0:
            answer += 10**(cnt-1)

print(answer)