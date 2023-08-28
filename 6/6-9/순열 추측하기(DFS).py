# import sys
# sys.stdin=open("in3.txt", "r")
#
# n, m = map(int, input().split())
#
#
# def PASCAL(pList):
#     temp = []
#     if len(pList) == 1:
#         print(pList[0])
#         return pList[0]
#     for i in range(len(pList)-1):
#         temp.append(pList[i] + pList[i+1])
#     return PASCAL(temp)
#
# def DFS(v):
#     if v == n:
#         sum_list = res[0] + res[len(res)-1]
#         for i in range(1, len(res)-1):
#             sum_list += res[i] * (v)
#         if sum_list == m:  #이제 여기서 파스칼로 찾아야 됨
#             if PASCAL(res) == m:
#                 for x in res:
#                     print(x, end= " ")
#                 sys.exit()
#     else:
#         for i in range(1, n+1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[v] = i
#                 DFS(v+1)
#                 ch[i] = 0
#
#
#
# ch = [0 for _ in range(n+1)]
# res = [0 for _ in range(n)]
# DFS(0)

import sys
sys.stdin=open("in1.txt", "r")

n, m = map(int, input().split())



def DFS(v, sum):
    if v == n and sum == m :
        for x in p:
            print(x, end= " ")
        sys.exit()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[v] = i
                DFS(v+1, sum + (p[v]*b[v]))
                ch[i] = 0

p = [0 for _ in range(n)]
b = [1 for _ in range(n)]
ch = [0 for _ in range(n+1)]

for i in range(1, n-1):
    b[i] = (b[i-1]*(n-i))//i


DFS(0, 0)