def solution(survey, choices):
    # type_cnt = []
    # for t1, t2 in (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')):
    #     type_cnt.append({t1: 0, t2: 0})
    type_cnt = {}
    for t in ('R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'):  # 사전 순서
        type_cnt[t] = 0
    scores = [0, -3, -2, -1, 0, 1, 2, 3]  # 0번 인덱스는 빈값
    for i in range(len(survey)):
        score = scores[choices[i]]
        k = 0 if score < 0 else 1
        type_cnt[survey[i][k]] = type_cnt.get(survey[i][k], 0) + abs(score)

    answer = ''
    for t1, t2 in (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')):
        if type_cnt[t1] >= type_cnt[t2]:
            answer += t1
        else:
            answer += t2
    return answer


result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
print(result)