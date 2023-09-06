# import sys
# sys.stdin=open("in1.txt", "r")
#
# n = int(input())
# pList = [list(map(int,input().split())) for _ in range(n)]
# center = n//2
# idx = 0
# res = 0
#
# for i in range(n):
#     res += sum(pList[i][center-idx:center+idx+1])
#     if i >=center:
#         idx -= 1
#     else:
#         idx += 1
# print(res)

import sys
from collections import deque
sys.stdin=open("in5.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0 for _ in range(n)] for _ in range(n)]
res = 0
dq = deque()
ch[n//2][n//2] = 1 #중심
res += a[n//2][n//2]
dq.append((n//2, n//2))
L = 0 #깊이
while True:
    if L == n//2:
        break
    size = len(dq)
    for i in range(size):
        temp = dq.popleft()
        for j in range(4):
            x = temp[0] + dx[j]
            y = temp[1] + dy[j]
            if ch[x][y] == 0:
                dq.append((x, y))
                ch[x][y] = 1
                res += a[x][y]
    L += 1


print(res)