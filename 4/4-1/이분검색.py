import sys
sys.stdin=open("in5.txt", "r")

N, NUM = map(int, input().split())

pList = list(map(int, input().split()))
pList.sort()
res = 0
start, end = 0, N-1
while True:
    mid = (end+start)//2
    if pList[mid] == NUM:
        break
    elif pList[mid] < NUM:
        start = mid+1
    elif pList[mid] > NUM:
        end = mid-1

print(mid+1)