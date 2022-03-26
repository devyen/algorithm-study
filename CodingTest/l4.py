def solution(arr, brr):
    # 순서: 양쪽 가장자리부터 안쪽으로 조정한다.
    cnt = 0
    for i in range(len(arr)//2 + len(arr)%2):

        for d, idx in enumerate([i, -(i+1)]):  # 양쪽 가장자리
            if arr[idx] != brr[idx]:
                cnt += 1
                gap = arr[idx] - brr[idx]
                arr[idx] = brr[idx]
                if d == 0:  # 왼쪽
                    arr[idx+1] += gap
                else:  # 오른쪽
                    arr[idx-1] += gap

    return cnt