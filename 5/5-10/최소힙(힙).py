# import sys
# sys.stdin=open("in3.txt", "r")
#
# pList = [0]
# while True:
#     temp = int(input())
#     if temp == -1:
#         break
#     elif temp == 0:
#         if len(pList) <= 2:
#             print(pList.pop())
#             continue
#         else:
#             print(pList[1])
#             pList[1] = pList.pop()
#             head = 1
#             while True:
#                 if (head*2) >= len(pList): #자식 노드가 없는 경우
#                     break
#                 elif (head*2) == len(pList) + 1: #자식 노드가 하나인 경우
#                     if pList[head] > pList[head*2]:  #부모 노드가 자식 노드보다 크다면
#                         pList[head], pList[head*2] = pList[head*2], pList[head]
#                         head = head * 2
#                     else:
#                         break
#                 elif (head*2) <= len(pList) + 2: #자식 노드가 다 있는 경우
#                     min_num = min(pList[head*2:head*2+2])
#                     min_idx = pList.index(min_num)
#                     if pList[head] < min_num:
#                         break
#                     else:
#                         pList[head], pList[min_idx] = pList[min_idx], pList[head]
#                         head = min_idx * 2
#     else:
#         #push하는 코드
#         pList.append(temp)
#         idx = len(pList)-1
#         while True:
#             if idx < 1:
#                 break
#             if temp < pList[idx//2]:
#                 pList[idx], pList[idx//2] = pList[idx//2], temp
#             else:
#                 break
#             idx//=2


import sys
import heapq as hq
sys.stdin=open("in1.txt", "r")
a= []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)

