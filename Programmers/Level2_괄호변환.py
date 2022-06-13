def is_wright(w):
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            stack.append(w[i])
        elif w[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) > 0:
        return False
    return True


def get_reverse(w):
    rst = ''
    for c in w:
        rst += ')' if c == '(' else '('
    return rst


def bracket(w):
    if w == '':
        return ''

    # 균형잡힌 괄호 문자열 u, v로 분리
    cnt1 = cnt2 = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt1 += 1
        elif w[i] == ')':
            cnt2 += 1
        if cnt1 == cnt2:
            u, v = w[:i+1], w[i+1:]
            break

    if is_wright(u):
        return u + bracket(v)
    else:
        rst = '(' + bracket(v) + ')' + get_reverse(u[1:-1])
        return rst


def solution(p):
    if is_wright(p):
        return p
    answer = bracket(p)
    return answer


result = solution("()))((()")
print(result)