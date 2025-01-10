n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

q, r = divmod(m, k+1)
answer = q*(arr[0]*k + arr[1]) + r*arr[0]
print(answer)
