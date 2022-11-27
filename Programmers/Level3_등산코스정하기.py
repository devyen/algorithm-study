from collections import deque


def solution(queue1, queue2):
    l = len(queue1+queue2)
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    answer = 0
    flag = 0
    while True:
        if s1 == s2:
            flag = 1
            break
        elif s1 > s2:
            tmp = q1.popleft()
            s1 -= tmp
            q2.append(tmp)
            s2 += tmp
        else:
            tmp = q2.popleft()
            s2 -= tmp
            q1.append(tmp)
            s1 += tmp
        answer += 1
        if answer > l:
            break
    if flag:
        return answer
    else:
        return -1


result = solution([1, 2, 1, 2], [1, 10, 1, 2])
print(result)
