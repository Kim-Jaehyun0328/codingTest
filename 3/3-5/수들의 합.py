import sys
sys.stdin=open("in2.txt", "r")

N, M = map(int, input().split())
pList = list(map(int, input().split()))
res = 0
# for i in range(N):
#     cnt = 0
#     for j in range(i, N):
#         cnt += pList[j]
#         if cnt == M:
#             res += 1
#             break
#         elif cnt > M:
#             break
#
# print(res)
lt = rt = cnt = 0
while  rt < N:
    if cnt < M:
        cnt += pList[rt]
        rt += 1
    elif cnt == M :
        res += 1
        cnt = 0
        lt += 1
        rt = lt
    elif cnt > M :
        cnt = 0
        lt += 1
        rt = lt

print(res)
