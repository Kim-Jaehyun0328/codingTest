def solution(keymap, targets):
    answer = []

    for target in targets:
        num = 0
        for i in range(len(target)):
            temp = int(1e9)
            for key in keymap:
                if target[i] not in key:
                    continue
                if temp > key.index(target[i]) + 1:
                    temp = key.index(target[i]) + 1
            if temp == int(1e9):
                answer.append(-1)
                break
            else:
                num += temp
        if temp != int(1e9):
            answer.append(num)

    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))