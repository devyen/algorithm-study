arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# arr = [1, 2, 3]

n = len(arr)
cnt = 0
for i in range(1<<n):  # 1<<n : 부분집합의 수 즉 모든 경우의 수
    sub = []  # 부분집합을 생성할 빈 리스트
    total = 0  # 원소의 합
    for j in range(n):  # j: 인덱스, 0부터 n-1까지 각 원소의 포함여부를 확인
        if i & (1<<j):  # j번째 원소가 있으면
            sub.append(arr[j])
            total += arr[j]

    if total == 0:
        print(sub)
        cnt += 1

print(f'총 {cnt}개')