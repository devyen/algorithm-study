'''
idea
교집합 -> set1을 돌면서 딕셔너리로 카운트하고, 그다음 set2를 돌면서 겹치는걸 카운트
합집합 -> 카운트한 딕셔너리에 해당 원소가 없으면 합집합 +1
'''
import math


def make_set(s):
    result = []
    for i in range(len(s)-1):
        if s[i:i+2].isalpha():
            result.append(s[i:i+2].upper())
    return result


def solution(str1, str2):
    set1, set2 = make_set(str1), make_set(str2)
    if len(set1) + len(set2) == 0:  # 둘다 공집합이면
        return 65536

    el_count = {}
    for el in set1:
        el_count[el] = el_count.get(el, 0) + 1

    inter, union = 0, len(set1)
    for el in set2:
        if el_count.get(el, 0):
            inter += 1
            el_count[el] -= 1  # 1개 겹치는거 체크했으면 1개 없애줘야함
        else:
            union += 1
    answer = math.trunc(inter/union * 65536)
    return answer


result = solution('FRANCE', 'french')
print(result)