n = int(input())

# 계수 정렬
matrix = [[] for _ in range(101)]
for _ in range(n):
    name, score = input().split()
    score = int(score)
    matrix[score].append(name)

for score in matrix:
    for name in score:
        print(name, end=' ')
