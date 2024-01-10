def solution(k, scores):
    answer = []
    best_k = []

    for i in range(len(scores)):
        if len(best_k) < k:
            best_k.append(scores[i])
            answer.append(min(best_k))
            continue
        min_num = min(best_k)
        if scores[i] > min_num:
            best_k.append(scores[i])
            best_k.pop(best_k.index(min_num))
        answer.append(min(best_k))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
