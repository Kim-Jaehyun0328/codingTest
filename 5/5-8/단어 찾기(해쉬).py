import sys
sys.stdin=open("in5.txt", "r")

N = int(input())
# pList = []
# for _ in range(N):
#     pList.append(input())
#
# for _ in range(N-1):
#     word = input()
#     pList.pop(pList.index(word))
#
# print(pList[0])

p = dict()
for _ in range(N):
    word = input()
    p[word] = 0

for _ in range(N-1):
    word = input()
    p[word] = 1
for key, val in p.items():
    if val == 0:
        print(key)
        break