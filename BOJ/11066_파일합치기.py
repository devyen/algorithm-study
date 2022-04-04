import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    minCost = [[0]*k for _ in range(k)]  # dp  # minCost[i][j]는 인덱스 i부터 j까지의 범위를 합치는 최소비용

    # 부분연속합을 구해 subSum 딕셔너리에 저장
    subSum = {0: files[0]}  # value -> 0부터 key인덱스까지의 합
    for i in range(1, k):
        subSum[i] = subSum[i-1] + files[i]  # 딕셔너리에 추가

    for size in range(1, k): # size 크기로 묶은 그룹들의 minCost구하기  # 바텀업 방식
        for start in range(k-1):  # 시작점은 0부터 k-2까지
            end = start + size
            if end >= len(files):
                break

            result = float('inf')
            for cut in range(start, end):
                result = min(result, minCost[start][cut] + minCost[cut+1][end] + subSum[end] - subSum[start-1])
            minCost[start][end] = result

    print(minCost[0][k-1])  # 0부터 k-1까지의 최소비용
