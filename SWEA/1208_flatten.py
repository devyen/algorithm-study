import sys
sys.stdin = open('input.txt')

# 평탄화 함수
def flatten(list, dump):
    # 덤프 수만큼 평탄화
    for _ in range(dump):
        max_height = max(list)  # 최고점 높이
        min_height = min(list)  # 최저점 높이
        dif = max_height - min_height  # 높이 차
        # 높이 차가 1 초과이면 평탄화 수행
        if dif > 1:
            for i in range(100):
                if list[i] == max_height:
                    list[i] -= 1
                    for j in range(100):
                        if list[j] == min_height:
                            list[j] += 1
                            break
                    break
        # 1 이내이면 높이차 반환
        else:
            return dif

    # 높이차가 1 이내가 되지 않았지만 덤프 수가 끝나면 높이차 반환
    return max(list) - min(list)

T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    # 최고점과 최저점 차이가 1 이상이면 평탄화를 수행한다.
    result = flatten(boxes, dump)

    print(f'#{tc} {result}')

