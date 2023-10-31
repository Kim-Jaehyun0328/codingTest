def solution(skill, skill_trees):
    answer = 0

    for x in skill_trees:
        temp = skill
        for i in range(len(x)):
            if len(temp) == 0:
                continue
            if x[i] == temp[0]:
                temp = temp[1:]
                continue
            if x[i] in temp[1:]:
                break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))