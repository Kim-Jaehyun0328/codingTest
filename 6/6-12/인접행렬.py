import sys
sys.stdin=open("practice", "r")

n, v = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(v):
    f, t, num = map(int, input().split())
    matrix[f-1][t-1] = num


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end= " ")
    print()