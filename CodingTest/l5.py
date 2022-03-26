def solution(abilities, k):
    abilities.sort(reverse=True)
    # 2개씩 끊어서 생각
    # 우선권은 무조건 앞에서 쓰는게 유리
    answer = 0
    for i in range(len(abilities), 2):
        if abilities[i] > abilities[i + 1] and k > 0:
            answer += abilities[i]
            k -= 1
        else:
            answer += abilities[i + 1]

    return answer


print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))