# import sys
# sys.stdin=open("practice", "r")
#
#
#
# def DFS(x, y):
#     print(x,y)
#     if dy[x][y] != 0:
#         return dy[x][y]
#     else:
#         dy[x][y] = min(DFS(x-1,y), DFS(x, y-1)) + arr[x][y]
#     return dy[x][y]
#
# if __name__ == "__main__":
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     dy = [[0 for _ in range(n)] for _ in range(n)]
#     dy[0][0] = arr[0][0]
#
#     for i in range(1, n):
#         dy[i][0] = dy[i-1][0] + arr[i][0]
#         dy[0][i] = dy[0][i-1] + arr[0][i]
#
#     print(DFS(n-1, n-1))

import sys
sys.stdin = open("practice", 'r')
def DFS(x, y):
    print(x, y)
    if dy[x][y]>0:
        return dy[x][y];
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1, y)+arr[x][y]
        elif x==0:
            dy[x][y]=DFS(x, y-1)+arr[x][y]
        else:
            dy[x][y]=min(DFS(x-1, y), DFS(x, y-1))+arr[x][y]
        return dy[x][y]

if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))