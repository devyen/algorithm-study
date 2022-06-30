def solution(n, build_frame):
    def install_check(i, j, type):
        if type:  # 보
            if 0 <= i+1 < n+1 and matrix2[i+1][j]:
                return True
            if 0 <= i+1 < n+1 and 0 <= j+1 < n+1 and matrix2[i+1][j+1]:
                return True
            if j == 0:
                return False
            if 0 <= j-1 < n+1 and 0 <= j+1 < n+1 and matrix1[i][j-1] and matrix1[i][j+1]:
                return True
        else:  # 기둥
            if i == n:
                return True
            if 0 <= j-1 < n+1 and matrix1[i][j-1]:
                return True
            if matrix1[i][j]:
                return True
            if 0 <= i+1 < n+1 and matrix2[i+1][j]:
                return True
        return False

    # def delete_check():
    #     if type:  # 보
    #         # 오른쪽보 matrix1[i][j+1], 왼쪽보 matrix1[i][j-1], 기둥1 matrix2[i][j], 기둥2 matrix2[i][j+1] 체크
    #         return install_check(i, j+1, 1) and install_check(i, j-1, 1) and install_check(i, j, 0) and install_check(i, j+1, 0)
    #     else:  # 기둥
    #         # 오른쪽보 matrix1[i-1][j], 왼쪽보 matrix1[i-1][j-1], 윗기둥 matrix2[i-1][j]
    #         return install_check(i-1, j, 1) and install_check(i-1, j-1, 1) and install_check(i-1, j, 0)

    matrix1 = [[0]*(n+1) for _ in range(n+1)]  # 보
    matrix2 = [[0]*(n+1) for _ in range(n+1)]  # 기둥

    for x, y, type, install in build_frame:  # type 0:기둥, 1:보
        i, j = n-y, x
        if install:  # 설치
            if install_check(i, j, type):
                if type:
                    matrix1[i][j] = 1
                else:
                    matrix2[i][j] = 1

        else:  # 일단 삭제하고 괜찮은지 체크
            if type:
                matrix1[i][j] = 0
            else:
                matrix2[i][j] = 0

            # 전체 체크
            flag = 0
            for r in range(n + 1):
                for c in range(n + 1):
                    if matrix1[r][c] and not install_check(r, c, 1):
                        flag = 1
                        break
                    if matrix2[r][c] and not install_check(r, c, 0):
                        flag = 1
                        break
                if flag:
                    break
            if flag:  # 복구
                if type:
                    matrix1[i][j] = 1
                else:
                    matrix2[i][j] = 1

            # if not delete_check():
            #     if type:
            #         matrix1[i][j] = 1
            #     else:
            #         matrix2[i][j] = 1

    answer = []
    for r in range(n+1):
        for c in range(n+1):
            if matrix1[r][c]:
                answer.append([c, n-r, 1])
            if matrix2[r][c]:
                answer.append([c, n-r, 0])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


result = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(result)