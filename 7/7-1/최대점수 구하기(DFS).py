import sys
sys.stdin=open("in5.txt", "r")

n, t = map(int, input().split())

def DFS(v, point, time):
    global res
    if time > t:
        return
    if v == n:
        if res < point:
            res = point
    else:
        DFS(v+1, pv[v]+point, pt[v]+time)
        DFS(v+1, point, time)


res = 0
pv=list()
pt=list()
for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)

DFS(0, 0, 0)
print(res)