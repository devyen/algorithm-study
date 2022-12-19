def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for s in range(0, len(score)-m+1, m):
        answer += score[s+m-1]*m
    return answer


result = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
print(result)
