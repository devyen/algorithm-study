def solution(m, n, board):
    def check(i, j):  # False OR 터트릴 블록들을 반환하는 함수
        k = matrix[i][j]
        if k == 0:
            return False
        blocks = [(i, j)]
        for di, dj in ((0, 1), (1, 1), (1, 0)):  # 2*2 왼쪽 꼭지점 기준으로 탐색
            ni, nj = i+di, j+dj
            if matrix[ni][nj] != k:
                return False
            blocks.append((ni, nj))
        return blocks

    def pang(i, j):
        nonlocal answer
        matrix[i][j] = 0  # 0으로 체크
        answer += 1
        while i > 0:  # 위 블록들 내리기
            matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]
            i -= 1

    matrix = [list(b) for b in board]
    answer = 0
    while True:
        # 터트릴 블록들 pang_blocks에 담기
        pang_blocks = []
        for i in range(m-1):
            for j in range(n-1):
                rst = check(i, j)
                if rst:
                    pang_blocks += rst
        pang_blocks = list(set(pang_blocks))  # 중복 블럭 제거
        pang_blocks.sort()
        if len(pang_blocks) == 0:  # 더이상 터트릴 것이 없으면 break
            break
        # 터트리기
        for block in pang_blocks:
            pang(block[0], block[1])

    return answer


result = solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
print(result)