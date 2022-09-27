import sys
sys.stdin = open('input.txt')


# 부분집합을 만들어 최적값을 찾는 문제!
def comb(idx, total):
    global low
    if idx == n or total >= B:  # 끝까지 탐색 or B를 이미 넘었으면 더 더할 필요X
        if low > total >= B:
            low = total
        return

    # idx번째 점원 키 포함
    comb(idx+1, total + heights[idx])
    # 안 포함
    comb(idx+1, total)


T = int(input())
for tc in range(1, T+1):
    n, B = map(int, input().split())
    heights = sorted(list(map(int, input().split())))

    low = float('inf')  # 최적값(B보다 높은 것 중 가장 낮은 탑)
    comb(0, 0)

    print(f'#{tc} {low-B}')