def solution(name, yearning, photo):
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    answer = []
    for ph in photo:
        num = 0
        for p in ph:
            num += score.get(p, 0)
        answer.append(num)
    return answer
