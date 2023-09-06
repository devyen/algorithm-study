def cal_expire(date, plus):
    y, m, d = date
    # month
    m += plus
    q, r = divmod(m, 12)
    if r == 0:
        q, r = q - 1, 12
    y, m = y + q, r
    # date
    d -= 1
    if d == 0:
        m, d = m - 1, 28
        if m == 0:
            y, m = y - 1, 12
    return [y, m, d]


def is_expired(date, today):
    for d, t in zip(date, today):
        if d > t:
            return False
        elif d < t:
            return True
    return False


def solution(today, terms, privacies):
    term_dict = {}
    for term in terms:
        name, due = term.split()
        term_dict[name] = int(due)

    answer = []
    today = list(map(int, today.split('.')))
    for idx, p in enumerate(privacies):
        date, name = p.split()
        date = list(map(int, date.split('.')))
        exp_date = cal_expire(date, term_dict[name])
        if is_expired(exp_date, today):
            answer.append(idx + 1)

    return answer
