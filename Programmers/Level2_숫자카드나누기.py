# def solution(number, limit, power):
#     answer = 0
#     for n in range(1, number+1):
#         cnt = 0
#         for i in range(1, int(n**(1/2))+1):  # n의 제곱근까지만 탐색
#             if n % i:
#                 continue
#             cnt += 1
#             if i ** 2 != n:  # 약수는 한 쌍
#                 cnt += 1
#             if cnt > limit:  # 가지 치기
#                 break
#         if cnt > limit:
#             answer += power
#         else:
#             answer += cnt
#     return answer

def check(i, arr1, arr2):
    for num in arr1:
        if num % i != 0:
            return False
    for num in arr2:
        if num % i == 0:
            return False
    return True


def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()
    answer = 0
    max_v = max([min(arrayA), min(arrayB)])
    for i in range(max_v, 1, -1):
        if min(arrayA) >= i and check(i, arrayA, arrayB):
            answer = max(answer, i)
            break
        if min(arrayB) >= i and check(i, arrayB, arrayA):
            answer = max(answer, i)
            break
    return answer


result = solution([10, 20], [5, 17])
print(result)