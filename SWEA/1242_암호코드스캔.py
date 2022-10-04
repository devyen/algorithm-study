import sys

'68B46DDB9346F4'
# b = bin(0x68B46DDB9346F4)#[2:]  # 맨 앞자리 숫자는 앞에 0이 생략되어 나온다
# print(b)
# print(len(b))

sys.stdin = open('input.txt')

T = int(input())
# T = 1
for tc in range(1, T+1):
    n, m = map(int, input().split())  # n: 세로 길이  m: 가로 길이
    matrix = [input() for _ in range(n)]

    # for row in matrix:
    #     for x in row:
    #         if x != '0':  # x가 '0'이 아니면
    #             pwds = row.split('0')
    #             for pwd in pwds:
    #                 if pwd and pwd not in temp:
    #                     temp.append(pwd)
    # print(f'#{tc}')
    # print(temp)

    # 내 코드
   # temp = []
    # raw_codes = []
    # for _ in range(n):
    #     row = input()
    #     temp = ''
    #     for c in range(m):
    #         if row[c] != '0':
    #             temp += row[c]
    #         elif row[c] == '0' and temp:  # 0인데 temp가 비어있지 않으면 => 코드가 완성되었다는 것
    #             if temp not in raw_codes:
    #                 raw_codes.append(temp)  # temp를 raw_codes에 추가하고
    #             temp = ''  # 다시 빈값으로 만들어준다.
    # print(raw_codes)
