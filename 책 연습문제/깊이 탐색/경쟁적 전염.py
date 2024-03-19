import sys
import heapq

sys.stdin=open("practice3", "r")
input=sys.stdin.readline

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X, Y = X-1, Y-1
virus = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            heapq.heappush(virus, (matrix[i][j], i, j))


dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(S):
    while virus:
        num, x, y = heapq.heappop(virus)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and matrix[nx][ny] == 0:
                matrix[nx][ny] = num

    if matrix[X][Y] != 0:
        break
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                heapq.heappush(virus, (matrix[i][j], i, j))

if matrix[X][Y] != 0:
    print(matrix[X][Y])
else:
    print(0)