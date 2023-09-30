def solution(operations):
    temp = []

    for x in operations:
        if x[0] == "I":
            if x[2].isdigit():  # 정수라면
                temp.append(int(x[2:]))
            else:
                temp.append((-1) * int(x[3:]))
        else:
            if x[2] == "1" and temp:  # 우선순위 큐가 비어있지 않고, "D 1" 이라면
                temp.remove(max(temp))
            elif x[2] == "-" and temp:
                temp.remove(min(temp))

    if not temp:
        return [0, 0]
    else:
        return [max(temp), min(temp)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))