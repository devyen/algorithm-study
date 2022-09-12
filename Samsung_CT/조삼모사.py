import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]

combs = combinations(range(n), n//2)
answer = float('inf')
for comb in combs:
    evening = []
    for num in range(n):
        if num not in comb:
            evening.append(num)
    # 2개씩 뽑는 순열
    perms1 = permutations(comb, 2)
    perms2 = permutations(evening, 2)
    m_sum = n_sum = 0
    for i, j in perms1:
        m_sum += P[i][j]
    for i, j in perms2:
        n_sum += P[i][j]
    answer = min(answer, abs(m_sum-n_sum))

print(answer)