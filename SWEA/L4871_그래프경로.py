import sys

sys.stdin = open('input.txt')


def is_there_way(V, S, G):
    # 경로 탐색 - 스택 이용
    stack = []  # 이전경로 저장용
    visited = [0] * (V + 1)

    i = S  # 현재 방문위치
    visited[i] = 1  # 방문 표시
    while i != G and i != 0:  # 종료조건 1. 도착노드 G에 도착했을 때 2. 길을 찾지 못하고 i = 0이 되었을 때
        for w in range(1, V + 1):
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i)  # 방문 경로 저장
                i = w  # 새 방문지 이동
                visited[i] = 1  # 방문 표시
                break
        else:  # 새 방문지가 없으면 이전 노드로 다시 돌아간다.
            if stack:
                i = stack.pop(-1)
            else:
                i = 0
                # break

    if i == G:  # 1. 도착노드 G에 도착하여 반복문이 끝난 경우 1 반환
        return 1
    else:       # 2. 길을 찾지 못하고 반복문이 끝난 경우 0 반환
        return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드 V개, 간선 E개

    # 인접 행렬 만들기
    # 노드 번호와 인덱싱을 똑같게 하기 위해, V+1만큼 만들고 0번째 행과 0번째 열을 0으로 채운다.
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):  # 간선정보 E개
        s, e = map(int, input().split())
        graph[s][e] = 1  # 방향이 있는 그래프이므로 s->e 인 경우만 넣기

    S, G = map(int, input().split())  # 출발노드 S, 도착노드 G  ex) 1 -> 6

    result = is_there_way(V, S, G)  # 길을 찾는 함수 호출

    print(f'#{tc} {result}')
