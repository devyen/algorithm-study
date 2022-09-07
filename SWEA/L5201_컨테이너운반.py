import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # n개의 컨테이너, m대의 트럭
    n, m = map(int, input().split())
    # 트럭과 화물 내림차순으로 정렬
    containers = sorted(list(map(int, input().split())))[::-1]
    check = [0] * n  # 이미 선택된 컨테이너인지를 판별하기 위한 체크리스트
    trucks = sorted(list(map(int, input().split())))[::-1]

    result = 0
    for truck in trucks:
        for i in range(n):
            if containers[i] <= truck and not check[i]:  # 화물 무게가 적재용량 이하이면
                result += containers[i]  # 무게 더하기
                check[i] = 1  # 체크
                break

    print(f'#{tc} {result}')