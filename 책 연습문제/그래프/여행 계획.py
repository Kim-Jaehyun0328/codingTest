import sys
sys.stdin=open("practice2", "r")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))
parent = [0 for _ in range(n)]
for i in range(len(parent)):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(i, j)


for i in range(len(parent)):
    parent[i] = find(i)

print(parent)

for i in range(len(direction)):
    direction[i] -= 1

idx = parent[direction[0]]
for x in direction:
    if parent[x] != idx:
        print("NO")
        break
else:
    print("YES")