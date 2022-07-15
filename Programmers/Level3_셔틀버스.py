def cal_time(str_time):
    h, m = map(int, str_time.split(':'))
    return h*60+m


def rev_cal_time(time):
    q, r = map(str, divmod(time, 60))
    if len(r) < 2:
        r = '0'+r
    if len(q) < 2:
        q = '0'+q
    return q+':'+r


def solution(n, t, m, timetable):
    answer = ''
    timetable.sort(key=lambda x: (int(x[:2]), int(x[3:])))

    p = 0  # 사람 인덱스
    for i in range(n):
        time = 9*60 + i*t
        cnt = 0
        while cnt < m and p < len(timetable) and cal_time(timetable[p]) <= time:
            if i == n-1 and cnt == m-1:
                if timetable[p-1] == timetable[p]:
                    answer = rev_cal_time(cal_time(timetable[p-1])-1)
                else:
                    answer = timetable[p-1]
                break
            cnt += 1
            p += 1
        if p == len(timetable):  # 모든 사람을 다 태운 경우 -> 마지막 타임
            answer = rev_cal_time(9*60 + (n-1)*t)
            break
        if i == n-1 and not answer:  # 마지막 타임인데 아무도 안 태웠으면 -> 마지막 타임
            answer = rev_cal_time(time)

    return answer


result = solution(10,60,45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
print(result)