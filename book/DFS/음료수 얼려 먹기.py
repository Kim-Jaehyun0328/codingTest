# import sys
# sys.stdin=open("practice", "r")
#
# N, M = map(int, input().split())
# matrix = [[0 for _ in range(M)] for _ in range(N)]
#
# for i in range(N):
#     s = input()
#     for j in range(M):
#         matrix[i][j] = int(s[j])

# def DFS(x, y):
#     matrix[x][y] = 1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0<= xx < N and 0<= yy < M and matrix[xx][yy] == 0:
#             matrix[xx][yy] = 1
#             DFS(xx, yy)
#
# answer = 0
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 0:
#             DFS(i, j)
#             answer += 1
#
# print(answer)







#
# from collections import deque
#
# queue = deque()
# answer = 0
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 0:  # BFS 시작
#             queue.append((i, j))
#             matrix[i][j] = 1  # 체크하기
#             while queue:
#                 temp = queue.popleft()
#                 for k in range(4):  # 상하좌우 탐색
#                     xx = dx[k] + temp[0]
#                     yy = dy[k] + temp[1]
#                     if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 0:
#                         queue.append((xx, yy))
#                         matrix[xx][yy] = 1
#             answer += 1
#
# print(answer)


# import sys
# from collections import deque
#
# sys.stdin = open("practice", "r")
#
# n, m = map(int, input().split(" "))
#
# graph = [list(map(int, input())) for _ in range(n)]
# visited = [[0 for _ in range(m)] for _ in range(n)] #1이면 방문, 0이면 아직 미방문
#
# # graph = []
# # for i in range(n):
# #     graph.append(list(map(int, input())))
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# q = deque()
# ans = 0
# for i in range(len(graph)):
#     for j in range(len(graph[0])):
#         if graph[i][j] == 0 and visited[i][j] == 0: #방문하지 않았고, 갈 수 있는 곳이라면
#             q.append((i, j))
#             visited[i][j] = 1
#
#             while q:
#                 v = q.popleft()
#                 print(v)
#                 for k in range(4): #현재 기준 상 하 좌 우 확인하기
#                     nx = v[0] + dx[k]
#                     ny = v[1] + dy[k]
#                     if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and graph[nx][ny] == 0:
#                         q.append((nx, ny))
#                         visited[nx][ny] = 1
#             ans += 1
#
# print(ans)


import sys

def dfs(graph, visited, i, j):
    visited[i][j] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            dfs(graph,visited, nx, ny)


sys.stdin=open("practice", "r")
n, m = map(int, input().split(" "))

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)] #방문했으면 1, 하지 않았으면 0
ans = 0

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0 and visited[i][j] == 0:
            dfs(graph, visited, i, j)
            ans += 1


print(ans)

















