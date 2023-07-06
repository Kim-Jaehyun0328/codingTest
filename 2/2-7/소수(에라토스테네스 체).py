import sys
sys.stdin=open("in2.txt", "rt")
N = int(input())
pList = [0 for i in range(N+1)]
cnt = 0
for i in range(2, len(pList)):
    if pList[i] == 0:
        cnt+=1
        for j in range(i, len(pList), i):
            pList[j] = 1
print(cnt)