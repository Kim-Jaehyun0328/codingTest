def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t)-length+1):
        temp = t[i:i+length]
        if temp <= p:
            answer += 1
    return answer

print(solution("3141592", "271"))