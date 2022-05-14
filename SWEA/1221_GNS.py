import sys
sys.stdin = open('input.txt')

# 문자 -> 숫자로 바꾸는 함수
def to_num(str):
    # 딕셔너리로 찾기
    num_dict = {
        'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
        'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
                }
    for key in num_dict:
        if str == key:
            return num_dict[key]  # 숫자를 리턴


# 숫자 -> 문자로 바꾸는 함수
def to_str(num):
    num_dict = {
        'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
        'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
                }
    for key in num_dict:
        if num == num_dict[key]:
            return key  # 문자를 리턴


T = int(input())

for _ in range(1, T+1):
    tc, n = input().split()
    n = int(n)
    words = list(input().split())

    # 1. 먼저 단어들을 숫자로 바꾼다.
    for i in range(n):
        words[i] = to_num(words[i])

    # 2. 작은 수부터 정렬 - 선택정렬
    for i in range(n-1):
        min = i

        for j in range(i+1, n):
            if words[j] < words[min]:
                min = j
        words[i], words[min] = words[min], words[i]  # 교환

    # 3. 숫자들을 다시 단어로 바꾼다.
    for i in range(n):
        words[i] = to_str(words[i])

    print(tc)
    print(*words)
