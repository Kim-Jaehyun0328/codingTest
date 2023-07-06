import sys
sys.stdin=open("in5.txt", "r")

N =  int(input())
pList = []
price = []
for i in range(N):
    pList.append(list(map(int,input().split())))

for i in range(len(pList)):
    if pList[i][0] == pList[i][1] == pList[i][2]:
        price.append(10000 + (pList[i][0]*1000))
    elif (pList[i][0] == pList[i][1] and pList[i][0] != pList[i][2]) or \
            (pList[i][0] == pList[i][2] and pList[i][0] != pList[i][1]) :
        price.append(1000 + (pList[i][0] * 100))
    elif (pList[i][1] == pList[i][2] and pList[i][0] != pList[i][1]):
        price.append(1000 + (pList[i][1] * 100))
    else:
        price.append(max(pList[i])*100)
print(max(price))


