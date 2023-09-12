import sys
sys.stdin=open("in1.txt", "r")
a = [list(map(int, input().split())) for _ in range(10)]
a.insert(0, [i for i in range(10)])

def DFS(x, y):
    if a[x][y] == 0:
        return
    if x == 10:
        if a[x][y] == 2:
            print(i)
            sys.exit()
    else:
        if 0 <= y-1 and a[x][y-1] == 1 and ch[x][y-1] == 0 : #왼쪽에 갈 길이 있다면
            ch[x][y - 1] = 1
            DFS(x, y-1)
        elif 10 > y+1 and a[x][y+1] == 1 and ch[x][y+1] == 0: #오른쪽에 갈 길이 있다면
            ch[x][y + 1] = 1
            DFS(x, y+1)
        elif a[x+1][y] != 0 and ch[x+1][y] == 0: #아래 갈 길이 있다면
            ch[x+1][y] = 1
            DFS(x+1, y)
    return


if __name__ == "__main__":
    for i in range(10):
        ch = [[0 for _ in range(10)] for _ in range(11)]
        DFS(1, i)