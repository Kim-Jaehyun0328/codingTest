def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    num = len(score) // m

    for i in range(0, len(score), m):
        if i + m > len(score):
            break
        temp = min(score[i:i + m]) * m
        answer += temp

    return answer

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))