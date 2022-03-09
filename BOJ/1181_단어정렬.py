import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    word = input().rstrip()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=lambda x: len(x))

for word in words:
    print(word)
