import sys

sys.stdin = open('input.txt')


def get_code_part():
    for r in range(N-1, -1, -1):  # 뒤에서부터 탐색
        for c in range(M-1, -1, -1):
            if matrix[r][c] == '1':
                code = matrix[r][c-56+1:c+1]
                return code  # 코드부분인 문자열을 반환


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]  # 인풋을 문자열로 받음
    # 1. 배열에서 암호코드 부분을 추출
    code_part = get_code_part()
    # 2. 암호코드 부분 -> 숫자로 변환
    code = [0]  # 암호 코드를 담을 리스트 (0번 인덱스를 비우기 위해 0을 담고 시작)
    for i in range(0, 56, 7):
        number = code_part[i:i + 7]
        if number == '0001101':
            code.append(0)
        elif number == '0011001':
            code.append(1)
        elif number == '0010011':
            code.append(2)
        elif number == '0111101':
            code.append(3)
        elif number == '0100011':
            code.append(4)
        elif number == '0110001':
            code.append(5)
        elif number == '0101111':
            code.append(6)
        elif number == '0111011':
            code.append(7)
        elif number == '0110111':
            code.append(8)
        elif number == '0001011':
            code.append(9)

    # 3. 정상적인 암호코드인지 확인 - 검증코드 확인
    # code = [0, 7, 5, 7, 5, 5, 0, 2, 7] (1 ~ 8번 인덱스)
    even_sum = odd_sum = 0
    for i in range(1, 8):
        if i & 1:  # & 비트연산 (1이면 홀수, 0이면 짝수)  # i가 홀수이면
            odd_sum += code[i]
        else: # i가 짝수이면 => 홀수 자리
            even_sum += code[i]

    total_sum = 0  # 총합을 0으로 설정
    if ((odd_sum * 3) + even_sum + code[8]) % 10 == 0:  # 연산 결과가 10의 배수이면 ->  정상코드
        total_sum = even_sum + odd_sum + code[8]

    print(f'#{tc} {total_sum}')
