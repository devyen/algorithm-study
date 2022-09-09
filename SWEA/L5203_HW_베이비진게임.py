import sys
sys.stdin = open('input.txt')


def baby_gin(numbers):
    check_1 = [0] * 10
    check_2 = [0] * 10
    for i in range(12):
        if not i % 2:  # 짝수 인덱스 -> 플레이어1
            number = numbers[i]
            check_1[number] += 1
            # triplet 체크
            if check_1[number] == 3:
                return 1  # 플레이어1 WIN
            # run 체크
            for j in range(8):
                if check_1[j] and check_1[j+1] and check_1[j+2]:
                    return 1  # 플레이어1 WIN
        else:
            number = numbers[i]
            check_2[number] += 1
            # triplet 체크
            if check_2[number] == 3:
                return 2  # 플레이어2 WIN
            # run 체크
            for j in range(8):
                if check_2[j] and check_2[j + 1] and check_2[j + 2]:
                    return 2  # 플레이어2 WIN

    return 0  # 무승부면 0 리턴


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    result = baby_gin(numbers)

    print(f'#{tc} {result}')