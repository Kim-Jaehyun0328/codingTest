import sys
sys.stdin=open("in5.txt", "r")

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num = int(input())

def DFS(L, s):
    global cnt
    if L == m:
        if sum(res[:])%num == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            res[L] = num_list[i]
            DFS(L+1, i+1)




res = [0 for _ in range(m)]
cnt = 0
DFS(0, 0)
print(cnt)


