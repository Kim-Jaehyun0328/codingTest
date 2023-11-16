def solution(order):
    answer = 0
    idx = 0
    temp = []
    for i in range(1, len(order)):
        temp.append(i)

        while temp and temp[-1] == order[idx]:
            temp.pop()
            answer += 1
            idx += 1

    return answer