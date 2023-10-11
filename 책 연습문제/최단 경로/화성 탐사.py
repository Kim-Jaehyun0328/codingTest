# import sys
# sys.stdin=open("practice3", "r")
# INF = int(1e9)
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# temp = [[INF for _ in range(n)] for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# temp[0][0] = arr[0][0]
#
# for i in range(n):
#     for j in range(n):
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 temp[nx][ny] = min(temp[nx][ny], temp[i][j] + arr[nx][ny])
#
#
# for x in temp:
#     print(x)
#
# print(temp[n-1][n-1])

import sys
sys.stdin=open("practice3", "r")
import heapq
INF = int(1e9)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[INF for _ in range(n)] for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q= []
x, y = 0, 0
distance[x][y] = graph[x][y]
heapq.heappush(q, (distance[x][y], x, y))
while q:
    dist, x, y = heapq.heappop(q)

    if distance[x][y] < dist:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))


for x in distance:
    print(x)
