import copy
import sys
input = sys.stdin.readline


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


def dfs(k, s):  # k : 1/2/3
    if s == n:  # 가지치기
        combs.append(copy.deepcopy(now))
        return

    if s > n:  # 가지치기
        return

    if k == 4:  # 베이스케이스
        return

    for i in range(n//k+1):
        for _ in range(i):
            now.append(k)
        dfs(k+1, s + k*i)
        for _ in range(i):
            now.pop()


T = int(input())
for _ in range(T):
    n = int(input())  # 1<= n <= 11

    combs = []
    now = []
    dfs(1, 0)

    cnt = 0
    for comb in combs:
        checks = [0] * 3  # check = [1의개수, 2의개수, 3의개수]
        for num in comb:
            checks[num-1] += 1  # num에서 1을 빼야 인덱스가 맞음

        tmp = factorial(len(comb))
        for check in checks:
            tmp /= factorial(check)
        cnt += tmp

    print(int(cnt))