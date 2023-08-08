import sys
sys.stdin=open("in1.txt", "r")

N, M = map(int, input().split())
pList = list(map(int, input().split()))

res = 0


lt, rt = 1, sum(pList)
while lt <= rt:
    cnt = 1
    temp = 0
    mid = (lt+rt)//2
    for i in pList:
        if (temp + i) > mid:
            temp = i
            cnt += 1
        else:
            temp += i
    if cnt > M:
        lt = mid + 1
    else:
            res = mid
            rt = mid - 1
print(res)