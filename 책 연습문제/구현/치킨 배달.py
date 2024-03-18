# from itertools import combinations
# import sys
#
#
# def get_sum(candidate):
#     result = 0
#     for hx, hy in house:
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx - cx) + abs(hy - cy))
#         result += temp
#     return result
# sys.stdin=open("practice2", "r")
# n, m = map(int, input().split())
# house, chicken = [], []
#
# for r in range(n):
#     l = list(map(int, input().split()))
#     for c in range(n):
#         if l[c] == 1:
#             house.append((r, c))
#         elif l[c] == 2:
#             chicken.append((r,c))
#
# candidates = list(combinations(chicken, m))
# result = 1e9
# for candidate in candidates:
#     result = min(result, get_sum(candidate))
#
#
# print(result)
#


import sys
from itertools import combinations

sys.stdin = open("practice2", "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
houses = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: #치킨집이라면
            chicken.append([i, j])
        elif arr[i][j] == 1: #집이라면
            houses.append([i, j])



answer = int(1e9)

comb = combinations(chicken, M)


for x in combinations(chicken, M):
    temp = 0
    for house in houses:
        each_house = int(1e9)
        for a in x:
            each_house = min(each_house, abs(house[0]-a[0]) + abs(house[1]-a[1]))
        temp += each_house

    answer = min(answer, temp)

print(answer)































