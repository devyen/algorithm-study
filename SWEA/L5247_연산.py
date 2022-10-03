import sys

sys.stdin = open('input.txt')

# 선형큐로 품


def bfs():
    # 주의사항
    # 1. 연산 결과는 1 ~ 100만
    # 2. 이미 만든 자연수는 기록하여 중복 생성 방지 ->  제한시간 초과가 안되려면 방문 체크가 필요함

    # 선형 큐 구현
    Q = [0] * 1000000
    front = rear = -1  # front가 머리, rear가 꼬리

    rear += 1
    Q[rear] = n
    memo[n] = 0

    while front != rear:
        front += 1
        tmp = Q[front]

        for res in (tmp+1, tmp-1, tmp*2, tmp-10):
            if 0 < res <= 1000000 and memo[res] == -1:
                memo[res] = memo[tmp] + 1  # cnt를 memo에 저장하는 방식
                if res == m:
                    return memo[res]
                rear += 1
                Q[rear] = res


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    memo = [-1] * 1000001

    print(f'#{tc} {bfs()}')