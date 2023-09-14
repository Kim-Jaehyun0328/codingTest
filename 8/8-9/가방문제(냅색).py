import sys
sys.stdin=open("in1.txt", "r")

n, limit = map(int, input().split())
arr = []
dy = [0 for _ in range(limit+1)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, limit+1):
        dy[j] = max(dy[j], dy[j-w] + v)
        # temp = dy[j-w] + v
        # if temp > dy[j]:
        #     dy[j] = temp

print(dy)
