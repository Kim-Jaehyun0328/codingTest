def solution(n, m, section):
    answer = 1
    temp = []

    for x in section:
        temp.append(x)
        if temp[len(temp) - 1] - temp[0] < m:
            continue
        else:
            temp.pop()
            answer += 1
            temp = []
            temp.append(x)

    return answer


print(solution(8, 4, [2, 3, 6]))