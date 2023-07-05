import sys
sys.stdin=open("in5.txt", "rt")

N = int(input())
pList = list(map(int, input().split()))
def digit_sum(x):
    length = len(str(x))
    sum=0
    for i in range(length):
        sum += x%10
        x//=10
    return sum
max = 0
for i in range(N):
    sum = digit_sum(pList[i])
    if sum > max:
        max = sum
        res = pList[i]

print(res)


