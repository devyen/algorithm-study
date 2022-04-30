'''
idea
'''


def to_binary(x, n):
    binary = ''
    while x > 0:
        binary = str(x % 2) + binary
        x = x // 2
    binary = '0' * (n - len(binary)) + binary
    return binary


def solution(n, arr1, arr2):
    matrix = [[' ']*n for _ in range(n)]
    for i in range(n):
        bin1, bin2 = to_binary(arr1[i], n), to_binary(arr2[i], n)
        for j in range(n):
            matrix[i][j] = '#' if (int(bin1[j]) or int(bin2[j])) else ' '

    answer = []
    for i in range(n):
        answer.append(''.join(matrix[i]))
    return answer


result = solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28])
print(result)