# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x
#
# def unioin_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = 6, 4
# arr = [(1,4),(2,3),(2,4),(5,6)]
# parent = [0 for _ in range(v+1)]
#
# for i in range(1, v+1):
#     parent[i] = i
#
# for a, b in arr:
#     unioin_parent(parent, a, b)
#
#
# print('각 원소가 속한 집합: ', end= " ")
# for i in range(1, v+1):
#     print(find_parent(parent, i), end= " ")
#
# print()
#
# print("부모 테이블: ", end= " ")
# for i in range(1, v+1):
#     print(parent[i], end= " ")



def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

def unioin_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 6, 4
arr = [(1,4),(2,3),(2,4),(5,6)]
parent = [0 for _ in range(v+1)]

for i in range(1, v+1):
    parent[i] = i


cycle = False
for a, b in arr:
    if find_parent(parent, parent[a]) == find_parent(parent, parent[b]):
        cycle = True
        break
    unioin_parent(parent, a, b)


print('각 원소가 속한 집합: ', end= " ")
for i in range(1, v+1):
    print(find_parent(parent, i), end= " ")

print()

print("부모 테이블: ", end= " ")
for i in range(1, v+1):
    print(parent[i], end= " ")