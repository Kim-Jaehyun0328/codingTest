import sys
sys.stdin=open("in1.txt", "r")

N = int(input())
pList = list(map(int, input().split()))

res = [0 for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == pList[i] and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            cnt += 1

for i in res:
    print(i, end=" ")