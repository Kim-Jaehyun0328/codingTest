import sys
sys.stdin=open("in5.txt", "r")

pList = [list(map(int, input().split())) for _ in range(7)]


res = 0
for i in range(7):
    for j in range(3):
        if pList[i][j] == pList[i][j+4] and pList[i][j+1] == pList[i][j+3]:
            res += 1

        if pList[j][i] == pList[j+4][i] and pList[j+1][i] == pList[j+3][i]:
            res += 1

print(res)