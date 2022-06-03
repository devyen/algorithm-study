import math


def calculate_time(in_time, out_time):
    in_h, in_m = map(int, in_time.split(':'))
    out_h, out_m = map(int, out_time.split(':'))
    time = (out_h - in_h) * 60 + out_m - in_m
    return time


def solution(fees, records):
    time_record = {}
    in_record = {}
    for r in records:
        info = r.split()
        if info[-1] == 'IN':
            in_record[info[1]] = info[0]
        else:
            time = calculate_time(in_record[info[1]], info[0])
            time_record[info[1]] = time_record.get(info[1], 0) + time
            in_record[info[1]] = 0  # 체크

    for key, val in in_record.items():
        if val != 0:
            time = calculate_time(val, '23:59')
            time_record[key] = time_record.get(key, 0) + time

    fee_record = {}
    for key, val in time_record.items():
        if val <= fees[0]:
            fee_record[key] = fees[1]
        else:
            fee = fees[1] + math.ceil((val-fees[0])/fees[2])*fees[3]
            fee_record[key] = fee

    answer = [x[1] for x in sorted(fee_record.items())]
    return answer


result = solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(result)