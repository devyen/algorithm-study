import sys
input = sys.stdin.readline

n = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(n)])

max_rst = -1
for i in range(n):
    if n - i + 1 <= max_rst:
        break
    s, e = meetings[i]
    cnt = 1
    for j in range(i+1, n):
        ns, ne = meetings[j]
        if ns >= e:
            cnt += 1
            s, e = ns, ne
    max_rst = max(max_rst, cnt)

print(max_rst)