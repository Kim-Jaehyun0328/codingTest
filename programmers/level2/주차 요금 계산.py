import math


def solution(fees, records):
    answer = []
    car_num = {}
    default_t, default_f, extra_t, extra_f = fees
    stacks = []
    last_time = 1439  # 23시59분
    for x in records:
        time, num, act = x.split(" ")
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
        if act[0] == "I":  # 입차라면
            if num not in car_num:
                car_num[num] = 0
            stacks.append([time, num])
        else:  # 출차라면
            for stack in stacks:
                if stack[1] == num:  # 입차, 출차 번호가 같다면
                    car_num[num] += (time - stack[0])  # 출차시간 - 입차시간
                    stacks.remove(stack)

    for x in stacks:
        car_num[x[1]] += (last_time - x[0])
        # stacks.remove(x)

    car_num = sorted(car_num.items())

    for x in car_num:
        if x[1] <= default_t:
            answer.append(default_f)
        else:
            fee = default_f + (math.ceil((x[1] - default_t) / extra_t)) * extra_f
            answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	))