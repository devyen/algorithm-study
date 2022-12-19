def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for e in range(m-1, len(score), m):
        answer += score[e]*m
    return answer


result = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
print(result)
