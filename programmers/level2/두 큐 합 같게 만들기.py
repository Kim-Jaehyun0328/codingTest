from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    total1 = sum(queue1)
    total2 = sum(queue2)

    while total1 != total2:
        if total1 > total2:
            temp = queue1.popleft()
            queue2.append(temp)
            total1 -= temp
            total2 += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            total1 += temp
            total2 -= temp
        answer += 1

        if answer == limit:
            return -1

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))