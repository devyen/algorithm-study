from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    # half = (sum(queue1) + sum(queue2)) // 2
    max_cnt = len(queue1)*2
    cnt = 0
    while sum(queue1) != sum(queue2) and cnt <= max_cnt:
        if sum(queue1) < sum(queue2):
            queue1.append(queue2.popleft())
            # queue1 = queue1 + [queue2[0]]
            # queue2 = queue2[1:]
        else:
            queue2.append(queue1.popleft())
            # queue2 = queue2 + [queue1[0]]
            # queue1 = queue1[1:]
        cnt += 1
    if sum(queue1) == sum(queue2):
        return cnt
    else:
        return -1


result = solution([1, 2, 1, 2],	[1, 10, 1, 2])
print(result)