def solution(logs):
    def check(log):
        if len(log) > 100:
            return 1

        if log.count(' ') != 11:
            return 1

        tokens = log.split()
        if len(tokens) != 12:
            return 1

        names = []
        for i in range(12):
            if not i % 3:
                names.append(tokens[i])
            if i % 3 == 1:
                if tokens[i] != ':':
                    return 1
            if i % 3 == 2:
                if not tokens[i].isalpha():
                    return 1

        if names != ['team_name', 'application_name', 'error_level', 'message']:
            return 1

        return 0

    cnt = 0
    for log in logs:
        cnt += check(log)
    return cnt