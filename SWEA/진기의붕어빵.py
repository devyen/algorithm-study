import sys
sys.stdin = open('진기의붕어빵.txt')

T = int(input())
for tc in range(1, T+1):
    # n명의 사람
    # m초에 k개의 붕어빵을 만든다.
    n, m, k = map(int, input().split())
    # 각 사람이 도착하는 시간(초)
    arrives = sorted(list(map(int, input().split())))  # 함정: input이 정렬되어 있지 않으므로 정렬해줌

    flag = 'Possible'
    sold = 0  # 팔린 빵 개수

    for arrive in arrives:  # [3, 4]
        # 손님이 도착한 시간에 최대로 만들 수 있는 빵의 개수 - 팔린 빵
        if (arrive//m)*k - sold <= 0:
            flag = 'Impossible'
            break
        else:
            sold += 1

    print(f'#{tc} {flag}')