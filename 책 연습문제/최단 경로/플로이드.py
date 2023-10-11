import sys
sys.stdin=open("practice", "r")

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
dy = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    dy[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n+1):
    for x in graph[i]:
        if x[1] < dy[i][x[0]]:
            dy[i][x[0]] = x[1]


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dy[i][j], end= " ")
    print()