def solution(id_list, report, k):
    answer = [0]*len(id_list)

    report_dic = {}
    for r in report:
        user1, user2 = r.split()
        report_dic[user2] = list(set(report_dic.get(user2, []) + [user1]))

    for key, val in report_dic.items():
        if len(val) >= k:
            for user in val:
                answer[id_list.index(user)] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))