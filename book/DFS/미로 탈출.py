from collections import deque


answer = 1
N, M = 5, 6
matrix = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
ch = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]  # 행
dy = [0, 1, 0, -1]  # 열

queue = deque()

queue.append((0, 0))
ch[0][0] = 1
cnt = 2

while queue:
    for x in range(len(queue)):
        temp = queue.popleft()
        for i in range(4):
            xx = temp[0] + dx[i]
            yy = temp[1] + dy[i]
            if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 1 and ch[xx][yy] == 0:
                ch[xx][yy] = cnt
                queue.append((xx, yy))
    cnt += 1

print(ch[N - 1][M - 1])