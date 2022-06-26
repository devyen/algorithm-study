def solution(n, t, m, p):
    def change_number(num):
        rst = ''
        while num > 0:
            q, r = divmod(num, n)
            if r >= 10:
                r = chr(r+55)
            rst = str(r) + rst
            num = q
        return rst

    p -= 1
    game = '0'
    num = 1
    while len(game) <= (t-1)*m + p:
        game += change_number(num)
        num += 1

    answer = ''
    for i in range(t):
        answer += game[i*m + p]

    return answer


result = solution(16, 16, 2, 1)
print(result)