import sys
sys.stdin=open("in1.txt", "r")


def DFS(L, sum):
    global res
    if L == n:
        if sum > 0:
            res.add(sum)
    else:
        DFS(L+1, sum+chu[L])
        DFS(L+1, sum-chu[L])
        DFS(L+1, sum)



if __name__ == "__main__":
    n = int(input())
    chu = list(map(int, input().split()))
    total = sum(chu)
    res = set()

    DFS(0, 0)
    print(total - len(res))