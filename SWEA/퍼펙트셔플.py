import sys
sys.stdin = open('퍼펙트셔플.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = input().split()  # ['A', 'B', 'C', 'D', 'E', 'F']

    if not n % 2:  # n이 짝수이면
        half1 = cards[:n//2]
        half2 = cards[n//2:]

        new = []
        for i in range(n//2):
            new.append(half1[i])
            new.append(half2[i])

    else:  # n이 홀수이면
        half1 = cards[:n//2 + 1]
        half2 = cards[n//2 + 1:]

        new = []
        for i in range(n//2):
            new.append(half1[i])
            new.append(half2[i])
        new.append(half1[-1])

    print(f'#{tc}', *new)