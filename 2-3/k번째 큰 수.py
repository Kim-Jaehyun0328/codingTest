import sys
sys.stdin = open("in5.txt", "rt")

n, k = map(int, input().split())
pList = list(map(int, input().split()))
temp = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for a in range(j+1, n):
            sum = pList[i] + pList[j] + pList[a]
            temp.append(sum)

temp = set(temp)
temp = list(temp)
temp.sort(reverse=True)
print(temp[k-1])