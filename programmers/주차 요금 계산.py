import math


def solution(fees, records):
    answer = []

    dict_ = {}  # 총요금
    dict2_ = {}  # 누적 주차 시간
    for i in range(len(records)):
        in_time = records[i][0:5]
        in_minutes = int(in_time[0:2]) * 60 + int(in_time[3:])
        car_num = records[i][6:10]
        if dict_.get(car_num) == None:
            dict_[car_num] = 0
            dict2_[car_num] = 0
        if records[i][11:] == "IN":
            for j in range(i + 1, len(records)):
                if records[j][6:10] == car_num and records[j][11:] == "OUT":
                    out_time = records[j][0:5]
                    out_minutes = int(out_time[0:2]) * 60 + int(out_time[3:])
                    total_minutes = out_minutes - in_minutes
                    dict2_[car_num] += total_minutes
                    break
            else:
                total_minutes = (23 * 60 + 59) - in_minutes
                dict2_[car_num] += total_minutes

    for key, value in dict2_.items():
        if value <= fees[0]:
            dict_[key] = fees[1]
        else:
            dict_[key] = int(fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3])

    pList = sorted(list(dict_.keys()))
    answer = [0] * len(pList)
    for i in range(len(pList)):
        for key, value in dict_.items():
            if pList[i] == key:
                answer[i] = value

    return answer