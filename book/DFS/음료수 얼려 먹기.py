import sys
sys.stdin=open("practice", "r")

N, M = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    s = input()
    for j in range(M):
        matrix[i][j] = int(s[j])

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








from collections import deque

queue = deque()
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:  # BFS 시작
            queue.append((i, j))
            matrix[i][j] = 1  # 체크하기
            while queue:
                temp = queue.popleft()
                for k in range(4):  # 상하좌우 탐색
                    xx = dx[k] + temp[0]
                    yy = dy[k] + temp[1]
                    if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 0:
                        queue.append((xx, yy))
                        matrix[xx][yy] = 1
            answer += 1

print(answer)
