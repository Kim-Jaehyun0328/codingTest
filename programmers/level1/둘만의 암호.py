def solution(s, skip, index):
    answer = ''
    # 97이 a, 122가 z
    for string in s:
        temp = string
        cnt = 0
        temp = string
        while cnt < index:
            temp = chr(ord(temp) + 1)
            if ord(temp) == 123:
                temp = 'a'
            if chr(ord(temp)) not in skip:
                cnt += 1
        answer += temp

    return answer


print(solution("aukks", "wbqd", 5))