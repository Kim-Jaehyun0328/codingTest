# import sys
# from collections import deque
# sys.stdin=open("in4.txt", "r")
#
# m, n = map(int, input().split()) #m이 열, n이 행
# tomato = []
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# res = 0
# cnt = 0
# for i in range(n):
#     tomato.append(list(map(int, input().split())))
#
# dq = deque()
#
# def BFS(dq):
#     global cnt
#     while dq:
#         temp = dq.popleft()
#         for k in range(4):
#             xx = temp[0] + dx[k]
#             yy = temp[1] + dy[k]
#             if 0 <= xx < n and 0 <= yy < m and tomato[xx][yy] == 0:
#                 tomato[xx][yy] = 1
#                 cnt += 1
#
# while True:
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if tomato[i][j] == 1:
#                 dq.append((i, j))
#                 # BFS(i, j)
#     BFS(dq)
#     res += 1
#     if cnt == 0:
#         print(-1)
#         sys.exit()
#
#     zero_count = 0
#     for x in tomato:
#         zero_count += x.count(0)
#     if zero_count == 0:
#         print(res)
#         sys.exit()

import sys
from collections import deque
sys.stdin=open("practice", "r")

m, n = map(int, input().split()) #m이 열, n이 행
tomato = []
dist = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    tomato.append(list(map(int, input().split())))

dq = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))

res = 1
while dq:
    for i in range(len(dq)):
        temp = dq.popleft()
        for i in range(4):
            xx = temp[0] + dx[i]
            yy = temp[1] + dy[i]
            if 0<=xx<n and 0<=yy<m and tomato[xx][yy] == 0 and dist[xx][yy] == 0:
                dq.append((xx, yy))
                dist[xx][yy] = res
                tomato[xx][yy] = 1
    res+=1

for x in tomato:
    if 0 in x:
        print(-1)
        sys.exit()

print(dist[temp[0]][temp[1]])

