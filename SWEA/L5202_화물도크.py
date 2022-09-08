import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    works = []
    for _ in range(n):
        s, e = map(int, input().split())
        time = e - s  # 소요시간
        works.append([s, e, time])

    # 그리디1. 소요시간이 적은 것부터 배치
    check = [0] * 24  # 24시간

