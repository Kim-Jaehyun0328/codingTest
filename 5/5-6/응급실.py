import sys
from collections import deque
sys.stdin=open("in2.txt", "r")

n, k = map(int, input().split())
pList = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
pList = deque(pList)
cnt = 0
while True:
    cur = pList.popleft()
    if any(cur[1] < x[1] for x in pList):
        pList.append(cur)
    else:
        cnt += 1
        if cur[0] == k:
            break


print(cnt)