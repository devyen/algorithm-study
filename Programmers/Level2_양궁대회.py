import copy


def solution(n, info):
    def cal_diff():
        ascore = lscore = 0
        for i in range(11):
            if info[i] == 0 and lion_info[i] == 0:
                continue
            elif info[i] >= lion_info[i]:
                ascore += 10-i
            else:
                lscore += 10-i
        return lscore - ascore

    def dfs(i, s):
        nonlocal lion_info, max_diff, result

        if s == n:
            diff = cal_diff()
            if diff:
                if diff > max_diff:
                    max_diff = diff
                    result = [copy.deepcopy(lion_info)]
                elif diff == max_diff:
                    result.append(copy.deepcopy(lion_info))
            return

        if i >= len(info):
            return

        # 마지막 점수면 남은 화살 모두
        if i == len(info)-1:
            lion_info[i] = n-s
            dfs(i + 1, s + lion_info[i])
            lion_info[i] = 0
            return

        # 2가지 경우
        # 어피치보다 1발 더 쏘거나
        if s+info[i]+1 <= n:
            lion_info[i] = info[i]+1
            dfs(i+1, s+lion_info[i])
        # 아예 쏘지 않거나
        lion_info[i] = 0
        dfs(i+1, s+lion_info[i])

        return

    lion_info = [0]*11
    max_diff = 0
    result = []
    dfs(0, 0)

    if len(result) == 0:
        return [-1]
    result.sort(key=lambda x: x[::-1], reverse=True)
    return result[0]


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))