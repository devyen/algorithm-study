import sys

sys.stdin = open('input.txt')

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우하좌상


def get_highests(matrix):
    max = 0
    highests = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] > max:  # max보다 큰 값이 나타나면
                max = matrix[r][c]  # max 갱신
                highests = []  # highests 초기화
                highests.append((r, c))
            elif matrix[r][c] == max:
                highests.append((r, c))
    # print(highests)
    return highests


# r, c: 좌표, work: 공사 여부, len_way: 지금까지 조성된 등산로 길이
def go(r, c, work, len_way):
    global answer
    if len_way > answer:
        answer = len_way

    visited[r][c] = 1  # 방문 표시
    now_height = mountain[r][c]  # 현재 위치의 높이

    for dr, dc in DIRECTION:
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            # 1. 현위치보다 낮은 곳으로 이동할 때
            if mountain[nr][nc] < now_height:
                go(nr, nc, work, len_way + 1)  # go 할때마다 길이는 1씩 증가
            # 2. 현위치보다 높거나 같은 곳으로 이동할 때
            elif not work and mountain[nr][nc] - k < now_height:  # 공사를 아직 하지 않았고, k만큼 깎은게 지금 높이보다 낮다면
                tmp = mountain[nr][nc]  # 원상복구를 위해 땅 파기 전 기록
                mountain[nr][nc] = mountain[r][c] - 1  # ★★ 현재높이 - 1 만큼 깎아버리기 (너무 많이 파면 다음 경로가 제한되므로 항상 현재높이-1 만큼만 깎는게 좋다.)

                # ★★★ 여기서 work = 1 로 바꾸면 남은 for문을 돌 때 이미 공사를 했다는게 됨. but 방향이 아예 다른 경로이므로 또 공사할 수 있다.
                go(nr, nc, 1, len_way + 1)  # => 따라서 go() 안에 인자로 1을 넘겨줘야한다

                mountain[nr][nc] = tmp  # 원상복구

                # dig = mountain[nr][nc] - now_height + 1
                # if dig <= k:
                #     work = 1
                #     mountain[nr][nc] -= dig  # 땅 팜
                #     go(nr, nc, work, len_way+1)
                #     mountain[nr][nc] += dig  # 돌아올땐 원상복귀

    visited[r][c] = 0  # 방문 체크를 다시 풀어준다.


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())  # n: 한 변의 길이  k: 최대 공사 깊이

    mountain = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    answer = 0  # 가장 긴 등산로를 저장할 변수

    # 1. 가장 높은 봉우리들을 찾기
    starts = get_highests(mountain)

    # 2. 봉우리 하나씩 탐색
    for start in starts:
        # work는 0, len_way는 1로 시작
        go(start[0], start[1], 0, 1)

    print(f'#{tc} {answer}')
