import sys
sys.stdin=open("in5.txt","r")

N = int(input())
pList = list(map(int,input().split()))

res = 0
cnt = 1
for i in range(N):
    if pList[i] == 0:
        cnt = 1
    else:
        res+=cnt
        cnt+=1
print(res)