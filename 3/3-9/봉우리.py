import sys
sys.stdin=open("in5.txt", "r")

N = int(input())
pList = [list(map(int, input().split())) for _ in range(N)]

pList.insert(0, [0 for _ in range(N+2)])
pList.append([0 for _ in range(N+2)])
res = 0
for i in range(1, N+1):
    pList[i].insert(0, 0)
    pList[i].append(0)

for i in range(1, N+1):
    for j in range(1, N+1):
        if pList[i][j] > pList[i-1][j] and pList[i][j] > pList[i+1][j] and pList[i][j] > pList[i][j-1] and pList[i][j] > pList[i][j+1]:
            res += 1

print(res)

