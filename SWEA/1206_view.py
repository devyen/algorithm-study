import sys
sys.stdin = open('input.txt')

# 앞 2칸 뒤 2칸이 조망되는지 확인하는 함수를 정의
def is_sight(i):
    l1 = houses[i] - houses[i - 1]
    l2 = houses[i] - houses[i - 2]
    r1 = houses[i] - houses[i + 1]
    r2 = houses[i] - houses[i + 2]
    if l1 > 0 and l2 > 0 and r1 > 0 and r2 > 0:
        # 가장 작은 값이 조망확보 세대수임
        return min(l1, l2, r1, r2)

T = 10  # 테스트 케이스 10개라고 주어짐

for tc in range(1, T+1):
    length = int(input())
    houses = list(map(int, input().split()))
    total = 0
    for i in range(length)[2:-2]:  # 앞뒤 두칸은 0이므로 이를 제외한 부분만 검사한다.
        sight = is_sight(i)
        if sight:
            total += sight

    print(f'#{tc} {total}')