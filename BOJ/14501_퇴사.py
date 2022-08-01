import sys
input = sys.stdin.readline


def dfs(now, s):
    global answer
    if s > answer:
        answer = s
    if now >= n:
        return
    for i in range(now, n):
        if i+consults[i][0] <= n:
            dfs(i+consults[i][0], s+consults[i][1])


n = int(input())
consults = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i, consult in enumerate(consults):
    if i+consult[0] <= n:
        dfs(i+consult[0], consult[1])

print(answer)