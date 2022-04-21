import sys
sys.stdin = open('input.txt')

def get_charge_num(K, N, charge_stop_list):

    # 길이가 N인 충전기 정류장 리스트
    # 충전기가 있으면 1, 없으면 0
    C = [0] * (N + 1)
    for i in charge_stop_list:
        C[i] = 1  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    # 길이가 N인 남은 에너지양 리스트
    E = [K] + [0] * N

    # 충전
    charge_total = 0
    # 정류장 1부터 10까지 돌면서
    for i in range(1, N+1):
        E[i] = E[i-1] - 1  # 에너지 -1

        if C[i] == 1: # 충전기가 있으면

            if i == charge_stop_list[-1]:  # 마지막 충전기인 경우는 다음 충전기가 없으므로 따로 처리
                if E[i] < N - i:  # 에너지 < 남은거리 이면
                    E[i] = K  # 충전
                    charge_total += 1  # 충전횟수 +1

            for idx, v in enumerate(C): # C에서 다음 충전기를 탐색
                if idx > i and v == 1:
                    remain = idx - i  # 남은 거리  3 - 1 = 2
                    if E[i] < remain:  # 에너지 < 남은거리 이면
                        E[i] = K  # 충전
                        charge_total += 1  # 충전횟수 +1
                    break

        # 충전기가 없는데 에너지가 0이면, 0을 리턴
        elif E[i] == 0 and i != N:
            return 0

    return charge_total


T = int(input())  # 3

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop_list = list(map(int, input().split()))

    total = get_charge_num(K, N, charge_stop_list)

    print(f'#{tc} {total}')