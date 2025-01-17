n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)  # 내림차순
for a in arr:
    print(a, end=' ')
