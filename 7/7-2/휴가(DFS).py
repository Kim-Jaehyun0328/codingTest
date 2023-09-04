import sys
sys.stdin=open("in5.txt", "r")

n = int(input())

t = [] #시간
p = []  #페이
res = 0 #최고 페이
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)



def DFS(time, pay):
    global res
    if time > n:
        return
    if res < pay :
        res = pay
    if time < n :
        DFS(t[time]+time, p[time]+pay)
        DFS(time+1, pay)
    return



DFS(0, 0)
print(res)