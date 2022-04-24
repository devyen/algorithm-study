from collections import deque


def solution(board, moves):
    basket = deque([0])
    answer = 0

    for move in moves:
        move -= 1
        last = basket[-1]
        for r in range(len(board)):
            pick = board[r][move]
            if pick > 0:
                if last == pick:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(pick)
                board[r][move] = -1  # 방문표시
                break
    return answer


b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
result = solution(b, m)
print(result)