def solution(s):
    answer = 1
    x = ""
    cnt = 0
    temp = 0

    for word in s:
        if cnt != 0 and temp != 0 and cnt == temp:
            answer += 1
            cnt = 0
            temp = 0
            x = ""
        if x == "":
            x = word
            cnt = 1
        elif x == word:
            cnt += 1
        else:
            temp += 1
    return answer

print(solution("banana"))