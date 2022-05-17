import sys

sys.stdin = open('input.txt')


### manacher 알고리즘으로도 풀어보기

def get_len_palindrome(matrix):  # N*N 글자판 안의 회문을 찾는 함수
    N = len(matrix)

    for M in range(N, 0, -1):  # 가장 긴 회문의 길이를 구하는 것이므로 M은 N부터 시작해서 작아진다

        # 가로 탐색
        for i in range(N):  # 행 인덱스 i를 고정
            for j in range(N - M + 1):  # 열 시작점: 0 ~ N-M까지
                case = matrix[i][j:j + M]  # 길이 M만큼 자른다.
                if is_palindrome(case):
                    return M  # 회문의 길이를 리턴

        # 세로 탐색
        for j in range(N):  # 열 인덱스 j를 고정
            for i in range(N - M + 1):  # 행 시작점: 0 ~ N-M까지
                case = ''
                for k in range(i, i + M):  # 행을 돌면서 인덱스 j에 있는 문자를 하나씩 가져온다.
                    case += matrix[k][j]
                if is_palindrome(case):
                    return M


def is_palindrome(s):  # 문자열이 회문인지 검사하는 함수
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


T = 10

for _ in range(T):
    tc = input()
    matrix = [input() for _ in range(100)]
    logest_length = get_len_palindrome(matrix)

    print(f'#{tc} {logest_length}')
