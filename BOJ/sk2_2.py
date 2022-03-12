def solution(n, clockwise):
    matrix = [[0]*n for _ in range(n)]

    def go(i, j, k):
        num = 0
        start = 0
        cnt = 0
        while num < 7:
            if num == 7:
                break
            if not start and k != 0:
                pass
            else:
                start = 1
                cnt += 1
                while j < n - cnt:  # 우향
                    num += 1
                    matrix[i][j] = num
                    j += 1

            if num == 7:
                break
            if not start and k != 1:
                pass
            else:
                start = 1
                i += 1
                j -= 1
                cnt += 1
                while i < n - cnt:  # 하향
                    num += 1
                    matrix[i][j] = num
                    i += 1

            if num == 7:
                break
            if not start and k != 2:
                pass
            else:
                start = 1
                j -= 1
                i -= 1
                cnt += 1
                while j >= n - cnt:  # 좌향
                    num += 1
                    matrix[i][j] = num
                    j -= 1

            if num == 7:
                break
            if not start and k != 2:
                pass
            else:
                start = 1
                i -= 1
                j += 1
                num += 1
                cnt += 1
                while i >= n - cnt:  # 상향
                    matrix[i][j] = num
                    num += 1
                    i += 1

    if clockwise:  # 시계방향
        for k, val in enumerate(((0, 0), (0, n-1), (n-1, n-1), (n-1, 0))):
            go(val[0], val[1], k)


    answer = [[]]
    return matrix


solution(5, True)