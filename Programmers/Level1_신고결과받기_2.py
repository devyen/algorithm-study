def solution(id_list, report, k):
    n = len(id_list)
    ids = {}

    for i, id in enumerate(id_list):
        ids[id] = i

    report_cnt = [set([]) for _ in range(n)]  # set으로 중복 제거
    for r in report:
        a, b = r.split()
        a, b = ids[a], ids[b]  # 닉네임을 번호로 변경
        report_cnt[b].add(a)

    answer = [0] * n
    for reporters in report_cnt:
        if len(reporters) >= k:
            for reporter in reporters:
                answer[reporter] += 1

    return answer


result = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(result)