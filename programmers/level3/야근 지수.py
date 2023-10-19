import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        now = heapq.heappop(works)
        now += 1
        heapq.heappush(works, now)

    return sum([w ** 2 for w in works])

print(solution(4, [4,3,3]))