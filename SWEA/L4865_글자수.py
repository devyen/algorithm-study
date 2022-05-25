import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str1에 포함된 글자를 키로 가지는 딕셔너리를 만든다.
    cnt = {}
    for i in str1:
        cnt[i] = 0

    # str2를 돌면서 str1에 있는 글자가 있다면 딕셔너리 value를 +1
    for j in str2:
        if j in str1:
            cnt[j] += 1

    # cnt 중 최대값 찾기
    max = 0
    for k in cnt.values():
        if k > max:
            max = k

    print(f'#{tc} {max}')