import sys
sys.stdin=open("in5.txt", "r")

n = int(input())
dy = [[100 for _ in range(n+1)] for _ in range(n+1)]


for i in range(1, n+1):
    dy[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dy[a][b] = 1
    dy[b][a] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dy[i][j] = min(dy[i][j],  dy[i][k] + dy[k][j])


# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if dy[i][j] == 100:
#             print(0, end= " ")
#         else:
#             print(dy[i][j], end= " ")
#     print()


res = [0 for _ in range(n+1)]

for i in range(1, n+1):
    res[i] = max(dy[i][1:])

min_num = min(res[1:])
min_people = res.count(min_num)
print(min_num, min_people)

for i in range(len(res)):
    if res[i] == min_num:
        print(i, end= " ")
