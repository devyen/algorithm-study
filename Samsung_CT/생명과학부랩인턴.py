import sys

input = sys.stdin.readline

DELTA = ((-1, 0), (1, 0), (0, 1), (0, -1))  # 상하우좌


def move(mold):
    x, y, s, d, b = mold
    for _ in range(s):
        nx, ny = x+DELTA[d][0], y+DELTA[d][1]
        if not (0 <= nx < n and 0 <= ny < m):
            d = d-1 if d % 2 else d+1
            x, y = x+DELTA[d][0], y+DELTA[d][1]
        else:
            x, y = nx, ny
    place_dict[(x, y)] = place_dict.get((x, y), []) + [[s, d, b]]


n, m, k = map(int, input().split())
molds = []
for _ in range(k):
    x, y, s, d, b = map(int, input().split())  # 행, 열, 속력, 방향, 크기
    molds.append([x-1, y-1, s, d-1, b])

answer = 0
# 0열부터 오른쪽으로 탐색
for j in range(m):
    col = []
    next_molds = []
    for mold in molds:
        if mold[1] == j:
            col.append(mold)
        else:
            next_molds.append(mold)
    # 채취
    if len(col) > 0:
        col.sort(key=lambda x: x[0])
        answer += col[0][4]
        next_molds += col[1:]
    # 곰팡이 이동
    place_dict = {}
    for n_mold in next_molds:
        move(n_mold)
    # 겹치는 곰팡이 합체
    new_molds = []
    for key, val in place_dict.items():
        if len(val) > 1:
            new_molds.append(list(key)+sorted(val, key=lambda x: -x[2])[0])
        else:
            new_molds.append(list(key)+val[0])
    molds = new_molds

print(answer)
