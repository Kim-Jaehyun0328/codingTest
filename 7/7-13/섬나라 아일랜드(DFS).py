import sys
sys.stdin=open("in5.txt", "r")


def DFS(x, y):
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            board[xx][yy] = 0
            DFS(xx, yy)

if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0
                cnt += 1
                DFS(i, j)

    print(cnt)

