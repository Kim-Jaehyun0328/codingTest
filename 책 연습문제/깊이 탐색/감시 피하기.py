import sys
from itertools import combinations
sys.stdin=open("practice5", "r")
input=sys.stdin.readline

N = int(input())
matrix = [list(input().split())for _ in range(N)]
teacher = []
student = []
empty = []

def add_wall(matrix, comb):
    for c in comb:
        matrix[c[0]][c[1]] = "O"

def remove_wall(matrix, comb):
    for c in comb:
        matrix[c[0]][c[1]] = "X"

def watch(x, y, direction):
    if direction == 0:
        while x >= 0:
            if matrix[x][y] == "S":
                return True
            if matrix[x][y] == "O":
                return False
            x -= 1
    if direction == 1:
        while y < N:
            if matrix[x][y] == "S":
                return True
            if matrix[x][y] == "O":
                return False
            y += 1
    if direction == 2:
        while x < N:
            if matrix[x][y] == "S":
                return True
            if matrix[x][y] == "O":
                return False
            x += 1
    if direction == 3:
        while y >= 0:
            if matrix[x][y] == "S":
                return True
            if matrix[x][y] == "O":
                return False
            y -= 1
    return False

def check(matrix, teacher):

    for t in teacher:
        x, y = t[0], t[1]
        for i in range(4):
            if watch(x, y, i):
                return True

    return False

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "T":
            teacher.append((i,j))
        elif matrix[i][j] == "S":
            student.append((i,j))
        else:
            empty.append((i,j))

result = "NO"
for comb in combinations(empty, 3):
    add_wall(matrix, comb)

    if not check(matrix, teacher):
        result = "YES"
        break

    remove_wall(matrix, comb)


print(result)