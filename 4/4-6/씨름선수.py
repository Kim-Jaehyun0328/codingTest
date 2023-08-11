import sys
sys.stdin=open("practice", "r")

N = int(input())

pList = []

for i in range(N):
    pList.append(list(map(int, input().split())))
pList.sort(key=lambda x: (x[0]))  #키 순으로 오름차순
res = len(pList)

for i in range(len(pList)):
    for j in range(i+1, len(pList)):
        if pList[i][1] < pList[j][1]:
            res -= 1
            break

print(res)