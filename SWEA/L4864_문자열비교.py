import sys
sys.stdin = open('input.txt')

def is_part_match(str1, str2):
    N, M = len(str1), len(str2)

    for i in range(M - N + 1):
        if str2[i:i+N] == str1:
            return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = is_part_match(str1, str2)

    print(f'#{tc} {result}')