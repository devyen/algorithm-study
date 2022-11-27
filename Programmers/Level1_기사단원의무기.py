def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        cnt = 0
        for i in range(1, int(n**(1/2))+1):  # n의 제곱근까지만 탐색
            if n % i:
                continue
            cnt += 1
            if i ** 2 != n:  # 약수는 한 쌍
                cnt += 1
            if cnt > limit:  # 가지 치기
                break
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer


result = solution(5, 3, 2)
print(result)
