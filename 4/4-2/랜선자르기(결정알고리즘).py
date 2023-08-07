import sys
sys.stdin=open("in1.txt", "r")

N, cnt = map(int, input().split())

pList = [int(input()) for _ in range(N)]

start, end = 1, max(pList)
res = 0

temp = 0  #시작과 끝 사이, 가장 적합한 값이 res가 됨
while start <= end:
    tempCnt = 0
    temp = (start+end)//2

    for i in pList:
        tempCnt += i//temp

    if tempCnt >= cnt:
        if res <= temp:
            res = temp
            start = temp + 1
    else:
        end = temp - 1

print(res)

