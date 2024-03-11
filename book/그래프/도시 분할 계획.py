# import sys
#
# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]
#
# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
#
#
# sys.stdin=open("practice2", "r")
#
# N, M = map(int,input().split())
#
# edges = []
# parent = [0 for _ in range(N+1)]
# answer = 0
#
# for i in range(1, N+1):
#     parent[i] = i
#
# for _ in range(M):
#     a, b, cost = map(int, input().split())
#     edges.append((cost,a,b))
#
#
# edges.sort()
# last = 0
#
#
# print(edges)
#
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(a) != find_parent(b):
#         union_parent(a, b)
#         answer += cost
#         last = cost
#
#
# print(answer, last)
# print(answer - last)


import sys
sys.stdin = open("practice2", "r")

N, M = map(int, input().split())
edges = []
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        last = cost

print(answer-last)












