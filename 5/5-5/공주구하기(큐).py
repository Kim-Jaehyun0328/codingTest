import sys
sys.stdin=open("in5.txt", "r")

n, num = map(int, input().split())
pList= [i for i in range(1, n+1)]

# while True:
#     if len(pList) == 1:
#         break
#     for _ in range(num-1):
#         pList.append(pList.pop(0))
#     else:
#         pList.pop(0)
#
# print(pList[0])

#deque를 쓰면 더 빠름
from collections import deque
pList = deque(pList)

while True:
    if len(pList) == 1:
        break
    for _ in range(num - 1):
        pList.append(pList.popleft())
    pList.popleft()

print(pList[0])