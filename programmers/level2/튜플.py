s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
    answer = []
    flag = False
    temp = ""
    tup = []
    result = []
    for i in range(1, len(s)-1):
        if s[i] == "{":
            temp = ""
            tup = []
            flag = True
        elif s[i].isdigit():
            temp += s[i]
        elif s[i] == "}":
            tup.append(int(temp))
            flag = False
            answer.append(tup)
        elif s[i] == "," and flag == True:
            tup.append(int(temp))
            temp = ""

    for i in range(1, len(answer)+1):
        for j in range(len(answer)):
            if len(answer[j]) == i:
                for k in answer[j]:
                    if k not in result:
                        result.append(k)


    return list(result)

print(solution(s))