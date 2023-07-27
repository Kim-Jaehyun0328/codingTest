import sys
sys.stdin=open("in5.txt", "r")

pList = [list(map(int, input().split())) for _ in range(9)]
flag = True

for i in range(9): #행, 열 체크
    if len(set(pList[i])) != 9: #행 체크
        flag = False
    temp = []
    for j in range(9):
        temp.append(pList[j][i])
    if len(set(temp)) != 9:
        flag =False

for i in range(0, 9, 3) : #3X3 체크
    for j in range(0, 9, 3):
        temp = []
        for k in range(3):
            for a in range(3):
                temp.append(pList[i+k][j+a])
        if len(set(temp)) != 9:
            flag = False

if flag == True:
    print("YES")
else:
    print("NO")