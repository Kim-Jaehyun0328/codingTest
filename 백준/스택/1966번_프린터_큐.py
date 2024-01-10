# import sys
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     n, find = map(int, sys.stdin.readline().split())
#     num = list(map(int, sys.stdin.readline().split()))
#     idx = 0
#     ans = 1
#     while True:
#         if num[idx] == max(num[idx:]):
#             if idx % n == find:
#                 print(ans)
#                 break
#             idx += 1
#             ans += 1
#             num.append(0)
#         else:
#             num.append(num[idx])
#             idx += 1


import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    n, find = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    idx = 0
    ans = 1
    pList = []
    for i in range(n):
        pList.append((i, num[i]))
    pList = deque(pList)

    while True:
        max_num = max([item[1] for item in pList])
        if pList[0][1] == max_num:
            if pList[0][0] == find:
                print(ans)
                break
            pList.popleft()
            ans += 1
        else:
            pList.append(pList.popleft())
