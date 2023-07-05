import sys
sys.stdin = open("in3.txt", "rt")

N, M = map(int, input().split())

#
# pList = {n: 0 for n in range(N+M+1)}
# for i in range(N):
#     for j in range(M):
#         sum = (i+1) + (j+1)
#         pList[sum] += 1
#
# temp = list(pList.values())
# print(temp)
# maxNum = max(temp)
#
# for i in range(len(temp)):
#     if temp[i] >= maxNum:
#         print("%d "%(i))

pList = [0 for i in range(N+M+1)]
for i in range(N):
    for j in range(M):
        pList[(i+1)+(j+1)] += 1
maxNum = max(pList)
for i in range(len(pList)):
    if pList[i] >= maxNum:
        print(i, end=' ')