n, m = map(int, input().split())
answer = 0
for _ in range(n):
    row_min = min(list(map(int, input().split())))
    answer = max(answer, row_min)

print(answer)
