# import sys
# sys.stdin=open("in1.txt", "r")
#
# N = int(input())
# pList = []
#
# for i in range(N):
#     pList.append(list(map(int, input().split())))
# pList.sort()
# print(pList)
# res = 0
# cnt = 0
# for i in range(N):
#     cnt = 1
#     lastFinish = pList[i][1]
#     # print(i, "번째 시도")
#     # print(pList[i])
#     for j in range(i+1, N):
#         if pList[j][0] >= lastFinish:
#             lastFinish = pList[j][1]
#             cnt += 1
#             # print(pList[j])
#
#     if res < cnt:
#         res = cnt
#     if res > len(pList[i + 1:]):
#         break
# print(res)
#


import sys
sys.stdin=open("in1.txt", "r")

N = int(input())
pList = []

for i in range(N):
    pList.append(list(map(int, input().split())))

pList.sort(key= lambda x : (x[1], x[0]))

cnt = 1
lastFinish = pList[0][1]
for i in range(1, N):
    if pList[i][0] >= lastFinish:
        lastFinish = pList[i][1]
        cnt += 1

print(cnt)

