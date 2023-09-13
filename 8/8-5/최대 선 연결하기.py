import sys
sys.stdin=open("in5.txt", "r")

n = int(input())


arr1 = [i for i in range(n+1)]
arr2 = list(map(int, input().split()))
arr2.insert(0, 0)
dy = [0 for _ in range(n+1)]
dy[1] = 1
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr2.index(j) < arr2.index(i) and dy[j] > max:
            max = dy[j]
        dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)