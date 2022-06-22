import sys

sys.stdin = open('input.txt')

# 왜 자꾸 오답..?


def forth_calculator(forth):  # ['10', '2', '+', '3', '4', '+', '*', '.']
    stack = [int(forth[0])]  # 첫번째 원소는 항상 숫자니까 먼저 스택에 넣고 시작
    i = 1
    while stack and i < len(forth):
        try:
            # 마침표이면 연산 결과를 리턴
            if forth[i] == '.':
                return stack.pop()

            # 사칙연산
            elif forth[i] == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif forth[i] == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif forth[i] == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif forth[i] == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a / b)

            else:  # 숫자이면 스택에 push
                stack.append(int(forth[i]))

            i += 1

        except:
            return 'error'

    # return 'error'

T = int(input())
for tc in range(1, T+1):
    postfix = list(input().split())

    print(f'#{tc} {forth_calculator(postfix)}')
