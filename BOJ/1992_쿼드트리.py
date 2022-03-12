import sys
input = sys.stdin.readline

'''
idea
재귀를 이용해 더 작은 문제로 쪼갠다.
'''


def quad_tree(i, j, k):  # i, j: 영역의 좌상단 좌표, k: 한변의 길이
    if k == 1:
        if matrix[i][j]:
            return '1'
        else:
            return '0'

    a = quad_tree(i, j, k//2)  # 왼쪽 위
    b = quad_tree(i, j+k//2, k//2)  # 오른쪽 위
    c = quad_tree(i+k//2, j, k//2)  # 왼쪽 아래
    d = quad_tree(i+k//2, j+k//2, k//2)  # 오른쪽 아래

    if a == b == c == d:
        if a == '1':
            return '1'
        else:
            return '0'

    return '(' + a + b + c + d + ')'


n = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]

result = quad_tree(0, 0, n)
if result[0] != '(':
    result = '(' + result + ')'
print(result)


