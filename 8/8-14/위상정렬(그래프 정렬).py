import sys
from collections import deque
sys.stdin=open("practice", "r")

n, m = map(int, input().split())

dy = [[0 for _ in range(n+1)] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
dq = deque()
for _ in range(m):
    a, b = map(int, input().split())
    dy[a][b] = 1
    degree[b]+=1

for i in range(1, n+1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    temp = dq.popleft()
    print(temp, end= " ")
    for i in range(1, n+1):
        if dy[temp][i] == 1:
            degree[i]-=1
            if degree[i] == 0:
                dq.append(i)
