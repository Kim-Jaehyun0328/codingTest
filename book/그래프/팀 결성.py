# import sys
#
#
# def find_parent(x):
#     if parents[x] != x:
#         find_parent(parents[x])
#     return parents[x]
#
# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b
#
#
# sys.stdin=open("practice", "r")
# N, M = map(int, input().split())
# parents = [0 for _ in range(N+1)]
#
# for i in range(N+1):
#     parents[i] = i
#
#
# for i in range(M):
#     a, b, c = map(int, input().split())
#
#     if a == 1:
#         if parents[b] == parents[c]:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         union_parent(b, c)
# print(parents)



import sys
sys.stdin = open("practice", "r")
N, M = map(int, input().split())
parent = [i for i in range(N+1)]


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


for _ in range(M):
    i, a, b = map(int, input().split())

    if i == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")




















