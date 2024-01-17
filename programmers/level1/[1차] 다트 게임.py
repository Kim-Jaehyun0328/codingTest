def solution(dartResult):
    num = []  # 1번째, 2번째, 3번째 점수를 넣는 리스트
    idx = -1
    flag = False

    for i in range(len(dartResult)):
        if flag == True:
            flag = False
            continue
        if dartResult[i].isdigit():
            if (dartResult[i]+dartResult[i+1]).isdigit(): #10
                point = int(dartResult[i]+dartResult[i+1])
                flag = True
            else:
                point = int(dartResult[i])
            num.append(point)
            idx += 1
        if dartResult[i] == "S":
            num[idx] = num[idx]
        elif dartResult[i] == "D":
            num[idx] = num[idx]**2
        elif dartResult[i] == "T":
            num[idx] = num[idx]**3

        if dartResult[i] == "#":
            num[idx] *= (-1)
        if dartResult[i] == "*":
            if idx == 0:
                num[idx] *= 2
            else:
                num[idx] *= 2
                num[idx-1] *= 2


    return sum(num)

print(solution("1S2D*3T"))