import sys
sys.stdin=open("in5.txt", "r")

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for i in range(len(house)):
            x1 = house[i][0]
            y1 = house[i][1]
            dist = 100000
            for j in cb:
                x2 = pizza[j][0]
                y2 = pizza[j][1]
                dist = min(dist, abs(x1-x2) + abs(y1-y2))
            sum += dist
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pizza)):
            cb[L] = i
            DFS(L+1, i+1)

    return

if __name__ == "__main__":
    house = []
    pizza = []
    cb = [0 for _ in range(m)]
    res = 100000
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1: #집이라면
                house.append((i, j))
            elif a[i][j] == 2: #피자집이라면
                pizza.append((i, j))
    DFS(0, 0)
    print(res)
