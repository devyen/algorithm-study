'''
idea
'''


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    scores = [0]  # 첫 번째 기회에서 *가 나오는 경우를 위해 맨앞에 0 세팅
    score = ''
    for char in dartResult:
        if char in ['S', 'D', 'T']:
            scores.append(int(score)**bonus[char])
            score = ''
        elif char == '*':
            scores[-1] *= 2
            scores[-2] *= 2
        elif char == '#':
            scores[-1] = -scores[-1]
        else:
            score += char
    return sum(scores)


result = solution('1D2S#10S')
print(result)