import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc}', end=' ')

    # 한 번 돌 때마다 맨 앞은 최대값, 두 번째는 최소값으로채운다.
    # 그래서 i는 2만큼 증가시킨다.
    for i in range(0, 10, 2):  # 10개까지만 출력

        # 최대값
        max = i  # 최대값 인덱스
        for j in range(i+1, len(arr)):
            if arr[max] < arr[j]:
                max = j  # 인덱스 교체

        print(arr[max], end=' ')
        arr[i], arr[max] = arr[max], arr[i]

        # 최소값
        min = i + 1  # 최소값 인덱스
        for j in range(i + 2, len(arr)):
            if arr[min] > arr[j]:
                min = j  # 인덱스 교체

        print(arr[min], end=' ')
        arr[i + 1], arr[min] = arr[min], arr[i + 1]

    print()
