from math import floor


def solution(enroll, referral, seller, amount):
    def divide_profit(now, profit):
        while now != -1:
            if profit < 10:
                answer[now] += profit
                return
            give = floor(profit*0.1)
            answer[now] += profit - give
            now, profit = parents[now], give  # 재할당

    # 처음에 번호 매겨서 딕셔너리에 저장 -> 시간초과 해결
    dic = {}
    for idx, e in enumerate(enroll):
        dic[e] = idx

    parents = [-1]*len(enroll)
    for idx, r in enumerate(referral):
        if r != '-':
            parents[idx] = dic[r]

    answer = [0]*len(enroll)
    for i in range(len(seller)):
        divide_profit(dic[seller[i]], amount[i]*100)
    return answer


result = solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10],
)
print(result)
