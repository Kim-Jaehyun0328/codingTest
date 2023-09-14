import sys
sys.stdin=open("in1.txt", "r")

def DFS(n):
    if a[n] != 0:
        return a[n]
    if n == 1 or n == 2:
        return n
    else:
        a[n] = DFS(n-1) + DFS(n-2)
        return a[n]



if __name__ == "__main__":
    n = int(input())
    a = [0 for _ in range(n+1)]
    a[1] = 1
    a[2] = 2
    res = DFS(n)
    print(res)