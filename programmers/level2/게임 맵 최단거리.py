from collections import deque


def solution(maps):
    arr = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    arr[0][0] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((0, 0))
    ch = set()
    ch.add((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 0:
                if (nx, ny) not in ch:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
                    ch.add((nx, ny))

    if arr[len(maps) - 1][len(maps[0]) - 1] == 0:
        return -1
    else:
        return arr[len(maps) - 1][len(maps[0]) - 1]

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))