# import sys
# sys.stdin=open("in5.txt", "r")
#
# n, m = map(int, input().split())
#
# def DFS(v):
#     global cnt
#     if v == m :
#         if len(set(res)) == len(res):
#             for x in res:
#                 print(x, end= " ")
#             print()
#             cnt += 1
#             return
#     else:
#         for i in range(1, n+1):
#             res[v] = i
#             DFS(v+1)
#
#
#
# cnt = 0
# res = [0 for _ in range(m)]
# DFS(0)
# print(cnt)
#

import sys
sys.stdin=open("in3.txt", "r")

n, m = map(int, input().split())

def DFS(v):
    global cnt
    if v == m :
        for x in res:
            print(x, end= " ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i
                DFS(v+1)
                ch[i] = 0

ch = [0 for _ in range(n+1)]
cnt = 0
res = [0 for _ in range(m)]
DFS(0)
print(cnt)

