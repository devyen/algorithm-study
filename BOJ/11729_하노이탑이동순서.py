import sys
input = sys.stdin.readline

'''
idea
재귀를 이용해 더 작은 문제로 쪼갠다.
'''


def hanoi(n, start, goal, sub):  # n개, start: 출발기둥, goal: 도착기둥, sub: 보조기둥
    if n == 1:
        print(start, goal)
        return

    hanoi(n-1, start, sub, goal)
    print(start, goal)
    hanoi(n-1, sub, goal, start)


n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)
