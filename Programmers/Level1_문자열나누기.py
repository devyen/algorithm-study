def solution(s):
    answer = 0
    x = s[0]
    cnt1 = cnt2 = 0
    for i, ch in enumerate(s):
        if ch == x:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer += 1
            cnt1 = cnt2 = 0
            if i < len(s)-1:
                x = s[i+1]

    if cnt1 > 0:
        answer += 1
    
    return answer
