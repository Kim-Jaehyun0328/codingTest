import sys
sys.stdin=open("in5.txt", "rt")

N = int(input())
pList = list(map(int, input().split()))

# sum=0
# for i in pList:
#     sum += i
#
# average = round(sum/N)

# temp = []
#
# for i in pList:
#     temp.append(abs(average-i))
#
# min = float('inf')
# idx = 0
# for i in range(len(temp)):
#     if temp[i] < min:
#         min = temp[i]
#         idx = i
# print("%d %d" %(average, idx+1))

average = round(sum(pList)/N)
min = float('inf')
for idx, x in enumerate(pList):
    temp = abs(average-x)
    if temp < min:
        min=temp
        score=x
        res=idx+1
    elif temp == min:
        if score < x:
            score = x
            res = idx + 1

print("%d %d" %(average, res))