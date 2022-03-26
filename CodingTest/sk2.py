def solution(n, clockwise):
    matrix = [[0]*n for _ in range(n)]


    def go(i, j, n, k):
        num = 1

        if n%2:
            cnt = 1
            while i != n//2 or j != n//2:
                while j < n - 1:  # 우향
                    if 0 <= j < n:
                        matrix[i][j] = num
                        num += 1
                        j += 1
                    else:
                        num -= 1
                        j -= 1
                        break

                i += 1
                num += 1
                while i < n - 2:  # 하향
                    matrix[i][j] = num
                    num += 1
                    i += 1

                j -= 1
                num += 1
                while j >= n - 3:  # 좌향
                    matrix[i][j] = num
                    num += 1
                    j -= 1

                i -= 1
                num += 1
                while i < n - 2:  # 상향
                    matrix[i][j] = num
                    num += 1
                    i += 1

        else:
            while (i, j) not in ((n//2, n//2), (n//2 + 1, n//2), (n//2, n//2 + 1), (n//2 + 1, n//2 + 1)):
                break






    if clockwise:  # 시계방향
        for i, j in ((0, 0), (0, n-1), (n-1, n-1), (n-1, 0)):


    answer = [[]]
    return matrix


solution(5, True)