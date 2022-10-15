# def solution(lottos, win_nums):
#     cnt1 = cnt2 = 0
#     for l in lottos:
#         if l in win_nums:
#             cnt1 += 1
#         elif l == 0:
#             cnt2 += 1
#     max_rank = 7-cnt1-cnt2
#     if max_rank > 6:
#         max_rank = 6
#     min_rank = 7-cnt1
#     if min_rank > 6:
#         min_rank = 6
#     answer = [max_rank, min_rank]
#     return answer


def solution(lottos, win_nums):
    cnt1 = cnt2 = 0
    for l in lottos:
        if l in win_nums:
            cnt1 += 1
        elif l == 0:
            cnt2 += 1

    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[cnt1 + cnt2], rank[cnt1]]
    return answer
