from collections import deque


def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        time = 0
        now = q.popleft()

        for x in q:
            time += 1
            if x < now:  # 가격이 떨어졌다면
                break
        answer.append(time)

    return answer

print(solution([1,2,3,2,3]))