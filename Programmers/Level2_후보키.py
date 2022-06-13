from itertools import combinations


def solution(relation):
    n = len(relation[0])

    candidate_keys = []
    for i in range(1, n+1):
        combs = list(combinations(range(n), i))

        # 해당 속성이 후보키인지 검사
        for comb in combs:
            # 최소성 체크
            flag = 0
            for key in candidate_keys:
                a = set(key)
                b = set(comb)
                if len(a & b) == len(a):  # 집합 a가 b에 포함되어있는지
                    flag = 1
                    break
            if flag:
                continue

            # 유일성 체크
            tuples = [tuple([r[c] for c in comb]) for r in relation]
            if len(list(set(tuples))) == len(tuples):  # 중복되는 것이 없을 때 -> 유일성
                candidate_keys.append(comb)
    return len(candidate_keys)


result = solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])
print(result)