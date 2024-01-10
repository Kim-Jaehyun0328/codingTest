def solution(s):
    answer = []
    hash_ = {}

    for x in s:
        if x not in hash_:
            answer.append(-1)
            hash_[x] = 0
        else:
            answer.append(hash_[x])
            hash_[x] = 0  # 가장 가까운 것으로 다시 초기화

        for key, val in hash_.items():
            hash_[key] += 1

    return answer

print(solution("banana"))