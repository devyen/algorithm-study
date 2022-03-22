import sys
input = sys.stdin.readline


def comb(i, s):
    global cnt

    if i == n:
        if s == target_s:
            cnt += 1
        return

    comb(i+1, s)  # 미포함
    comb(i+1, s + A[i])  # 포함


n, target_s = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
comb(0, 0)

if target_s == 0:  # 타겟 값이 0인 경우는
    cnt -= 1  # 모든 원소를 포함하지 않는 부분집합(공집합)을 제외해야한다.

print(cnt)