def operate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2


def get_result(perm, splited):  # perm 순서에 따라 계산하는 함수
    for o in perm:
        i = 0
        while i < len(splited):
            if splited[i] == o:
                rst = operate(o, splited[i-1], splited[i+1])
                splited = splited[:i-1] + [rst] + splited[i+2:]
            else:
                i += 1
    return splited[0]


def solution(expression):
    # 숫자와 연산자로 쪼개기
    splited = []
    num = ''
    for c in expression:
        if c in ('+', '-', '*'):
            splited.append(int(num))
            num = ''
            splited.append(c)
        else:
            num += c
    splited.append(int(num))

    # 순열 만들기
    perms = []
    for o1 in ('+', '-', '*'):
        for o2 in ('+', '-', '*'):
            if o2 != o1:
                for o3 in ('+', '-', '*'):
                    if o3 != o1 and o3 != o2:
                        perms.append([o1, o2, o3])

    # 완전탐색하며 최대값 갱신
    answer = 0
    for perm in perms:
        answer = max(answer, abs(get_result(perm, splited)))

    return answer


result = solution("100-200*300-500+20")
print(result)