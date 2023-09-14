import sys
sys.stdin=open("in1.txt", "r")

n, m = map(int, input().split())
# dy = [[0 for _ in range(m+1)] for _ in range(n)]
#
# for i in range(1, n):
#     p, t = map(int, input().split())
#     for j in range(t, m+1):
#         dy[i][j] = max(dy[i-1][j], dy[i-1][j-t]+p)
#
#
# for x in dy:
#     print(x)
# print(dy[n-1][m])

dy = [0 for _ in range(m+1)]

for i in range(n):
    p, t = map(int, input().split())
    for j in range(m, t-1, -1):
        dy[j] = max(dy[j], dy[j-t] + p)

print(max(dy))