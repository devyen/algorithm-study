import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())  # num = 0.625
    result = ''

    for i in range(-1, -13, -1):  # 소수점 아래 12자리까지 확인
        result += str(int(num // 2**i))  # 나눈 몫이 있다는건 이진수가 1이라는 것
        num %= 2**i  # 나머지를 다시 num에 저장
        if num == 0:
            break

    if num: # 12자리를 넘었는데 남은 수가 있으면
        result = 'overflow'

    print(f'#{tc} {result}')