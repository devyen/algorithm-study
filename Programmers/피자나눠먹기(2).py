def solution(n):
    num = n
    while num <= 300:
        if num % 6 == 0:
            break
        num += n

    return num // 6
