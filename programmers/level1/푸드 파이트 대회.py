from collections import deque


def solution(food):
    answer = deque()
    answer.append("0")

    for i in range(len(food) - 1, 0, -1):
        num = food[i] // 2
        for j in range(num):
            answer.append(str(i))
            answer.appendleft(str(i))

    return "".join(answer)

print(solution([1,3,4,6]))