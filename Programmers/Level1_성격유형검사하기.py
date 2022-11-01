def solution(survey, choices):
    def decide_type(t1, t2):
        t1, t2 = sorted([t1, t2])  # 사전 순 정렬
        nonlocal answer
        if points[t1] >= points[t2]:
            answer += t1
        else:
            answer += t2

    points = {}
    for char in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']:
        points[char] = 0

    for idx, choice in enumerate(choices):
        if choice < 4:
            points[survey[idx][0]] += 4 - choice
        elif choice > 4:
            points[survey[idx][1]] += choice - 4

    answer = ''
    for a, b in [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        decide_type(a, b)
    return answer


result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
print(result)
