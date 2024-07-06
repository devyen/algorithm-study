def solution(keymap, targets):
    l = max(len(key) for key in keymap)
    print(l)
    dp = {}

    def get_press_cnt(a):
        if dp.get(a):
            return dp[a]
        
        for i in range(l):
            for key in keymap:
                if i >= len(key):
                    continue
                if key[i] == a:
                    dp[a] = i+1
                    return dp[a]
        dp[a] = -1
        return dp[a]
        
    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            res = get_press_cnt(t)
            if res == -1:
                cnt = -1
                break
            cnt += res
        answer.append(cnt)
        
    return answer
