import sys
from collections import deque
sys.stdin=open("in1.txt", "r")

a = [list(map(int, input().split())) for _ in range(7)]
a.insert(0, [-2 for _ in range(9)])
a.append([-2 for _ in range(9)])
for i in range(1, 8):
    a[i].insert(0, -2)
    a[i].append(-2)
ch = [[0 for _ in range(9)] for _ in range(9)]
ch[1][1] = 1
dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq.append((1, 1))
res = 0
while dq:
    size = len(dq)
    for i in range(size):
        temp = dq.popleft()
        if temp[0] == temp[1] == 7:
            print(res)
            sys.exit()

        for j in range(4):
            x = temp[0] + dx[j]
            y = temp[1] + dy[j]
            if a[x][y] == 0 and ch[x][y] == 0:
                ch[x][y] = 1
                dq.append((x, y))
    res += 1

print("-1")