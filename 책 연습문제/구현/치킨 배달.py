from itertools import combinations
import sys


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result
sys.stdin=open("practice2", "r")
n, m = map(int, input().split())
house, chicken = [], []

for r in range(n):
    l = list(map(int, input().split()))
    for c in range(n):
        if l[c] == 1:
            house.append((r, c))
        elif l[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))


print(result)

