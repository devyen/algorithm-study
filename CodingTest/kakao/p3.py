# from collections import deque
import math

def solution(alp, cop, problems):
    # 풀수있는 문제 없는 문제 먼저 가르기
    # solved, unsolved = deque([]), deque([])
    solved = []
    unsolved = []
    for p in problems:
        if p[0] <= alp and p[1] <= cop:
            solved.append(p)
        else:
            unsolved.append(p)
    solved.sort(key=lambda x: -(x[2]+x[3])/x[4])  # 가성비 순
    unsolved.sort(key=lambda x: (x[0], x[1]))  # 난이도 순

    cnt = 0
    if len(solved) == 0 or solved[0][2]+solved[0][3] <= solved[0][4]:
        alp_req, cop_req = unsolved[0][:2]
        cnt += alp_req - alp + cop_req - cop

    while unsolved:
        now = unsolved[0]
        alp_gap = now[0] - alp
        cop_gap = now[1] - cop
        # 뭐가 더 효율적인지 비교
        for s in solved:  # 효율 순으로 정렬되어있다고 가정
            if s[4] <= alp_gap + cop_gap:
                num = max(math.ceil(alp_gap//s[2]), math.ceil(cop_gap//s[3]))
                time = s[4]*num
                if time <= alp_gap + cop_gap:
                    cnt += time
                    alp += s[2]*num
                    cop += s[3]*num
                else:
                    cnt += alp_gap + cop_gap
                    alp, cop = now[0], now[1]

                solved.append(unsolved[0])
                solved.sort(key=lambda x: -(x[2]+x[3])/x[4])  # 재정렬
                unsolved = unsolved[1:]
                break

    answer = 0
    return answer


result = solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
print(result)