import sys
sys.stdin=open("in1.txt", "r")
n = int(input())


def DFS(v):
    if v == n+1:
        for i in range(len(ch)):
            if ch[i] == 1:
                print(i, end= " ")
        print()
        return
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


ch = [0 for _ in range(n+1)]
DFS(1)
