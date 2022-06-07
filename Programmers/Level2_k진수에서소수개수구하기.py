def to_k_number(n, k):
    result = ''
    while n >= k:
        q, r = divmod(n, k)
        result = str(r) + result
        n = q
    result = str(n) + result
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
    

def solution(n, k):
    k_number = to_k_number(n, k)
    nums = k_number.split('0')
    answer = 0
    for num in nums:
        if num == '':
            continue
        if int(num) > 1 and is_prime(int(num)):
            answer += 1
    return answer


result = solution(110011, 10)
print(result)