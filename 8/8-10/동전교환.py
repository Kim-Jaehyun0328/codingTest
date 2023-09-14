import sys
sys.stdin=open("in5.txt", "r")

n = int(input())
coin = list(map(int, input().split()))
limit = int(input())
dy = [1000 for _ in range(limit+1)]
dy[0] = 0
for i in range(n):
    for j in range(coin[i], limit+1):
        dy[j] = min(dy[j], dy[j-coin[i]]+1)

print(dy[-1])