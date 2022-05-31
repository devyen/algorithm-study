import sys

sys.stdin = open('input.txt')


def is_there_way(E, paths):
    graph = [[0] * 100 for _ in range(100)]
    for i in range(0, E * 2, 2):
        s, e = paths[i], paths[i + 1]
        graph[s][e] = 1

    # 경로 탐색 - 스택 이용
    stack = []  # 이전경로 저장용
    visited = [0] * 100

    i = 0  # 0부터 시작
    visited[0] = 1  # 방문 표시
    while i != 99 and i != -1:  # 종료조건 1. 도착노드 99에 도착했을 때 2. 길을 찾지 못하고 i = -1이 되었을 때
        for w in range(1, 100):
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i)  # 방문 경로 저장
                i = w  # 새 방문지 이동
                visited[i] = 1  # 방문 표시
                break
        else:  # 새 방문지가 없으면 이전 노드로 다시 돌아간다.
            if stack:
                i = stack.pop(-1)
            else:  # 이전 노드가 없으면 종료조건인 i = -1을 만든다.
                i = -1
                # break

    if i == 99:  # 1. 도착노드에 도착하여 반복문이 끝난 경우 1 반환
        return 1
    else:  # 2. 길을 찾지 못하고 반복문이 끝난 경우 0 반환
        return 0


for _ in range(10):
    tc, E = map(int, input().split())  # 간선 E개

    paths = list(map(int, input().split()))
    result = is_there_way(E, paths)

    print(f'#{tc} {result}')
