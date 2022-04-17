def solution(record):
    logs = []
    nickname = {}
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            logs.append(['enter', tmp[1]])
            nickname[tmp[1]] = tmp[2]
        elif tmp[0] == 'Leave':
            logs.append(['leave', tmp[1]])
        elif tmp[0] == 'Change':
            nickname[tmp[1]] = tmp[2]

    answer = []
    for log in logs:
        if log[0] == 'enter':
            answer.append(f'{nickname[log[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname[log[1]]}님이 나갔습니다.')
    return answer


result = solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
])
print(result)