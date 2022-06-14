from collections import deque


def solution(queue1, queue2):
    def dfs(from_q, to_q, s):
        nonlocal min_cnt, flag

        queue = deque([(from_q, to_q)])
        while queue:
            now = queue.popleft()

            queue.append((from_q, to_q))
            queue.append((to_q, from_q))

        if s >= min_cnt or s >= max_cnt:
            return
        if sum(from_q) == half:
            min_cnt = min(min_cnt, s)
            flag = 1
            return

        if len(from_q) == 0:
            return
        to_q.append(from_q.popleft())

        dfs(from_q, to_q, s+1)
        dfs(to_q, from_q, s+1)

        from_q.appendleft(to_q.pop())

    queue1, queue2 = deque(queue1), deque(queue2)
    half = (sum(queue1) + sum(queue2)) // 2
    max_cnt = len(queue1)*2*2
    flag = 0
    min_cnt = float('inf')
    for from_q, to_q in ((queue1, queue2), (queue2, queue1)):
        dfs(from_q, to_q, 0)

    if flag:
        return min_cnt
    else:
        return -1


result = solution([1, 2, 1, 2],	[1, 10, 1, 2])
print(result)