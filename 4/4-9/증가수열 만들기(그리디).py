import sys
from collections import deque
sys.stdin=open("in5.txt", "r")

N = int(input())
pList = list(map(int, input().split()))
pList = deque(pList)

#맨 끝에 있는 숫자보다 크되, 더 작아야함(맨 앞 맨 뒤를 비교했을 때 둘 중에 작은 것이 선택됨)
res = ""
last = 0

while True:
    if pList[0] < last and pList[len(pList)-1] < last:
        break

    if pList[0] < last < pList[len(pList) - 1]:
        res += "R"
        last = pList.pop()
        continue
    elif pList[0] > last > pList[len(pList) - 1]:
        res += "L"
        last = pList.popleft()
        continue

    if pList[0] < pList[len(pList)-1]:
        res += "L"
        last = pList.popleft()
    else:
        res += "R"
        last = pList.pop()

print(len(res))
print(res)
