import copy
import sys
from itertools import combinations
from collections import deque

sys.stdin=open("practice", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

zero = []
virus = []

#비어있는 칸 추가
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero.append((i, j))
        elif matrix[i][j] == 2:
            virus.append((i, j))


def add_wall(matrix, comb):
    for x, y in comb:
        matrix[x][y] = 1
    return

def remove_wall(matrix, comb):
    for x, y in comb:
        matrix[x][y] = 0
    return

def check_safe(matrix, virus):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    temp_matrix = copy.deepcopy(matrix)
    temp = 0
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #가야할 곳이 0이라면(감염될 수 있다면)
            if 0<=nx<N and 0<=ny<M and temp_matrix[nx][ny] == 0:
                temp_matrix[nx][ny] = 2
                q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if temp_matrix[i][j] == 0:
                temp += 1
    return temp


answer = 0
for comb in combinations(zero, 3):
    add_wall(matrix, comb)
    #안전지대 확인
    temp = check_safe(matrix, virus)
    if temp > answer:
        answer = temp
    remove_wall(matrix, comb)


print(answer)