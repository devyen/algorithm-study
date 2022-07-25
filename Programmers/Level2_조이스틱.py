def solution(progresses, speeds):
    answer = []
    day = 0
    for i in range(len(progresses)):
        if progresses[i]+speeds[i]*day >= 100:
            answer[-1] += 1
            continue
        day, r = divmod(100-progresses[i], speeds[i])
        if r:
            day += 1
        answer.append(1)
    return answer


result = solution([93, 30, 55], [1, 30, 5])
print(result)