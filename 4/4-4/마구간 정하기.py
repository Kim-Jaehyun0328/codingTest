import sys
sys.stdin=open("in3.txt", "r")

def Count(len):
    cnt = 1
    ep = pList[0]
    for i in range(1, N):
        if pList[i]-ep >= len:
            cnt += 1
            ep = pList[i]
    return cnt


N, C = map(int, input().split())

pList = [int(input()) for _ in range(N)]
pList.sort()

lt, rt = 1, pList[len(pList)-1]

res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
