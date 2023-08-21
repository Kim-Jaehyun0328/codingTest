import sys
from collections import deque
sys.stdin=open("in2.txt", "r")

s = input()
N = int(input())

# for i in range(N):
#     temp_s = deque(s)
#     dq = deque(input())
#     while temp_s:
#         if len(dq) == 1 and dq[0] not in temp_s:
#             print("#", i + 1, "NO")
#             break
#         cur = dq.popleft()
#         if cur not in temp_s:
#             continue
#         if cur == temp_s[0]:
#             temp_s.popleft()
#         elif cur != temp_s[0]:
#             print("#",i+1, "NO")
#             break
#     else:
#         print("#",i+1, "YES")

for i in range(N):
    temp_s = deque(s)
    dq = deque(input())
    for x in dq:
        if x not in temp_s:
            continue
        if x != temp_s[0]:
            print("#%d NO" %(i+1))
            break
        else:
            temp_s.popleft()
    else:
        if temp_s:
            print("#%d NO" %(i+1))
        else:
            print("#%d YES" %(i+1))