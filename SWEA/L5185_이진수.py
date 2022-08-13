import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, h = input().split()  # n: 자리수, h: 16진수
    result = ''
    for i in range(int(n)):  # 16진수 한 자리씩 -> 2진수(4자리)로 변환
        b = bin(int(h[i], 16))[2:]
        if len(b) % 4:  # 이진수가 4자리가 안되면 앞을 0으로 채워줘야한다.
            b = '0'*(4-len(b)) + b
        result += b

    print(f'#{tc} {result}')