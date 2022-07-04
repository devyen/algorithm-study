def solution(gems):
    def check_all_in():
        for v in dicts.values():
            if v < 1:
                return False
        return True

    goal = len(set(gems))
    if goal == 1:
        return [1, 1]
    if goal == len(gems):
        return [1, len(gems)]

    dicts = {}
    min_l = len(gems)+1
    i = j = 0
    answer = []
    while i < len(gems) and j <= len(gems):
        if j < i:
            j = i
        l = j-i
        if l >= min_l:  # 가지치기
            dicts[gems[i]] -= 1
            if dicts[gems[i]] == 0:
                del dicts[gems[i]]
            i += 1
            continue
        if len(dicts) == goal:
            min_l = l
            answer = [i+1, j]
            dicts[gems[i]] -= 1
            if dicts[gems[i]] == 0:
                del dicts[gems[i]]
            i += 1
        else:
            if j >= len(gems):
                break
            dicts[gems[j]] = dicts.get(gems[j], 0)+1
            j += 1

    return answer


result = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
print(result)