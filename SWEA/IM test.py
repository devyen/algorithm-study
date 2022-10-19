import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    pattern = [0] + list(map(int, input().split()))  # 인덱스를 led 번호와 맞추기 위해 0번 인덱스를 추가

    # idea: 반대로 현재 패턴에서 몇 번을 조작하면 모두 off 가 되는지 구한다!
    # 스위치를 누르면 i의 배수의 상태가 전부 바뀌므로 앞에서 뒤로 순회한다.
    cnt = 0  # 스위치 조작 횟수
    for i in range(1, n+1):
        if pattern[i] == 1:  # i번 led가 켜져있으면 버튼 누르기
            cnt += 1
            for k in range(i, n+1, i):  # i의 배수를 돌면서
                if pattern[k] == 1:  # 불이 켜져있으면
                    pattern[k] = 0  # 끄기
                else:  # 불이 꺼져있으면
                    pattern[k] = 1  # 켜주기

    print(f'#{tc} {cnt}')