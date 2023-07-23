import sys
sys.stdin=open("in5.txt", "r")

N = int(input())
pList = []
for i in range(N):
    pList.append(list(map(int,input().split())))

# pList = [list(map, int(input().split())) for _ in range(N)]

res = temp = 0

for i in range(N):
    if sum(pList[i]) > res:
        res = sum(pList[i])
    for j in range(N):
        temp += pList[i][j]
    if temp > res:
        res = temp
    temp = 0
temp1 = temp2 = 0
for k in range(N):
    temp1 += pList[k][k]
    temp2 += pList[k][-1-k]

if temp1 > res:
    res = temp1
elif temp2 > res:
    res = temp2

print(res)

a = [[1,2],[3,4]]
