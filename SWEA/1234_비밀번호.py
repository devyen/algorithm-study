import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, password = input().split()  # password = '1238099084'

    while True:
        for i in range(len(password)-1):  # 여기서 range(n)으로 했다가 out of range 오류 났음! n을 len(password)로 바꿔주었다.
            if password[i] == password[i+1]:
                password = password[:i] + password[i+2:]  # i, i+1을 기준으로 앞뒤를 잘라내서 다시 붙인다.
                break
        else:  # 같은 번호 쌍이 없으면 반복문을 끝낸다.
            break

    print(f'#{tc} {password}')
