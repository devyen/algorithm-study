import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = 10

for _ in range(T):
    tc = int(input())
    word = input()  # 찾을 문자열
    sentence = input()  # 검색할 문장

    cnt = 0
    for i in range(len(sentence)):
        if sentence[i:i+len(word)] == word:  # i 부터 찾는 문자열 길이만큼 슬라이싱
            cnt += 1

    print(f'#{tc} {cnt}')