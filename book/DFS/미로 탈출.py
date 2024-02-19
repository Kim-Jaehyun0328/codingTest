# from collections import deque
#
#
# answer = 1
# N, M = 5, 6
# matrix = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# ch = [[0 for _ in range(M)] for _ in range(N)]
# dx = [-1, 0, 1, 0]  # 행
# dy = [0, 1, 0, -1]  # 열
#
# queue = deque()
#
# queue.append((0, 0))
# ch[0][0] = 1
# cnt = 2
#
# while queue:
#     for x in range(len(queue)):
#         temp = queue.popleft()
#         for i in range(4):
#             xx = temp[0] + dx[i]
#             yy = temp[1] + dy[i]
#             if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 1 and ch[xx][yy] == 0:
#                 ch[xx][yy] = cnt
#                 queue.append((xx, yy))
#     cnt += 1
#
# print(ch[N - 1][M - 1])


# def dfs(matrix, x, y, cnt):
#
#     if x == N-1 and y == M-1:
#         return
#
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<N and 0<=ny<M and matrix[nx][ny] == 1 and ch[nx][ny] == 0:
#             ch[nx][ny] += cnt+1
#             dfs(matrix, nx, ny, cnt+1)
#
# N, M = 5, 6
# matrix = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# ch = [[0 for _ in range(M)] for _ in range(N)]
# ch[0][0] = 1
# dfs(matrix, 0, 0, 1)
#
# print(ch[N-1][M-1])






from collections import deque

N, M = 5, 6
matrix = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
ch = [[0 for _ in range(M)] for _ in range(N)]
ch[0][0] = 1
q = deque()
q.append((0,0))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    v = q.popleft()
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0<=nx<N and 0<=ny<M and ch[nx][ny] == 0 and matrix[nx][ny] == 1:
            ch[nx][ny] = ch[v[0]][v[1]] + 1
            q.append((nx, ny))

print(ch[N-1][M-1])
















