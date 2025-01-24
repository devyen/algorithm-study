# 이진 탐색으로 최적화 문제를 푼다
n, m = map(int, input().split())
cakes = list(map(int, input().split()))


def get_cut_cakes(cut):
    res = 0
    for cake in cakes:
        if cake > cut:
            res += cake-cut
    return res


def binary_search(s, e):
    answer = 0
    while s <= e:
        mid = (s+e)//2
        res = get_cut_cakes(mid)
        if res < m:
            e = mid-1
        else:
            answer = mid  # 최대한 덜 잘랐을 때가 정답이므로 조건을 충족하는 높이값을 계속 갱신
            s = mid+1
    return answer


binary_search(0, max(cakes))
