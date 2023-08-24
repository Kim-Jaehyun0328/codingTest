import sys
sys.stdin=open("in5.txt", "r")

total, n = map(int, input().split())
dogs = list(int(input()) for _ in range(n))

# if sum(dogs) < total:
#     print(sum(dogs))
#     sys.exit()
def DFS(v, kg, tsum):
    global max
    if kg + (total_kg - tsum) < max:
        return
    if kg > total:
        return
    else:
        if max < kg:
            max = kg
    if v == n:
        return
    else:
        DFS(v+1, kg + dogs[v], tsum + dogs[v])
        DFS(v+1, kg, tsum + dogs[v])


max = 0
total_kg = sum(dogs)
DFS(0, 0, 0)

print(max)