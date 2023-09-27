def solution(progresses, speeds):
    answer = []
    cnt = 0
    idx = 0
    while True:
        for i in range(idx, len(progresses)):
            progresses[i] += speeds[i]

        if progresses[idx] >= 100:
            for j in range(idx, len(progresses)):
                if progresses[j] >= 100:
                    cnt += 1
                    idx += 1
                else:
                    break
        if cnt != 0:
            answer.append(cnt)
        cnt = 0

        if idx == len(progresses):
            break

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))