def solution(N, stages):
    m = len(stages)  # 전체 플레이어 수
    stop_cnt = [0] * (N + 2)  # 0번 인덱스는 빈 자리, n+1번 인덱스는 n+1 체크
    for stage in stages:
        stop_cnt[stage] += 1

    # 실패율 구하기
    rates = []
    p = m  # 스테이지에 도달한 플레이어 수 카운팅
    for i in range(1, N + 1):
        p -= stop_cnt[i - 1]  # 점점 감소
        if p == 0:  # 0으로 나누는 경우 처리 -> 안하면 런타임에러 발생함
            rates.append((0, i))
        else:
            rates.append((stop_cnt[i] / p, i))  # (실패율, 인덱스)
    r = sorted(rates, key=lambda rate: (-rate[0], rate[1]))
    answer = [rate[1] for rate in r]
    return answer


b = [2, 1, 2, 6, 2, 4, 3, 3, 0]
result = solution(5, b)
print(result)