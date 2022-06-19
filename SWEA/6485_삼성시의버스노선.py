import sys

sys.stdin = open('input.txt')

# # 1. 모든 노선 체크
# def bus_count(bus_stop):
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()  # 버스 노선 수
#
#     bus_route = []  # 버스의 노선들을 저장해놓을 리스트
#
#     for i in range(N):
#         A, B = map(int, input().split())
#         bus_route.append((A, B))
#
#     # 내가 확인하고 싶은 정류장의 개수
#     P = int(input())
#     answer = []  # 버스 수를 저장해놓을 리스트
#
#     for i in range(P):
#         C = int(input())
#         answer.append(bus_count(C))

######################################################
# # 2. 정류장을 미리 계산
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())  # 버스 노선 수
#
#     start = [0] * 5001  # 출발 정류장
#     end = [0] * 5001  # 도착 정류장
#     bus_stop = [0] * 5001  # 계산한 버스 표시
#
#     for i in range(N):
#         A, B = map(int, input().split())
#         start[A] += 1
#         end[B] += 1
#
#     # 버스 계산
#     for i in range(len(bus_stop)-1):
#         bus_stop[i+1] = bus_stop[i] + start[i+1] - end[i]
#
#     P = int(input())
#     print(f'#{tc}', end=' ')
#     for i in range(P):
#         C = int(input())  # 우리가 확인하고 싶은 정류장 번호
#         print(bus_stop[C], end=' ')
#     print()


# 3. 미리 계산
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 버스 노선 수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B + 1):
            bus_stop[j] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        C = int(input())  # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()