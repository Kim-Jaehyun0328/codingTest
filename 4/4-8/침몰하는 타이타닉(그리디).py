# import sys
# sys.stdin=open("in5.txt", "r")
#
# N, kg = map(int, input().split())
# pList = list(map(int, input().split()))
#
# min_kg = min(pList)
# max_kg = max(pList)
#
# res = 0
# while True:
#     min_kg = min(pList)
#     max_kg = max(pList)
#     if min_kg + max_kg <= kg:
#         pList.remove(min_kg)
#         pList.remove(max_kg)
#         res += 1
#     else:
#         pList.remove(max_kg)
#         res += 1
#     if len(pList) == 1:
#         res +=1
#         break
#     elif len(pList) == 0 :
#         break
#
# print(res)
#

import sys
from collections import deque
sys.stdin=open("in5.txt", "r")

N, kg = map(int, input().split())
pList = list(map(int, input().split()))
pList.sort()
pList = deque(pList)
res = 0
while pList:
    if len(pList) == 1:
        res += 1
        break
    if pList[0] + pList[-1] > kg:
        pList.pop()
        res += 1
    else:
        pList.pop()
        pList.popleft()
        res += 1

print(res)