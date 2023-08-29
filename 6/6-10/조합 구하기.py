# import sys
# sys.stdin=open("in5.txt", "r")
#
# n, m = map(int, input().split())
#
# def DFS(v):
#     global cnt
#     if m == v:
#         temp = res[:]
#         temp.sort()
#         if temp in pList:
#             return
#         for x in res:
#             print(x, end= " ")
#         cnt += 1
#         pList.append(res[:])
#         print()
#         return
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
#
# pList = []
# cnt = 0
# ch = [0 for _ in range(n+1)]
# res = [0 for _ in range(m)]
# DFS(0)
# print(cnt)
#


import sys
sys.stdin=open("in1.txt", "r")

n, m = map(int, input().split())


def DFS(L, s):
    global cnt
    if L == m:
        for x in res:
            print(x, end= " ")
        cnt += 1
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)


cnt = 0
res = [0 for _ in range(m)]
DFS(0, 1)
print(cnt)