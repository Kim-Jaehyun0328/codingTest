import sys
sys.stdin=open("in1.txt", "r")

N = int(input())
pList = list(map(int, input().split()))
cnt = int(input())

highest = max(pList)
highest_idx = pList.index(highest)
lowest = min(pList)
lowest_idx = pList.index(lowest)

for i in range(cnt):
    pList[highest_idx] -= 1
    pList[lowest_idx] += 1
    highest = max(pList)
    highest_idx = pList.index(highest)
    lowest = min(pList)
    lowest_idx = pList.index(lowest)

print(highest - lowest)
