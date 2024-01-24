def solution(survey, choices):
    answer = ''
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for s, c in zip(survey, choices):
        if c > 4:
            dic[s[1]] += c - 4
        elif c < 4:
            dic[s[0]] += 4 - c

    items = list(dic.items())

    for i in range(0, 8, 2):
        if items[i][1] < items[i + 1][1]:
            answer += items[i + 1][0]
        else:
            answer += items[i][0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5,3,2,7,5]))