import sys
sys.stdin=open("in1.txt", "r")

n, m = map(int, input().split())

def DFS(v):
    global cnt
    if v == m :
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            res[v] = i
            DFS(v+1)





res = [0 for _ in range(m)]
cnt = 0
DFS(0)
print(cnt)