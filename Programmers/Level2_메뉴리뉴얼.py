'''
idea
- 부분집합 -> 2**n 이진수로 비트 활용
- subsets 딕셔너리로 부분집합 카운트
- 각 길이별로 가장 많이 주문된 조합을 구하기 위해 tmp에서 갱신
'''


def solution(orders, course):
    subsets = {}
    for order in orders:
        order = ''.join(sorted(order))  # 각 원소 또한 알파벳 오름차순으로 정렬
        for i in range(2**len(order)):  # 비트로 부분집합 만들기
            subset = ''
            binary = bin(i)[2:]
            binary = '0'*(len(order) - len(binary)) + binary
            for j in range(len(binary)):
                if binary[j] == '1':
                    subset += order[j]
            if len(subset) in course:
                subsets[subset] = subsets.get(subset, 0) + 1
    tmp = {}
    for key, val in subsets.items():
        if val >= 2 and val >= tmp.get(len(key), [0])[0]:
            if val == tmp.get(len(key), [0])[0]:  # 동일한 카운트가 있는 경우
                tmp[len(key)] += [key]
            else:
                tmp[len(key)] = [val, key]
    answer = []
    for key, val in tmp.items():
        answer += val[1:]
    answer.sort()
    return answer


result = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
print(result)