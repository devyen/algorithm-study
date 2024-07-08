from collections import deque


def solution(n, m, section):
    q = deque(section)
    answer = 1
    x = q.popleft()
    paint = x + m - 1
    while q:        
        x = q.popleft()
        if x > paint:
            answer += 1        
            paint = x + m - 1

    return answer
