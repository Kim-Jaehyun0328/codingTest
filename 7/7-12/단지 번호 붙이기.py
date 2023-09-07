import sys
from collections import deque
sys.stdin=open("in5.txt", "r")

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    final = [[0 for _ in range(n)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    num = 1

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and final[i][j] == 0:
                dq.append((i, j))
                final[i][j] = num
                while dq:
                    size = len(dq)
                    for k in range(size):
                        temp = dq.popleft()
                        for x in range(4):
                            xx = temp[0] + dx[x]
                            yy = temp[1] + dy[x]
                            if 0<=xx<n and 0<=yy<n and final[xx][yy] == 0 and a[xx][yy] == 1:
                                dq.append((xx, yy))
                                final[xx][yy] = num
                num += 1
    cnt_lst = [0 for _ in range(num-1)]

    for i in range(n):
        for j in range(n):
            if final[i][j] != 0:
                cnt_lst[final[i][j]-1] += 1

    cnt_lst.sort()
    print(num-1)
    for x in cnt_lst:
        print(x)
