'''
점화식 d[i] = max(d[i-2]+foods[i], d[i-1])
'''

# 보텀업
n = int(input())
foods = list(map(int, input().split()))
d = [0] * n
d[0] = foods[0]
d[1] = max(foods[0], foods[1])

for i in range(2, n):
    d[i] = max(d[i-2]+foods[i], d[i-1])

print(d[n-1])