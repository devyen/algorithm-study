def solution(id_list, report, k):
    report_cnt = {}
    for r in report:
        a, b = r.split()
        report_cnt[b] = list(set(report_cnt.get(b, []) + [a]))

    get_mail = {}
    for id in id_list:
        get_mail[id] = 0

    for key, val in report_cnt.items():
        if len(val) >= k:
            for v in val:
                get_mail[v] += 1

    answer = [val for key, val in get_mail.items()]  # items가 순서 보장이 안됐었는데 -> 3.6부터는 보장됨
    return answer


result = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(result)