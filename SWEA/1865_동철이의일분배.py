import sys

sys.stdin = open('input.txt')


# idx: 현재 누가할지 정할 일의 인덱스, s: 현재까지의 확률
def dfs(idx, s):  # idx번째의 일을 할 사람을 정한다
    global result

    if idx == n:
        # 완성. 확률 계산해서 최대값과 비교
        if s > result:
            result = s
        return

    # 가지치기: s는 1이하의 확률이기 때문에 곱할수록 같거나 작아진다. 따라서 현재 s값이 최대값보다 작으면 더 이상 보지 않아도 된다.
    if s > result:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(idx+1, s*matrix[i][idx]/100)  # 해당 확률을 곱한다
                visited[i] = 0  # 방문체크 해제


T = int(input())
T = 1
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    result = 0
    dfs(0, 1)

    print(f'#{tc} {result*100:.6f}')