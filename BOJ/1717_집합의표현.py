import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[a] = b


n, m = map(int, input().split())
parent = list(range(n+1))
for _ in range(m):
    cal, a, b = map(int, input().split())

    if cal:
        if a == b:
            print('YES')
        else:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')
    else:
        union(a, b)