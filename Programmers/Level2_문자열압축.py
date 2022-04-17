def solution(s):
    n = len(s)
    answer = float('inf')
    for k in range(1, n//2+1):
        result = ''
        pattern = s[0:k]
        i, cnt, flag = k, 1, 0
        while i < n:
            if n-i < k:  # next 길이가 모자란 경우 -> 이전 패턴 & 남은 부분을 result에 이어붙인다
                result += str(cnt) + pattern + s[i:]
                flag = 1
                break
            next = s[i:i+k]
            if next == pattern:
                cnt += 1
            else:
                result += str(cnt) + pattern
                pattern = next
                cnt = 1
            i += k
        if not flag:  # 마지막 패턴 이어붙이기
            result += str(cnt) + pattern
        result = result.replace('1', '')
        answer = min(answer, len(result))
    return answer


result = solution('aabbaccc')
print(result)