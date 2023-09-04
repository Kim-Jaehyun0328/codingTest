import sys
sys.stdin=open("in1.txt", "r")

def DFS(L, a, b, c):
    global res
    if L == n:
        temp = max(a, b, c) - min(a, b, c)
        if res > temp and a != b and b != c and a != c:
            res = temp
    else:
        DFS(L+1, a+coin[L], b, c)
        DFS(L+1, a, b+coin[L], c)
        DFS(L+1, a, b, c+coin[L])



if __name__ == "__main__":
    n = int(input())
    coin = []
    res = 100000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0, 0, 0, 0)
    print(res)

