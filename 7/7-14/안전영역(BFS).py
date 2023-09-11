import sys
from collections import deque
sys.stdin=open("in5.txt", "r")


def BFS(x, y, h):
    dq = deque()
    dq.append((x, y))
    ch[x][y] = 1
    while dq:
        temp = dq.popleft()
        for p in range(4):
            xx = temp[0] + dx[p]
            yy = temp[1] + dy[p]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and a[xx][yy] > h:
                dq.append((xx, yy))
                ch[xx][yy] = 1


if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    res = 0

    for h in range(100):
        ch = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if a[i][j] > h and ch[i][j] == 0:
                    cnt += 1
                    BFS(i, j, h)
        if cnt == 0:
            break
        res = max(res, cnt)

    print(res)
