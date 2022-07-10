# 1. 탑다운
d = [0]*100


def fibo(x):
    if x <= 2:
        return 1
    if not d[x]:
        d[x] = fibo(x-2) + fibo(x-1)
    return d[x]


print(fibo(99))

# 2. 보텀업
d = [0] * 100  # 계산 결과를 저장하기 위한 dp테이블 초기화

d[1] = 1  # 1,2항의 값은 1
d[2] = 1

for i in range(3, 100):  # 반복문으로 보텀업
    d[i] = d[i - 2] + d[i - 1]

print(d[99])

