'''
idea
- 튜플의 부분집합들이므로 먼저 길이로 정렬한다.
- 원소를 순서대로 구하기 위해선 이전 부분집합에 포함되지 않은 원소 하나를 찾으면 된다 -> `set`의 차집합 활용
'''


def solution(s):
    subsets = []
    split_list = s[1:-1].split('}')
    for sp in split_list:
        if len(sp) == 0:
            continue
        tmp = set([])
        for c in sp.replace('{', '').split(','):
            if c == '':
                continue
            tmp.add(int(c))
        subsets.append(tmp)
    subsets.sort(key=lambda x : len(x))

    answer = []
    prev = set([])
    for subset in subsets:
        answer.append(list(subset-prev)[0])  # 차집합
        prev = subset

    return answer


tc = "{{20,111},{111}}"
result = solution(tc)
print(result)