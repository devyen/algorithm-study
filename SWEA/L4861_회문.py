import sys
sys.stdin = open('input.txt')


def find_palindrome(matrix, N, M):  # N*N 글자판 안의 회문을 찾는 함수
    # 가로 탐색
    for i in range(N):  # 행 인덱스 i를 고정
        for j in range(N - M + 1):  # 열 시작점: 0 ~ N-M까지
            case = matrix[i][j:j + M]  # 길이 M만큼 자른다.
            if is_palindrome(case):
                return case
    # 세로 탐색
    for j in range(N):  # 열 인덱스 j를 고정
        for i in range(N - M + 1):  # 행 시작점: 0 ~ N-M까지
            case = ''
            for k in range(i, i + M):  # 행을 돌면서 인덱스 j에 있는 문자를 하나씩 가져온다.
                case += matrix[k][j]
            if is_palindrome(case):
                return case


def is_palindrome(s):  # 문자열이 회문인지 검사하는 함수
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 배열 길이 M 찾는 회문 길이
    matrix = [input() for _ in range(N)]

    result = find_palindrome(matrix, N, M)

    print(f'#{tc} {result}')
