import sys

sys.stdin = open('input.txt')


# 10진수로 변환
def change_to_dec(num, notation):
    result = 0
    for n, val in enumerate(list(map(int, num))[::-1]):  # enumerate: idx와 값을 동시에 빼줌
        result += val * notation**n
    return result


# 2진수 후보 만들기와 3진수에서 정답 찾기를 한 함수로!
def check(num, notation):
    decimal = change_to_dec(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = decimal - val*(notation**n) + j*(notation**n)

            if tmp not in candidates:
                candidates.append(tmp)
            else:
                return tmp


T = int(input())
for tc in range(1, T+1):
    binary = input()  # '1010'
    ternary = input()

    candidates = []
    check(binary, 2)

    print(f'#{tc} {check(ternary, 3)}')


    # # 2. 한 자리씩 바꾼다.
    # candidates = []
    # for i in range(n):
    #     candidates.append(decimal ^ (1 << i))  # XOR 연산
    # print()
