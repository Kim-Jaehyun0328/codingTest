import sys
sys.stdin=open("in1.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0 for _ in range(n)] for _ in range(n)]
dy[0][0] = arr[0][0]
for i in range(1, n):
    dy[i][0] = dy[i-1][0] + arr[i][0]
    dy[0][i] = dy[0][i-1] + arr[0][i]


for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
        # if dy[i-1][j] > dy[i][j-1]: #왼쪽에서 온 게 더 좋음
        #     dy[i][j] = dy[i][j-1] + arr[i][j]
        # elif dy[i-1][j] < dy[i][j-1]:
        #     dy[i][j] = dy[i-1][j] + arr[i][j]
        # elif dy[i-1][j] == dy[i][j-1]:
        #     dy[i][j] = dy[i - 1][j] + arr[i][j]


print(dy[n-1][n-1])
