v, e = 7, 9
arr = [[1,2,29], [1,5,75],[2,3,35],[2,6,34],[3,4,7],[4,6,23],[4,7,13],[5,6,53],[6,7,25]]

parent = [0 for _ in range(v+1)]
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for a, b, c in arr:
    edges.append((c,a,b))



def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges.sort()

for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])
        result += edge[0]

print(result)