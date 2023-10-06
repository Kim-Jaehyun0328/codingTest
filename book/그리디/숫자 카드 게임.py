N, M = 2, 4

cards = [[7, 3], [3,3],[1,3],[8,4]]
min_list = []
for x in cards:
    min_list.append(min(x))

print(min_list.index(max(min_list)))