# 교재에 있는 방법: i, j 로 인덱스 조절하여 정렬하는 방법 -> 함수 2개로 쪼개짐
def quick_sort(a, l, r):
    if l < r:  # 정렬할 구간이 남아있으면
        s = hoare_partition(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)
    return a


# partition 부분을 quick_sort 안에 넣는 것도 가능함!
# hoare partition
def hoare_partition(a, l, r):
    pivot = a[l]
    i, j = l, r

    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] >= pivot:
            j -= 1
        # i랑 j랑 교환
        if i < j:
            a[i], a[j] = a[j], a[i]

    # j < i 가 되면 피봇과 j를 교환
    a[l], a[j] = a[j], a[l]

    return j

# # 시도1) 배열 a는 그대로고 l, r이 바뀌어야하는데 이 함수는 l, r이 없음.
# def quick_sort(a):
#     if len(a) > 1:
#         s = partition(a)
#         # 양쪽을 따로 재귀 돌린다
#         quick_sort(a[:s])
#         quick_sort(a[s+1:])
#     return a
#
#
# def partition(a):
#     # partition 파트
#     pivot = a[0]  # 가장 왼쪽 값을 피봇으로
#     i, j = 0, len(a) - 1
#     if i == j:
#         return
#     while i <= j:
#         while i < j and a[i] <= pivot:
#             i += 1
#         while i < j and a[j] >= pivot:
#             j -= 1
#         # i랑 j랑 교환
#         if i < j:
#             a[i], a[j] = a[j], a[i]
#
#     # j < i 가 되면 피봇과 j를 교환
#     a[0], a[j] = a[j], a[0]
#
#     return j


a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

test = [2, 2, 1, 1, 3]

# print(quick_sort(a, 0, 5))
print(quick_sort(test, 0, 4))