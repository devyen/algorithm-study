data = input()  # a1
i = ord(data[0]) - ord('a') + 1
j = int(data[1])

d = ((-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1))
result = 0
for di, dj in d:
    ni, nj = i+di, j+dj
    if 1 <= ni <= 8 and 0 <= nj <= 8:
        result += 1

print(result)
