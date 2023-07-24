import sys
sys.stdin=open("in5.txt", "r")

N = int(input())

pList = [list(map(int, input().split())) for _ in range(N)]
res = 0
center = N//2
for i in range(N):
    if i < center:
        res += pList[i][center]
        res += sum(pList[i][center-i:center])
        res += sum(pList[i][center+1:center+i+1])
    elif i == center:
        res += sum(pList[i])
    elif i > center:
        res += pList[i][center]
        res += sum(pList[i][i-center:center])
        res += sum(pList[i][center+1:-(i%center)])

print(res)

