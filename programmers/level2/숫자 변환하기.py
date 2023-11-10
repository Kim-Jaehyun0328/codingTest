from collections import deque


def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = set()

    while q:
        i, j = q.popleft()
        if i in visited:
            continue
        if i == y:
            return j

        for a in (i * 3, i * 2, i + n):
            if a < n:
                visited.add(a)
                q.append((a, j + 1))

    return -1

print(solution(10,40,2))