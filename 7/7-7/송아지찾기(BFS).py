# import sys
# sys.stdin=open("practice", "r")
#
# s, e = map(int, input().split())
#
#
#
# if __name__ == "__main__":
#     if s > e:
#         print(s-e)
#     else:
#         temp = e - s
#         a = temp//5
#         b = temp%5
#         if b == 0:
#             print(a)
#         elif b >= 3:
#             print((a+1) + 5-b)
#         elif b<= 2:
#             print((a) + b)

import sys
from collections import deque
sys.stdin=open("in5.txt", "r")

s, e = map(int, input().split())

if __name__ == "__main__":
    dis = [0 for _ in range(10001)]
    ch = [0 for _ in range(10001)]
    ch[s] = 1
    dis[s] = 0
    dQ = deque()
    dQ.append(s)
    while dQ:
        temp = dQ.popleft()

        for next in (temp-1, temp+1, temp+5):
            if 0<next<=10000 and ch[next] ==0:
                dQ.append(next)
                ch[next]=1
                dis[next] = dis[temp]+1

        if ch[e] != 0:
            print(dis[e])
            break

