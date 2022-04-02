import sys
input = sys.stdin.readline


def comb(level, cnt):
    global result

    if cnt == n//2:
        team_b = []
        for i in range(n):
            if i not in team_a:
                team_b.append(i)

        score_a = 0
        score_b = 0
        for a in team_a:
            for aa in team_a:
                score_a += S[a][aa]
        for b in team_b:
            for bb in team_b:
                score_b += S[b][bb]
        if result > (difference := abs(score_a - score_b)):
            result = difference
        return

    # 베이스케이스
    if level == n:
        return

    team_a.append(level)
    comb(level + 1, cnt + 1)
    if level != 0:  # 1번(level==0)이 들어가는 조합만 구한다 -> 같은 조합을 2번씩 구하는걸 막기 위해
        team_a.pop()
        comb(level + 1, cnt)


n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

team_a = []
result = float('inf')
comb(0, 0)

print(result)