import sys
sys.stdin=open("in5.txt", "r")


def DFS(minx, miny, prevnum):
    global res
    if minx == destx and miny == desty:
        res += 1
        return
    else:
        for i in range(4):
            temp = a[minx][miny] #이전
            xx = minx + dx[i]
            yy = miny + dy[i]
            if 0<=xx<n and 0<=yy<n:
                next = a[xx][yy]  # 이제 갈 곳
                if a[xx][yy] != -1 and next > prevnum:
                    a[minx][miny] = -1
                    DFS(xx, yy, next)
                    a[minx][miny] = temp

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    min_num = 10000
    max_num = -10000
    startx = 100
    starty = 100
    destx = 100
    desty = 100
    res = 0

    for i in range(n):
        for j in range(n):
            if a[i][j] > max_num:
                max_num = a[i][j]
                destx = i
                desty = j
            if a[i][j] < min_num:
                min_num = a[i][j]
                startx = i
                starty = j

    DFS(startx,starty, min_num)
    print(res)

