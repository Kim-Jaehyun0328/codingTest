import sys
sys.stdin=open("in5.txt", "r")

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse= True)
m = int(input())
def DFS(c, cs):
    global res
    if cs > m or res < c:
        return
    if cs == m and res > c:
        res = c
    for i in range(n):
        DFS(c+1, cs + coins[i])



res = 1000
DFS(0, 0)
print(res)