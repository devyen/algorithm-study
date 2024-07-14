# 시간 초과
# def solution(players, callings):
#     for c in callings:
#         idx = players.index(c)
#         p = players[idx-1]
#         players[idx-1], players[idx] = c, p
#     return players

def solution(players, callings):
    dic1 = {}
    dic2 = {}
    for i, p in enumerate(players):
        dic1[p] = i
        dic2[i] = p
        
    for c in callings:
        # dic1 update
        idx = dic1[c]
        loser = dic2[idx-1]
        dic1[c], dic1[loser] = idx-1, idx
        # dic2 update        
        dic2[idx-1], dic2[idx] = c, loser
        
    answer = [v for k, v in sorted(dic2.items(), key=lambda x: x[0])]
    return answer
