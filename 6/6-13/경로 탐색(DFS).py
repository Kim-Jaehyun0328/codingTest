import sys
sys.stdin=open("in1.txt", "r")

n, v = map(int, input().split())


def DFS(sour):
    global cnt
    if sour == n-1:
        cnt += 1
        return
    else:
        for i in range(1, n):
            if matrix[sour][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0


matrix = [[0 for _ in range(n)] for _ in range(n)]
ch = [0 for _ in range(n)]
ch[0] = 1
cnt = 0
for _ in range(v):
    f, t = map(int, input().split())
    matrix[f-1][t-1] = 1


DFS(0)
print(cnt)