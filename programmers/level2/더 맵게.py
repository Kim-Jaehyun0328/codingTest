import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer += 1

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))