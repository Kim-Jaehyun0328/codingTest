import sys
sys.stdin=open("in2.txt","r")

N = int(input())

pList = [list(map(int, input().split())) for _ in range(N)]


for _ in range(int(input())):
    row, corr, cnt = map(int, input().split())
    row -= 1
    if corr == 0: #왼쪽으로 이동
        for _ in range(cnt):
            pList[row].append(pList[row].pop(0))
    elif corr == 1: #오른쪽으로 이동
        for _ in range(cnt):
            pList[row].insert(0, pList[row].pop())

#모래시계
s, e = 0, N-1
res = 0
center = N//2
for i in range(N):
    # res += sum(pList[i][s:e])
    for j in range(s, e+1):
        res += pList[i][j]
    if i < center:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)